IMAGE_NAME = individual_assessment_1

build:
	docker build -t $(IMAGE_NAME) -f docker/Dockerfile .

run:
	docker run -it $(IMAGE_NAME)