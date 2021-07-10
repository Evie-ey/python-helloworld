FROM python:3.9.4
LABEL maintainer="Evelyne Namwoyo"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

# Commend to run on container to start
CMD [ "python", "app.py"]
