FROM hdgigante/python-opencv:4.7.0-ubuntu
LABEL authors="ilya3"
RUN apt-get update && apt-get install -y libgl1-mesa-glx
COPY . /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
# Установка переменной окружения
ENV SECRET_KEY=mhotep

EXPOSE 5000
CMD python3 ./FlaskAPP_YOLOv8_Weapon_Detection/flaskapp.py
