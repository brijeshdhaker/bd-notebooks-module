#
import os
import getpass
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from crewai import LLM

#
# "groq:llama3–8b-8192"
# "groq:llama3-70b-8192" 
# "groq:openai/gpt-oss-20b"
# "groq:llama-3.1-70b-versatile"

load_dotenv()

class LLMManager:
    """
    """
    __agent = None
    __model = None


    @classmethod
    def get_agent(cls):
        #
        if not os.environ.get("OPENAI_API_KEY"):
            os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key : ")

        # Initialize models
        if not cls.__agent :
            cls.__agent = create_agent(
                model="groq:openai/gpt-oss-20b",
                system_prompt="You are a helpful assistant."
            )

        return cls.__agent
    
    @classmethod
    def get_model(cls):
        # Initialize models
        if not cls.__model :
            cls.__model = init_chat_model("groq:openai/gpt-oss-20b")
            #self.llm = ChatOpenAI(
            #    model="openai/gpt-oss-20b", 
            #    api_key=os.getenv("OPENAI_API_KEY"),
            #    base_url="https://api.groq.com/openai/v1",
            #    temperature=0
            #)
        return cls.__model
    
    #
    @classmethod
    def create_llm(cls, type: str) -> LLM :
    
        load_dotenv()
        
        # Groq llm client
        if type == 'ollama' :
            # LLM setup using litellm
            return LLM(model="ollama/llama3.2:1b-instruct-q8_0", base_url="http://localhost:11434")

        # Groq llm client
        if type == 'groq' :
            return LLM(model="groq/openai/gpt-oss-20b", base_url="https://api.groq.com/openai/v1")
        
        # OpenAI llm client
        if type == 'openai' :
            #
            if not os.environ.get("OPENAI_API_KEY"):
                os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")
            return LLM(model="openai/llama3.2:1b-instruct-q8_0", base_url="http://localhost:11434/v1")