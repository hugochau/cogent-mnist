# Adapted from https://hub.docker.com/_/python
FROM python:3.6

WORKDIR /usr/src/cogentmnist

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000

# CMD [ "bash", "src/main.sh" ]
# ENTRYPOINT ["bash", "src/main.sh"]
