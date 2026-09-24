from ultralytics import YOLO

def main():
    # Carrega um modelo base leve do YOLOv8 (o 'n' significa nano, que é rápido para testes locais)
    model = YOLO("yolov8n.pt")

    # Inicia o treinamento com o seu arquivo yaml
    results = model.train(
        data="../yolo_data/data.yaml", # <-- Adicione os dois pontos aqui ("../")
        epochs=50,
        imgsz=640,
        batch=8
    )

    print("Treinamento concluído com sucesso!")

if __name__ == "__main__":
    main()