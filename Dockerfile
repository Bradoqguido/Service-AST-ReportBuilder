FROM node:18.12.1-alpine
LABEL maintainer="Jeferson Eduardo Guido <JefersonEduardoGuido@gmail.com>"

RUN apk update
RUN apk add py-pip
RUN apk add --no-cache python3-dev
RUN pip install --upgrade pip

WORKDIR /app
COPY . /app

RUN python3 -m venv venv
RUN source venv/bin/activate
RUN pip --no-cache-dir install -U -r requirements.txt

EXPOSE 3011/tcp

CMD ["python3", "src/app.py"]