# Use the official Python image as a base image
FROM python:3.13

# Set the working directory in the container
WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y sudo default-jre
    
# Install oh-my-zsh
RUN apt-get update && apt-get install -y zsh && \
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# Set zsh as the default shell
RUN chsh -s $(which zsh)

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
