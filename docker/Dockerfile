FROM python:3.8

WORKDIR /app
COPY . .

RUN pip install -r requirements/requirements.txt
RUN chmod +x grobid_client_python/setup.py
RUN ./setup.py

CMD ["./entry-point.sh"]