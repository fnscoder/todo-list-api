# TO DO List API

API to create a TO DO list app with Django and React.

The frontend project is available [here](https://github.com/fnscoder/todo-list-web)

### How to run the API

1. Create the virtual env
2. Activate the virtual env
3. Install the requirements
4. Create the .env file
5. Run the migrations
6. Run the project

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/.env-sample .env
python manage.py migrate
python manage.py run server
```