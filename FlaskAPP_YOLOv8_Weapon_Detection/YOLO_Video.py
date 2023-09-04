from ultralytics import YOLO
import cv2
import math
import datetime
import os


def video_detection(path_x):
    video_capture = path_x
    # Create a Webcam Object
    cap = cv2.VideoCapture(video_capture)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    print(frame_width)
    print(frame_height)
    # out=cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P','G'), 10, (frame_width, frame_height))
    current_directory = os.getcwd()
    print(current_directory)
    model = YOLO("./YOLO-Weights/best_YOLO.pt")
    classNames = ["empty", "full"]

    frame_count = -1
    skip_frames = 20  # Количество кадров для пропуска между сохранениями

    while True:
        success, img = cap.read()
        results = model(img, stream=True)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                print(x1, y1, x2, y2)
                conf = math.ceil((box.conf[0] * 100)) / 100
                cls = int(box.cls[0])
                print(cls)
                class_name = classNames[cls]
                print(class_name)
                label = f'{class_name}{conf}'
                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                print(t_size)
                c2 = x1 + t_size[0], y1 - t_size[1] - 3
                if class_name == 'full':
                    color = (45, 194, 255)
                else:
                    color = (12, 255, 34)
                if conf > 0.25:
                    cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)
                    cv2.rectangle(img, (x1, y1), c2, color, -1, cv2.LINE_AA)  # filled
                    cv2.putText(img, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)
                if conf > 0.7:
                    dir_name = "./static/Predictions"
                    # Проверяем, существует ли директория
                    if not os.path.exists(dir_name):
                        os.makedirs(dir_name)  # Создаем директорию, если ее нет
                    frame_count += 1
                    if frame_count % skip_frames == 0:
                        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Получение текущего времени
                        print(timestamp)
                        resize_img = cv2.resize(img, (640, 480))
                        # Расчет размера метки времени
                        (label_width, label_height), baseline = cv2.getTextSize(timestamp, cv2.FONT_HERSHEY_SIMPLEX,
                                                                                1.5, 3)
                        # Получение размеров изображения
                        height, width, _ = resize_img.shape
                        # Отрисовка текста в нижнем правом углу, черный контур
                        resize_img = cv2.putText(resize_img, timestamp, (width - label_width - 10, height - 10),
                                                 cv2.FONT_HERSHEY_SIMPLEX,
                                                 1.5, (0, 0, 0), 4, cv2.LINE_AA)
                        # Отрисовка текста в нижнем правом углу, белый текст
                        resize_img = cv2.putText(resize_img, timestamp, (width - label_width - 10, height - 10),
                                                 cv2.FONT_HERSHEY_SIMPLEX,
                                                 1.5, (255, 255, 255), 2, cv2.LINE_AA)

                        is_saved = cv2.imwrite(os.path.join(dir_name, f"{timestamp}.jpg"), resize_img)
                        print(f"Image saved: {is_saved}")

        yield img
        # out.write(img)
        # cv2.imshow("image", img)
        # if cv2.waitKey(1) & 0xFF==ord('1'):
        # break
    # out.release()

