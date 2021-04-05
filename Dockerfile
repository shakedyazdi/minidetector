FROM python:3.8

ADD . .

RUN python setup.py install

ENTRYPOINT ["python", "-m", "minidetector.main"]
