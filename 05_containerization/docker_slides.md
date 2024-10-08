---
title: Containerization with Docker
author: Alexander Jaust, Bernd Flemisch, Gerasimos Chourdakis
institute: University of Stuttgart
type: slide
slideOptions:
  transition: slide
  width: 1400
  height: 900
  margin: 0.1
---

<style>
    .reveal strong {
      font-weight: bold;
      color: orange;
    }
    .reveal p {
      text-align: left;
    }
    .reveal section h1 {
      color: orange;
    }
    .reveal section h2 {
      color: orange;
    }
</style>


# Containerization with Docker

<img src="https://www.docker.com/wp-content/uploads/2022/03/Moby-logo.png" width=40%; style="margin-left:auto; margin-right:auto; padding-top: 25px; padding-bottom: 25px">

<small>[https://www.docker.com/company/newsroom/media-resources](https://www.docker.com/company/newsroom/media-resources)</small>


---

## What is Docker?

- According to documentation: Docker is an open platform for developing, shipping, and running applications.

- Docker Desktop: Developer productivity tools and a local Kubernetes environment.

- Docker Engine: Open source containerization technology for building and containerizing your applications.

- Docker Hub: Cloud-based application registry and development team collaboration services.

- Docker Compose: Tool for defining and running multi-container Docker applications.

- Docker Inc.: Company promoting Docker.

---

## Introduction

- 2010: Docker Inc. founded.

- 2013: First Docker release based on [LXC](https://linuxcontainers.org/), open-source.

- 2014: Replaced LXC by own execution environment.

- 2017: [Moby project](https://mobyproject.org/), an open-source framework created by Docker to assemble specialized container systems without reinventing the wheel.

- Nowadays one of the most popular container frameworks/services.

---

## Typical Docker Applications

- Applications as Microservices.

- Containers for consistent development environment.

- Containers for consistent testing environment.

- Portable format for sharing applications.

- Avoid tedious installation procedures by providing Docker containers ([FEniCS](https://fenicsproject.org/download/), [GitLab](https://docs.gitlab.com/ee/install/docker.html)...).

---

## Docker Architecture

<img src="https://docs.docker.com/get-started/images/docker-architecture.webp" width=80%; style="margin-left:auto; margin-right:auto; padding-top: 0px; padding-bottom: 10px">

[https://docs.docker.com/get-started/images/docker-architecture.webp](https://docs.docker.com/get-started/images/docker-architecture.webp)

---

## Building Blocks

- Docker daemon `dockerd`

    * Controlling instance of containers and reacts to API requests.
    * Server process.

- Docker client

    * Interface/tools to interact with, create, manage containers etc. via daemon.
    * That means no direct interaction with containers, images etc.

- Docker registries

    * Registries that manage Docker images to be used.

---

## Docker objects

- **Images**

    * Read-only template for creating a container.

    * An image can be based on another image.

- **Containers**

    * Runnable instance of an image.

---

## Connection to Host

- Container communicates via daemon `dockerd` (runs as root).

- Strong isolation (`namespaces` and `cgroups`)

    * You cannot access host filesystem by default.

    * Several [mount options](https://docs.docker.com/storage) available.

---

## Requirements

- Root rights for installation.

- `dockerd` runs as root -> Interaction needs root rights

    * Prefix commands with `sudo`.
    * Be member of group `docker` (=makes you root), expected by some applications (e.g. `act`).
    * Check [security notes](https://docs.docker.com/engine/security/).
    * Alternative: [Rootless mode](https://docs.docker.com/engine/security/rootless/).

---

## Useful Commands 1/2

- `docker run OPTIONS`: Run a container.

- `docker image ls`: List locally available images.

- `docker pull NAME:TAG`: Pulls an image from registry, `TAG` optional.

- `docker container create IMAGE`: Create container from image.

- `docker container ls` or `docker ps`: List running containers, add `-a` to see all.

---

## Useful Commands 2/2

- `docker container start/stop NAME`: Start/stop container.

- `docker container attach NAME`: Attach to running container.

- `docker build`: Creates an image from a given Dockerfile.

- `docker cp`: Copy files in/out of container.

- `docker image history IMAGE`: Show layers of image (including commands).

- `docker system prune`: Remove all unused objects (images, containers...).

---

## Demo: Running prebuilt images

<!--Details available in [`docker_demo.md`](https://github.com/RSE-102/Lecture-Material/blob/main/05_containerization/docker_demo.md)-->

---

## Defining and Building own Images 1/2

- Define container in `Dockerfile`

    * Git-friendly text file.
- Start from base image

    * Find images on repository such as [DockerHub](https://hub.docker.com/).
- Extend image by additional layers

    * Layers are added separately -> Keep number of layers low.
    * Layers are cached.
    * Changed layer requires downstream layers to be recreated.
- Container (layers) have commit hashes.

---

## Defining and Building own Images 2/2

- `FROM`: Defines base image.

- `RUN`: Defines commands to execute during `build`.

- `WORKDIR`: Defines working directory for following commands.

- `COPY`: Copy for from source to destination.

- `ADD`: Add for from source to destination (powerful and confusing).

- `CMD`: Command to run under `docker run`.

- `ENV`: Sets environment variable.

- `ARG`: Environment variable for **only** build process.

---

## Dockerfile Simple Example

```Dockerfile
FROM ubuntu:24.04

RUN apt update -y && apt install -y neofetch
WORKDIR /app
COPY testfile .
CMD ["neofetch"]
```

---

## Dockerfile Example from DuMux-Pub

```Dockerfile
# densitydrivendissolution docker container
# see https://github.com/phusion/baseimage-docker for information on the base image
# It is Ubuntu LTS customized for better Docker compatibility
FROM phusion/baseimage:focal-1.1.0
MAINTAINER bernd@iws.uni-stuttgart.de

# run Ubuntu update as advised on https://github.com/phusion/baseimage-docker
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt-get upgrade -y -o Dpkg::Options::="--force-confold" \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# install the basic dependencies
RUN apt-get update \
    && apt-get install --no-install-recommends --yes \
    ca-certificates \
    vim \
    python3-dev \
    python3-pip \
    git \
    pkg-config \
    build-essential \
    cmake \
    gfortran \
    mpi-default-bin \
    mpi-default-dev \
    libsuitesparse-dev \
    libsuperlu-dev \
    libeigen3-dev \
    doxygen \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# add the permission helper script to the my_init service
COPY setpermissions.sh /etc/my_init.d/setpermissions.sh

# create a dumux user
# add the welcome message (copied further down) output to bashrc
# make the set permission helper script executable
# add user to video group which enables graphics if desired
RUN useradd -m --home-dir /dumux dumux \
    && echo "cat /dumux/WELCOME" >> /dumux/.bashrc \
    && chmod +x /etc/my_init.d/setpermissions.sh \
    && usermod -a -G video dumux

# switch to the dumux user and set the working directory
USER dumux
WORKDIR /dumux

# create a shared volume communicating with the host
RUN mkdir /dumux/shared
VOLUME /dumux/shared

# This is the message printed on entry
COPY WELCOME /dumux/WELCOME

# set git user in case installation requires to apply patches
RUN git config --global user.name "densitydrivendissolution"
RUN git config --global user.email "st111492@stud.uni-stuttgart.de"

# Install the dumux module and its dependencies
# This expects the install script to do everything from clone to configure
COPY installscript.sh /dumux/installscript.sh
RUN ./installscript.sh && rm -f /dumux/installscript.sh

# unset git user
RUN git config --global --unset user.name
RUN git config --global --unset user.email

# switch back to root
WORKDIR /dumux
USER root

# set entry point like advised https://github.com/phusion/baseimage-docker
# this sets the permissions right, see above
ENTRYPOINT ["/sbin/my_init","--quiet","--","/sbin/setuser","dumux","/bin/bash","-l","-c"]

# start interactive shell
CMD ["/bin/bash","-i"]
```
[https://git.iws.uni-stuttgart.de/dumux-pub/buerkle2021a/-/blob/master/docker/Dockerfile](https://git.iws.uni-stuttgart.de/dumux-pub/buerkle2021a/-/blob/master/docker/Dockerfile)

---

# Demo: Building own image

<!--Details available in [`README.md`](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/02_virtualization_and_containers/README.md)-->

---

## Publish own Images

- Publication on registry (e.g. [DockerHub](https://hub.docker.com/)).

- `docker build -t ACCOUNT/REPOSITORY[:TAG] .`

    * Creates image.

- `docker push ACCOUNT/REPOSITORY[:TAG]`

    * Push image to registry (default DockerHub).

    * Needs account and must be logged in via `docker login`.

---

## Advanced Topics

- User ID mapping.

- [Multistage builds](https://docs.docker.com/develop/develop-images/multistage-build/)

    * Build image by combining layers created from different base images.

- [Different mount types](https://docs.docker.com/storage)

    * Volumes, bind mount, tmpfs mount.

- [Persisting data](https://docs.docker.com/get-started/05_persisting_data/).

- [Multi-container apps](https://docs.docker.com/get-started/07_multi_container/).

- And many more. Check out the [Docker documentation](https://docs.docker.com).

---

## Summary and Outlook

- Lightweight virtualization technique.

- Run application in isolated environment.

- Run application in consistent environment.

- Share environments and applications with containers.

- Plenty of options and feature-rich CLI.

- Important building block for CI/CD pipelines (future lectures).

---

## Further Reading

- [Docker](https://www.docker.com/)

- [Docker documentation](https://docs.docker.com)

- [DockerHub](https://hub.docker.com/)

- [DockerHub documentation](https://docs.docker.com/docker-hub/)

- [Open Container Initiative (OCI)](https://opencontainers.org/)

- [Malicious Docker Hub Container Images Used for Cryptocurrency Mining](https://www.trendmicro.com/vinfo/fr/security/news/virtualization-and-cloud/malicious-docker-hub-container-images-cryptocurrency-mining)
