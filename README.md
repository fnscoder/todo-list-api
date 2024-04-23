# TO DO List API

API to create a TO DO list app with Django and React.

The frontend project is available [here](https://github.com/fnscoder/todo-list-web)

### How to run the API with docker compose (recommended)
You'll need to install [docker and compose](https://docs.docker.com/desktop/)

1. Clone the project
2. Enter on the project folder
3. Create the .env file
4. Build the containers
5. Run the containers
6. Apply the migrations
7. Create a superuser

```bash
git clone git@github.com:fnscoder/todo-list-api.git
cd todo-list-api
cp contrib/.env-sample .env
docker compose build
docker compose up
docker compose exec app python manage.py migrate
docker compose exec -it app python manage.py createsuperuser
```

### How to run the API locally

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

### How to run the API with Dockerfile and postgres

First clone the project and create the .env file

Install [docker](https://docs.docker.com/desktop/)

1. Create a network
2. Create postgres volume
3. Run postgres with docker on the network created
4. Build the image
5. Check the DATABASE_URL on your .env file
6. Run the app container on the network created
7. Run the migrations inside the app container
8. On the next time just start the postgres and backend container instead of using the `run` command again

```bash
docker network create backend-network
docker volume create postgres
docker run --network=backend-network --name postgres -e POSTGRES_PASSWORD=mysecretpassword -e POSTGRES_USER=backend -p 5432:5432 -v postgres:/var/lib/postgresql/data postgres
docker build .
DATABASE_URL=postgres://backend:mysecretpassword@postgres:5432/backend
docker run --network=backend-network --name backend --env-file=.env --publish 8000:8000 <image_id>
docker exec -it backend python manage.py migrate
docker start postgres
docker start backend
```
