# Module 6 Flask Web Application - Docker Deployment Guide

This guide explains how to run the Module 6 Flask web application as a Docker container.

## Prerequisites
- [Docker](https://www.docker.com/products/docker-desktop) installed on your system.
- https://hub.docker.com/repository/docker/arose42/module_6/general the image for this website

## Run the Docker Container
After building the image, start the container with:

```powershell
docker run -p 8080:8080 arose42/module_6:v1
```
- The app will be accessible at [http://localhost:8080](http://localhost:8080)

## Notes
- Any changes to the code require rebuilding the Docker image.
- The container exposes port 8080 as defined in `run.py` and the Dockerfile.

