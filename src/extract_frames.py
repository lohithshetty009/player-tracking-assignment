import cv2
import os

def extract_frames(video_path, output_dir, interval_sec=0.5):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    interval_frames = int(fps * interval_sec)

    frame_count = 0
    saved_count = 0
    success = True

    while success:
        success, frame = cap.read()
        if not success:
            break

        if frame_count % interval_frames == 0:
            frame_name = f"frame_{saved_count:04d}.jpg"
            frame_path = os.path.join(output_dir, frame_name)
            cv2.imwrite(frame_path, frame)
            saved_count += 1

        frame_count += 1

    cap.release()
    print(f"Extracted {saved_count} frames to {output_dir}")
