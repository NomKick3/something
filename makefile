cwd := $(shell pwd)

build-frontend:
	docker build -t frontend-image -f frontend/DockerFile frontend

build-backend:
	docker build -t backend-image -f backend/DockerFile backend

run-backend:
	docker run -d -p 5000:5000 --name backend-container backend-image

run-frontend:
	docker run -d -p 8080:80 --name frontend-container frontend-image

clean:
	docker rm -f backend-container frontend-container || true
	docker rmi -f backend-image frontend-image || true

build: build-backend build-frontend

run: run-backend run-frontend