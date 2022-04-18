# start by pulling the python image
FROM python:3.7

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt

ENTRYPOINT [ "flask" ]
CMD ["run", "--host=127.0.0.1", "--port=5000"]