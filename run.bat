@echo off
set IMAGE_NAME=miniprojekti

echo Building Docker image...
docker build -t %IMAGE_NAME% .

echo Running Docker container...
docker run --rm --name miniprojekti-kontti %IMAGE_NAME% %*
