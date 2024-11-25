import cv2

class Extractor():
    def __init__(self, route):
        self.route = route
        self.frameCount = 0

    def saveFrame(self, frame):
        self.frameCount += 1
        frame_filename = f'frames/frame_{self.frameCount}.jpg'
        cv2.imwrite(frame_filename, frame)

    def readFrames(self):
        video = cv2.VideoCapture(fr'{self.route}')
        if not video.isOpened():
            print("Error al abrir el video")
            exit()
            
        while True:
            ret, frame = video.read()
            if not ret:
                break

            self.saveFrame(frame);
        video.release()

        print(f'Se extrajeron {self.frameCount} frames del video.')


if __name__ == "__main__":
    extractor = Extractor(r'C:\Users\jorge_zepeda\Desktop\Extractor-de-frames\Flujo.mp4')
    extractor.readFrames()
