[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9335238&assignment_repo_type=AssignmentRepo)


![ML Status](https://github.com/software-students-fall2022/containerized-app-exercise-6/actions/workflows/machine-learning.yml/badge.svg?event=push)
![Web App Status](https://github.com/software-students-fall2022/containerized-app-exercise-6/actions/workflows/webapp.yml/badge.svg?event=push)

# Containerized App Description
Our app utilizes two different Machine Learning packages. One is for face recognition that captures all faces in the group photo. The other one is for emotion analysis. When a photo of user is taken by the Machine Learning client, the original photo will be processed by the facial recognition model. It will output images of individual face appearing in the photo. Then the individual images will be processed by the emotion model, which will output emotion for each face respectively. 

The web app works as a dashboard that displays statistics of the emotional analysis for each photo, including percentage of each emotion, min number of emotions, and max number of emotions in the group photo.

# Contibutors
[Tim Chen](https://github.com/cty288)

[James Liu](https://github.com/liushuchen2025)

[Wenni Fan](https://github.com/fwenni)

[Yanchong Xu](https://github.com/yx-xyc)

[Iris Qian](https://github.com/okkiris)

[George Zhang](https://github.com/jiawei-zhang-a)

[Sagynbek Talgatuly](https://github.com/sagynbek001)

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

