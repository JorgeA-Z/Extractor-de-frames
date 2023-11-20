import cv2

# Abre el archivo de video
video_capture = cv2.VideoCapture('1.mov')

# Verifica si el archivo de video se abrió correctamente
if not video_capture.isOpened():
    print("Error al abrir el video")
    exit()

# Contador para llevar el seguimiento del número de frames
frame_count = 0

# Bucle para leer y guardar cada frame del video
while True:
    ret, frame = video_capture.read()

    if not ret:
        break

    # Aquí puedes procesar o guardar cada frame como desees
    frame_count += 1

    # Por ejemplo, puedes guardar el frame en un archivo de imagen
    frame_filename = f'frame_{frame_count}.jpg'
    cv2.imwrite(frame_filename, frame)

# Cierra la captura de video
video_capture.release()

print(f'Se extrajeron {frame_count} frames del video.')

