import streamlit as st
st.title('Simple To-Do list')
if "all_task" not in st.session_state:
        st.session_state.all_task = []
my_tasks = st.text_input('What tasks u want to do today ?')
if st.button('Add'):
    st.session_state.all_task.append(my_tasks)
    st.write("Current List:", st.session_state.all_task)
    



    