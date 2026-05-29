# Handle Models and URLs in Django

 ## 1\. Django Models

 - **Model = Database table** in Django.
- Models are usually written inside an app's `models.py`.
- Django uses an **ORM (Object-Relational Mapping)** to communicate with the database.
- You generally **do not write SQL directly**.
- Because of ORM, you can switch databases such as:
  - SQLite
  - PostgreSQL
  - MySQL
- Much of the Python/Django model code remains the same when changing databases.

 ### Basic model structure

```
from django.db import models

class ChaiVariety(models.Model):
    name = models.CharField(max_length=100)
```

---

 ## 2\. Common Model Fields

 ### `CharField`

 Used for short text.

```
name = models.CharField(max_length=100)
```

 - `max_length` specifies the maximum number of characters.

 ### `TextField`

 Used for longer text such as descriptions.

```
description = models.TextField(default="")
```

 ### `DateTimeField`

 Stores both date and time.

```
from django.utils import timezone

created_at = models.DateTimeField(default=timezone.now)
```

 - `DateField` → only date
- `DateTimeField` → date + time

 ### `ImageField`

 Used for uploaded images.

```
image = models.ImageField(upload_to="chai/")
```

 - Django stores the **image file separately**.
- The database stores information/path related to the image rather than the complete image itself.
- Image handling requires **Pillow**.

 Install:

```
python -m pip install Pillow
```

---

 ## 3\. Restricting Values with Choices

 Sometimes a field should allow only predefined values.

 Example:

```
CHAI_TYPE_CHOICES = [
    ("ML", "Masala"),
    ("GR", "Ginger"),
    ("KT", "Kesar"),
    ("PL", "Plain"),
]

type = models.CharField(
    max_length=2,
    choices=CHAI_TYPE_CHOICES
)
```

 ### Why use `choices`?

 Instead of allowing users to enter anything:

 > Masala, Ginger, Coffee, Pizza, etc.

 you restrict the field to predefined options.

 `choices` = controlled/restricted values.

---

 ## 4\. Handling Images in Django

 For media files, Django needs media settings.

 ### `settings.py`

```
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

 Think of them as:

 - **MEDIA\_URL** → URL through which media is accessed.
- **MEDIA\_ROOT** → physical location where uploaded media is stored.

 You also need to configure media serving in the **main project's `urls.py`** during development.

---

 ## 5\. Migrations 

 Whenever you create or modify a model, Django needs to know that the database structure has changed.

 There are **two main commands**:

 ### Step 1 — Create migration

```
python manage.py makemigrations
```

 This creates migration files describing the database changes.

 ### Step 2 — Apply migration

```
python manage.py migrate
```

 This actually applies those changes to the database.

 > **Model changed → `makemigrations` → `migrate`**

 Migration files essentially contain the instructions Django needs to modify the database.

---

 ## 6\. Django Admin Panel

 Django provides a built-in admin interface.

 To make your model appear there:

 ### `admin.py`

```
from .models import ChaiVariety
from django.contrib import admin

admin.site.register(ChaiVariety)
```

 Now the model can be managed through Django Admin.

 ### Custom display name

 You can define `__str__()` in the model:

```
def __str__(self):
    return self.name
```

 Instead of seeing:

 > ChaiVariety object (1)

 you can see:

 > Large Masala Tea

 > `admin.py` → register model → manage data through Admin.

---

 ## 7\. Getting Data from the Database

 Django ORM lets you query the database without writing SQL.

 Example:

```
chai = ChaiVariety.objects.all()
```

 This retrieves all `ChaiVariety` objects.

 The result can then be passed to a template.

 ### Important ORM idea

```
Model
  ↓
.objects
  ↓
Query
  ↓
Database
  ↓
Results
```

 Common ORM operations include:

 - `.all()`
- `.filter()`
- `.get()`
- `.create()`
- `.count()`
- Aggregation and other query operations

---

 ## 8\. Passing Database Data to Templates

 In a view:

```
def all_chai(request):
    chais = ChaiVariety.objects.all()

    return render(
        request,
        "chai/all_chai.html",
        {"chais": chais}
    )
```

 The third argument is the **context**.

```
{"chais": chais}
```

 It makes the database data available inside the template.

---

 ## 9\. Displaying Data with a Template Loop

 Inside HTML:

```
{% for chai in chais %}
    <h3>{{ chai.name }}</h3>
{% endfor %}
```

 - `{{ variable }}` → **display a value**
- `{% ... %}` → **template logic**

 For example:

```
{{ chai.name }}
{{ chai.description }}
```

 and:

```
{% for chai in chais %}
{% endfor %}
```

---

 ## 10\. Dynamic Detail Pages

 The next step is allowing users to click a particular chai and see its details.

 The flow is:

```
Home/List Page
      ↓
Click a chai
      ↓
URL contains ID
      ↓
View receives ID
      ↓
Database query
      ↓
Detail template
```

---

 ## 11\. Dynamic URL with ID

 Example:

```
path(
    "<int:chai_id>/",
    views.chai_detail,
    name="chai_detail"
)
```

 Here:

```
<int:chai_id>
```

 means:

 - URL should contain an integer.
- That integer is passed to the view as `chai_id`.

 Example:

```
/chai/1/
/chai/2/
/chai/3/
```

---

 ## 12\. `get_object_or_404()`

 For detail pages, Django provides a very useful shortcut:

```
from django.shortcuts import get_object_or_404
```

 Then:

```
chai = get_object_or_404(
    ChaiVariety,
    pk=chai_id
)
```

 Meaning:

 - Find the object with that primary key.
- If found → return it.
- If not found → return **404 Not Found**.

 ### Easy memory trick

 > **Need one object? `get_object_or_404()`**

---

 ## 13\. Named URLs

 Give URLs names:

```
path(
    "<int:chai_id>/",
    views.chai_detail,
    name="chai_detail"
)
```

 Named URLs make it easier to reuse URLs throughout the project.

 Instead of hardcoding:

```
/chai/1/
```

 Django can generate the correct URL dynamically.

---

 ## 14\. Dynamic URL in Templates

 Use Django's `{% url %}` template tag.

 Example:

```
<a href="{% url 'chai_detail' chai.id %}">
    View Details
</a>
```

 The important idea is:

```
URL name + required parameter
```

 So each chai gets its own dynamic URL.

---

 ## 15\. Detail View

 A typical detail view:

```
def chai_detail(request, chai_id):
    chai = get_object_or_404(
        ChaiVariety,
        pk=chai_id
    )

    return render(
        request,
        "chai/chai_detail.html",
        {"chai": chai}
    )
```

 Then in the template:

```
<h1>{{ chai.name }}</h1>
<p>{{ chai.description }}</p>
```

 No loop is necessary because this page represents **one chai object**.

---

 ## 16\. The Complete Django Data Flow

```
MODEL
  ↓
DATABASE
  ↓
ORM QUERY
  ↓
VIEW
  ↓
CONTEXT
  ↓
TEMPLATE
  ↓
HTML PAGE
```

 For a detail page:

```
User clicks chai
      ↓
Dynamic URL /chai/2/
      ↓
URL pattern
      ↓
chai_detail(request, chai_id)
      ↓
get_object_or_404()
      ↓
Database
      ↓
chai object
      ↓
Template
      ↓
Display details
```

---

 # 🔑 Quick Revision

 - **Model** → represents a database table.
- **Field** → represents a column.
- **ORM** → lets Python/Django interact with the database without directly writing SQL.
- **`CharField`** → short text.
- **`TextField`** → long text.
- **`ImageField`** → uploaded images.
- **`choices`** → restrict allowed values.
- **Pillow** → required for Django image handling.
- **`MEDIA_ROOT`** → where uploaded media is stored.
- **`MEDIA_URL`** → URL used to access media.
- **`makemigrations`** → create migration instructions.
- **`migrate`** → apply them to the database.
- **`admin.site.register()`** → expose a model in Django Admin.
- **`.objects.all()`** → retrieve all objects.
- **Context** → sends data from view → template.
- **`{% for %}`** → loop through data.
- **`{{ }}`** → display data.
- **`get_object_or_404()`** → fetch one object or return 404.
- **Named URL** → makes URLs reusable and dynamic.
