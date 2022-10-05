Containerization and Docker
===========================

## Preparation

Please install Docker on your system as described in the [Docker documentation](https://docs.docker.com/engine/install/ubuntu/).

For Ubuntu, for example:

```bash
sudo apt-get remove docker docker-engine docker.io containerd runc

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

docker run hello-world
```

The first line you only need if you have Docker already installed.
