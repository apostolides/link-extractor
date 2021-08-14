FROM python:3.7

WORKDIR /usr/src/app

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python","./src/main.py"]