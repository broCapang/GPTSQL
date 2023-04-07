import os
# import langchain.llms
# import sqlite3
# from langchain.agents import create_sql_agent
# from langchain.agents.agent_toolkits import SQLDatabaseToolkit
# from langchain.sql_database import SQLDatabase
# from langchain.llms.openai import OpenAI
# from langchain.agents import AgentExecutor
# from dotenv import load_dotenv

import openai



def nlp(text):

    os.environ['OPENAI_API_KEY'] = "API KEY"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    SQL_PREFIX = """You are an agent designed to give SQL Query.
    You are given a table and a question.
    You must answer the question using SQL.
    You must answer ONLY SQL Query.
    The table is as follows:
    `Table: Products
    product_id (integer, primary key)
    product_name (varchar(255))
    description (text)
    price (decimal)
    category_id (integer, foreign key)
    Table: Staff
    staff_id (integer, primary key)
    first_name (varchar(255))
    last_name (varchar(255))
    email (varchar(255))`
    The question is as follows:
    """
    complete = SQL_PREFIX + text
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=complete,
        temperature=0,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    output = response
    return output