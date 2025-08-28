import streamlit as st
import text_to_sql_chain

st.title('Text to SQL Agent 🦜⛓️📊')

st.write('''
TextToSQL lets you ask questions in natural language and get answers from your SQL Server database. Powered by LangChain and Groq, it generates safe, read-only SQL queries, executes them, and summarizes the results in plain English. Only SELECT queries are allowed for safety. Configure your connection in the .env file and start exploring your data!
''')

query = st.text_area('Enter your question:', height=150)

if st.button('Get Answer'):
    if not query.strip():
        st.warning('Please enter a question.')
    else:
        with st.spinner('Generating answer...'):
            try:
                answer = text_to_sql_chain.main(query)
                st.subheader('Answer:')
                st.write(answer)
            except Exception as e:
                st.error(f'Error: {e}')