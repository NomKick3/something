cwd := $(shell pwd)

docker-build-backend:
	docker build -t my-backend-service backend/.

docker-build-frontend:
	docker build -t my-frontend-service frontend/.

docker-run-backend:
	docker run -d -p 3000:3000 --name backend-container my-backend-service

docker-run-frontend:
	docker run -d -p 8080:80 --name frontend-container my-frontend-service