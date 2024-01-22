import cv2

cap = cv2.VideoCapture(0)

used_codes = []

camera = True

while camera == True:
    success, frame = cap.read()

    detector = cv2.QRCodeDetector()

    data, bbox, clear_qrcode = detector.detectAndDecode(frame)

    if data not in used_codes:
        print('Продукт найден')
        print(data)
        used_codes.append(data)

    elif data in used_codes:
        print('Данный продукт уже был найден ранее')

    else:
        pass

    cv2.imshow('Testing-code-scan', frame)

    print(f"Распознаны следующие продукты: {used_codes}")
    print(f"Количество продуктов: {len(used_codes) - 1}")

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
