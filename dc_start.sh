#!/bin/bash

# enabling error handling
set -e

if [ "$1" == "down" ]; then
	echo "Stopping and removing Docker containers...."
	docker compose down
	exit 0
elif [ "$1" == "up" ]; then
	# build Docker images
	echo "Building Docker images...."
	docker compose build

	# run the containers
	echo "Starting Docker containers...."
	docker compose up #-d  detached mode
	exit 0
elif [ "$1" == "clean" ]; then
  echo "Cleaning up Docker environment...."
  docker compose down --volumes --remove-orphans
  docker system prune -af

  echo "Docker environment cleaned. Ready for a fresh build."
  exit 0
else
  echo "Usage: $0 {up|down|clean}"
  exit 1
fi

echo "Docker containers are now up and running!"

