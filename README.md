# 🤖 ChonBot — Visão Computacional e Mapeamento de Ambiente Exógeno

[![Status do Projeto](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange?style=flat-square)]()
[![Python](https://img.shields.io/badge/Python-3.12%2B-blue?style=flat-square&logo=python&logoColor=white)]()
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-yellow?style=flat-square&logo=opencv&logoColor=white)]()
[![CEFET/RJ](https://img.shields.io/badge/CEFET%2FRJ-Sistemas%20de%20Informação-green?style=flat-square)]()

Repositório dedicado ao módulo de **Visão Computacional e Percepção** do projeto **ChonBot**, desenvolvido no âmbito do curso de **Sistemas de Informação no CEFET/RJ**. 

O projeto explora a integração entre sistemas multiagentes (SMA) utilizando o framework **JaCaMo** e algoritmos de Deep Learning (**YOLOv8**) para o mapeamento e localização de objetos em ambientes exógenos.

---

## 📋 Sobre o Projeto

O objetivo principal desta etapa é construir uma **"ponte de dados"** confiável que:
* Capte o ambiente real através de uma câmara zenital;
* Detece os robôs e os objetos de interesse (como a bola) em tempo real;
* Extraia coordenadas espaciais precisas para alimentar o raciocínio cognitivo BDI (**Crenças, Desejos e Intenções**) dos agentes.

---

## 🚀 Funcionalidades Atuais

* **Aquisição e Tratamento de Imagens:** Captura de fluxo de vídeo em tempo real através de câmara/webcam.
* **Deteção com YOLOv8:** Modelo treinado com dataset personalizado para alta precisão e baixa taxa de falsos positivos.

---

## 🛠️ Tecnologias Utilizadas

* **[Python 3.12+](https://www.python.org/)**
* **[Ultralytics YOLOv8](https://ultralytics.com/yolov8)** (Deep Learning para Deteção de Objetos)
* **[OpenCV](https://opencv.org/)** (`cv2` — Processamento de Imagem)

---

## ⚙️ Como Executar o Projeto

Siga os passos abaixo para configurar e executar o ambiente de visão computacional localmente:

### 1. Clonar o Repositório
```bash
git clone https://github.com/teu-utilizador/chonbot-computer-vision.git
cd chonbot-computer-vision
```

### 2. Criar e Ativar o Ambiente Virtual (`venv`)

* **No Windows (PowerShell):**
  ```powershell
  python -m venv venv_visao
  .\venv_visao\Scripts\Activate.ps1
  ```

* **No Linux / macOS:**
  ```bash
  python3 -m venv venv_visao
  source venv_visao/bin/activate
  ```

### 3. Instalar as Dependências
```bash
pip install --upgrade pip
pip install opencv-python ultralytics flask
```

### 4. Executar o Script de Deteção
```bash
python train_local.py
```



---

## 📄 Licença

Este projeto está sob a licença [MIT](LICENSE).
