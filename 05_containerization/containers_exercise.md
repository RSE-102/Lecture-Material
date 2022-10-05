# Exercise: Containerization with Docker

In this exercise we work with the container techniques that we have seen in the lecture. In particular, we build our own container using Docker which runs a selected application.

## Tasks

This exercise consists of the following main steps:

1. Select an application.
2. Create a fork of the GitHub repository ["Containerization Exercise"](https://github.com/RSE-102/containerization-exercise).
3. Set up the `Dockerfile`.
4. Create a merge request containing your changes.

### 1. Select an Application

Select an application from your daily scientific work, possibly a data analysis script or a numerical simulation. The application should depend mostly on publicly available packages or repositories. In particular, the number of required local files should be minimal. Running the application should be fast.

### 2. Create a Fork

Follow the link in the task list above and fork the repository. The repository initially contains an empty file called `Dockerfile`. Please also create a new branch in your fork to work on the task.

### 3. Set up the `Dockerfile`

- Currently, the [`Dockerfile`](https://docs.docker.com/engine/reference/builder/) is empty. Edit the file such that an image with the following properties will be built:
    - Choose a base image which corresponds to your employed OS (`cat /etc/os-release`) from [Docker Hub](https://hub.docker.com/).
    - Run `apt update -y` or similar and install all required packages.
    - Set a working directory.
    - Clone all required repositories.
    - If necessary, build the application executable.
    - Copy all required local files.
    - Make sure that the default command to be executed when running the container is `/bin/bash`.
    - **Note:** In the `Dockerfile` you do not have to prefix commands such as `apt` with `sudo` since the script is executed with superuser rights.
- Test your Docker container locally. Can you run the application inside the container?
    - **Note:** If you rebuild your container often, you might end up with dangling containers. You can remove them (and unused images, containers, or objects) with [`docker [image|container|system] prune`)](https://docs.docker.com/engine/reference/commandline/system_prune/) depending on what you want to remove.
- Add a `README.md` which explains how to build the image, instantiate a container and run the application.

### 4. Create a Merge Request

- Open a merge request in the GitHub Repository ["Containerization Exercise"](https://github.com/RSE-102/containerization-exercise).
    - As title choose "[`USERNAME`] Docker Container Recipe", where `USERNAME` is your GitHub username.
    - Put all required local files under version control.
    - Assign the merge request to `berndflemisch`.
    - Double-check that all files are in the repository and up to date.
    - If everything looks good, create the merge request.

## Further Information

- [Dockerfile documentation](https://docs.docker.com/engine/reference/builder/)
- [Docker](https://www.docker.com/)
- [Docker documentation](https://docs.docker.com)
- [DockerHub](https://hub.docker.com/)
- [DockerHub documentation](https://docs.docker.com/docker-hub/)


## Optional Tasks

- Publish a [Docker base image](https://docs.docker.com/develop/develop-images/baseimages/) to DockerHub.
    - Link the published DockerHub repository in the issue.
    - Please add all files (`Dockerfile` etc.) that you have used to set up this container and shortly describe which commands you have used to do so.
