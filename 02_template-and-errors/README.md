# Template and Errors in Django

 ## 1\. Core Django Request–Response Flow

 Django is a **web framework** that follows a simple request → response architecture.

 ### Basic flow

```
User
 ↓
Request
 ↓
Django
 ↓
URL Resolver
 ↓
urls.py
 ↓
views.py
 ↓
Logic / Database / Template
 ↓
Response
 ↓
Browser
```

---

 ## 2\. URL Resolver & `urls.py`

 When a user requests something like:

```
/login/
/register/
/tweet/123/
```

 Django's internal **URL Resolver** determines where the request should go.

 It then uses `urls.py` to identify the appropriate view.

 ### Important distinction

 - **URL Resolver** → Django's internal mechanism that resolves URLs.
- **`urls.py`** → Where we define URL-to-view mappings.
- Large projects can have **multiple URL files** for different apps/modules.

 Example:

```
path("", views.home, name="home")
path("about/", views.about, name="about")
path("contact/", views.contact, name="contact")
```

 ### Memory trick

 > **`urls.py` = Which view should handle this URL?**

---

 ## 3\. `views.py` — Main Logic

 `views.py` contains the application's main logic.

 A view can:

 - Return a direct response.
- Communicate with the database.
- Use `models.py`.
- Render an HTML template.
- Perform other application logic.

 Example:

```
from django.http import HttpResponse

def home(request):
    return HttpResponse("You are at Chai and Django Home Page")
```

 ### Important points

 - A view receives a **request**.
- A view returns a **response**.
- The function name can generally be chosen by the developer.
- Django expects the file to follow the conventional name **`views.py`**.

---

 ## 4\. Connecting URLs to Views

 First import the views:

```
from . import views
```

 Then connect each URL to its view:

```
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
```

 ### Example mapping

 | URL | View |
| --- | --- |
| `/` | `home()` |
| `/about/` | `about()` |
| `/contact/` | `contact()` |

The `name` parameter gives a URL a reusable name.

```
path("about/", views.about, name="about")
```

---

 ## 5\. Running the Django Server
To run: 

```
python manage.py runserver
```

 ### If `manage.py` isn't found

 Check the current directory:

```
ls
```

 Then move into the correct Django project directory.

 ### Remember

 > **`manage.py` directory → Run Django commands**

---

 ## 6\. Django Templates

 Returning plain text using `HttpResponse` is useful for testing, but real websites usually return **HTML pages**.

 Templates contain HTML.

 Typical structure:

```
project/
├── manage.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── project/
    └── settings.py
```

---

 ## 7\. `render()` — Returning Templates

 Instead of:

```
return HttpResponse("Hello World")
```

 Use:

```
from django.shortcuts import render

def home(request):
    return render(request, "index.html")
```

 ### Remember

 > **`render()` = Load HTML template + return response**

 The view still receives the request because Django needs the request information while processing the page.

---

 ## 8\. Configuring the Templates Directory

 If Django doesn't automatically know where your templates are, configure the directory in `settings.py`.

```
TEMPLATES = [
    {
        ...
        "DIRS": [BASE_DIR / "templates"],
        ...
    },
]
```

 This tells Django:

 > **Look inside `BASE_DIR/templates/` for templates.**

 Templates can be organized into folders.

```
templates/
└── website/
    └── index.html
```

 Then:

```
return render(request, "website/index.html")
```

 ### Why use subfolders?

 Useful for keeping templates organized when a project contains multiple applications or sections.

---

 ## 9\. Django Template Engine

 Django's template system allows you to inject dynamic/programmatic information into HTML.

 Two important syntaxes:

 ### `{% ... %}`

 Used for **template instructions/tags**.

 Example:

```
{% load static %}
```

 ### `{{ ... }}`

 Used to **display values**.

 ### Easy memory trick

 > **`{% %}` → Do something**\
>  **`{{ }}` → Show something**

---

 ## 10. Static Files

 Static files are frontend assets that don't normally change for each request.

 Examples:

 - CSS
- JavaScript
- Images

 Typical structure:

```
static/
└── style.css
```

---

 ## 11\. Loading CSS in Django

 You should not simply reference the CSS file with a normal relative path and expect Django's static-file system to handle it.

 Instead, use Django's **static template tag**.

 At the top of the template:

```
{% load static %}
```

 Then:

```
<link rel="stylesheet" href="{% static 'style.css' %}">
```

 ### Why `{% load static %}`?

 Without loading the static tag library, Django can produce an error such as:

```
Invalid block tag: 'static'
```

 ### Memory trick

 > **Load static → Use static**

---

 ## 12\. Static Files Configuration

 In `settings.py`, configure where Django should find static files.

```
STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

 ### Meaning

 | Setting | Purpose |
| --- | --- |
| `STATIC_URL` | URL prefix for static files |
| `STATICFILES_DIRS` | Tells Django where static files are located |

---

 ## 13\. Why Direct CSS Paths Can Fail

 A path such as:

```
<link rel="stylesheet" href="../static/style.css">
```

 is not the preferred Django approach.

 Instead use:

```
{% load static %}
<link rel="stylesheet" href="{% static 'style.css' %}">
```

 Django's template/static system generates the appropriate URL.

---

 ## 14\. `os` and `BASE_DIR`

 Django's settings use a base directory to construct project paths.

 A common configuration is:

```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
```

 Conceptually:

 > **BASE\_DIR + static → Full static-files location**

 This makes paths more portable across different environments.

---

 ## 15\. Complete Flow With Templates & CSS

```
Browser
   ↓
Request
   ↓
Django
   ↓
URL Resolver
   ↓
urls.py
   ↓
views.py
   ↓
Application Logic
   ↓
render()
   ↓
HTML Template
   ↓
Static CSS / JS / Images
   ↓
Response
   ↓
Browser
```

---

 # 🧠 Final Django Cheat Sheet

 | Component | Job |
| --- | --- |
| **URL Resolver** | Resolves incoming URL |
| **`urls.py`** | Maps URL → View |
| **`views.py`** | Contains application logic |
| **`models.py`** | Database-related structure/data |
| **`render()`** | Returns an HTML template |
| **Templates** | Store HTML |
| **`static/`** | CSS, JS, images |
| **`settings.py`** | Project configuration |
| **`manage.py`** | Django management commands |
| **`{% load static %}`** | Loads static template tags |
| **`{% static 'file.css' %}`** | Generates static-file URL |
| **`BASE_DIR`** | Base project directory |


 - **`urls.py` → Where should the request go?**
- **`views.py` → What should happen?**
- **`render()` → Which HTML should be returned?**
- **`templates/` → HTML files**
- **`static/` → CSS, JS, images**
- **`{% %}` → Template instructions**
- **`{{ }}` → Display values**
- **`{% load static %}` → Enable static tags**
- **`{% static 'style.css' %}` → Load static CSS**
- **`settings.py` → Tell Django where things are located**