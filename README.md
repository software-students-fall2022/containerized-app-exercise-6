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

[Jiawei Zhang](https://github.com/jiawei-zhang-a)

[Sagynbek Talgatuly](https://github.com/sagynbek001)

# Running the Project
1. Navigate to the root folder of this project, then:
   ```
   docker compose up
   ```

2. Note that the machine-learning client has dependencies that need significant amount of time for Docker to setup (~10 minutes, depending on your Internet connection). If you don't want to wait, you can remove `mlclient` section from `docker-compose.yaml` and setup a virtural environment for the ML client by following this [instruction](https://github.com/software-students-fall2022/containerized-app-exercise-6/blob/main/machine-learning-client/README.md) (This tends to be much faster)
   * Note that, even if you choose to run `mlclient` in a venv, it still requires the database to run in Docker
<br>
<br>
3. The ML client (if run by Docker) will run at `127.0.0.1:7001`. The webapp will run at `127.0.0.1:6001`. A database container will also be created.
   
4. In the ML client, you can take a photo (with other people) and submit. After you submit, the machine-learning algorithm will run for 5~10 seconds and upload the result to the database.

5. After you have some initial analysis with the ML client, you can view results in the web-app by going to `127.0.0.1:6001`. The web-app contains a gallary of all photos you took and you can view detailed analyzed results in their result pages. 

# How to run Pytests
## Webapp
1. Navigate to web-app directory
```
cd web-app
```
2. Run:
```
python -m pytest
```

## ML Client
You don't need to start the database to run tests for the ML client
1. Navigate to machine-learning-client directory
```
cd machine-learning-client
```
2. Run:
```
python -m pytest
```
