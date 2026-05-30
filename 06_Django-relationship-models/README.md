# Django Relationship Models

 ## 1\. Django & Databases

 Django provides an **ORM (Object-Relational Mapper)** that acts as a layer between your Python code and the database.

 Instead of directly writing SQL, you work with **Django Models**.

 **Benefit:** The underlying database can potentially be changed without rewriting all database-related application code.

---

 ## 2\. Database Relationships

 Suppose we have:

 - `Tea`
- `Review`
- `Store`
- `Certificate`

 The relationship between these entities determines how Django models should be connected.

 ### A. One-to-Many

 **One Tea → Many Reviews**

 Example:

```
Tea
 ├── Review 1
 ├── Review 2
 └── Review 3
```

 A review belongs to one tea, but a tea can have many reviews.

 #### Django implementation

 Use a `ForeignKey`:

```
tea = models.ForeignKey(
    TeaVariety,
    on_delete=models.CASCADE,
    related_name="reviews"
)
```

 #### Important

 - `ForeignKey` represents a **many-to-one relationship from the field's perspective**.
- The reverse side becomes **one-to-many**.
- Django automatically handles the relationship using the referenced model's primary key.

---

 #### `on_delete`

 `on_delete` tells Django what should happen to related records when the referenced object is deleted.

 Common example:

```
on_delete=models.CASCADE
```

 ##### `CASCADE`

 If the parent object is deleted, its related objects are also deleted.

 Example:

```
Tea deleted
   ↓
Its Reviews deleted
```

---

 #### Django's Built-in User Model

 Django already provides a built-in user model.

 It can be imported using:

```
from django.contrib.auth.models import User
```

 You can associate your own models with Django's `User` model.

 Example:

```
user = models.ForeignKey(
    User,
    on_delete=models.CASCADE
)
```

 This allows you to know **which user created a review**, for example.

---

 #### Example: Tea Review Model

 A review can contain:

 - User
- Tea
- Rating
- Comment
- Date added

 Conceptually:

```
User ──────┐
           ↓
        Review ←──── Tea
           │
           ├── Rating
           ├── Comment
           └── Date Added
```

 A review therefore connects both the **user** and the **tea**.

---

 ### B\. Many-to-Many Relationship

 Example:

 - One tea can be available in many stores.
- One store can sell many teas.

```
Tea A ──┬── Store 1
        ├── Store 2
        └── Store 3

Tea B ──┬── Store 1
        └── Store 2
```

 This is a **Many-to-Many** relationship.

 #### Django

 Use:

```
stores = models.ManyToManyField(
    TeaVariety,
    related_name="stores"
)
```

 The key idea:

 > **Many objects on both sides → `ManyToManyField`**

---

 #### `related_name`

 `related_name` defines the name used to access the relationship from the reverse side.

 Example:

```
tea = models.ForeignKey(
    TeaVariety,
    on_delete=models.CASCADE,
    related_name="reviews"
)
```

 You can then access reviews through:

```
tea.reviews
```

 Think of it as:

 > **"What should this relationship be called when accessed from the other model?"**

---

 ### C\. One-to-One Relationship

 A One-to-One relationship means:

 > One object is associated with exactly one object on the other side.

 Example:

```
Tea ───── Certificate
```

 One tea gets one certificate, and one certificate belongs to one tea.

 #### Django

 Use:

```
certificate = models.OneToOneField(
    TeaVariety,
    on_delete=models.CASCADE,
    related_name="certificate"
)
```

 Django enforces the one-to-one restriction.

---

 ### Quick Relationship Cheat Sheet

 | Relationship | Django Field | Example |
| --- | --- | --- |
| One-to-Many | `ForeignKey` | Tea → Reviews |
| Many-to-Many | `ManyToManyField` | Tea ↔ Stores |
| One-to-One | `OneToOneField` | Tea ↔ Certificate |

#### Easy memory trick

 **FK → Many**

 **M2M → Many ↔ Many**

 **O2O → One ↔ One**

---

 ## 3\. Migrations

 Whenever you change your models, Django needs to update the database.

 Two important commands:

 ### Step 1 — Create migration files

```
python manage.py makemigrations
```

 This detects model changes and creates migration instructions.

 ### Step 2 — Apply migrations

```
python manage.py migrate
```

 This actually applies those changes to the database.

 ### Remember

```
Models changed
     ↓
makemigrations
     ↓
Migration files
     ↓
migrate
     ↓
Database updated
```

---

 ### 4\. Django Admin Customization

 Django Admin can be customized through `admin.py`.

 Instead of simply registering a model:

```
admin.site.register(TeaVariety)
```

 you can create a custom `ModelAdmin`.

 Example:

```
class TeaVarietyAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "date_added")
```

 Then:

```
admin.site.register(TeaVariety, TeaVarietyAdmin)
```

---

 #### `list_display`

 Controls which fields appear in the Admin list page.

 Example:

```
list_display = ("name", "type", "date_added")
```

 Instead of showing only the object name, Admin can display multiple columns.

---

 #### `list_display_links`

 Controls which displayed fields are clickable.

 This allows you to decide which columns open the object's detailed Admin page.

---

 #### Admin Filters

 You can add filters using:

```
list_filter = ("type",)
```

 This gives Admin users a filtering interface.

 ##### Example

 If teas have different types:

```
Filter:
☐ Masala
☐ Ginger
☐ Green
```

 This makes large datasets easier to manage.

---

 #### Inline Admin

 One of the most useful Admin features shown in the video.

 Suppose:

```
Tea
 ├── Review 1
 ├── Review 2
 └── Review 3
```

 Instead of creating reviews separately, you can display them **inside the Tea Admin page**.

 ##### Example

```
class TeaReviewInline(admin.TabularInline):
    model = TeaReview
    extra = 2
```

 Then add it to the Tea Admin:

```
class TeaVarietyAdmin(admin.ModelAdmin):
    inlines = [TeaReviewInline]
```

 Now when adding/editing a tea, its reviews can appear directly underneath it.

---

 #### `extra`

 In an inline:

```
extra = 2
```

 means Django initially displays **2 extra empty forms** for adding related objects.

 For example:

```
Review 1: [          ]
Review 2: [          ]
```

 You can change the number as needed.

---

 #### `TabularInline`

 `TabularInline` displays related objects in a compact table-like format.

 Useful when you want to manage multiple related records directly from a parent object's Admin page.

---

 #### Admin Customization Pattern

 A common pattern is:

```
class SomeModelAdmin(admin.ModelAdmin):
    list_display = (...)
    list_filter = (...)
    list_display_links = (...)
```

 Then:

```
admin.site.register(SomeModel, SomeModelAdmin)
```

 #### Memory rule

 **Model → ModelAdmin → Register**

---

 ### 5\. Complete Mental Model

```
Django Models
     │
     ├── ForeignKey
     │      └── One-to-Many
     │
     ├── ManyToManyField
     │      └── Many-to-Many
     │
     └── OneToOneField
            └── One-to-One

     ↓
makemigrations
     ↓
migrate
     ↓
Database

     ↓
admin.py
     ↓
ModelAdmin
     ├── list_display
     ├── list_display_links
     ├── list_filter
     └── inlines
```

 - **ForeignKey** → One-to-Many
- **ManyToManyField** → Many-to-Many
- **OneToOneField** → One-to-One
- **`on_delete`** → Defines what happens when the referenced object is deleted.
- **`related_name`** → Name used to access a relationship from the reverse side.
- **`makemigrations`** → Creates migration instructions.
- **`migrate`** → Applies migrations to the database.
- **`ModelAdmin`** → Customizes Django Admin.
- **`list_display`** → Controls displayed columns.
- **`list_filter`** → Adds filters.
- **`inlines`** → Shows related objects inside the parent object's Admin page.
- **`extra`** → Number of extra inline forms.