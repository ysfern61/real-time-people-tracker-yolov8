<!-- Dil Seçimi / Language Selection -->
<p align="right">
  <a href="#türkçe">Türkçe</a> | <a href="#english">English</a>
</p>

<!-- Proje Başlığı / Project Title -->
<a name="türkçe"></a>
# 🚶‍♂️ YOLOv8 Gerçek Zamanlı İnsan Sayacı

Bu proje, Python, YOLOv8 ve OpenCV kullanılarak geliştirilmiş basit ve etkili bir gerçek zamanlı insan takip ve sayma uygulamasıdır. Web kamerası akışını işleyerek ekrandaki insan sayısını anlık olarak gösterir. Özellikle üniversite oryantasyon haftası gibi etkinliklerde stant yoğunluğunu izlemek için tasarlanmıştır.



### ✨ Özellikler

- **Gerçek Zamanlı Tespit:** Web kamerasından gelen görüntüyü anlık olarak işler.
- **Canlı İnsan Sayısı:** Ekranda tespit edilen toplam insan sayısını canlı olarak gösterir.
- **Yüksek Performans:** Hafif ve hızlı olan `YOLOv8n` modelini kullanır, bu sayede standart bir bilgisayarda bile akıcı çalışır.
- **Basit ve Anlaşılır Kod:** Kod, kolayca anlaşılabilir ve yeni özellikler eklemek için değiştirilebilir bir yapıdadır.

---

### 🛠️ Kullanılan Teknolojiler

- **Python 3.x**
- **OpenCV:** Görüntü ve video işleme için.
- **Ultralytics YOLOv8:** Nesne tespiti ve takibi için.

---

### 🚀 Kurulum ve Çalıştırma

#### 1. Repository'yi Klonlayın
Öncelikle projeyi bilgisayarınıza indirin:
```bash
git clone https://github.com/KULLANICI-ADIN/REPOSITORY-ADIN.git
cd REPOSITORY-ADIN
```

#### 2. Sanal Ortam Oluşturun (Önerilir)
Proje bağımlılıklarını sisteminizden izole tutmak için bir sanal ortam oluşturun ve aktif edin:
```bash
# Sanal ortamı oluştur
python -m venv venv

# Windows için aktif etme
venv\Scripts\activate

# macOS/Linux için aktif etme
source venv/bin/activate
```

#### 3. Gerekli Kütüphaneleri Yükleyin
Projenin ihtiyaç duyduğu kütüphaneleri `requirements.txt` dosyası üzerinden otomatik olarak yükleyin:
```bash
pip install -r requirements.txt
```
*(Eğer `requirements.txt` dosyanız yoksa, bu isimde bir dosya oluşturup içine `ultralytics` ve `opencv-python` yazın.)*

#### 4. Uygulamayı Çalıştırın
Her şey hazır! Aşağıdaki komutla uygulamayı başlatın:
```bash
python app.py
```
Uygulama başladığında web kameranız açılacaktır. Çıkmak için pencere seçiliyken `q` tuşuna basın.

<br>
<hr>
<br>

<!-- ENGLISH SECTION -->

<a name="english"></a>
# 🚶‍♂️ YOLOv8 Real-Time People Counter

This is a simple yet effective real-time people tracking and counting application developed using Python, YOLOv8, and OpenCV. It processes a webcam feed to display a live count of the people detected on screen. It was specifically designed for monitoring crowd density at events like a university orientation week.
### ✨ Features

- **Real-Time Detection:** Processes the video feed from the webcam instantly.
- **Live People Count:** Displays the total number of detected people on the screen in real-time.
- **High Performance:** Utilizes the lightweight and fast `YOLOv8n` model, allowing it to run smoothly even on a standard computer.
- **Simple & Understandable Code:** The codebase is designed to be easily understandable and modifiable for adding new features.

---

### 🛠️ Tech Stack

- **Python 3.x**
- **OpenCV:** For image and video processing.
- **Ultralytics YOLOv8:** For object detection and tracking.

---

### 🚀 Installation and Usage

#### 1. Clone the Repository
First, download the project to your local machine:
```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git
cd YOUR-REPOSITORY-NAME
```

#### 2. Create a Virtual Environment (Recommended)
Create and activate a virtual environment to keep project dependencies isolated from your system:
```bash
# Create the virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

#### 3. Install Required Libraries
Automatically install the necessary libraries using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```
*(If you don't have a `requirements.txt` file, create one with that name and add `ultralytics` and `opencv-python` to it.)*

#### 4. Run the Application
You're all set! Launch the application with the following command:
```bash
python app.py
```
When the application starts, your webcam will open. To quit, press the `q` key while the window is selected.
