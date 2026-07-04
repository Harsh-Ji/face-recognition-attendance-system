# Import necessary libraries
import cv2
import face_recognition
import numpy as np
import pandas as pd
import os
import json
from datetime import datetime
import winsound
import time

# Load the embeddings
print("\n\n 🔃 Loading Embeddings... 🔃")
embeddings = np.loadtxt("embeddings/embeddings.txt")
time.sleep(2)

# Initialize the camera
print("\n 📸 Capturing Started 📸")
winsound.Beep(3100, 500)
cap = cv2.VideoCapture(0)

# Initialize today's date
tday = str(datetime.now().strftime("%d-%b-%Y"))

# Load the attendance log
if not os.path.exists("Backup/Attendance.json"):
    with open("Backup/Attendance.json", "w") as f:
        json.dump({}, f)
    print("\n ✍🏻 Creating attendence log... ✍🏻")
with open("Backup/Attendance.json", "r") as f:
    attendance = json.load(f)



# Recognize the faces and mark attendance
while True:
    ret, frame = cap.read()
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(embeddings, face_encoding)
        if True in matches:
            index = matches.index(True)
            name = "user_" + str(index+1)
            if name not in attendance:
                attendance[name] = datetime.now().strftime("%Y-%b-%d %I:%M:%S %p")
                with open("Backup/Attendance.json", "w") as f:
                    json.dump(attendance, f)
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord('e'):
        break
cap.release()
cv2.destroyAllWindows()

print("\n ❗ -- Please wait while attendence is being saved -- ❗")

# Write the attendance data to an Excel file

save = str("Attendence/"+tday+".csv")  # To save file with current date

data = pd.read_json('Backup/Attendance.json',orient='index')
data.to_csv(save)

print ("\n\n 👍📝 Attendence Is Saved 📝👍\n\n")