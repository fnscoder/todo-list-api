# TO DO List API

API to create a TO DO list app with Django and React.

The frontend project is available [here](https://github.com/fnscoder/todo-list-web)

### How to run the API

1. Clone the project
2. Enter on the project folder
3. Create the virtual env
4. Activate the virtual env
5. Install the requirements
6. Create the .env file
7. Run the migrations
8. Run the project

```bash
git clone git@github.com:fnscoder/todo-list-api.git
cd todo-list-api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/.env-sample .env
python manage.py migrate
python manage.py run server
```

The API will be running on [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/)
