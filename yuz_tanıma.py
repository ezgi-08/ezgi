import cv2
from deepface import DeepFace
import os

# Kendi fotoğrafının yolu (Dosya adının aynı olduğundan emin ol)
reference_img_path = "ben.jpg"

cap = cv2.VideoCapture(0)

print("Yüz tanıma başlıyor... Kapatmak için 'q' tuşuna basın.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        # DeepFace ile kameradaki görüntüyü senin fotoğrafınla karşılaştır
        # En hızlı sonuç için 'opencv' dedektörünü kullanıyoruz
        result = DeepFace.verify(frame, reference_img_path, enforce_detection=False, detector_backend='opencv')
        
        if result["verified"]:
            label = "Giris Onaylandi: Merhaba!"
            color = (0, 255, 0) # Yeşil
        else:
            label = "Taninmadi"
            color = (0, 0, 255) # Kırmızı
            
        # Ekrana yazı yazdır
        cv2.putText(frame, label, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        
    except Exception as e:
        print("Hata:", e)

    cv2.imshow("Yuz Tanima Sistemi", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()