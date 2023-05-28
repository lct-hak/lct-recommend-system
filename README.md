### Как развернуть

1. ```bash 
   $ python -m venv venv
   ```
2. ```bash
   $ (venv) pip instan pipenv
    ```
3. ```bash
   $ (venv) pipenv install
    ```

4. ```bash
   $ (venv) export FLASK_APP=main.py
   ```

5. ```bash
   $ (venv) flask run
   ```

Заполненная база данных лежит в файле database.db (SQLite)

Рекоммендации получить через роут GET /recommend/<user_id>