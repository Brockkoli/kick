#!/bin/bash

cd /home/ubuntu/Desktop/3203_test_practice


echo "Stopping the containers..."
docker-compose down

echo "Buidling the containers..."
docker-compose up --build -d --remove-orphans

echo "Containers up and running..."
