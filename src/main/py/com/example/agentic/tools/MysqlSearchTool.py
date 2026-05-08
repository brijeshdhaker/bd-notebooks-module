import os
from crewai import Agent, Crew, Process, Task
from crewai.tools import tool
from crewai_tools import MySQLSearchTool
from com.example.agentic.tools.config import _rag_tool_config






# Initialize the tool with the database URI and the target table name
mysqluser = os.environ["MYSQL_ADMIN_USER"]
mysqlpass = os.environ["MYSQL_ADMIN_PASSWORD"]
mysql_uri = f"mysql://{mysqluser}:{mysqlpass}@mysqlserver.sandbox.net:3306/SANDBOXDB"
tool = MySQLSearchTool(
    db_uri=mysql_uri,
    table_name='CUSTOMERS',
    config=_rag_tool_config
)

print(tool.run("select * from CUSTOMERS"))

# from crewai_tools import NL2SQLTool
# nl2sql = NL2SQLTool(
#     db_uri=f'mysql+pymysql://{mysqluser}:{mysqlpass}@mysqlserver.sandbox.net:3306/SANDBOXDB',
#     allow_dml=True,
#     #tables=['CUSTOMERS']
# )

# print(nl2sql.run("list CUSTOMERS who live in city Hyderabad"))

#nl2sql.run("Retrieve the average, maximum, and minimum monthly revenue for each city,"
#           "but only include cities that have more than one user. Also, count the number"
#           "of user in each city and sort the results by the average monthly revenue in descending order")