import os
import faiss
from pathlib import Path
import numpy as np
import pickle
from typing import List, Any
from sentence_transformers import SentenceTransformer
from com.example.agentic.embedding.EmbeddingManager import EmbeddingManager
from com.example.agentic.loader.LoadManager import LoadManager
from com.example.agentic.vectors.VectorStore import VectorStore
import uuid

class FaissVectorStore(VectorStore):
    """
    FaissVectorStore : Facebook AI Similarity Search
    """
    def __init__(self, 
                 persist_dir: str = "faiss", 
                 embedding_model: str = "all-MiniLM-L6-v2", 
                 chunk_size: int = 1000, 
                 chunk_overlap: int = 200):
        #        
        super().__init__(persist_dir,embedding_model,chunk_size,chunk_overlap) 
        #
        self.index = None
        self.metadata = []
        
    #
    def build_from_documents(self, documents: List[Any]):
        print(f"[INFO] Building vector store from {len(documents)} raw documents...")
        chunks = self.embeddingManager.chunk_documents(documents)
        embeddings = self.embeddingManager.embed_chunks(chunks)

        # Prepare data for Faiss Vector Store
        ids = []
        metadatas = []
        documents_text = []
        embeddings_list = []
        
        for i, (doc, embedding) in enumerate(zip(chunks, embeddings)):
            # Generate unique ID
            doc_id = f"doc_{uuid.uuid4().hex[:8]}_{i}"
            ids.append(doc_id)
            
            # Prepare metadata
            metadata = dict(doc.metadata)
            metadata['doc_index'] = doc_id
            metadata['doc_length'] = len(doc.page_content)
            metadata['doc_content'] = doc.page_content
            metadatas.append(metadata)
            
            # Document content
            #documents_text.append(doc.page_content)
            
            # Embedding
            embeddings_list.append(embedding.tolist())

        # Add to Vector Store
        try:
            self.add_embeddings(np.array(embeddings_list).astype('float32'), metadatas)
            self.save()
        except Exception as e:
            print(f"Error adding documents to vector store: {e}")
            raise
        print(f"[INFO] Vector store built and saved to {self.persist_directory}")
        print(f"Successfully added {len(documents)} documents to vector store")

    #
    def add_embeddings(self, embeddings: np.ndarray, metadatas: List[Any] = None):
        dim = embeddings.shape[1]
        if self.index is None:
            self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)
        if metadatas:
            self.metadata.extend(metadatas)
        print(f"[INFO] Added {embeddings.shape[0]} vectors to Faiss index.")

    def save(self):
        faiss_path = os.path.join(self.persist_directory, "faiss.index")
        meta_path = os.path.join(self.persist_directory, "metadata.pkl")
        faiss.write_index(self.index, faiss_path)
        with open(meta_path, "wb") as f:
            pickle.dump(self.metadata, f)
        print(f"[INFO] Saved Faiss index and metadata to {self.persist_directory}")

    def load(self):
        faiss_path = os.path.join(self.persist_directory, "faiss.index")
        meta_path = os.path.join(self.persist_directory, "metadata.pkl")
        self.index = faiss.read_index(faiss_path)
        with open(meta_path, "rb") as f:
            self.metadata = pickle.load(f)
        print(f"[INFO] Loaded Faiss index and metadata from {self.persist_directory}")
    
    #
    def search(self, query_embedding: np.ndarray, top_k: int = 5):
        # D → distances, 
        # I → indices of matching chunks.
        D, I = self.index.search(query_embedding, top_k)
        results = []
        for i, (idx, distance) in enumerate(zip(I[0], D[0])):
            metadata = self.metadata[idx] if idx < len(self.metadata) else None
            similarity_score = 1 - distance
            results.append({
                "id": metadata['doc_index'],
                "content": metadata['doc_content'], 
                "distance": distance,
                "similarity_score": similarity_score, 
                "metadata": metadata,
                "rank": i + 1
            })
        return results

    def query(self, query_text: str, top_k: int = 5):
        print(f"[INFO] Querying vector store for: '{query_text}'")
        qm_embedding = self.embeddingManager.embed_query([query_text])
        qt_embedding = self.model.encode([query_text]).astype('float32')
        return self.search(qt_embedding, top_k=top_k)

# Example usage
if __name__ == "__main__":
    
    #
    document_dir = "docs"
    #douments = LoadManager.from_directory(document_dir, inclusions=["txt"])
    #print(f"[*INFO] Total loaded documents: {len(douments)}")
    store = FaissVectorStore("faiss")
    #store.build_from_documents(douments)
    store.load()
    print(store.query("What are benefits of microservices ?", top_k=3))