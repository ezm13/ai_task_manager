## 🚀 Installation & Execution

### 1️⃣ Clone the repository
```bash
git clone https://github.com/ezm13/ai_task_manager.git
cd ai_task_manager
2️⃣ Create virtual environment and install dependencies
bash
Copy code
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
💡 If you don’t have the requirements.txt file, you can generate it with:

bash
Copy code
pip freeze > requirements.txt
3️⃣ Create the data folder
bash
Copy code
mkdir -p data
chmod 777 data
4️⃣ Run the application
bash
Copy code
python app.py
Then open your browser and go to:
👉 http://127.0.0.1:5000

💬 Example Interaction
👤 User: hello
🤖 Assistant: Hi! I’m your local AI assistant. Ready to plan your day?

👤 User: I want to learn advanced Flask
🤖 Assistant: 📊 It seems related to **learning** (84.3%). Would you like me to add it as a task?

👤 User: yes
🤖 Assistant: ✅ Task successfully added (learning, 84.3%).

🗂️ Project Structure
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
✨ Author
👤 Eroz Meléndez
📧 eroz@example.com
💻 Systems Engineering Student
🌍 Costa Rica

🧾 License
This project is licensed under the MIT License.
You can freely use, modify, and improve it as long as proper credit is given to the original author.