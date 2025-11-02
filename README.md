 🤖 AI Task Manager

**AI Task Manager** es una aplicación web desarrollada en **Flask** que combina un gestor de tareas con un **asistente de inteligencia artificial local**.  
Permite crear, clasificar y gestionar tus tareas diarias con ayuda de un asistente conversacional completamente **offline**, sin depender de conexión a la API de OpenAI.

---

## 🧩 Características principales

✅ **Gestión de usuarios** — Registro, inicio y cierre de sesión con autenticación segura.  
✅ **Panel de control (Dashboard)** — Visualiza, agrega y elimina tareas fácilmente.  
✅ **Asistente IA local** — Interactúa por chat y analiza automáticamente tus tareas por categoría.  
✅ **Modo 100% offline** — No requiere conexión a internet ni API externa.  
✅ **Persistencia de datos** — Las tareas se almacenan en una base de datos SQLite local.  
✅ **Diseño moderno oscuro** — Interfaz limpia y elegante con Bootstrap + CSS personalizado.

---

## 🧠 Tecnología utilizada

| Tecnología | Descripción |
|-------------|--------------|
| 🐍 **Python 3.13** | Lenguaje principal del proyecto |
| ⚙️ **Flask** | Framework backend ligero |
| 💾 **SQLite** | Base de datos local |
| 🎨 **Bootstrap 5** | Estilos y diseño responsive |
| 🤖 **IA local (simulada)** | Motor de análisis y conversación sin conexión |
| 🔒 **Flask-Login** | Autenticación de usuarios |

---

## 🚀 Instalación y ejecución

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/ezm13/ai_task_manager.git
cd ai_task_manager
2️⃣ Crear entorno virtual e instalar dependencias
bash
Copy code
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
💡 Si no tienes el archivo requirements.txt, puedes generarlo con:

bash
Copy code
pip freeze > requirements.txt
3️⃣ Crear carpeta de datos
bash
Copy code
mkdir -p data
chmod 777 data
4️⃣ Ejecutar la aplicación
bash
Copy code
python app.py
Luego abre en tu navegador:
👉 http://127.0.0.1:5000

💬 Ejemplo de interacción
yaml
Copy code
👤 Usuario: hola  
🤖 Asistente: ¡Hola! Soy tu asistente IA local. ¿Listo para planificar tu día?

👤 Usuario: quiero aprender flask avanzado  
🤖 Asistente: 📊 Parece relacionado con **aprendizaje** (84.3%). ¿Quieres que lo agregue como tarea?

👤 Usuario: sí  
🤖 Asistente: ✅ Tarea añadida correctamente (aprendizaje, 84.3%).
🗂️ Estructura del proyecto
arduino
Copy code
ai_task_manager/
├── app.py
├── ai_helper.py
├── config.py
├── extensions.py
├── models.py
├── data/
│   └── tasks.db
├── static/
│   └── style.css
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── login.html
│   └── register.html
└── README.md
✨ Autor
👤 Eroz Meléndez
📧 eroz@example.com
💻 Estudiante de Ingeniería en Sistemas
🌍 Costa Rica

🧾 Licencia
Este proyecto está bajo la licencia MIT.
Puedes usarlo, modificarlo y mejorarlo libremente mencionando al autor original.