FROM python:3-slim

WORKDIR /opt/edutest

COPY . /opt/edutest

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=src/edutest:app
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
