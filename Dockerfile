FROM ghcr.io/prefix-dev/pixi:latest AS build

COPY . /app
WORKDIR /app
RUN pixi run build-wheel
RUN pixi run postinstall-production
RUN pixi shell-hook -e prod > /shell-hook
RUN echo "uvicorn ves.main:app --host 0.0.0.0 --port 8000" >> /shell-hook

FROM ubuntu:22.04 AS production

# only copy the production env and the shell-hook script to the production image
COPY --from=build /app/.pixi/envs/prod /app/.pixi/envs/prod
COPY --from=build /shell-hook /shell-hook

WORKDIR /app

EXPOSE 8000
CMD ["/bin/bash", "/shell-hook"]
# RUN rm -rf .pixi

# RUN pixi install 

# ENV MODULE_NAME=src.main
# ENV ENTRYPOINT=app

# EXPOSE 8000


