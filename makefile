cwd := $(shell pwd)

build-frontend:
	docker build -t nomkick/frontend-image -f frontend/DockerFile frontend

build-backend:
	docker build -t nomkick/backend-image -f backend/DockerFile backend

run-backend:
	docker run -d -p 5000:5000 --name backend-container nomkick/backend-image

run-frontend:
	docker run -d -p 8080:80 --name frontend-container nomkick/frontend-image

clean:
	docker rm -f backend-container frontend-container || true
	docker rmi -f nomkick/backend-image nomkick/frontend-image || true

build: build-backend build-frontend

run: run-backend run-frontend

compose-up:
	docker-compose -f docker-compose-project.yml up -d --build

compose-down:
	docker-compose -f docker-compose-project.yml down

compose-logs:
	docker-compose -f docker-compose-project.yml logs -f

make deploy:
	kubectl apply -f kubernetes-config/application.yaml

make undeploy:
	kubectl delete -f kubernetes-config/application.yaml
