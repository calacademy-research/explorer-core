
docker run --name api_db -e MYSQL_ROOT_PASSWORD=password1 -e MYSQL_DATABASE=api_tables -d -p 3311:3306 -v $(pwd):/home/ mysql:8

docker exec -it api_db bash
