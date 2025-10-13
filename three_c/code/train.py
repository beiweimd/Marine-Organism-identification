


from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("yolo11s.pt")
    model.train(
        data=r"D:\yolo\yolov11\mydata.yaml",
        epochs=150,
        batch=-1,                # 会自动评估，当前卡会落到≈3
        workers=0,
        imgsz=960,
        optimizer="AdamW",
        cos_lr=True, warmup_epochs=3, patience=50,
        mosaic=1.0, mixup=0.15, copy_paste=0.1,
        close_mosaic=10, cache=True, amp=True
    )

