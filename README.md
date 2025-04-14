# 📝 Django TODO List App

This is a simple and clean TODO List web application built with **Django**. It allows users to create, manage, and organize tasks with optional deadlines, tags, and completion statuses.

## ⚙️ Technologies

- **Django**
- **Tailwind CSS**

---

## 🚀 Features

- ✅ Mark tasks as complete or incomplete
- 🗓️ Set deadlines
- 🏷️ Add and manage tags for tasks
- ✏️ Edit existing tasks
- ❌ Delete tasks

## 🛠️ Installation

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

4. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Apply migrations:

    ```bash
    python manage.py migrate
    ```

6. Load sample data (optional):

    ```bash
    python manage.py loaddata fixture_data.json
    ```

7. Run the server:

    ```bash
    python manage.py runserver
    ```
   
## 📁 Fixtures

1. Sample tasks and tags are provided in `fixture_data.json`.
2. You can load the data using the `loaddata` command:

    ```bash
    python manage.py loaddata fixture_data.json
    ```