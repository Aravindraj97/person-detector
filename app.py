from fastapi import FastAPI,UploadFile,File
from ultralytics import YOLO
import shutil
import os


model = YOLO("yolov8n.pt")

app = FastAPI()

@app.post("/detect_person")
async def detect_person(file:UploadFile = File(...)):
    temp_file = f"temp_{file.filename}"
    with open(temp_file,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)



# running the yolo detection 

    results = model(temp_file)

    detections = []
    person_count = 0

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            if label == "person":
                person_count += 1
                confidence = float(box.conf[0])
                x1,y1,x2,y2 = box.xyxy[0].tolist()

                detections.append({
                    "confidence": round(confidence,2),
                    "bounding_box":{
                        "x1":round(x1,2),
                        "y1":round(y1,2),
                        "x2":round(x1,2),
                        "y2":round(x1,2),
                    }
                })

    
    os.remove(temp_file)


    return {
        "person_detected":person_count > 0,
        "person_count":person_count,
        "details":detections

    }

