import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My To-Do App")
st.subheader("This is my todo app.")
st.write("This app helps you to increase your productivity.")

#st.checkbox("Buy new car.") #for single todo

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label=" ", placeholder="Add new todo",
              on_change=add_todo, key="new_todo")

#st.session_state # it is a session of the object with dictionary type which store the value as key value pair