FROM python:3.8
# FROM --platform=linux/amd64 python:3.8

WORKDIR /app
COPY . /app

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get install -y google-chrome-stable

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "index.py"]
