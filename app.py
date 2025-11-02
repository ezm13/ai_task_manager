from flask import Flask, render_template, redirect, url_for, request, flash
from extensions import db, login_manager
from config import Config
from models import User, Task
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from ai_helper import analizar_tarea
import os
from flask import jsonify
from ai_helper import analizar_tarea

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash("Credenciales incorrectas.", "danger")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = generate_password_hash(request.form.get('password'))
        
        if not username or not email or not password:
            flash("Por favor completa todos los campos.", "warning")
            return redirect(url_for('register'))

        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash("Registro exitoso, ahora inicia sesión.", "success")
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/dashboard')
@login_required
def dashboard():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
@login_required
def add_task():
    title = request.form.get('title')
    if title:
        categoria, confianza, texto_clave = analizar_tarea(title)
        nueva_tarea = Task(
            title=f"{texto_clave} [{categoria} - {confianza}%]",
            user_id=current_user.id
        )
        db.session.add(nueva_tarea)
        db.session.commit()
        flash(f"Tarea añadida y clasificada como '{categoria}' ({confianza}%)", "success")
    return redirect(url_for('dashboard'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Sesión cerrada.", "info")
    return redirect(url_for('login'))


@app.route('/get_tasks')
@login_required
def get_tasks():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    task_data = [{"id": t.id, "title": t.title} for t in tasks]
    return jsonify({"tasks": task_data})

@app.route('/delete_task/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        flash("No puedes eliminar esta tarea.", "danger")
        return redirect(url_for('dashboard'))
    
    db.session.delete(task)
    db.session.commit()
    flash("Tarea eliminada exitosamente.", "success")
    return redirect(url_for('dashboard'))

@app.route('/ai_assistant', methods=['POST'])
@login_required
def ai_assistant():
    from models import Task
    from ai_helper import analizar_tarea, responder_asistente

    data = request.get_json()
    user_message = data.get("message", "").strip().lower()

    # Respuesta general del asistente local
    respuesta = responder_asistente(user_message)

    # Detectar si el usuario quiere confirmar agregación
    if user_message in ["sí", "si", "claro", "ok", "agrega", "añádelo", "añade"]:
        session_data = getattr(app, 'session_data', None)
        if session_data and session_data.get("last_text"):
            nueva_tarea = Task(
                title=f"{session_data['last_text']} [{session_data['last_category']} - {session_data['last_confidence']}%]",
                user_id=current_user.id
            )
            db.session.add(nueva_tarea)
            db.session.commit()
            app.session_data = {}
            return jsonify({"reply": f"✅ Tarea añadida correctamente ({session_data['last_category']}, {session_data['last_confidence']}%)."})

        return jsonify({"reply": "⚠️ No tengo una tarea pendiente para agregar. Escribe algo nuevo."})

    # Si el mensaje parece una tarea nueva
    categoria, confianza = analizar_tarea(user_message)
    app.session_data = {
        "last_text": user_message,
        "last_category": categoria,
        "last_confidence": confianza
    }

    # Enviar respuesta simulada del asistente
    return jsonify({"reply": respuesta})






if __name__ == '__main__':
    with app.app_context():
        if not os.path.exists('data'):
            os.makedirs('data')
        db.create_all()

    app.run(debug=True)
