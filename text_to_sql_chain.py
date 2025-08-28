import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains.sql_database.query import create_sql_query_chain
from langchain_community.utilities.sql_database import SQLDatabase
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers.string import StrOutputParser

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment
sql_server = os.getenv('SQL_SERVER')
sql_database = os.getenv('SQL_DATABASE')
groq_api_key = os.getenv('GROQ_API_KEY')

# Set up the language model
llm = ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    temperature=0,
    reasoning_format="hidden",
)

# Connect to SQL Server using LangChain's SQLDatabase
db_uri = f"mssql+pyodbc://{sql_server}/{sql_database}?driver=ODBC+Driver+17+for+SQL+Server"
db = SQLDatabase.from_uri(db_uri, schema='Posting', engine_args={'isolation_level':'READ COMMITTED'})

def get_schema(_):
    return db.get_table_info()

def run_query(query):
    print('Running this query', query)
    return db.run(query, execution_options={'isolation_level':'READ COMMITTED'})

def write_sql_query(llm):
    template = """write a T-SQL query that would answer the question below based on the schema provided do NOT explain what you do. no pre-amble. Do not include any Markdown code fences (, sql, etc.). Only return the raw SQL text.
    {schema}
    
    Question: {question}"""

    prompt = ChatPromptTemplate.from_messages(
        [
            ('system', '''given an input question, convert it to a T-SQL query, do NOT return anything except the query, do NOT explain what you do, no pre-amble. Do not include any Markdown code fences (, sql, etc.). Only return the raw SQL text.'''),
            ('human', template)
        ]
    )
    return (
        RunnablePassthrough.assign(schema=get_schema)
        | prompt
        | llm
        | StrOutputParser()
        )

def answer_query(query, llm):
    template = '''Based on the table schema below, questoin, sql query and the sql response, write a natural language response, no pre-amble.
    {schema}
    
    Questoin: {question}
    SQL Query: {query}
    SQL Response: {response}'''

    prompt_reponse = ChatPromptTemplate.from_messages(
        [
            ('system',
             'given an input and a sql response, convert it to a natural language answer, if there were no answer then feel free to tell the user so.'),
             ('human',
              template)
        ]
    )

    full_chain = (
        RunnablePassthrough.assign(query=write_sql_query(llm))
        | RunnablePassthrough.assign(
            schema=get_schema,
            response=lambda x: run_query(x['query']))
        | prompt_reponse
        | llm
        | StrOutputParser()
        )
    return full_chain.invoke({'question': query})

def main(query:str):    
    forbidden_statements = ['insert', 'update', 'delete', 'create', 'drop', 'alter']
    if any(stmt in query.lower() for stmt in forbidden_statements):
        raise ValueError("Please ask the agent for queries and not to modify the database.")
    return answer_query(query, llm)


if __name__ == "__main__":
    main()
