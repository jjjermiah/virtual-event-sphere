

# Dockerfile Description

This Dockerfile defines two stages for building a Docker image for your application.

## Build Stage

The first stage, named `build`, starts from the `ghcr.io/prefix-dev/pixi:latest` image. It copies your application code into the `/app` directory in the Docker image and sets it as the working directory.

In this stage, the Dockerfile runs several commands:

- `pixi run build-wheel`: This command builds a wheel distribution of your application.
- `pixi run postinstall-production`: This command performs post-installation tasks for the production environment.
- `pixi shell-hook -e prod > /shell-hook`: This command generates a shell hook script for the production environment and saves it to `/shell-hook`.
- `echo "uvicorn ves.main:app --host 0.0.0.0 --port 8000" >> /shell-hook`: This command appends a command to start your application to the shell hook script.

## Production Stage

The second stage, named `production`, starts from the `ubuntu:22.04` image. It copies the production environment and the shell hook script from the `build` stage into the Docker image.

In this stage, the Dockerfile sets the working directory to `/app`, exposes port 8000, and sets the command to run when the Docker container starts to `/bin/bash /shell-hook`. This command runs the shell hook script, which sets up the environment and starts your application.

# Dockerfile Commands

Here's a brief description of the Dockerfile commands:

- [`FROM`](command:_github.copilot.openSymbolInFile?%5B%22Dockerfile%22%2C%22FROM%22%5D "Dockerfile"): This command sets the base image for the Docker image.
- [`COPY`](command:_github.copilot.openSymbolInFile?%5B%22Dockerfile%22%2C%22COPY%22%5D "Dockerfile"): This command copies files from the Docker build context into the Docker image.
- [`WORKDIR`](command:_github.copilot.openSymbolInFile?%5B%22Dockerfile%22%2C%22WORKDIR%22%5D "Dockerfile"): This command sets the working directory for subsequent [`RUN`](command:_github.copilot.openSymbolInFile?%5B%22Dockerfile%22%2C%22RUN%22%5D "Dockerfile"), [`CMD`](command:_github.copilot.openSymbolInFile?%5B%22Dockerfile%22%2C%22CMD%22%5D "Dockerfile"), `ENTRYPOINT`, [`COPY`](command:_github.copilot.openSymbolInFile?%5B%22Dockerfile%22%2C%22COPY%22%5D "Dockerfile"), and `ADD` commands.
- [`RUN`](command:_github.copilot.openSymbolInFile?%5B%22Dockerfile%22%2C%22RUN%22%5D "Dockerfile"): This command runs a command in a new layer on top of the current image and commits the results.
- [`EXPOSE`](command:_github.copilot.openSymbolInFile?%5B%22Dockerfile%22%2C%22EXPOSE%22%5D "Dockerfile"): This command informs Docker that the Docker container listens on the specified network ports at runtime.
- [`CMD`](command:_github.copilot.openSymbolInFile?%5B%22Dockerfile%22%2C%22CMD%22%5D "Dockerfile"): This command provides defaults for an executing container.