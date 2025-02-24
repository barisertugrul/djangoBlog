# Django Blog Project

Bu Django projesi, blog yazıları oluşturup yönetebileceğiniz bir web uygulamasıdır.

## Gereksinimler

- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)

## Kurulum

### 1. Projeyi İndirin
```
git clone https://github.com/barisertugrul/djangoBlog.git
cd djangoBlog
```

### 2. Sanal Ortam Oluşturun ve Aktif Edin

Windows için:
```
python -m venv venv
venv\Scripts\activate
```

Linux/macOS için:
```
python3 -m venv venv
source venv/bin/activate
```

### 3. Gerekli Paketleri Yükleyin
```
pip install -r requirements.txt
```

Eğer requirements.txt dosyası yoksa, aşağıdaki paketleri manuel olarak yükleyin:
```
pip install django
pip install django-crispy-forms
pip install crispy-bootstrap5
pip install django-ckeditor
pip install Pillow
pip install django-cleanup
```

### 4. Gerekli Klasörleri Oluşturun
```
mkdir static
mkdir media
mkdir staticfiles
```

### 5. Veritabanı İşlemleri
```
python manage.py makemigrations
python manage.py migrate
```

### 6. Statik Dosyaları Toplayın
```
python manage.py collectstatic
```

### 7. Süper Kullanıcı Oluşturun
```
python manage.py createsuperuser
```

### 8. Projeyi Çalıştırın
```
python manage.py runserver
```

Tarayıcınızda `http://127.0.0.1:8000` adresine giderek projeyi görüntüleyebilirsiniz.

## Önemli Notlar

- Projeyi production ortamına almadan önce `settings.py` dosyasındaki `DEBUG = True` değerini `False` olarak değiştirin.
- `SECRET_KEY` değerini güvenli bir şekilde saklayın.
- Production ortamında güvenli bir veritabanı kullanın.

## Klasör Yapısı

```
proje_klasörü/
│
├── static/          # Statik dosyalar (CSS, JS, resimler)
├── media/          # Kullanıcı yüklemeleri
├── staticfiles/    # Toplanan statik dosyalar
├── templates/      # HTML şablonları
└── venv/           # Sanal ortam
