import cv2

# Cargar el clasificador de Haar para la detección de rostros
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Capturar el video desde la cámara predeterminada (índice 0)
cam = cv2.VideoCapture(1)

while True:
    # Leer el cuadro de la cámara
    _, img = cam.read()

    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detectar rostros en la imagen en escala de grises
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Dibujar un rectángulo alrededor de cada rostro detectado
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Mostrar la imagen con los rectángulos dibujados
    cv2.imshow("img", img)

    # Esperar 30 ms y salir si se presiona la tecla 'ESC'
    exit_program = cv2.waitKey(30)
    if exit_program == 27:
        break

# Liberar el objeto de captura y cerrar todas las ventanas
cam.release()
cv2.destroyAllWindows()
