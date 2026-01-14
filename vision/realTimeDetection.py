import cv2
import inference
from inference.models.utils import get_roboflow_model

# 1. Configurações
MODEL_ID = "custom-workflow-object-detection-fag06/4"
API_KEY = "N7ccZitEfhVtcmB8EpcC"

# 2. Carregar o modelo (isso baixa o modelo na primeira execução)
model = inference.get_model(model_id=MODEL_ID, api_key=API_KEY)

# 3. Inicializar Webcam
cap = cv2.VideoCapture(0)

print("Iniciando detecção local... Pressione 'q' para sair.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 4. Inferência Local (Super rápida, sem upload de imagem)
    results = model.infer(frame, confidence=0.4)[0]

    # 5. Processar e desenhar resultados
    for prediction in results.predictions:
        # Extrair coordenadas
        x = int(prediction.x)
        y = int(prediction.y)
        w = int(prediction.width)
        h = int(prediction.height)
        
        label = prediction.class_name
        conf = prediction.confidence

        # Calcular cantos para o OpenCV
        x1, y1 = int(x - w / 2), int(y - h / 2)
        x2, y2 = int(x + w / 2), int(y + h / 2)

        # Desenhar na tela
        color = (0, 255, 0) # Verde
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        
        # Etiqueta
        texto = f"{label} {conf:.2f}"
        cv2.putText(frame, texto, (x1, y1 - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # 6. Exibir o frame
    cv2.imshow("Roboflow Local Inference", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()