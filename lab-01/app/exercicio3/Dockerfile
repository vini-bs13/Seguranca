FROM python:3.14

WORKDIR /app

RUN pip install flask redis

ENV FLASK_APP=app.python
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONUNBUFFERED=1

CMD [ "flask", "run" ]