# 📝 Todo List API

A simple RESTful API for managing your daily tasks, built with Django and Django REST Framework.

---

## 🚀 Features

- 🔐 Authenticated todo CRUD
- 👤 Each user sees only their todos
- 📄 Swagger API docs via drf-yasg
- 🌐 Ready to deploy on [Render](https://render.com)

---

## 🛠️ Setup

```bash
git clone https://github.com/your-username/todo-list-api.git
cd todo-list-api
python -m venv env && source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```


📦 API Endpoints
Method	Endpoint	Description
GET	/api/todos/	List user todos
POST	/api/todos/	Create a new todo
GET	/api/todos/<id>/	Get a specific todo
PUT	/api/todos/<id>/	Update a todo
DELETE	/api/todos/<id>/	Delete a todo

📄 License
MIT License

