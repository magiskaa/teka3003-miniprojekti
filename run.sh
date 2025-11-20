#!/bin/bash

IMAGE_NAME="miniprojekti"

echo "Building Docker image..."
docker build -t $IMAGE_NAME .

echo "Running Docker container..."
docker run --rm -it -v "$(pwd)/data:/app/data" -v "$(pwd)/reports:/app/reports" --name miniprojekti-kontti $IMAGE_NAME "$@"
