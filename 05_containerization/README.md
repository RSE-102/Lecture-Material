Containerization and Docker
===========================

## Preparation

Please install Docker on your system as described in the [Docker documentation](https://docs.docker.com/engine/install/ubuntu/).

For Ubuntu, for example:

If you already have previous versions of Docker installed, remove them by

```bash
sudo apt-get remove docker docker-engine docker.io containerd runc
```

Get and run the official installation script:

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

Create a group `docker` and add your user to it:

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```

Log out and back in again so that your group membership is re-evaluated. Run a hello-world example by

```bash
docker run hello-world
```
