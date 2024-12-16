import streamlit as st
from database import get_tasks, add_task, update_task_status, delete_task, update_task
from models import SessionLocal, Status

import pandas as pd

# Configuración de la aplicación
st.set_page_config(page_title="To-Do App", layout="centered")

# Cargar estados desde la base de datos
def load_statuses():
    session = SessionLocal()
    statuses = session.query(Status).all()
    session.close()
    return {status.name: status.id for status in statuses}

# Función principal
def main():
    st.title("To-Do App con Streamlit")
    st.subheader("Organiza tus tareas de manera sencilla")


    st.header("➕ Añadir nueva tarea")
    title = st.text_input("Titulo")
    status = st.selectbox("Estado", options=list(load_statuses().keys()))
    description = st.text_area("Description", placeholder="Escribe una breve descripcion de tu tarea")
    if st.button("Añadir"):
        if title:
            add_task(title, description, status)
            st.success("Task added!")
        else:
            st.error("Title is required!")

    # Sección: Mostrar tareas existentes
    st.header("📋 Lista de tareas")


    tasks = get_tasks()
    if not tasks:
        st.info("No hay tareas disponibles.")
    else:
        for task in tasks:
            with st.container():
                cols = st.columns([5, 4, 2, 2])
                with cols[0]:
                    st.write(f"**{task['title']}**")
                    st.caption(task["description"])
                with cols[1]:
                    st.write(f"Estado: `{task['status']}`")
                with cols[2]:
                    if st.button("Edit", key=f"edit_task_form_{task['id']}"):
                        open_edit_modal(task, load_statuses().keys(), status)           
                with cols[3]:
                    if st.button("Delete", key=f"delete_{task['id']}", type="primary"):
                        #st.warning(f"Tarea '{task['title']}' eliminada.")
                        delete_task(task["id"])
                        st.rerun()

#Descargar las tareas en formato json

def get_tasks_json():
    try:
        # Consultar todas las tareas
        tasks = get_tasks()
        # Crear un DataFrame a partir de los datos
        df = pd.DataFrame(tasks)

        # Exportar a JSON
        return df.to_json(orient="records", indent=4, force_ascii=False)

    except Exception as e:
        st.error(f"Error exportando las tareas")
        return None




# Sección de Streamlit para exportar tareas
st.sidebar.title("Exportar Datos")
if st.sidebar.button("Exportar Tareas a JSON"):
    json_data = get_tasks_json()
    if json_data:
        # Crear botón para descargar el archivo JSON
        st.sidebar.download_button(
            label="Descargar JSON",
            data=json_data,
            file_name="tasks.json",
            mime="application/json"
        )
        st.sidebar.success("Archivo generado y listo para descargar.")
    else:
        st.sidebar.error("No se pudo generar el archivo JSON.")
# Función para abrir un modal de edición
@st.dialog("Edita tu tarea...")
def open_edit_modal(task, statuses, actualState):
    with st.form(f"edit_task_form_{task['id']}"):
        st.subheader("Editar tarea")
        updated_title = st.text_input("Título", value=task['title'])
        updated_description = st.text_area("Descripción", value=task['description'])
        updated_status = st.selectbox("Estado", options=list(statuses), index=list(statuses).index(actualState))
        submitted = st.form_submit_button("Guardar cambios")
        print(statuses, actualState)
        if submitted:
            update_task(task['id'], updated_title, updated_description, updated_status)
            st.success(f"Tarea '{task['title']}' actualizada.")
            st.rerun()

if __name__ == "__main__":
    main()
