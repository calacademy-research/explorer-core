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
fi

echo "Docker containers are now up and running!"
