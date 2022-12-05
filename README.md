[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9335238&assignment_repo_type=AssignmentRepo)


![ML Status](https://github.com/software-students-fall2022/containerized-app-exercise-6/actions/workflows/machine-learning.yml/badge.svg?event=push)
![Web App Status](https://github.com/software-students-fall2022/containerized-app-exercise-6/actions/workflows/webapp.yml/badge.svg?event=push)

# Containerized App Description
Our app utilizes two different Machine Learning packages. 
   -  One is for face recognition that captures all faces in the group photo. 
   -  Second is for emotion analysis. 

When a photo of the user is taken by the Machine Learning client, the original photo will be processed by the facial recognition model. It will output images of individual face appearing in the photo. Then the individual images will be processed by the emotion model, which will output emotion for each face respectively. 

The web app works as a dashboard that displays statistics of the emotional analysis for each photo, including ratio of each emotion, min number of emotions, and max number of emotions in the group photo.

# Product Vision Statement
Simple face and emotion recognition web app based on machine learning algorithms with a statistical logger.

# Running the Project
1. Navigate to the root folder of this project, then run:
   ```
   docker compose up
   ```

2. Note that the machine-learning client has dependencies that need significant amount of time for Docker to setup for the first time (~10 minutes). If you don't want to wait, you can remove `mlclient` section from `docker-compose.yaml` and setup a virtural environment for the ML client by following this [instruction](https://github.com/software-students-fall2022/containerized-app-exercise-6/blob/main/machine-learning-client/README.md)
   * Note that, even if you choose to run `mlclient` in a venv, it still requires the database to run in Docker
3. The ML client (if run by Docker) will run at `127.0.0.1:7001`. The web-app will run at `127.0.0.1:6001`. A database container will also be created.
   
4. In the ML client, you can take a photo (with other people) and submit. After you submit, the machine-learning algorithm will run for 5~10 seconds and upload the result to the database.

5. After you have some initial analysis with the ML client, you can view results in the web-app by going to `127.0.0.1:6001`. The web-app contains a gallery of all photos you took and you can view detailed analysis results in their result pages. Also, you can delete any of the records.

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

# Structure
├── docker-compose.yaml
├── .git
│   ├── branches
│   ├── config
│   ├── description
│   ├── HEAD
│   ├── hooks
│   │   ├── applypatch-msg.sample
│   │   ├── commit-msg.sample
│   │   ├── fsmonitor-watchman.sample
│   │   ├── post-update.sample
│   │   ├── pre-applypatch.sample
│   │   ├── pre-commit.sample
│   │   ├── pre-merge-commit.sample
│   │   ├── prepare-commit-msg.sample
│   │   ├── pre-push.sample
│   │   ├── pre-rebase.sample
│   │   ├── pre-receive.sample
│   │   ├── push-to-checkout.sample
│   │   └── update.sample
│   ├── index
│   ├── info
│   │   └── exclude
│   ├── logs
│   │   ├── HEAD
│   │   └── refs
│   │       ├── heads
│   │       │   └── main
│   │       └── remotes
│   │           └── origin
│   │               └── HEAD
│   ├── objects
│   │   ├── info
│   │   └── pack
│   │       ├── pack-9c42ea6a6b0284edd50769be6ee20d443e94b39c.idx
│   │       └── pack-9c42ea6a6b0284edd50769be6ee20d443e94b39c.pack
│   ├── packed-refs
│   └── refs
│       ├── heads
│       │   └── main
│       ├── remotes
│       │   └── origin
│       │       └── HEAD
│       └── tags
├── .github
│   ├── .keep
│   └── workflows
│       ├── machine-learning.yml
│       └── webapp.yml
├── .gitignore
├── instructions.md
├── LICENSE
├── machine-learning-client
│   ├── app.py
│   ├── common
│   │   └── libs
│   │       ├── __init__.py
│   │       └── Url_Manager.py
│   ├── config
│   │   └── base_setting.py
│   ├── controllers
│   │   └── index.py
│   ├── Dockerfile
│   ├── README.md
│   ├── requirements.txt
│   ├── static
│   │   ├── css
│   │   │   └── photo_demo.css
│   │   └── plugins
│   │       ├── bootstrap_v3
│   │       │   ├── css
│   │       │   │   ├── bootstrap.css
│   │       │   │   ├── bootstrap.css.map
│   │       │   │   ├── bootstrap.min.css
│   │       │   │   ├── bootstrap.min.css.map
│   │       │   │   ├── bootstrap-theme.css
│   │       │   │   ├── bootstrap-theme.css.map
│   │       │   │   ├── bootstrap-theme.min.css
│   │       │   │   └── bootstrap-theme.min.css.map
│   │       │   ├── fonts
│   │       │   │   ├── glyphicons-halflings-regular.eot
│   │       │   │   ├── glyphicons-halflings-regular.svg
│   │       │   │   ├── glyphicons-halflings-regular.ttf
│   │       │   │   ├── glyphicons-halflings-regular.woff
│   │       │   │   └── glyphicons-halflings-regular.woff2
│   │       │   └── js
│   │       │       ├── bootstrap.js
│   │       │       ├── bootstrap.min.js
│   │       │       └── npm.js
│   │       ├── jquery.min.js
│   │       └── layer
│   │           ├── layer.js
│   │           ├── mobile
│   │           │   ├── layer.js
│   │           │   └── need
│   │           │       └── layer.css
│   │           └── skin
│   │               └── default
│   │                   ├── icon-ext.png
│   │                   ├── icon.png
│   │                   ├── layer.css
│   │                   ├── loading-0.gif
│   │                   ├── loading-1.gif
│   │                   └── loading-2.gif
│   ├── templates
│   │   ├── common
│   │   │   └── layout.html
│   │   ├── gallery
│   │   │   └── gallery.html
│   │   └── photo
│   │       ├── main_page.html
│   │       └── result_page.html
│   └── tests
│       ├── test_fear.jpg
│       ├── test_group.jpg
│       ├── test_happy.jpg
│       ├── test_noface.jpg
│       ├── test_sad.jpg
│       └── test_test.py
├── README.md
├── s.txt
└── web-app
    ├── app.py
    ├── common
    │   └── libs
    │       ├── __init__.py
    │       └── Url_Manager.py
    ├── config
    │   └── base_setting.py
    ├── controllers
    │   ├── gallery.py
    │   ├── index.py
    │   └── __init__.py
    ├── Dockerfile
    ├── requirements.txt
    ├── static
    │   ├── css
    │   │   └── photo_demo.css
    │   └── plugins
    │       ├── bootstrap_v3
    │       │   ├── css
    │       │   │   ├── bootstrap.css
    │       │   │   ├── bootstrap.css.map
    │       │   │   ├── bootstrap.min.css
    │       │   │   ├── bootstrap.min.css.map
    │       │   │   ├── bootstrap-theme.css
    │       │   │   ├── bootstrap-theme.css.map
    │       │   │   ├── bootstrap-theme.min.css
    │       │   │   └── bootstrap-theme.min.css.map
    │       │   ├── fonts
    │       │   │   ├── glyphicons-halflings-regular.eot
    │       │   │   ├── glyphicons-halflings-regular.svg
    │       │   │   ├── glyphicons-halflings-regular.ttf
    │       │   │   ├── glyphicons-halflings-regular.woff
    │       │   │   └── glyphicons-halflings-regular.woff2
    │       │   └── js
    │       │       ├── bootstrap.js
    │       │       ├── bootstrap.min.js
    │       │       └── npm.js
    │       ├── jquery.min.js
    │       └── layer
    │           ├── layer.js
    │           ├── mobile
    │           │   ├── layer.js
    │           │   └── need
    │           │       └── layer.css
    │           └── skin
    │               └── default
    │                   ├── icon-ext.png
    │                   ├── icon.png
    │                   ├── layer.css
    │                   ├── loading-0.gif
    │                   ├── loading-1.gif
    │                   └── loading-2.gif
    ├── templates
    │   ├── common
    │   │   └── layout.html
    │   └── photo
    │       ├── details.html
    │       └── index.html
    └── tests
        └── test_index.py


# Contributors

[Tim Chen](https://github.com/cty288)

[James Liu](https://github.com/liushuchen2025)

[Wenni Fan](https://github.com/fwenni)

[Yanchong Xu](https://github.com/yx-xyc)

[Iris Qian](https://github.com/okkiris)

[Sagynbek Talgatuly](https://github.com/sagynbek001)

[Jiawei Zhang](https://github.com/jiawei-zhang-a)
