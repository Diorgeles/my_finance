FROM python:3.5.7-jessie

COPY . /my_finance
WORKDIR /my_finance

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - \
    && apt-get install nodejs -y \
    && npm install -g yarn \
    && yarn \
    && python3 -m pip install --upgrade pip setuptools \
    && python3 -m pip install -r requirements.txt

EXPOSE 8000

CMD "python manage.py runserver 0.0.0.0:$PORT"
