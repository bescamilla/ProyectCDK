FROM python:3.7-alpine

ADD ./src /code

WORKDIR /code

RUN pip install -r dependencies.txt

EXPOSE 3000

CMD ["python", "WebService.py"]


