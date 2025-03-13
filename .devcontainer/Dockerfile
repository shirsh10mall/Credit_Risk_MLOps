# Use the official Python image as a base image
FROM python:3.13

# Set the working directory in the container
WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install oh-my-zsh
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# Set zsh as the default shell
RUN chsh -s $(which zsh)

# # Update and install necessary dependencies
# RUN apt install default-jre

# # Set the environment variable for JAVA_HOME
# ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

# # Update PATH variable
# ENV PATH=$JAVA_HOME/bin:$PATH

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip3 install pre-commit refurb
RUN pip install --no-cache-dir -r requirements.txt
RUN pip3 install  --no-cache-dir sort-requirements


# Set environment variables
ENV PYTHONUNBUFFERED 1

# Add the project files to the container
COPY . .

# Expose the ports the container will use
EXPOSE 8800
