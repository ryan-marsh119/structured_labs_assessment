FROM python:3.12-slim

WORKDIR /app

# Install nodejs and npm (needed for frontend)
RUN apt-get update && apt-get install -y nodejs npm

# Copy pyproject.toml
COPY pyproject.toml .

# Install dependencies from pyproject.toml
RUN pip install .

# Install preswald with exact version
RUN pip install preswald=={preswald_version}

# Copy app and assets
COPY . .

EXPOSE {port}

ENV PYTHONPATH=/app
ENV SCRIPT_PATH=/app/app.py
ENV PORT={port}

# Use startup script that calls start_server
CMD ["python", "run.py"]