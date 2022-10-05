---
title: Containerization with Docker
author: Alexander Jaust, Bernd Flemisch, Sarbani Roy
institute: University of Stuttgart
type: slide
slideOptions:
  transition: slide
  width: 1400
  height: 900
  margin: 0.1
theme: "Frankfurt"
colortheme: "beaver"
fonttheme: structurebold
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

# Docker

![[https://www.docker.com/company/newsroom/media-resources](https://www.docker.com/company/newsroom/media-resources)](Moby-logo.jpg){ width=60% }


# What is Docker?

- According to documentation: Docker is an open platform for developing, shipping, and running applications.

- Docker Desktop: Developer productivity tools and a local Kubernetes environment.

- Docker Engine: Open source containerization technology for building and containerizing your applications.

- Docker Hub: Cloud-based application registry and development team collaboration services.

- Docker Compose: Tool for defining and running multi-container Docker applications.

- Docker Inc.: Company promoting Docker.


# Introduction

- 2010: Docker Inc. founded.

- 2013: First Docker release based on [LXC](https://linuxcontainers.org/), open-source.

- 2014: Replaced LXC by own execution environment.

- 2017: [Moby project](https://mobyproject.org/), an open-source framework created by Docker to assemble specialized container systems without reinventing the wheel.

- Nowadays one of the most popular container frameworks/services.


# Typical Docker Applications

- Applications as Microservices.

- Containers for consistent development environment.

- Containers for consistent testing environment.

- Portable format for sharing applications.

- Avoid tedious installation procedures by providing Docker container ([FEniCS](https://fenicsproject.org/download/), [GitLab](https://docs.gitlab.com/ee/install/docker.html)...).


# Docker Architecture

![[https://docs.docker.com/engine/images/architecture.svg](https://docs.docker.com/engine/images/architecture.svg)](docker_architecture.jpg){ width=80% }


# Building Blocks

- Docker daemon `dockerd`

    * Controlling instance of containers and reacts to API requests.
    * Server process.

- Docker client

    * Interface/tools to interact with, create, manage containers etc. via daemon.
    * That means no direct interaction with containers, images etc.

- Docker registries

    * Registries that manage Docker images to be used.


# Docker objects

- **Images**

    * Read-only template for creating a container.

    * An image can be based on another image.

- **Containers**

    * Runnable instance of an image.


# Connection to Host

- Container communicates via daemon `dockerd` (runs as root).

- Strong isolation (`namespaces` and `cgroups`)

    * You cannot access host filesystem by default.

    * Several [mount options](https://docs.docker.com/storage) available.


# Requirements

- Root rights for installation.

- `dockerd` runs as root -> Interaction needs root rights

    * Prefix commands with `sudo`.
    * Be member of group `docker` (=makes you root), expected by some applications (e.g. `act`).
    * [Attack surface?!](https://docs.docker.com/engine/security/#docker-daemon-attack-surface)

        + [Isolate user namespace](https://docs.docker.com/engine/security/userns-remap/).
        + Use trustworthy containers.

- Alternatives:

    * [Rootless mode](https://docs.docker.com/engine/security/rootless/).
    * Run Docker in a VM.

- Check [security notes](https://docs.docker.com/engine/security/).


# Useful Commands 1/2

- `docker run OPTIONS`: Run a container.

- `docker image ls`: List locally available images.

- `docker pull NAME:TAG`: Pulls an image from registry, `TAG` optional.

- `docker container create IMAGE`: Create container from image.

- `docker container ls`: List running containers, add `-a` to see all.


# Useful Commands 2/2

- `docker container start/stop NAME`: Start/stop container.

- `docker container attach NAME`: Attach to running container.

- `docker build`: Creates an image from a given Dockerfile.

- `docker cp`: Copy files in/out of container.

- `docker image history IMAGE`: Show layers of image (including commands).

- `docker system prune`: Remove all unused objects (images, containers...).


# Demo: Running prebuilt images

<!--Details available in [`docker_demo.md`](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/02_virtualization_and_containers/docker_demo.md)-->


# Defining and Building own Images 1/2

- Define container in `Dockerfile`

    * Git-friendly text file.

- Start from base image

    * Find images on repository such as [DockerHub](https://hub.docker.com/).

- Extend image by additional layers

    * Layers are added separately -> Keep number of layers low.

    * Layers are cached.

    * Changed layer requires downstream layers to be recreated.

- Container (layers) have commit hashes.


# Defining and Building own Images 2/2

- `FROM`: Defines base image.

- `RUN`: Defines commands to execute.

- `WORKDIR`: Defines working directory for following commands.

- `COPY`: Copy for from source to destination.

- `ADD`: Add for from source to destination (powerful and confusing).

- `CMD`: Command to run under `docker run`.

- `ENV`: Sets environment variable.

- `ARG`: Environment variable for **only** build process.


# Dockerfile Simple Example

```Dockerfile
FROM ubuntu:22.04

RUN apt update -y && apt install -y neofetch
WORKDIR /app
COPY testfile .
CMD ["echo", "hello"]
```


# Dockerfile Example from Automation

```Dockerfile
FROM ubuntu:22.04

# install basic dependencies, curl & graphics libs are required for paraview
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt-get upgrade -y -o Dpkg::Options::="--force-confold" \
    && apt-get install --no-install-recommends --yes \
        libcurl4 libgomp1 libgl1-mesa-glx libglu1-mesa libegl1-mesa \
        python3-dev \
        python3-pip \
        wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Get a headless version of paraview. This is not optimal, but the standard
# package installed via apt-get is not headless, causing errors due to graphics
# drivers. There are also paraview images, but there we had problems installing
# missing python packages.
ARG PVVERSION="ParaView-5.10.1-egl-MPI-Linux-Python3.9-x86_64"
RUN URL="https://www.paraview.org/paraview-downloads/download.php?submit=Download&version=v5.10&type=binary&os=Linux&downloadFile=${PVVERSION}.tar.gz" \
    && wget "$URL" -O ${PVVERSION}.tar.gz \
    && tar -xvf ${PVVERSION}.tar.gz \
    && rm ${PVVERSION}.tar.gz
ENV PATH="${PATH}:/${PVVERSION}/bin"

WORKDIR /my_simulation
VOLUME /my_simulation

# Install python depenendencies
RUN python3 -m pip install matplotlib

# It is generally better if you get the ressources from a persistent source!
COPY make_plot_data.py .
COPY plot.py .
COPY pvstate.pvsm .
COPY render_state.py .
COPY simulation.py .
COPY automation.sh .
```

# Demo: Building own image

<!--Details available in [`README.md`](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/02_virtualization_and_containers/README.md)-->


# Publish own Images

- Publication on registry (e.g. [DockerHub](https://hub.docker.com/)).

- `docker build -t ACCOUNT/REPOSITORY[:TAG] .`

    * Creates image.

- `docker push ACCOUNT/REPOSITORY[:TAG]`

    * Push image to registry (default DockerHub).

    * Needs account and must be logged in via `docker login`.


# Advanced Topics

- User ID mapping.

- [Multistage builds](https://docs.docker.com/develop/develop-images/multistage-build/)

    * Build image by combining layers created from different base images.

- [Different mount typs](https://docs.docker.com/storage)

    * Volumes, bind mount, tmpfs mount.

- [Persisting data](https://docs.docker.com/get-started/05_persisting_data/).

- [Multi-container apps](https://docs.docker.com/get-started/07_multi_container/).

- And many more. Check out the [Docker documentation](https://docs.docker.com).


# Summary and Outlook

- Lightweight virtualization technique.

- Run application in isolated environment.

- Run application in consistent environment.

- Share environments and applications with containers.

- Plenty of options and feature-rich CLI.

- Important building block for CI/CD pipelines (future lectures).


# Further Reading

- [Docker](https://www.docker.com/)

- [Docker documentation](https://docs.docker.com)

- [DockerHub](https://hub.docker.com/)

- [DockerHub documentation](https://docs.docker.com/docker-hub/)

- [Open Container Initiative (OCI)](https://opencontainers.org/)

- [Malicious Docker Hub Container Images Used for Cryptocurrency Mining](https://www.trendmicro.com/vinfo/fr/security/news/virtualization-and-cloud/malicious-docker-hub-container-images-cryptocurrency-mining)
