import cv2
from ultralytics import YOLO

# Carrega o seu modelo treinado
model = YOLO('best.pt')

# Inicia a captura da câmera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Não foi possível receber o frame da câmera.")
        break

    # AJUSTES DE PRECISÃO:
    # conf=0.50  -> Só exibe detecções com 50% ou mais de certeza
    # imgsz=640  -> Resolução de entrada para a rede neural
    # verbose=False -> Silencia as mensagens repetidas do terminal
    results = model(frame, conf=0.60, imgsz=640, verbose=False)

    # Desenha as caixas e rótulos
    annotated_frame = results[0].plot()

    # Exibe o resultado na janela
    cv2.imshow("ChonBot - Detecção de Alta Precisão", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()