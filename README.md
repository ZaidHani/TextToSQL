
# TextToSQL

TextToSQL is a Python project that allows you to ask questions in natural language and get answers from your SQL Server database. It uses LangChain, Groq LLM, and Streamlit for a simple, interactive experience.

## Features

- Natural language to SQL query generation
- Connects to SQL Server (multiple databases supported via `.env`)
- Only allows safe, read-only (SELECT) queries
- Summarizes and explains query results in plain English
- Streamlit web interface and CLI support

## Quick Start

### 1. Install dependencies

```sh
pip install -r requirements.txt
```

### 2. Configure your environment

Create a `.env` file with your SQL Server and LLM API credentials. Example:

```
SQL_SERVER=your_server
SQL_DATABASE=your_database
GROQ_API_KEY=your_groq_key
```

You can also specify multiple databases with:
```
SQL_DATABASES=DB1;DB2;DB3
```

### 3. Run the app

- **Streamlit UI:**
	```sh
	streamlit run app.py
	```
- **CLI:**
	```sh
	python text_to_sql_chain.py
	```

## How it works

- The app uses LangChain and Groq to convert your question into a safe SQL query.
- It executes the query on your SQL Server database (schema is set to 'Posting' by default in the code).
- The results are summarized and explained in plain English.

## Safety

- Only `SELECT` queries are allowed. Any attempt to run `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, or `ALTER` statements will be blocked.

## Customization

- Edit `text_to_sql_chain.py` to change the default schema or add more advanced logic.
- Add more databases in your `.env` as needed.

## Author

Zaid Hani

