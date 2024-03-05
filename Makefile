IMAGE_NAME = individual_assessment_1
TAG_NAME = latest
LOCAL_DIR = $(CURDIR)/data
NETWORK_MODE = host

build:
	docker build -t $(IMAGE_NAME):$(TAG_NAME) -f docker/Dockerfile .

run:
	docker run --network=$(NETWORK_MODE) -v $(LOCAL_DIR):/app/data $(IMAGE_NAME):$(TAG_NAME)

shell:
	docker run -it $(IMAGE_NAME):$(TAG_NAME) /bin/bash

clean:
	docker stop $(IMAGE_NAME):$(TAG_NAME)
	docker rm $(IMAGE_NAME)
	docker volume prune
	docker image prune -a

build-test:
	docker build -t $(IMAGE_NAME):test -f docker/Dockerfile_test .

run-test:
	docker run $(IMAGE_NAME):test