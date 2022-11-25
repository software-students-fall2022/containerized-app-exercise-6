# in Docker, it is common to base a new image on a previously-created image
# Use an official Python runtime image as a parent image to base this image on
FROM python:3.7-slim
# Set the working directory within the image to /app
WORKDIR /machine-learning-client
# the ADD command is how you add files from your local machine into a Docker image
# Copy the current directory contents into the container at /app
ADD . /machine-learning-client


RUN apt-get update && apt-get install build-essential -y

# Install any needed packages specified in requirements.txt
# in Python, a requirements.txt file is a way of indicating dependencies in a way that the package manager, pip, can understand
RUN python -m pip install --upgrade pip

RUN pip3 install cmake 
RUN pip3 install pytest
RUN pip3 install -r requirements.txt

COPY . .
# by default Docker containers are closed off to the external world
# Make port 80 available to the world outside this container
EXPOSE 7001

# Define an environment variable... this will be available to programs running inside the container
#ENV NAME World
# Run app.py when the container launches
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=7001"]