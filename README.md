AI Task Manager is a web application built with Flask, combining a task manager with a local artificial intelligence assistant.
It allows you to create, classify, and manage your daily tasks through a conversational AI interface — working 100% offline, without requiring OpenAI API access.

🧩 Key Features

✅ User Management — Secure registration, login, and logout.
✅ Dashboard — Easily view, add, and delete your tasks.
✅ Local AI Assistant — Chat and automatically categorize your tasks.
✅ Offline Mode — Works completely without internet.
✅ Data Persistence — Uses SQLite local storage.
✅ Modern UI — Clean dark interface with Bootstrap + custom CSS.

🚀 Installation & Execution
1️⃣ Clone the repository
git clone https://github.com/ezm13/ai_task_manager.git
cd ai_task_manager

2️⃣ Create virtual environment & install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


💡 If you don’t have requirements.txt, generate it with:

pip freeze > requirements.txt

3️⃣ Create data folder
mkdir -p data
chmod 777 data

4️⃣ Run the app
python app.py


Then open your browser:
👉 http://127.0.0.1:5000

💬 Example Interaction

👤 User: hello
🤖 Assistant: Hi! I’m your local AI assistant. Ready to plan your day?

👤 User: I want to learn advanced Flask
🤖 Assistant: 📊 It seems related to **learning** (84.3%). Would you like me to add it as a task?

👤 User: yes
🤖 Assistant: ✅ Task successfully added (learning, 84.3%).

🧾 License

This project is licensed under the MIT License.
You can freely use, modify, and improve it as long as proper credit is given to the original author.