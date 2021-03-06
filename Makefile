DESTDIR=server

all: start
	@echo "Done"

docker-all: docker-build docker-start
	@echo "DONE"

docker-build:
	@echo "building the image from docker file..."
	docker build --no-cache --pull -t mvidali:mushroom_classifier .
	@echo "image DONE"

docker-start:
	@echo "starting the NEW service in container..."
	docker run  -p 8080:8080 mvidali:mushroom_classifier

service:
	@echo "creating the service..."
	pip install --upgrade pip
	pip install -r requirements.txt

start:  
	@echo "starting the NEW service..."
	pip3 install --upgrade pip
	pip3 install -r requirements.txt
	python3 app/backend/server.py

docker-stop:
	@echo "stoping the service..."
	docker stop $$(docker ps -alq)
	@echo "service stopped"

docker-remove:
	@echo "removing the image..."
	docker rmi -f mvidali/mushroom_classifier
	@echo "image removed"

docker-clean: docker-stop docker-remove
	@echo "DONE"

clean:
	@echo "removing service files created"
	rm -rf $(CREATED)
