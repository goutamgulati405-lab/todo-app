import streamlit as st

st.title("📝 TaskMate")
st.subheader("🤝 To-Do List")
st.write("Plan it. Do it. Complete it. 🚀")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

task = st.text_input("Enter your task:")

if st.button("Add Task"):
    if task:
        st.session_state.tasks.append(task)
        st.success("Task added successfully!")

st.subheader("📋 My Tasks")

for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.write(f"☐ {task}")
    with col2:
        if st.button("Delete", key=i):
            st.session_state.tasks.pop(i)
            st.rerun()

st.divider()
st.caption("💻 Created by Goutam Gulati | BCA Student")
