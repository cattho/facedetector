# Detección de Rostros con Python y OpenCV

## Descripción

Este proyecto realiza la detección de rostros utilizando la librería `cv2` de OpenCV y clasificadores Haar cascades. Los archivos XML contienen los clasificadores entrenados para la detección de rostros humanos y felinos.

## Explicación:

- **Inicializar cámara**: La función `initialize_cam` crea un objeto `cv2.VideoCapture` para acceder a la cámara especificada por el índice (por defecto, 0 para la cámara principal). Si no se puede abrir la cámara, muestra un mensaje de error y finaliza el programa.

- **Detectar rostros**: La función `detect_faces` utiliza un clasificador Haar preentrenado (en este caso, `face_cascade`) para detectar rostros en la imagen en escala de grises. El método `detectMultiScale` busca rostros a diferentes escalas y tamaños, lo que permite detectar caras tanto cercanas como lejanas en la imagen.

- **Dibujar rectángulos**: La función `draw_faces` recorre cada rostro detectado y dibuja un rectángulo alrededor de él en la imagen original, utilizando las coordenadas devueltas por `detectMultiScale`.

- **Función principal**: La función `main` es el punto de entrada del programa. Carga el clasificador de rostros, inicializa la cámara, lee imágenes de la cámara en un bucle, detecta rostros, dibuja los rectángulos y muestra los resultados en una ventana.

- **Nota**: Para que este código funcione, debes asegurarte de tener el clasificador de rostros preentrenado (por ejemplo, `haarcascade_frontalface_default.xml`) en la carpeta adecuada o especificar la ruta correcta. Este clasificador puede descargarse desde los repositorios de OpenCV.
