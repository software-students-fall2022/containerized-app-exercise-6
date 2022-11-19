[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9335238&assignment_repo_type=AssignmentRepo)
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
2. Run the docker-compose coomand to start and stop all containers together
```
docker-compose up
```