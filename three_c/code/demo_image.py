from ultralytics import YOLO

model = YOLO(r"D:\yolo\yolov11\runs\detect\train\weights\best.pt")
results = model.predict(source=r'D:\yolo\yolov11\datasets\images\train', stream=True, show=True, imgsz=640, save=True)

for result in results:
    print(result.boxes.xyxy)
