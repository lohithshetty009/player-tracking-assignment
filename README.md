# Player Tracking Assignment

This project solves two video analytics tasks using a fine-tuned YOLOv11 model:

---

## Tasks

### 1.Cross-Camera Player Mapping
- **Goal**: Map each player between two different camera angles: `tacticam.mp4` and `broadcast.mp4`
- **Challenge**: Ensure player identities remain consistent across views

### 2.Re-Identification in a Single Feed
- **Goal**: Assign consistent IDs to players in `15sec_input_720p.mp4`, even when they go out-of-frame and return
- **Challenge**: Maintain identity through occlusions or re-entries

---

## Folder Structure

```
player-tracking-assignment/
├── model/                         # best.pt model (manual download)
├── videos/                        # video inputs (manual download)
├── outputs/                       # processed videos/results
├── src/                           # all source code
│   ├── detect.py                  # YOLO inference script
│   ├── reid_single.py             # Option 2: re-identification tracking
│   ├── cross_camera_map.py       # Option 1: cross-view mapping
│   └── utils.py                   # helper functions
├── requirements.txt               # pip dependencies
├── Player_Tracking_Assignment.ipynb  # main Colab notebook
├── report.md / report.pdf         # methodology & analysis
└── README.md                      # this file
```

---

## How to Run (Google Colab)

1. **Mount Google Drive**
```python
from google.colab import drive
drive.mount('/content/drive')
```

2. **Set Your Paths**
```python
base_path = "/content/drive/MyDrive/player_tracking_assignment"
model_path = f"{base_path}/model/yolov11.pt"
video_path = f"{base_path}/videos/15sec_input_720p.mp4"
```

3. **Run Detection**
```python
from src.detect import detect_players
detect_players(video_path, model_path, save_output=True)
```

---

## Download Files Before Running

Please download them manually:

### 🔗 Google Drive Folder (All Files)
 [Shared Folder – Click Here](https://drive.google.com/drive/folders/1Nx6H_n0UUI6L-6i8WknXd4Cv2c3VjZTP)

### 📦 Model
- `best.pt` → place in: `model/`

### 🎥 Videos
- `broadcast.mp4`
- `tacticam.mp4`
- `15sec_input_720p.mp4`  
Place all in: `videos/`

---

## 📦 Install Dependencies

In Colab:
```python
!pip install -r requirements.txt
```

---

## ⚙️ Requirements

- Python 3.8+
- YOLOv11 (Ultralytics)
- OpenCV
- Google Colab (recommended)

---

## 👤 Author

**Lohith Bheemisetty**  
B.Tech CSE (AI & ML)  
Vellore Institute of Technology, Chennai  
