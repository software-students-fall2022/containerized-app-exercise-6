[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9335238&assignment_repo_type=AssignmentRepo)

![Workflow Status](https://github.com/software-students-fall2022/containerized-app-exercise-6/machine-learning-client/actions/workflows/python-package.yml/badge.svg?event=push)
![Workflow Status](https://github.com/software-students-fall2022/containerized-app-exercise-6/web-app/actions/workflows/python-package.yml/badge.svg?event=push)

# Containerized App Exercise
Build a containerized app that uses machine learning. See [instructions](./instructions.md) for details.


# Mongodb
## Setting up
1. mongodb cluster access: create an MongoDB Atlas account
2. create a cluster with --host=0.0.0.0 (share accesss with anyone)
3. create databases in the cluster
4. Put the link of the database with username and password into pymongo.MongoClient() to connect to the database

## Running
1. Start a MongoDB container using Docker with the following command:
```
docker run --name mongodb -d mongo
```
2. To start all containers together
```
docker compose up
```
3. To start all containers together at back-end
```
docker compose up -d
```
4. To end all containers together
```
docker compose down
```
5. To restart all containers together
```
docker compose up --build
```

