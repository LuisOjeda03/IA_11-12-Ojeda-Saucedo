import torch
import torch.nn as nn
import cv2
import numpy as np
import time

# Configuración de seguridad para PyTorch
torch.backends.cudnn.benchmark = True
torch.set_flush_denormal(True)

class EmotionCNN(nn.Module):
    def __init__(self, num_classes=4):
        super(EmotionCNN, self).__init__()
        
        # Bloques convolucionales 
        self.features = nn.Sequential(
            nn.Conv2d(1, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Dropout(0.25),
            
            nn.Conv2d(64, 128, kernel_size=5, padding=2),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Dropout(0.25),
            
            nn.Conv2d(128, 512, kernel_size=3, padding=1),
            nn.BatchNorm2d(512),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Dropout(0.25),
            
            nn.Conv2d(512, 512, kernel_size=3, padding=1),
            nn.BatchNorm2d(512),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Dropout(0.25),
        )
        
        # Capas fully connected
        self.classifier = nn.Sequential(
            nn.Linear(512 * 3 * 3, 256), 
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(0.25),
            
            nn.Linear(256, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(0.25),
            
            nn.Linear(512, num_classes),
        )
    
    def forward(self, x):
        x = self.features(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x

def load_model_safe():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = EmotionCNN().to(device)
    
    try:
        # Intenta cargar con weights_only=True primero (mas seguro)
        state_dict = torch.load(
            r'C:\Users\luiso\OneDrive\Escritorio\Tec2025\Inteligencia_Artificial\U4\modelo_CNN_state_dict.pth',
            map_location=device,
            weights_only=True
        )
    except:
        state_dict = torch.load(
            r'C:\Users\luiso\OneDrive\Escritorio\Tec2025\Inteligencia_Artificial\U4\modelo_CNN_state_dict.pth',
            map_location=device
        )
    
    model.load_state_dict(state_dict)
    model.eval()
    return model, device

def main():
    # Configuración inicial
    emotion_labels = ['Angry', 'Happy', 'Sad', 'Surprise']
    model, device = load_model_safe()
    
    # Intenta cargar Haar Cascade desde diferentes ubicaciones
    cascade_paths = [
        r'C:\Users\luiso\OneDrive\Escritorio\Tec2025\Inteligencia_Artificial\U4\haarcascade_frontalface_default.xml',
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    ]
    
    face_classifier = None
    for path in cascade_paths:
        try:
            face_classifier = cv2.CascadeClassifier(path)
            if not face_classifier.empty():
                break
        except:
            continue
    
    if face_classifier is None or face_classifier.empty():
        raise FileNotFoundError("No se pudo cargar el clasificador Haar Cascade")

    # Configuración de la camara con limites de recursos
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 15)

    try:
        while True:
            start_time = time.time()
            
            # Lectura de frame con timeout
            ret, frame = cap.read()
            if not ret:
                print("Error leyendo frame")
                time.sleep(0.1)
                continue

            # Procesamiento optimizado
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(
                gray, 
                scaleFactor=1.1, 
                minNeighbors=5, 
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )

            for (x, y, w, h) in faces:
                try:
                    roi_gray = gray[y:y+h, x:x+w]
                    roi_resized = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
                    
                    if np.sum(roi_resized) > 100:  # Umbral mínimo de iluminación
                        roi_tensor = torch.from_numpy(roi_resized).float().div(255).unsqueeze(0).unsqueeze(0).to(device)
                        
                        with torch.no_grad():
                            outputs = model(roi_tensor)
                            _, predicted = torch.max(outputs, 1)
                            label = f"{emotion_labels[predicted.item()]}"
                            
                        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,255), 2)
                        cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
                
                except Exception as e:
                    print(f"Error procesando rostro: {str(e)}")
                    continue

            # Control FPS y uso de recursos
            fps = 1.0 / (time.time() - start_time)
            cv2.putText(frame, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
            cv2.imshow('Emotion Detector', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
            # Limitar FPS para reducir carga
            elapsed = time.time() - start_time
            if elapsed < 0.05:  # ~20 FPS máximo
                time.sleep(0.05 - elapsed)
                
    finally:
        # Liberacion segura de recursos
        cap.release()
        cv2.destroyAllWindows()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

if __name__ == "__main__":
    main()