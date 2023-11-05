import cv2
import numpy as np
import pyttsx3
import time
from datetime import datetime
from driver_prediction import predict_result  # You should import this from the appropriate module

class VideoCaptureWithSegments:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = None
        self.segment_start_time = None
        self.speech_time = None  # To track the speech time

    def start_segment(self):
        filename = "segment_{}.avi".format(int(time.time()))
        self.out = cv2.VideoWriter(filename, self.fourcc, 10.0, (640, 480))  # Adjust the fps as needed
        self.segment_start_time = time.time()
        self.speech_time = None  # Reset the speech time

    def end_segment(self):
        if self.out:
            self.out.release()
            self.out = None
        self.segment_start_time = None
        self.speech_time = None  # Reset the speech time

    def capture_and_save(self):
        threelabel = ""  # Initialize threelabel

        (H, W) = (None, None)  # Moved from inside the loop
        last_label = None
        same_label_start_time = None

        while True:
            ret, frame = self.cap.read()
            if ret:
                if W is None or H is None:
                    (H, W) = frame.shape[:2]
                output = frame.copy()
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (128, 128))
                frame = np.expand_dims(frame, axis=0).astype('float32') / 255 - 0.5

                label = predict_result(frame)
                text = "activity: {}".format(label)
                cv2.putText(output, text, (35, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.25, (0, 255, 0), 5)

                if last_label != label:
                    same_label_start_time = time.time()
                    last_label = label

                if self.out:
                    self.out.write(output)
                    current_time = time.time()

                    if self.speech_time is None and label != "SAFE DRIVING":
                        self.speech_time = current_time
                        engine = pyttsx3.init()
                        engine.say(label)
                        engine.runAndWait()

                    if current_time - self.segment_start_time >= 15:
                        self.end_segment()
                        print("Segment saved.")

                cv2.imshow('Live Feed', output)

                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break

                if label == "SAFE DRIVING":
                    self.end_segment()  # End the current segment before starting a new one
                elif label != threelabel:
                    threelabel = label
                    now = datetime.now()
                    pre_time = int(now.strftime("%S"))
                else:
                    current_time = int(datetime.now().strftime("%S"))
                    if current_time <= 2:
                        current_time = 60 + current_time
                    if current_time - pre_time == 3:
                        self.start_segment()

        self.cap.release()
        cv2.destroyAllWindows()

def main():
    video_capture = VideoCaptureWithSegments()
    video_capture.capture_and_save()

if __name__ == "__main__":
    main()
