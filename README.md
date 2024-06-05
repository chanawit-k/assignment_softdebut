# assignment_softdebut
## Getting Started
1. Create Virtual Environment
  ```python
  python -m venv .venv
  ```

2. Activate Virtual Environment:
  windows
  ```python
  venv\Scripts\activate
  ```
  mac
  ```python
  source venv/bin/activate
  ```

3. Install requirements.txt
  ```python
  pip install -r requirements.txt
  ```

4. Migrate Database
  ```python
  python manage.py migrate
  ```

5. Initialize the database with initial data:
  ```python
  python manage.py init_db
  ```
