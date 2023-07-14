FROM python:3.11-slim
LABEL authors="ilya3"
WORKDIR /app
RUN apt-get update && apt-get install -y libgl1-mesa-glx
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

# Установка переменной окружения
ENV SECRET_KEY=mhotep

EXPOSE 5000
CMD python ./FlaskAPP_YOLOv8_Weapon_Detection/flaskapp.py
