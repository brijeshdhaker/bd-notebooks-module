#
# python src/main/py/com/example/rag/mcp/weatherserver.py
#
from mcp.server.fastmcp import FastMCP

#mcp server name
mcp = FastMCP("MCP Server")

@mcp.tool()
def getWeather(location: str) -> str:
    """_summary_
    get weather for location
    """
    return f"Its always raining in {location} !!!"

#
if __name__ == "__main__":
    mcp.run(transport="streamable-http")
