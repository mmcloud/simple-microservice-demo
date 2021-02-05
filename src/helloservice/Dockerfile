FROM python:3.8-slim

RUN apt-get update -qqy && \
    apt-get -qqy install wget g++ && \
    rm -rf /var/lib/apt/lists/*
RUN mkdir /helloservice 

# show python logs as they occur
ENV PYTHONUNBUFFERED=0 \
    POETRY_VERSION=1.0.3 

RUN pip3 install poetry
# download the grpc health probe
RUN GRPC_HEALTH_PROBE_VERSION=v0.3.6 && \
    wget -qO/bin/grpc_health_probe https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/${GRPC_HEALTH_PROBE_VERSION}/grpc_health_probe-linux-amd64 && \
    chmod +x /bin/grpc_health_probe

WORKDIR /helloservice
COPY pyproject.toml /helloservice
ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# Add files
COPY . .

ENV PORT "8080"
EXPOSE 8080
ENTRYPOINT ["python", "/helloservice/hello_server.py"]
