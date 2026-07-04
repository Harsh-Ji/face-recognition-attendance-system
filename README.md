# Face Recognition Attendance System

> Created in late 2023 as an early computer vision learning project.

A Python-based attendance system that uses face recognition to automatically identify registered users and record attendance.

---

## Features

- 📷 Real-time webcam face recognition
- 🧠 Face embedding generation
- ✅ Automatic attendance marking
- 📄 Attendance exported as CSV
- 💾 Backup attendance log in JSON
- 👤 Supports multiple registered users

---

## Technologies Used

- Python
- OpenCV
- face_recognition
- NumPy
- Pandas

---

## Project Structure

```
main.py
create_embeddings.py
dataset/
embeddings/
attendance/
backup/
```

---

## Getting Started

### Install dependencies

```bash
pip install -r requirements.txt
```

### Add images

Place one image for each registered person inside the `dataset` folder.

### Generate embeddings

```bash
python create_embeddings.py
```

### Start attendance

```bash
python main.py
```

Attendance records will be stored as CSV files inside the `attendance` folder.

---

## Notes

- Developed and tested on Windows.
- This project uses the `face_recognition` library for face encoding and matching.
- The repository intentionally excludes sample datasets and generated embeddings.

---

## Status

> Archived learning project.
