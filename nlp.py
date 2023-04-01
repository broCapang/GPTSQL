import pandas as pd
import os
import langchain.llms
import sqlite3
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor





def nlp(text):

    os.environ['OPENAI_API_KEY'] = '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'
    # Close the database connection
    # connection.close()

    SQL_PREFIX = """You are an agent designed to interact with a SQL database.
    Given an input question, create a syntactically correct {dialect} query to run, then look at the results of the query and return the syntatically correct {dialect} query itself as an answer not the results.
    Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most {top_k} results.
    You can order the results by a relevant column to return the most interesting examples in the database.
    Never query for all the columns from a specific table, only ask for a the few relevant columns given the question.
    You have access to tools for interacting with the database.
    Only use the below tools. Only use the information returned by the below tools to construct your final answer.
    You MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.
    DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.
    If the question does not seem related to the database, just return "I don't know" as the answer.
    """

    db = SQLDatabase.from_uri("sqlite:///./test.db")
    toolkit = SQLDatabaseToolkit(db=db)

    agent_executor = create_sql_agent(
        llm=OpenAI(temperature=0),
        toolkit=toolkit,
        verbose=False,
        prefix = SQL_PREFIX
    )

    output = str(agent_executor.run(text))
    return output