IMAGE_NAME = individual_assessment_1:latest

build:
	docker build -t $(IMAGE_NAME) -f docker/Dockerfile .

docker-ls:
	docker run -it --rm $(IMAGE_NAME) ls /app/individual_assessment_1

run:
	docker run -it -v $(pwd)/output:/app/individual_assessment_1/output --rm $(IMAGE_NAME)