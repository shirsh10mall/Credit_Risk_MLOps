FROM python:3.12

# Install system deps for Spark + compilation
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      openjdk-21-jre-headless curl build-essential git ca-certificates && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin

WORKDIR /app

# copy requirements first for Docker cache benefits
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /app/requirements.txt

# copy app code
COPY . /app

# make scripts executable
RUN chmod +x /app/start.sh

EXPOSE 8000 7860

# Use a non-root user (optional)
RUN useradd -m -s /bin/bash mlops && chown -R mlops:mlops /app
USER mlops

CMD [ "bash", "/app/start.sh" ]
