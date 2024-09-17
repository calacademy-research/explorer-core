#!/bin/bash

# Usage: ./wait-for-it.sh host:port -- command_to_run_after

host_port=$1
shift
cmd="$@"

# Extract host and port from the input
host=$(echo $host_port | cut -d: -f1)
port=$(echo $host_port | cut -d: -f2)

# Check if host and port are provided
if [ -z "$host" ] || [ -z "$port" ]; then
  echo "Usage: $0 host:port -- command"
  exit 1
fi

# Loop until the host is reachable on the specified port
while ! nc -z "$host" "$port"; do
  echo "Waiting for $host:$port..."
  sleep 2
done

echo "$host:$port is available - executing command"
exec $cmd
