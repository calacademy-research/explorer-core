#!/bin/bash

# enabling error handling
set -e

PROJECT_NAME=galapagateway_api

calculate_project_size() {
  docker system df -v | grep $PROJECT_NAME | awk '{print $4}' | awk -F "GB" '{print $1}'
}
before_build=$(docker system df --format "{{.Size}}" | grep -Eo '[0-9.]+')

if [ "$1" == "down" ]; then
	echo "Stopping and removing Docker containers...."
	docker compose -p $PROJECT_NAME down --rmi all --volumes --remove-orphans
	docker builder prune --filter "label=project=$PROJECT_NAME" -f
	exit 0
elif [ "$1" == "up" ]; then
  echo "Storage used before build: ${before_build} GB"
	# build Docker images
	echo "Building Docker images...."
	docker compose -p $PROJECT_NAME build --no-cache
	# run the containers
	echo "Starting Docker containers...."
	docker compose -p $PROJECT_NAME up #-d  detached mode
  # calculate how much storage used for build
  after_build=$(docker system df --format "{{.Size}}" | grep -Eo '[0-9.]+')
  build_GB=$(echo "$after_build - $before_build" | bc)
  echo "Storage used after build: ${after_build} GB"
  echo "Difference in storage usage: ${build_GB} GB"
  exit 0
elif [ "$1" == "prune" ]; then
  echo "Pruning unused Docker resources for $PROJECT_NAME...."
  docker compose -p $PROJECT_NAME down --volumes --rmi all --remove-orphans
  docker container prune --filter "label=com.docker.compose.project=$PROJECT_NAME" -f
  docker volume prune --filter "label=com.docker.compose.project=$PROJECT_NAME" -f
  docker image prune --filter "label=com.docker.compose.project=$PROJECT_NAME" -f
  docker builder prune --filter "label=project=$PROJECT_NAME" -f
  echo "Docker environment cleaned. Ready for a fresh build."
  exit 0
elif [ "$1" == "cleanup" ]; then
  echo "This will FULLY remove all unused resources, build cache, intermediate layers, etc."
  read -p "Are you sure you want to do this? [Y/n]: " confirm
  if [[ "$confirm" != "Y" && "$confirm" != "y" ]]; then
    echo "Cleanup canceled."
    exit 0
  fi
  read -p "Positive? [Y/n]: " confirm_final
  if [[ "$confirm_final" != "Y" && "$confirm_final" != "y" ]]; then
    echo "Cleanup canceled."
    exit 0
  fi
  echo "Removing all unused build cache and intermediate layers...."
  docker builder prune -a
  echo "Removed build cache and intermediate layers"

  echo "Docker disk usage after cleanup:"
  docker system df
  echo "Cleanup successful."
  exit 0

else
  echo "Usage: $0 {up|down|prune|cleanup}"
  exit 1
fi

echo "Docker containers are now up and running!"

