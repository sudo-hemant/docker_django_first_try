# docker_django_first_try
My first hands on docker.

# To make the project work : 
1. clone this repo
2. open the terminal
3. run the following commands to stop the local running services of nginx, postgresql, if any
   
   1. sudo systemctl stop postgresql.service
   2. sudo systemctl stop nginx.service
4. go inside the root directory
5. run the command 
   1. docker-compose up --build -d
6. If everything works fine, visit the "localhost:1337/api/todo".

Make any changes if you want and then open the terminal and go inside the root directoy and run the command mentioned in 5th point

# Helpful docker commands
To stop the container, run -- docker-compose down 


To restart the container, run -- docker-compose up -d


To go inside the container, run -- docker exec -it <container_name>(you can find the container name in compose file) bash

example command : docker exec -it django bash


To check logs of a particular container, run -- sudo docker logs -f <container_name>