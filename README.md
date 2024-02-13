# ngmetar
Script to pull in Metar weather data.

## Build the package
This repository has a series of workflows that will automatically build and publish packages on commit.

## Build the container image
```shell
docker build  \
-t mrytest:1  \
--build-arg BASE_IMAGE=python:3  \
--build-arg PYPI_REPO_VAR=https://pypi.python.org/simple   \
.
```
If using podman, you may need to run ```sudo setenforce 0``` to disable selinux while the build takes place. Run ```sudo setenforce 1``` when the build is complete. Yes, I'm aware this is lazy and I will add an issue to put a proper fix in place. 

If you are using Fedora, you can probably mitigate this with
```shell
$ sudo dnf install container-selinux
$ restorecon -R -v $HOME
```

## Run the container
```shell
docker run -it -e METAR_ICAO="EGGD" -e METAR_API_KEY="[INSERT METAR KEY HERE]" -e METAR_SERVICE_URI="https://api.checkwx.com/metar/EGGD/decoded" [IMAGE_NAME_HERE]
```
