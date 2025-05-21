from flask import Flask, render_template, request, jsonify, Response
import cv2
import numpy as np
from ultralytics import YOLO
import os
import time
from datetime import datetime
import threading

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Charger le modèle (avec vérification)
try:
    model = YOLO('models/best.pt')
    print("Modèle chargé avec succès!")
except Exception as e:
    print(f"Erreur de chargement du modèle: {e}")
    model = None

# Détection en temps réel
camera_active = False
alert_status = False

def generate_frames():
    cap = cv2.VideoCapture(0)
    while camera_active:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Détection
            results = model.track(frame, persist=True)
            annotated_frame = results[0].plot()
            
            # Vérifier les alertes
            global alert_status
            alert_status = any(obj in results[0].boxes.cls for obj in [0,1,2])  # IDs des classes d'alerte
            
            # Encodage
            ret, buffer = cv2.imencode('.jpg', annotated_frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/detect_alert')
def detect_alert():
    return jsonify({'alert': alert_status})

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Aucun fichier envoyé'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Aucun fichier sélectionné'}), 400
    
    if file:
        # Sauvegarde temporaire
        filename = f"detect_{int(time.time())}.jpg"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        
        # Traitement
        img = cv2.imread(filepath)
        results = model.predict(img)
        
        # Sauvegarde résultat
        result_filename = f"result_{filename}"
        result_path = os.path.join(UPLOAD_FOLDER, result_filename)
        cv2.imwrite(result_path, results[0].plot())
        
        return jsonify({
            'original': filename,
            'result': result_filename,
            'alert': any(obj in results[0].boxes.cls for obj in [0,1,2])
        })

@app.route('/control_camera', methods=['POST'])
def control_camera():
    global camera_active
    camera_active = not camera_active
    return jsonify({'status': camera_active})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)