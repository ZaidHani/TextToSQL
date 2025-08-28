# TextToSQL: Natural Language to SQL for Multiple Databases

TextToSQL is a Python project that enables users to ask questions in natural language and get answers from multiple SQL Server databases and schemas. It leverages LLMs (like Groq/OpenAI) and LangChain to generate, execute, and analyze SQL queries, supporting both agentic and RAG (Retrieval-Augmented Generation) workflows.

## Features
- **Multi-database and multi-schema support**
- **Agentic RAG pipeline**: Combines agent reasoning with vector database retrieval for scalable, context-aware SQL generation
- **Cross-database querying and analysis**
- **Schema and relationship awareness** (including foreign keys and cross-db relationships)
- **Safe execution**: Only allows SELECT queries by default
- **Streamlit UI and CLI support**

## Quick Start

### 1. Clone the repository
```sh
git clone https://github.com/ZaidHani/TextToSQL.git
cd TextToSQL
```

### 2. Install dependencies
```sh
pip install -r requirements.txt
```

### 3. Configure your environment
Create a `.env` file (see `.env.example`) with your SQL Server and LLM API credentials. Example:
```
SQL_SERVER=your_server
SQL_DATABASES=DB1,dbo;DB2,Fact;DB3,Posting
GROQ_API_KEY=your_groq_key
```

### 4. Run the agent or chain
- **Agent (multi-db, cross-db analysis):**
	```sh
	python text_to_sql_agent.py
	```
- **Chain (single-db, RAG-style):**
	```sh
	python text_to_sql_chain.py
	```
- **Streamlit app:**
	```sh
	streamlit run app.py
	```

## How It Works
- **Agentic RAG:**
	- Uses a vector database to store schema/table/relationship info (from DDL or live introspection)
	- Agent retrieves relevant schema context and plans multi-step/cross-db queries
- **Chain:**
	- Retrieves relevant schema info and generates SQL for a single DB/schema

## Schema Ingestion
- You can ingest schema info from live DBs or from `CREATE TABLE` scripts (DDL)
- Relationships and foreign keys are included for better cross-db reasoning

## Safety
- By default, only `SELECT` queries are allowed (no `CREATE`, `ALTER`, `DROP`, etc.)
- Prompts and runtime checks enforce this

## Customization
- Add more databases/schemas in your `.env`
- Extend schema ingestion to include descriptions, relationships, or sample data
- Swap LLMs (Groq, OpenAI, Azure, etc.) as needed

## License
MIT

## Author
Zaid Hani
This project uses langchain to create an app that uses text to sql, the app will query the data from sql server database, read the results of the query and extracts valuable info about it for analysis.

