import cv2


# cargar el clasificador de Haar
def load_face_cascade():
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    if face_cascade.empty():
        print("Error: No se pudo cargar el clasificador de rostros")
        exit
    return face_cascade


# inicializar camara
def initialize_cam(index=0):
    cam = cv2.VideoCapture(index)
    if not cam.isOpened():
        print("Error:No se pudo acceder a la cámara")
        exit()
    return cam


# detectar rostros
def detect_faces(face_cascade, gray_image):
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=4)
    return faces


# dibujo de rectangulos en los rostros
def draw_faces(image, faces):
    for x, y, w, h in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)


# main function del programa
def main():
    face_cascade = load_face_cascade()
    cam = initialize_cam(0)
    try:
        while True:
            ret, img = cam.read()
            if not ret:
                print("Error en el recuadro de la camara")
                break
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detect_faces(face_cascade, gray)
            draw_faces(img, faces)
            cv2.imshow("Face Detection", img)
            if cv2.waitKey(30) & 0xFF == 27:
                break
    except Exception as e:
        print(f"error:{e}")
    finally:
        cam.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
