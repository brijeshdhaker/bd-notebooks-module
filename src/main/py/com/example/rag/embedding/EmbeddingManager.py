import numpy as np
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from langchain_huggingface import HuggingFaceEmbeddings
import chromadb
from chromadb.config import Settings
#from langchain_chroma import Chroma
import uuid
from typing import List, Dict, Any, Tuple
from sklearn.metrics.pairwise import cosine_similarity
from com.example.rag.loader.LoadManager import LoadManager

#
# model_name="sentence-transformers/all-mpnet-base-v2"
# model_name="sentence-transformers/all-MiniLM-L6-v2"
#
class EmbeddingManager:
    """Handles document embedding generation using SentenceTransformer"""
    
    def __init__(self, 
                 model_name: str = "all-MiniLM-L6-v2",
                 chunk_size: int = 1000, 
                 chunk_overlap: int = 200):
        """
        Initialize the embedding manager
        Args:
            model_name: HuggingFace model name for sentence embeddings
        """
        self.model_name = model_name
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.model = None
        self._load_model()

    def _load_model(self):
        """Load the SentenceTransformer model"""
        try:
            print(f"Loading embedding model: {self.model_name}")
            self.model = SentenceTransformer(self.model_name)
            print(f"Model {self.model_name} loaded successfully.")
            print(f"Embedding dimension: {self.model.get_sentence_embedding_dimension()}")
        except Exception as e:
            print(f"Error loading model {self.model_name}: {e}")
            raise

    def generate_text_embeddings(self, texts: List[str]) -> np.ndarray:
        """
        Generate embeddings for a list of texts
        Args:
            texts: List of text strings to embed
        Returns:
            numpy array of embeddings with shape (len(texts), embedding_dim)
        """
        if not self.model:
            raise ValueError("Model not loaded")
        
        print(f"Generating embeddings for {len(texts)} texts...")
        embeddings = self.model.encode(texts, show_progress_bar=True)
        print(f"Generated embeddings with shape: {embeddings.shape}")
        return embeddings
    
    def generate_doc_embeddings(self, documents: List[str]) -> np.ndarray:
        """
        Generate embeddings for a list of texts
        Args:
            texts: List of text strings to embed
        Returns:
            numpy array of embeddings with shape (len(texts), embedding_dim)
        """
        _chunks = self.chunk_documents(documents)
        print(f"Generating embeddings for {len(_chunks)} texts...")
        embeddings = self.__embed_chunks(_chunks)
        return embeddings
    
    def __embed_chunks(self, chunks: List[Any]) -> np.ndarray:
        if not self.model:
            raise ValueError("Model not loaded")
        
        _texts = [chunk.page_content for chunk in chunks]
        print(f"[INFO] Generating embeddings for {len(_texts)} chunks...")
        embeddings = self.model.encode(_texts, show_progress_bar=True)
        #huggingFaceEmbeddings = HuggingFaceEmbeddings(model_name=self.model_name)
        #embeddings = huggingFaceEmbeddings.embed_documents(_texts)
        print(f"[INFO] Generated Embeddings shape: {embeddings.shape}")
        return embeddings
    
    def chunk_documents(self, documents: List[Any]) -> List[Any]:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
        chunks = splitter.split_documents(documents)
        print(f"[INFO] Split {len(documents)} documents into {len(chunks)} chunks.")
        # Show example of a chunk
        if chunks:
            print(f"\Sample chunk:")
            print(f"Content: {chunks[0].page_content[:200]}...")
            print(f"Metadata: {chunks[0].metadata}")
        return chunks


# Example usage
if __name__ == "__main__":
    #
    document_dir = "docs"
    load_manager = LoadManager(document_dir)
    douments = load_manager.from_directory()
    print(f"[*INFO] Total loaded documents: {len(douments)}")
    
    embedding_manager=EmbeddingManager()
    embeddings = embedding_manager.generate_embeddings(douments)
    
    #chunks = emb_pipe.chunk_documents(docs)
    #embeddings = emb_pipe.embed_chunks(chunks)
    print("[INFO] Example embedding:", embeddings[0] if len(embeddings) > 0 else None)