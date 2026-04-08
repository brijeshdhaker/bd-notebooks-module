from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List, Dict, Any, Tuple

class SplitManager:

    def __init__(self,
                 chunk_size : str = 1000,
                 chunk_overlap : int = 200):
        """
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_documents(self, documents: List[Any]) -> List[Any]:
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
            print(f"Sample Chunk [0]:")
            print(f"Content: {chunks[0].page_content[:200]}...")
            print(f"Metadata: {chunks[0].metadata}")
        return chunks

# Example usage
if __name__ == "__main__":
    #
    _docs = []
    from langchain_core.documents import Document
    for i in range(50000):
        _docs.append(Document(
            page_content="this is the main text content for testing and I am using to create RAG",
            metadata={
                "source":"exmaple.txt",
                "pages":1,
                "author":"Brijesh K. Dhaker",
                "date_created":"2026-04-01"
            })
        )

    split_manager = SplitManager(chunk_size=100, chunk_overlap=20)
    _chunks = split_manager.split_documents(_docs)
    print(f"[*INFO] Total splitted chunks: {len(_chunks)}")
