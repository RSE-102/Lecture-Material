# Docker quiz

- Quiz "What is Docker?"
    - Start slido quiz
    - Answer depends on when in time and    you ask.
        - Containerization framework, container management, company...

## Introduction to Docker and some practical examples

- [`act`](https://github.com/nektos/act) is a tool to debug/run GitHub actions locally
- The most popular container framework one finds at the moment
- Short backstory:
    - Started as wrapper around lxc/lxd (Linux' native container format)
- Docker, Docker Engine, Docker Compose, Docker Hub? What is going on?
- Server-client layout
- Quite strong encapsulation from Host (**TODO**: Check for file exchange, networking etc.)
- **Generally useful commands** (see slides as well)
    - `docker run OPTIONS`
        - Run a container
    - `docker image ls`
        - List locally available images
    - `docker pull NAME:TAG`
        - Pulls an image from registry, `TAG` optional
    - `docker container create IMAGE`
        - Create container from image
    - `docker container ls`
        - List running containers
        - Add `-a` to see all containers
    - `docker container start/stop NAME`
        - Start/stop container
    - `docker container attach NAME`
        - Attach to running container
    - `docker build`
        - Creates an image from a given Dockerfile
    - `docker cp`
        - Copy files in/out of container
    - `docker image history IMAGE`
        - Show layers of image (including commands)Vagrant
    - `docker system prune`
        - Remove all unused objects (images, containers...)
    - `docker logs ID/NAME`
        - Shows log files of container
- Explain text-based format (infrastructure as code)
- One can pre-build own images to reuse them later.
- Has a layer based build process (which is nice). We do not have to rebuild from scratch, if build fails.
- Images can be shared via DockerHub or other registries
- Building an image can be pain in the neck as it depends on a fast internet connection.
- Installation issue/security risks: Docker user group is basically root
    - Rootless installation of Docker
    - Namespaces
    - Docker considers itself quite safe
- We focus on tools to create, run and interact with containers

Source: [https://docs.docker.com/get-started/overview/](https://docs.docker.com/get-started/overview/)

## Demo: Run existing container

- Show containers on [DockerHub](https://hub.docker.com/)

## Some Management Commands

- Show running containers `docker container ls`
- Show all containers `docker container ls -a`
- Show images `docker images`
- Potentially remove some image/container `docker image rm NAME` or `docker container rm NAME/ID`

## Tutorial Case

- From tutorial `docker run -i -t ubuntu /bin/bash`
    - This pulls the latest `ubuntu` image `docker pull ubuntu`
    - Creates container `docker container create`
    - Creates read-write filesystem (last layer)
    - Creates network interface
    - Starts container and runs `/bin/bash`
    - `-i` means interactive
    - `-t` allocates pseudo-tty
- Note that the container will still be there `docker container list -a` vs. `docker container list -a`
- We can make sure that the container is removed after exiting by the `--rm` options, i.e., `docker run --rm -i -t ubuntu /bin/bash`

- When container is running, we see it when calling `docker ps`
- Start container (with name `tutoral`) `docker run --rm -i -t --name tutorial ubuntu    /bin/bash`
- Leave it `CTRL-P` + `CTRL-Q` (do not let go of `CTRL` while doing this)
- Show container running `docker ps`
- Reattach to container `docker container attach tutorial`
- After quitting againg show `docker ps -a`

## Files in containers

- We can change files inside the container.
    - `docker run -i -t ubuntu /bin/bash`
    - `touch asdf`
    - leave container
    - enter container `docker run -i -t ubuntu /bin/bash`
    - File is not present because we implicitly created a new container based on the same image.

## Bind Mount

- `docker run -i -t --mount type=bind,source="$(pwd)",target=/mnt/share ubuntu`
    - Create detached container and bind mount
    - Mounts current directory on Host to `/mnt/share`.
    - Bind mount your source code for development for example
    - I do not need `/bin/bash` because that is the default command for the `ubuntu` image.

## Restarting a stopped container

- This is currently not possible. The default command or entrypoint is part of the runnable container. One has to create a new image from the stopped container to start it with another command
- Add a file in a base image, exit the container
- Get the container ID by `docker ps -a`
```bash
docker commit $STOPPED_CONTAINER new-image-name
docker run -it new-image-name /bin/bash
```

## Demo: Building own example

- `cd dockerfile-example`
- Contains Dockerfile

```Dockerfile
FROM ubuntu:22.04

RUN apt update -y
WORKDIR /app
COPY testfile .
CMD ["echo", "hello"]
```

- `docker build --tag testimage .`
- `docker run -i -t testimage /bin/bash`
- `docker run testimage` will run container and `CMD` will be executed
- Create file `touch testfile`, if not present.
- When going into the container we are in the directory `/app` and the file `testfile` is present.
- Copy files with `docker cp`. `touch file-to-copy`
- `docker cp file-to-copy CONTAINERNAME:/app`
- `docker cp CONTAINERNAME:/app file-to-copy`
- This will fix preserve user and group id
- `docker run -i -t -v $(pwd):/app testimage /bin/bash` starts container, creates volume `/app` and sets working directory to /app

