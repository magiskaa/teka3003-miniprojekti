#!/bin/bash

IMAGE_NAME="miniprojekti"

echo "Building Docker image..."
docker build -t $IMAGE_NAME .

echo "Running Docker container..."
docker run --rm -it -v "$(pwd)/data:/app/data" -v "$(pwd)/reports:/app/reports" -v "$(pwd)/output:/app/output" --name miniprojekti-kontti $IMAGE_NAME "$@"
