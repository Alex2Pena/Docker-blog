# Basic Docker Blog

1. ```mkdir``` a folder for the docker project
1. ```cd``` into project folder
1. ```touch Dockerfile``` to make a blank Dockerfile
1. ``` code .``` to launch code editor
1. add the following to Docker file
    ```
    FROM python:3
    ENV PYTHONDONTWRITEBYTECODE 1
    ENV PYTHONUNBUFFERED 1
    RUN mkdir /code
    WORKDIR /code
    COPY . /code/
    ```
2. make a file called ```main.py```
3. add to main .py the following
```
print("Hello World")
```

4. ```docker build .``` to run docker file and make an image
5. 
