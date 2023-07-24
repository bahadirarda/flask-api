# Employee Management API 🧑‍💼

Merhaba! Proje, Flask kullanılarak oluşturulmuş temel bir Python web API'sidir. API sayesinde sınıfa ait örnek verilere CRUD (Create, Read, Update, Delete) işlemlerini gerçekleştirebilirsiniz. 🎉

## Özellikler ✨

- Yeni bir çalışan ekleyebilir, isim, yaş ve departman bilgilerini girebilirsiniz.
- Tüm çalışanları listeleme özelliği mevcuttur.
- Çalışanları ID numarasına göre tek tek sorgulayabilirsiniz.
- Mevcut çalışanların bilgilerini güncelleyebilirsiniz.
- İstediğiniz çalışanı ID numarasına göre silme işlemi yapabilirsiniz.

## Gereksinimler 📋

- Python 3.x
- Flask
- Flask SQLAlchemy

## Kurulum 🚀

1. Projeyi bilgisayarınıza indirin.
2. Bir sanal ortam oluşturun: `python -m venv venv`.
3. Sanal ortamı etkinleştirin:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Gerekli kütüphaneleri yükleyin
5. Programı başlatın: `python app.py`.
6. API, `http://127.0.0.1:5000` adresinden erişilebilir olacak.

## Kullanım 🚀

- `GET /api/employees`: Tüm çalışanları listeleme.
- `GET /api/employees/<employee_id>`: ID numarasına göre tek bir çalışanı sorgulama.
- `POST /api/employees`: Yeni bir çalışan eklemek için bu endpointi kullanın. İsim, yaş ve departman bilgilerini JSON formatında gönderin.
- `PUT /api/employees/<employee_id>`: Mevcut bir çalışanın bilgilerini güncellemek için bu endpointi kullanın.
- `DELETE /api/employees/<employee_id>`: İstediğiniz bir çalışanı ID numarasına göre silme.

## Örnek İstek ve Cevaplar 📝

1. Yeni bir çalışan ekleme (POST `/api/employees`):

Gönderilecek olan örnek istek:
```json
{
    "name": "Zlatan Ibrahimovic",
    "age": 30,
    "department": "HR"
}
```

Alınacak örnek cevap:
```
{
    "status": "success",
    "message": "Çalışan başarıyla eklendi"
}
```

## Katkı 🤝
Projeye katkıda bulunmak isterseniz, dilediğiniz zaman bana ulaşabilirsiniz.

## Lisans 📄
Bu proje MIT Lisansına sahiptir.
