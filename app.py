import streamlit as st
import text_to_sql_chain

st.title('Text to SQL Agent 🦜⛓️📊')

st.write('''
This app demonstrates a multi-database Text-to-SQL agent using LangChain and Groq. It can connect to multiple SQL databases/schemas, generate SQL queries from natural language questions, execute them, and summarize the results.''')

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