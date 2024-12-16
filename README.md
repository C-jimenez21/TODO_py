

# 📝 To-Do App  

Una aplicación de lista de tareas sencilla pero funcional, desarrollada para organizar y gestionar tareas personales o laborales. Esta aplicación utiliza tecnologías modernas para manejar datos de manera eficiente y presenta una interfaz de usuario interactiva y amigable.  

---

## 📖 Propósito de la Aplicación  

La **To-Do App** permite:  
- Crear tareas con un título, descripción y estado.  
- Editar y actualizar las tareas existentes.  
- Eliminar tareas cuando ya no son necesarias.  
- Visualizar tareas organizadas por su estado.  

Esta aplicación fue diseñada para aprender y demostrar el uso de **Streamlit**, **SQLAlchemy** y otros componentes esenciales para el desarrollo de aplicaciones web ligeras con Python.  

---

## 🛠️ Tecnologías Utilizadas  

- **Python**: Lenguaje de programación principal.  
- **Streamlit**: Framework para crear aplicaciones web interactivas.  
- **SQLAlchemy**: ORM para la gestión de bases de datos.  
- **SQLite**: Base de datos relacional ligera (puede reemplazarse por PostgreSQL o MySQL).  
 

---

## ⚙️ Instalación  

### **Prerrequisitos**  

- Python 3.8 o superior instalado en tu máquina.  
- Git (opcional, pero recomendado para clonar el repositorio).  

### **Pasos de Instalación**  

1. **Clona el repositorio:**  
   ```bash
   git clone https://github.com/C-jimenez21/to-do-app.git
   cd to-do-app
   ```

2. **Crea un entorno virtual (recomendado):**  
   ```bash
   python -m venv venv
   source venv/bin/activate        # Para macOS/Linux
   venv\Scripts\activate           # Para Windows
   ```

3. **Instala las dependencias:**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura la base de datos:**  
   Ejecuta el archivo `database.py` para crear las tablas iniciales:  
   ```bash
   python database.py
   ```

---

## 🚀 Cómo Ejecutar la Aplicación  

1. Asegúrate de que el entorno virtual esté activo.  
2. Ejecuta el siguiente comando:  
   ```bash
   streamlit run app.py
   ```
3. Accede a la aplicación desde tu navegador en [http://localhost:8501](http://localhost:8501).  

---

## 🧑‍💻 Uso de la Aplicación  

### **Inicio**  
Al abrir la aplicación, verás una lista de tareas existentes y un formulario para agregar nuevas tareas.  

### **Funciones principales:**  
1. **Agregar una nueva tarea:**  
   - Completa los campos de título, descripción y estado.  
   - Haz clic en "Guardar".  

2. **Editar una tarea existente:**  
   - Haz clic en el botón "Editar" junto a una tarea para cargarla en el formulario.  
   - Modifica los valores y guarda los cambios.  

3. **Eliminar una tarea:**  
   - Haz clic en el botón "Eliminar" para borrar una tarea de la lista.  

### **Capturas de Pantalla**  
![add task](img/im7.png)
![review task](img/im2.png)
![update task](img/im3.png)
![list task](img/im4.png)
![delete task](img/im5.png)


---

## 🔧 Configuración Adicional  

### Cambiar el motor de base de datos  
Por defecto, se utiliza **SQLite** como base de datos. Si deseas usar **PostgreSQL** o **MySQL**, sigue estos pasos:  
1. Instala el driver correspondiente:  
   - Para PostgreSQL:  
     ```bash
     pip install psycopg2-binary
     ```
   - Para MySQL:  
     ```bash
     pip install pymysql
     ```
2. Actualiza el archivo `models.py` con la URL de tu base de datos. Por ejemplo:  
   ```python
   DATABASE_URL = "postgresql://usuario:contraseña@localhost/nombre_db"
   ```

### Personalización del diseño  
Puedes personalizar la interfaz de usuario modificando el archivo `app.py`. Streamlit facilita la implementación de nuevas funcionalidades y cambios visuales.  

---

## 🧪 Testing  

Para garantizar la calidad del código, se puede analizar con **SonarQube**:  
1. Configura un servidor de SonarQube local o en la nube.  
2. Genera un archivo de análisis:  
   ```bash
   sonar-scanner
   ```
3. Corrige los problemas detectados para mejorar la calidad del código.  

---


## 🧑‍🚀 Autor  

**Cristian Julian Jimenez Celis**  
- [GitHub](https://github.com/C-jimenez21)  


