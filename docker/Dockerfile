FROM python:3.8

LABEL maintainer="tureNature"
LABEL version="1.0"
LABEL description="individual_assessment_1"

WORKDIR /app

COPY ./requirements /app/requirements
COPY ./individual_assessment_1 /app/individual_assessment_1

RUN pip install -r requirements/requirements.txt

RUN adduser --disabled-password appuser
RUN chown -R appuser /app
USER appuser

CMD ["python3", "/app/individual_assessment_1/main.py"]
