# Django Forms

 ## 1\. What are Django Forms?

 Django Forms provide a structured way to:

 - Take input from users.
- Validate submitted data.
- Display fields such as text boxes and dropdowns.
- Connect user input with Django models.

 **Basic Django flow:**

 `Model → Form → View → Template`

 Forms add an extra layer between the **Model** and the **View**.

---

 ## 2\. Why Use Forms?

 Forms make it easier to:

 - Display model data as input fields.
- Create dropdowns automatically.
- Receive `GET`/`POST` data.
- Validate and clean user input.
- Protect forms against **CSRF attacks**.

---

 ## 3\. `forms.py`

 A separate `forms.py` file is commonly used to define forms.

 Example:

```
from django import forms
from .models import TeaVariety

class TeaVarietyForm(forms.Form):
    tea_variety = forms.ModelChoiceField(
        queryset=TeaVariety.objects.all(),
        label="Select Tea Variety"
    )
```

 ### Important parts

 - `forms.Form` → creates a Django form.
- `ModelChoiceField` → creates a dropdown using model objects.
- `queryset` → specifies which model objects should appear in the dropdown.
- `label` → text shown to the user.

---

 ## 4\. `ModelChoiceField`

 This is especially useful when choices should come directly from a database model.

 For example:

```
forms.ModelChoiceField(
    queryset=TeaVariety.objects.all()
)
```

 Django automatically creates a **dropdown** containing available tea varieties.

 Instead of manually creating:

```
Small Ginger Tea
Medium Masala Tea
Large Masala Tea
```

 Django gets the choices from the database.

 ### Remember

 **ModelChoiceField = Database objects → Dropdown**

---

 ## 5\. View Handles the Form

 The view generally handles two major situations:

 ### Case 1: Display the form

 The user has not submitted anything yet.

```
form = TeaVarietyForm()
```

 ### Case 2: Form is submitted

 Check the request method:

```
if request.method == "POST":
    form = TeaVarietyForm(request.POST)
```

 `request.POST` contains the data submitted by the user.

---

 ## 6\. Form Validation

 Before using submitted data:

```
if form.is_valid():
```

 Django checks whether the submitted data is valid.

 After validation, cleaned data can be accessed through:

```
form.cleaned_data
```

 For example:

```
tea_variety = form.cleaned_data["tea_variety"]
```

 ### Easy flow to remember

 **POST → Form → Validate → Cleaned Data → Query Database**

---

 ## 7\. Filtering Related Data

 In the example, the goal was:

 > Select a tea variety → Find stores where that tea is available.

 After getting the selected tea variety, the `Store` model can be filtered using it.

 Conceptually:

```
stores = Store.objects.filter(
    tea_varieties=tea_variety
)
```

 The resulting `stores` can then be sent to the template.

---

 ## 8\. Passing Data to Template

 The view can pass both the form and query results:

```
return render(
    request,
    "tea_stores.html",
    {
        "form": form,
        "stores": stores
    }
)
```

 The template can then:

 - Display the form.
- Loop through available stores.
- Show store names and locations.

---

 ## 9\. Rendering a Form

 Django provides convenient ways to render forms.

 For example:

```
{{ form }}
```

 Or:

```
{{ form.as_p }}
```

 `form.as_p` renders the form fields inside paragraph elements.

---

 ## 10\. CSRF Protection

 Django protects POST forms against **Cross-Site Request Forgery (CSRF)** attacks.

 Inside a POST form, include:

```
<form method="POST">
    {% csrf_token %}
    {{ form }}
    <button type="submit">Search Store</button>
</form>
```

 ### Remember

 **POST Form + Django = `{% csrf_token %}`**

 Without it, Django can return:

 `CSRF verification failed`

 Django automatically generates and manages the CSRF token.

---

 ## 11\. Complete Conceptual Flow

```
User opens page
      ↓
Form is created
      ↓
Django gets model data
      ↓
Dropdown is displayed
      ↓
User selects a tea variety
      ↓
User submits form (POST)
      ↓
View receives request.POST
      ↓
Form validates the data
      ↓
cleaned_data is obtained
      ↓
Database is filtered
      ↓
Matching stores are found
      ↓
Stores are displayed
```

---

 ## 12\. Key Points to Remember

 - **`forms.py`** → defines forms.
- **`forms.Form`** → creates a form class.
- **`ModelChoiceField`** → creates a model-based dropdown.
- **`queryset`** → determines available choices.
- **`request.POST`** → receives submitted form data.
- **`form.is_valid()`** → validates the form.
- **`form.cleaned_data`** → gives cleaned/validated data.
- **`filter()`** → finds matching database records.
- **`{{ form }}` / `{{ form.as_p }}`** → renders the form.
- **`{% csrf_token %}`** → protects POST forms from CSRF attacks.
