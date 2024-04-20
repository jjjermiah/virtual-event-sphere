FROM ghcr.io/prefix-dev/pixi:latest

WORKDIR /myapp

COPY . /myapp/

RUN rm -rf .pixi

RUN pixi install 

ENV MODULE_NAME=src.main
ENV ENTRYPOINT=app
ENV PORT=8000
EXPOSE 8000

CMD ["sh", "-c", "pixi run uvicorn src.main:app --host 0.0.0.0 --port ${PORT}"]
