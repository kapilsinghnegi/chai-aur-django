# Jinja2 and Django Apps

# Django Apps & Jinja Templates — Concise Notes

 ## 1\. Jinja / Django Templates

 - Django uses the **Django Template Language (DTL)** by default.
- **Jinja** is another popular template engine with very similar syntax.
- Templates allow you to combine:
  - HTML
  - Variables
  - Loops
  - Conditions
  - Template inheritance
  - Static files

 ### Important Jinja Syntax

 | Syntax | Purpose |
| --- | --- |
| `{{ variable }}` | Display/inject a variable |
| `{% ... %}` | Template logic such as loops, conditions, loading static files |
| `{# ... #}` | Template comment |

Example:

```
<h1>{{ name }}</h1>
```

 For template logic:

```
{% if user %}
    Welcome!
{% endif %}
```

---

 ## 2\. Django Project vs Django App

 ### Project

 The **project** is the overall Django website/application.

 It contains important configuration such as:

 - `settings.py`
- Main `urls.py`
- `manage.py`

 You generally create the **project once**.

```
django-admin startproject project_name
```

 ### App

 An **app** is a specific feature/module inside the project.

 Examples:

 - Blog app
- Authentication app
- Products app
- Orders app
- Social media app

 You can create **multiple apps** inside one project.

```
python manage.py startapp chai
```

---

 ## 3\. What `startapp` Creates

 Running:

```
python manage.py startapp chai
```

 creates a structure similar to:

```
chai/
├── migrations/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

 Important files:

 - `views.py` → Handles requests and returns responses.
- `models.py` → Defines database models.
- `admin.py` → Django admin configuration.
- `apps.py` → App configuration.
- `tests.py` → Testing.
- `migrations/` → Database migration files.

---

 ## 4\. Creating an App Is Not Enough

 After creating an app, Django needs to **know that the app exists**.

 Go to:

```
settings.py
```

 and add the app to:

```
INSTALLED_APPS = [
    ...
    'chai',
]
```

 ### Remember:

 > **Create App → Register App in `INSTALLED_APPS`**

 Without registration, Django doesn't properly treat the new app as part of the project.

---

 ## 5\. App-Level Templates

 A common structure is:

```
chai/
├── templates/
│   └── chai/
│       └── all_chai.html
```

 The extra `chai` folder inside `templates` helps keep templates organized and avoids naming conflicts between different apps.

---

 ## 6\. Views → URLs → Templates

 A typical Django request flow is:

```
URL
 ↓
View
 ↓
Template
 ↓
HTML Response
```

 For example:

```
def all_chai(request):
    return render(request, 'chai/all_chai.html')
```

 The view receives the request and renders the template.

---

 ## 7\. App-Level `urls.py`

 A newly created app does **not automatically contain `urls.py`**.

 You can create it manually:

```
chai/
└── urls.py
```

 Example:

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_chai, name='all_chai'),
]
```

---

 ## 8\. Connecting App URLs to Project URLs

 The main project's `urls.py` controls the overall URL structure.

 Use `include()` to transfer URL handling to an app:

```
from django.urls import path, include

urlpatterns = [
    path('chai/', include('chai.urls')),
]
```

 Now:

```
/chai/
```

 is handled by:

```
chai/urls.py
```

 ### Very important concept

```
Project urls.py
        ↓
   include()
        ↓
  App urls.py
        ↓
      View
        ↓
    Template
```

 This keeps each app's URL logic separate and organized.

---

 ## 9\. URL Names

 Example:

```
path('', views.all_chai, name='all_chai')
```

 The `name` is important because Django can use it to refer to the URL programmatically.

 Instead of hardcoding URLs everywhere, you can later use the URL's **name** to generate links.

 ### Why?

 If the URL changes later, you don't have to manually change every HTML link.

---

 ## 10\. Template Inheritance

 One of the most useful features of Django/Jinja templates is **template inheritance**.

 Suppose every page has the same:

 - Navbar
- CSS
- Layout
- Footer
- Basic HTML structure

 Instead of repeating all of that on every page, create a common base template.

 Example:

```
templates/
└── layout.html
```

---

 ## 11\. `{% block %}`

 In the base template:

```
<title>
    {% block title %}Default Title{% endblock %}
</title>

{% block content %}
{% endblock %}
```

 These are **replaceable blocks**.

 A child template can replace them.

---

 ## 12\. `{% extends %}`

 A child template can inherit the base template:

```
{% extends "layout.html" %}
```

 Then override specific blocks:

```
{% block title %}
    Home Page
{% endblock %}

{% block content %}
    <h1>Chai & Code</h1>
{% endblock %}
```

 ### Concept

```
layout.html
     ↓
   extends
     ↓
index.html
```

 The child template **inherits the common structure** and only provides the content that changes.

---

 ## 13\. Why Template Inheritance Is Useful

 Without inheritance:

```
Page 1 → Repeat navbar + CSS + HTML
Page 2 → Repeat navbar + CSS + HTML
Page 3 → Repeat navbar + CSS + HTML
```

 With inheritance:

```
Base Template
      ↓
 ┌────┼────┐
 ↓    ↓    ↓
Home Blog Products
```

 So common code is written **once**.

 > **Write once → Reuse everywhere**

---

 ## 14\. Loading Static Files

 Django templates can load static resources such as:

 - CSS
- JavaScript
- Images

 Using:

```
{% load static %}
```

 This is another example of `{% ... %}` syntax because it performs template logic rather than simply displaying a variable.

---

 ## 15\. Django's Template Search

 Django can look for templates in configured locations.

 A common setup is:

```
app/
└── templates/
    └── app_name/
        └── page.html
```

 You can also configure a project-level templates directory.

 So Django can search through the configured template locations to find the requested template.

---

 # ⭐ Most Important Takeaways

 1. **Project = complete Django project; App = individual feature/module.**
2. Create apps with:

   ```
   python manage.py startapp app_name
   ```
3. Register the app in `INSTALLED_APPS`.
4. Typical flow:

   ```
   URL → View → Template
   ```
5. Apps can have their own `urls.py`.
6. Use `include()` in the main `urls.py` to hand URL control to an app.
7. `name=` gives a URL a reusable name.
8. `{{ }}` → display variables.
9. `{% %}` → template logic/tags.
10. `{% extends %}` → inherit a base template.
11. `{% block %}` → create sections that child templates can replace.
12. **Template inheritance prevents repeated HTML/CSS/navbar code.**