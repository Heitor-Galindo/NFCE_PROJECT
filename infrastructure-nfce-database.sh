#!/bin/bash

docker rm -f nfce-database || true
docker compose -f nfce_operations/database_operations/docker-compose.yml up