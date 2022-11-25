# How to Install and Run the Machine Learning Client

Due to the compability issues of the machine-learning library, we suggest you to run this machine learning client in a virtual environment.

1. Setup a Python virtual environment
   ```
   python3 -m venv .venv
   ```

2. Activate the virtual environment
   ```
   .venv\Scripts\activate.bat
   ```
   If the above one doesn't work, try this:
   ```
   .venv\Scripts\activate.ps1
   ```


3. IMPORTANT: Install cmake to your device before installing requirements.txt!
   
    ```
    pip3 install cmake                                                                  
    ```
    for mac:
    ```
    brew install cmake
    ```
    (for some reasons, the above command must be performed before installing requirements.txt. It even doen't work if you put it in requirements.txt)

4. Install requirements.txt
   ```
   pip3 install -r requirements.txt
   ```

5. Run the App
   ```
   set FLASK_APP=app.py
   set FLASK_ENV=development
   python -m flask run
   ```