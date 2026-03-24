# Exercise: Containerization with Docker

In this exercise we work with the container techniques that we have seen in the lecture. In particular, we build our own container using Docker which runs a selected application.

Select an application from your daily scientific work, possibly a data analysis script or a numerical simulation. The application should depend mostly on publicly available packages or repositories. In particular, the number of required local files should be minimal. Running the application should be fast.

## Set up the `Dockerfile`

- Create an empty file called [`Dockerfile`](https://docs.docker.com/engine/reference/builder/). Edit the file such that an image with the following properties will be built:
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

