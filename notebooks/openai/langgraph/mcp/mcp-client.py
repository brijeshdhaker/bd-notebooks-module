#
# python notebooks/openai/langgraph/mcp/mcp-client.py
#
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from dotenv import load_dotenv

import asyncio

async def main():
    #
    client = MultiServerMCPClient({
        "math":{
            "command":"python",
            "args":["/home/brijeshdhaker/ideaProjects/bd-notebooks-module/notebooks/openai/langgraph/mcp/mathserver.py"],           # Put absolute path here
            "transport":"stdio"
        },
        
        "weather":{
            "url":"http://127.0.0.1:8000/mcp",  # Ensure Server is Running Here
            "transport":"streamable_http"
        },
    })
    
    #
    import os
    import getpass
    from langchain.chat_models import init_chat_model

    #
    if not os.environ.get("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")

    tools = await client.get_tools()
    model=init_chat_model(model="groq:openai/gpt-oss-20b")
    agent = create_agent(model, tools)


    math_response = await agent.ainvoke({
        "messages":[{
            "role":"user", "content": "What is (3 + 5)*12 ?"
        }]
    })

    print("math_response : " + math_response["messages"][-1].content)


    weather_response = await agent.ainvoke({
        "messages":[{
            "role":"user", "content": "What is weather in 'Mumbia' ?"
        }]
    })

    print("weather_response : " + weather_response["messages"][-1].content)

# To call async method 
asyncio.run(main())