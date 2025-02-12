#!/bin/bash

# enabling error handling
set -e

PROJECT_NAME=galapagateway_api

#calculate_project_size() {
#  docker system df -v | grep $PROJECT_NAME | awk '{print $4}' | awk -F "GB" '{print $1}'
#}
#before_build=$(docker system df --format "{{.Size}}" | grep -Eo '[0-9.]+')

if [ "$1" == "down" ]; then
	echo "Stopping and removing Docker containers...."
	docker compose -p $PROJECT_NAME down
	docker builder prune --filter "label=project=$PROJECT_NAME" -f
	docker image prune --filter "label=com.docker.compose.project=$PROJECT_NAME" -f
	exit 0
elif [ "$1" == "up" ]; then
  echo "Storage used before build, Images, Containers, Local Volumes, Build Cache:"
  echo "${before_build}"
	# build Docker images
	echo "Building Docker images...."
	docker compose -p $PROJECT_NAME build --no-cache
	# run the containers
	echo "Starting Docker containers...."
	docker compose -p $PROJECT_NAME up #-d  detached mode
  # calculate how much storage used for build
#  after_build=$(docker system df --format "{{.Size}}" | grep -Eo '[0-9.]+')
#  build_GB=$(echo "$after_build - $before_build" | bc)
  echo "Storage used after build:"
#  echo "${after_build} GB"
  echo "Difference in storage usage:"
#  echo "${build_GB} GB"
  exit 0
elif [ "$1" == "prune" ]; then
  echo "Pruning unused Docker resources for $PROJECT_NAME...."
  docker compose -p $PROJECT_NAME down
  docker container prune --filter "label=com.docker.compose.project=$PROJECT_NAME" -f
  docker volume prune --filter "label=com.docker.compose.project=$PROJECT_NAME" -f
#  docker volume prune --filter "label=project=$PROJECT_NAME" -f
  docker image prune --filter "label=com.docker.compose.project=$PROJECT_NAME" -f
#  docker builder prune --filter "label=project=$PROJECT_NAME" -f
  docker builder prune
  echo "Docker environment for $PROJECT_NAME cleaned. Ready for a fresh build."
  exit 0
elif [ "$1" == "cleanup" ]; then
  echo "This will remove all unused/unreferenced resources, images, volumes, build cache, intermediate layers, etc."
  read -p "Are you sure you want to do this? [Y/n]: " confirm
  if [[ "$confirm" != "Y" && "$confirm" != "y" ]]; then
    echo "Cleanup canceled."
    exit 0
  fi
  echo
#  echo "Removing all unused build cache and intermediate layers...."
#  docker builder prune -a
#  echo "Removed build cache and intermediate layers"
#
#  echo "Removing all unused images...."
#  docker image prune -a
#  echo "Removed all unused and dangling images"
#
#  echo "Removing all unused volumes...."
#  docker volume prune -a
#  echo "Removed all unused volumes"
#
#  echo "Removing all unused containers"
  echo "Cleaning up all unused containers, networks, images (dangling and unreferenced), and volumes...."
  docker system prune
  echo "Docker system prune successful"
  echo
  echo "Docker disk usage after cleanup:"
  docker system df
  echo
  read -p "Would you like to FULLY cleanup entire builder cache [Y/n]: " confirm_final
  if [[ "$confirm_final" != "Y" && "$confirm_final" != "y" ]]; then
    echo "Cleanup canceled."
    exit 0
  fi
  echo "Cleaning up all builder cache...."
  docker builder prune -a
  echo "Docker builder cache cleanup successful"
  echo
  echo "Docker disk usage after full cleanup:"
  docker system df
  exit 0
else
  echo "Usage: $0 {up|down|prune|cleanup}"
  exit 1
fi

echo "Docker containers are now up and running!"

