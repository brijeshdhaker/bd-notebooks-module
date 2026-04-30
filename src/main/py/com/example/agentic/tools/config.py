import os
from dotenv import load_dotenv

"""
"""
load_dotenv()

_tool_config = dict(
    chunk_size=1000, 
    chunk_overlap=200,
    batch_size = 100,
    llm=dict(
        provider="ollama",
        config=dict(
            model=os.environ["OPENAI_MODEL_NAME"],
            base_url="http://localhost:11434",
            temperature=0.3,
            max_tokens=4096,
            timeout=300,
            # num_predict=256,
            # top_p=1,
            # stream=true,
        ),
    ),
    embedder=dict(
        provider="ollama",
        config=dict(
            model_name=os.environ["OPENAI_EMBEDDING_MODEL_ID"], 
            url="http://localhost:11434/api/embeddings"
        )
    ),
    embedding_model= dict(
        provider="ollama",
        config=dict(
            model= os.environ["OPENAI_EMBEDDING_MODEL_ID"], 
            api_key="", 
            platform_url="http://localhost:11434/api/embeddings"
        )
    ),
    vectordb=dict(
        provider="chromadb",
        config={
            #"collection_name": "sandbox_documents",
            #"persist_directory":"/home/brijeshdhaker/IdeaProjects/crewai_design_document/vectorstore/chroma", 
            #"allow_reset": "true", 
            #"is_persistent": "true"
        }
    )
)

#
_rag_tool_config = dict(
    chunk_size=1000, 
    chunk_overlap=200,
    batch_size = 100,
    llm=dict(
        provider="openai",
        config=dict(
            model=os.environ["OPENAI_MODEL_NAME"],
            base_url="http://localhost:11434/v1",
            max_tokens=4096,
            temperature=0.3,
            timeout=300,
            # top_p=1,
            # stream=true,
        ),
    ),
    embedder=dict(
        provider="openai",
        config=dict(
            model_name=os.environ["OPENAI_EMBEDDING_MODEL_ID"],
            api_base="http://localhost:11434/v1",
            api_version="v1",
            api_key="ollama",
            api_type="ollama",
            default_headers={"X-Custom-Header": "ollama"},
            organization_id="sandbox"
        )
    ),
    embedding_model= dict(
        provider="openai",
        config=dict(
            model_name= os.environ["OPENAI_EMBEDDING_MODEL_ID"], 
            organization_id="sandbox",
            api_base="http://localhost:11434/v1",
            api_version="v1",
            api_key="ollama",
            api_type="ollama",
            default_headers={"X-Custom-Header": "ollama"}
        )
    ),
    vectordb=dict(
        provider="chromadb",
        config={
            #"collection_name": "sandbox_documents",
            #"persist_directory":"/home/brijeshdhaker/IdeaProjects/crewai_design_document/vectorstore/chroma", 
            #"allow_reset": "true", 
            #"is_persistent": "true"
        }
    )
)

# Embedders
_embedder_config_hf={
    "provider": "huggingface", 
    "config": {"model_name": "sentence-transformers/all-MiniLM-L6-v2"}
}

from crewai.rag.embeddings.providers.huggingface.types import HuggingFaceProviderSpec


_embedding_model_hf: HuggingFaceProviderSpec = {
    "provider": "huggingface",
    "config": {
        "model": "sentence-transformers/all-MiniLM-L6-v2"
    }
}

from crewai.rag.embeddings.providers.openai.types import OpenAIProviderSpec
from crewai.rag.embeddings.providers.ollama.types import OllamaProviderSpec

## Memory
from com.example.agentic.agent.LLMManager import LLMManager
from crewai import Memory

def create_memory(type: str = 'openai') -> Memory :
    _llm = LLMManager.create_llm('openai')
    _embedder = _rag_tool_config['embedder']
    # 
    if type == 'ollama' :
        _embedder = embedder=_tool_config['embedder']
    # 
    if type == 'hf' :
        _embedder = _embedder_config_hf
    
    return Memory(llm=_llm,embedder=_embedder)
