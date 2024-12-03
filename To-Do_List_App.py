import streamlit as st
import json

st.markdown("""
<h1 style='text-align: center;'>To-Do List</h1>""",
    unsafe_allow_html=True
)

if 'tasks' not in st.session_state:
    st.session_state.tasks = {}

task=st.text_input("Input your task")

if st.button("Submit"):
    if task:

        st.session_state.tasks.update({f"Task{str(len(st.session_state.tasks)+1)}": task})
        st.rerun()

st.write("Your tasks:")
st.write(st.session_state.tasks)
json_data = json.dumps(st.session_state.tasks)

st.download_button(
    label="Download JSON File",
    data=json_data,
    file_name="tasks.json",
    mime="application/json"
)
