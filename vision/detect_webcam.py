from ultralytics import YOLO
import cv2

model = YOLO(r"C:\Projetos\chonbot-computer-vision\runs\detect\train-4\weights\best.pt")

# Abre a webcam do computador
cap = cv2.VideoCapture(0)

print("Iniciando detecção local. Pressione 'q' para sair.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Faz a detecção na imagem da webcam
    results = model(frame, conf=0.6, verbose=False)

    # Plota as caixinhas na tela
    annotated_frame = results[0].plot()

    # Mostra a janela com o vídeo ao vivo
    cv2.imshow("ChonBot - Visao Local", annotated_frame)

    # Aperte 'q' no teclado para fechar a janela
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()