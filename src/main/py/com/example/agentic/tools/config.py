"""
"""
_tool_config = dict(
    llm=dict(
        provider="ollama", # or google, openai, anthropic, llama2, ...
        config=dict(
            model="llama3.2:1b-instruct-q8_0",
            # num_predict=256,
            # temperature=0.7,
            # top_p=1,
            # stream=true,
        ),
    ),
    embedder=dict(
        provider="ollama", # or openai, ollama, ...
        config=dict(model_name="nomic-embed-text", task_type="RETRIEVAL_DOCUMENT")
    ),
    embedding_model= dict(
        provider="openai",
        config=dict(model= "nomic-embed-text", api_key="", platform_url="http://localhost:11434/v1")
    ),
    vectordb=dict(
        provider="chromadb",
        config={"persist_directory":"agentic-ai/chromadb", "allow_reset": "true", "is_persistent": "true"}
    )
)

#
_rag_tool_config = dict(
    llm=dict(
        provider="ollama", # or google, openai, anthropic, llama2, ...
        config=dict(
            model="llama3.2:1b-instruct-q8_0",
            # temperature=0.5,
            # top_p=1,
            # stream=true,
        ),
    ),
    embedder=dict(
        provider="ollama", # or openai, ollama, ...
        config=dict(model_name="all-minilm", task_type="RETRIEVAL_DOCUMENT")
    ),
    embedding_model= dict(
        provider="openai",
        config=dict(model= "nomic-embed-text", api_key="", platform_url="http://localhost:11434/v1")
    ),
    vectordb=dict(
        provider="chromadb",
        config={"persist_directory":"agentic-ai/chromadb", "allow_reset": "true", "is_persistent": "true"}
    )
)

# Embedders
_embedder_config_ollama={"provider": "ollama", "config": {"model": "nomic-embed-text", "url": "http://localhost:11434/api/embeddings"}}

_embedder_config_openai={"provider": "openai", "config": {"model": "nomic-embed-text", "api_key":"", "platform_url":"http://localhost:11434/v1"}}
