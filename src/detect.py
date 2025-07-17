# src/detect.py

from ultralytics import YOLO
import cv2
import os

def detect_players(video_path, model_path, save_output=False, output_path="outputs/detected.avi"):
    model = YOLO(model_path)
    cap = cv2.VideoCapture(video_path)

    width  = int(cap.get(3))
    height = int(cap.get(4))
    fps    = cap.get(cv2.CAP_PROP_FPS)

    if save_output:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        for result in results:
            annotated = result.plot()
            if save_output:
                out.write(annotated)
            else:
                cv2.imshow("Frame", annotated)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    cap.release()
    if save_output:
        out.release()
    cv2.destroyAllWindows()
