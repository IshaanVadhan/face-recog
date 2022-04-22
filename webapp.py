import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from flask import Flask, render_template, send_file, Response

app = Flask(__name__)
path = 'images'
images = []
personName = []
myList = os.listdir(path)
print(myList)
for cu_img in myList:
    current_Img = cv2.imread(f'{path}/{cu_img}')
    images.append(current_Img)
    personName.append(os.path.splitext(cu_img)[0])
print(personName)

def faceEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = faceEncodings(images)
print("All Encodings Complete!")

time_today = datetime.now()
todayDate = time_today.strftime('%d-%m-%Y')
filename = "Attendance - " + todayDate + ".csv"
with open(f'records/{filename}', 'a+') as fp:
    if(os.path.getsize(f'records/{filename}') == 0):
        fp.writelines(f'Name,Date,Time')

def attendance(name):
    with open(f'records/{filename}', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        dateList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            dateList.append(entry[1])
        generate_info(nameList)
        if name not in nameList:
            time_now = datetime.now()
            tStr = time_now.strftime('%H:%M:%S')
            dStr = time_now.strftime('%d/%m/%Y')
            f.write("\n")
            f.writelines(f'{name},{dStr},{tStr}')

cap = cv2.VideoCapture(0)

def generate_frames():
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        else:
            faces = cv2.resize(frame, (0,0), None, 0.25, 0.25)
            faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

            facesCurrentFrame = face_recognition.face_locations(faces)
            encodesCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)

            for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    name = personName[matchIndex].upper()
                    y1,x2,y2,x1 = faceLoc
                    y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                    cv2.rectangle(frame,(x1,y1),(x2,y2),(100,75,245),2)
                    cv2.rectangle(frame,(x1, y2-35),(x2,y2),(100,75,245),cv2.FILLED)
                    cv2.putText(frame, name, (x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
                    attendance(name)

            ret,buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
        
            yield(b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def generate_info(name):
    return name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/teams')
def teams():
    return render_template('teams.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/download')
def download_file():
    p = f"/College/Coding/SY/face-recog/records/{filename}"
    return send_file(p,as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True,use_reloader=False)