FROM python:3.11
LABEL authors="ilya3"

COPY . /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
# Установка переменной окружения
ENV SECRET_KEY=mhotep

EXPOSE 5000
CMD python ./FlaskAPP_YOLOv8_Weapon_Detection/flaskapp.py
