import streamlit as st
from database import get_tasks, add_task, update_task, delete_task
from models import SessionLocal, Status

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

    # Cargar estados
    statuses = load_statuses()

    # Variables de estado para edición
    if "edit_mode" not in st.session_state:
        st.session_state.edit_mode = False
    if "current_task" not in st.session_state:
        st.session_state.current_task = None

    # Sección: Mostrar tareas existentes
    st.header("📋 Lista de tareas")
    tasks = get_tasks()
    st.dataframe(tasks)
    if not tasks:
        st.info("No hay tareas disponibles.")
    else:
        for task in tasks:
            with st.container():
                cols = st.columns([3, 2, 1, 1])
                with cols[0]:
                    st.write(f"**{task['title']}**")
                    st.caption(task['description'])
                with cols[1]:
                    st.write(f"Estado: `{task['status']}`")
                with cols[2]:
                    if st.button("Editar", key=f"edit_{task['id']}"):
                        enter_edit_mode(task)
                with cols[3]:
                    if st.button("Eliminar", key=f"delete_{task['id']}"):
                        delete_task(task['id'])
                        st.warning(f"Tarea '{task['title']}' eliminada.")
                        st.rerun()

    # Sección: Agregar/Editar tareas
    st.header("cccAgregar/Editar tarea")
    with st.form("task_form"):
        # Campos del formulario
        title = st.text_input("Título de la tarea", max_chars=100, value=(st.session_state.current_task['title'] if st.session_state.edit_mode else ""))
        description = st.text_area("Descripción", max_chars=300, value=(st.session_state.current_task['description'] if st.session_state.edit_mode else ""))
        status_name = st.selectbox(
            "Estado",
            options=list(statuses.keys()),
            index=(list(statuses.keys()).index(st.session_state.current_task['status']) if st.session_state.edit_mode and st.session_state.current_task else 0)
        )
        
        # Botones del formulario
        submitted = st.form_submit_button("Guardar")
        if submitted:
            if title.strip():
                if st.session_state.edit_mode:  # Modo edición
                    update_task(
                        task_id=st.session_state.current_task['id'],
                        title=title,
                        description=description,
                        status_name=status_name,
                    )
                    st.success(f"Tarea '{title}' actualizada correctamente.")
                    st.session_state.edit_mode = False
                    st.session_state.current_task = None
                else:  # Modo añadir
                    add_task(title=title, description=description, status_name=status_name)
                    st.success(f"Tarea '{title}' agregada correctamente.")
                st.rerun()
            else:
                st.error("El título de la tarea no puede estar vacío.")

# Componente para mostrar una tarea
   

# Función para entrar al modo de edición
def enter_edit_mode(task):
    st.session_state.edit_mode = True
    st.session_state.current_task = task

if __name__ == "__main__":
    main()
