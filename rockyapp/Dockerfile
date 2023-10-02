FROM python:3.8-slim-buster
WORKDIR /app
COPY app.py requirements.txt .
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
