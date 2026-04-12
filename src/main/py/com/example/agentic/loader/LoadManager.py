#
from pathlib import Path
from typing import List, Any
from langchain_community.document_loaders.base import BaseLoader
from langchain_community.document_loaders import PyPDFLoader, TextLoader, CSVLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders.excel import UnstructuredExcelLoader
from langchain_community.document_loaders import JSONLoader
from langchain_community.document_loaders import WebBaseLoader

#
class LoadManager:
    """Handles document embedding generation using SentenceTransformer"""
    
    documents = []

    def __init__(self, data_dir: str):
        """
        Initialize the document load manager
        
        Args:
            model_name: HuggingFace model name for sentence embeddings
        """
        self.data_dir = data_dir
        self._load_documents()

    # Public: For external use
    def from_directory(self): 
        """

        """
        return self.documents

    # "Internal" or Protected Convention
    def _load_documents(self):
        """ 
        Load all supported files from the data directory and convert to LangChain document structure.
        Supported: PDF, TXT, CSV, Excel, Word, JSON 
        """
        # Use project root data folder
        data_path = Path(self.data_dir).resolve()
        print(f"[DEBUG] Data path: {data_path}")
        _documents = []
        # PDF files
        pdf_files = list(data_path.glob('**/*.pdf'))
        print(f"[DEBUG] Found {len(pdf_files)} PDF files: {[str(f) for f in pdf_files]}")
        for pdf_file in pdf_files:
            print(f"[DEBUG] Loading PDF: {pdf_file}")
            try:
                loader = PyPDFLoader(str(pdf_file))
                loaded = loader.load()
                print(f"[DEBUG] Loaded {len(loaded)} PDF docs from {pdf_file}")
                _documents.extend(loaded)
            except Exception as e:
                print(f"[ERROR] Failed to load PDF {pdf_file}: {e}")

        # TXT files
        txt_files = list(data_path.glob('**/*.txt'))
        print(f"[DEBUG] Found {len(txt_files)} TXT files: {[str(f) for f in txt_files]}")
        for txt_file in txt_files:
            print(f"[DEBUG] Loading TXT: {txt_file}")
            try:
                loader = TextLoader(str(txt_file))
                loaded = loader.load()
                print(f"[DEBUG] Loaded {len(loaded)} TXT docs from {txt_file}")
                _documents.extend(loaded)
            except Exception as e:
                print(f"[ERROR] Failed to load TXT {txt_file}: {e}")

        # CSV files
        csv_files = list(data_path.glob('**/*.csv'))
        print(f"[DEBUG] Found {len(csv_files)} CSV files: {[str(f) for f in csv_files]}")
        for csv_file in csv_files:
            print(f"[DEBUG] Loading CSV: {csv_file}")
            try:
                loader = CSVLoader(str(csv_file))
                loaded = loader.load()
                print(f"[DEBUG] Loaded {len(loaded)} CSV docs from {csv_file}")
                _documents.extend(loaded)
            except Exception as e:
                print(f"[ERROR] Failed to load CSV {csv_file}: {e}")

        # Excel files
        xlsx_files = list(data_path.glob('**/*.xlsx'))
        print(f"[DEBUG] Found {len(xlsx_files)} Excel files: {[str(f) for f in xlsx_files]}")
        for xlsx_file in xlsx_files:
            print(f"[DEBUG] Loading Excel: {xlsx_file}")
            try:
                loader = UnstructuredExcelLoader(str(xlsx_file))
                loaded = loader.load()
                print(f"[DEBUG] Loaded {len(loaded)} Excel docs from {xlsx_file}")
                _documents.extend(loaded)
            except Exception as e:
                print(f"[ERROR] Failed to load Excel {xlsx_file}: {e}")

        # Word files
        docx_files = list(data_path.glob('**/*.docx'))
        print(f"[DEBUG] Found {len(docx_files)} Word files: {[str(f) for f in docx_files]}")
        for docx_file in docx_files:
            print(f"[DEBUG] Loading Word: {docx_file}")
            try:
                loader = Docx2txtLoader(str(docx_file))
                loaded = loader.load()
                print(f"[DEBUG] Loaded {len(loaded)} Word docs from {docx_file}")
                _documents.extend(loaded)
            except Exception as e:
                print(f"[ERROR] Failed to load Word {docx_file}: {e}")

        # JSON files
        json_files = list(data_path.glob('**/*.json'))
        print(f"[DEBUG] Found {len(json_files)} JSON files: {[str(f) for f in json_files]}")
        for json_file in json_files:
            print(f"[DEBUG] Loading JSON: {json_file}")
            try:
                loader = JSONLoader(str(json_file))
                loaded = loader.load()
                print(f"[DEBUG] Loaded {len(loaded)} JSON docs from {json_file}")
                _documents.extend(loaded)
            except Exception as e:
                print(f"[ERROR] Failed to load JSON {json_file}: {e}")
        
        #
        self.documents = _documents
        print(f"[DEBUG] Total loaded documents: {len(_documents)}")

    @classmethod
    def from_web(cls, web_paths: List[str]):
        _documents = []
        # Web urls
        print(f"[DEBUG] Found {len(web_paths)} page : {[str(f) for f in web_paths]}")
        for web_path in web_paths:
            print(f"[DEBUG] Loading pages from : {web_path}")
            try:
                loader = WebBaseLoader(web_paths=[web_path])
                loaded = loader.load()
                print(f"[DEBUG] Loaded {len(loaded)} pages from {web_path}")
                _documents.extend(loaded)
            except Exception as e:
                print(f"[ERROR] Failed to load pages {web_path}: {e}")

        return _documents
    
    # "Private" with Name Mangling (__name)
    def __setupLoader(self):
        """

        """

# Example usage
if __name__ == "__main__":
   
    load_manager = LoadManager("docs")
    dir_douments = load_manager.from_directory()
    print(f"[*INFO] Total loaded documents: {len(dir_douments)}")

    web_douments = LoadManager.from_web(['https://educosys.com/#faq'])
    print(f"[*INFO] Total loaded documents: {len(web_douments)}")
