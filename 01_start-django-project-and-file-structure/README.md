# Django - Introduction and File Structure

 ## 1\. What is Django?

 - **Django is a mature Python web framework** designed for **rapid development**.
- It is known for being:
  - Very fast to develop with
  - Secure by default
  - Scalable
  - Production-ready
- Django should not be directly compared with JavaScript frameworks like **Express, NestJS, or Gatsby** because their approaches are different.
- Comparisons with **Laravel** or **Ruby on Rails** are more reasonable.

 ## 2\. Why Django is popular

 - You can build applications with relatively **less code**.
- Many security protections are provided **out of the box**.
- It can scale well even on relatively modest infrastructure.
- It is widely used in production and is attractive to companies because of its scalability and mature ecosystem.

---

 ## 3\. UV – Faster Python Package Manager

 UV is an **extremely fast Python package/dependency manager**, written in Rust.

 Creating a virtual environment:

```
uv venv
```

 Installing Django:

```
uv pip install Django
```

---

 ## 4\. Creating a Django Project

 After installing Django, the main command introduced is:

```
django-admin
```

 Two important concepts:

 - `startproject` → creates the **main Django project**
- `startapp` → creates an individual **application inside the project**

 To create a new project:

```
django-admin startproject <project_name>
```

 This creates the Django project structure.

 ### Typical structure

```
project_name/
│
├── manage.py
│
└── project_name/
    ├── settings.py
    ├── urls.py
    ├── ...
```

 The extra inner folder is **normal and intentional**. It is a standard Django project structure.

---

 ## 5\. `manage.py`

 `manage.py` is one of the most important files.

 It acts as the **main command-line entry point** for your Django project.

 For example:

```
python manage.py runserver
```

 You use it for many Django management operations.

---

 ## 6\. Running the Django Server

 Command:

```
python manage.py runserver
```

 By default, Django runs on:

```
http://127.0.0.1:8000/
```

---

 ## 7\. SQLite Database

 When the project is created, Django automatically creates:

```
db.sqlite3
```

 SQLite is Django's **default database**.

 An important advantage is that Django's database abstraction allows you to change databases later.

 For example, you can move between:

 - SQLite
- PostgreSQL
- MySQL

 without rewriting your entire application/database logic.

 Django also supports NoSQL databases through appropriate tools, although traditional SQL databases are common in Django applications.

---

 ## 8\. Django's Important Files

 ### `settings.py`

 Contains the **project-wide configuration**.

 Examples include:

 - Database configuration
- Installed apps
- Middleware
- Authentication settings
- Language
- Time zone
- Static files
- Other Django settings

---

 ### `urls.py`

 Controls **URL routing**.

 It determines which URL should be handled by which part of the application.

---

 ### `views.py`

 Contains the application's **views/business logic**.

 A view receives a request and decides what response should be returned.

 For example, it might return:

 - HTML
- JSON
- Text
- Other responses

---

 ### `models.py`

 Defines the **data/database models**.

 This is where you describe the structure of the application's data.

---

 ## 9\. Django's Basic Request Flow

```
User
  ↓
URL
  ↓
urls.py
  ↓
View
  ↓
Business Logic
  ↓
Database / Other Services
  ↓
Response
```

 In simple terms:

 1. User visits a URL.
2. Django's `urls.py` determines which route matches.
3. The corresponding view handles the request.
4. The view performs the required logic.
5. It may interact with models/database.
6. A response is returned to the user.

---

 ## 10\. Django Apps

 A Django project is usually divided into **multiple smaller apps**.

 For example, an e-commerce project might have:

```
Project
├── products
├── categories
├── coupons
├── checkout
└── users
```

 Each app can contain its own logic and can interact with other apps.

 ### Why?

 - Better organization
- Separation of concerns
- Easier teamwork
- Easier maintenance
- Reusable components

---

 ## 11\. Django's Built-in Features

 Django provides many features **out of the box**, including:

 - Authentication
- Admin panel
- Middleware
- Security protections
- Sessions
- Password validation
- CSRF protection
- Clickjacking protection
- Database abstraction
- Template system

 This is one of Django's major strengths.

---

 ## ⭐ Most Important Takeaways

 - **Django = Python framework for rapid web development.**
- It is **mature, secure, scalable, and production-oriented**.
- Use a **virtual environment** for each project.
- **UV** can be used for fast Python environment/package management.
- `django-admin startproject` → creates a Django project.
- `manage.py` → project's command-line entry point.
- `runserver` → starts the development server.
- Default port → **8000**.
- `settings.py` → configuration.
- `urls.py` → routing.
- `views.py` → business/request logic.
- `models.py` → database/data structure.
- Django projects are commonly divided into **multiple apps**.
- SQLite is the default database.
- Django provides many **security and development features automatically**.