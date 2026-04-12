#
import os
import getpass
from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI

#
# "groq:llama3–8b-8192"
# "groq:llama3-70b-8192" 
# "groq:openai/gpt-oss-20b"
# "groq:llama-3.1-70b-versatile"

class AgentManager:
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