from ultralytics import YOLO

def main():
    # Carrega o modelo pré-treinado YOLOv8 nano
    model = YOLO('yolov8n.pt')

    # Inicia o treinamento com as configurações do data.yaml
    results = model.train(
        data='../yolo_data/data.yaml',
        epochs=50,
        imgsz=640,
        batch=16,
        name='treino_chonbot'
    )

if __name__ == '__main__':
    main()