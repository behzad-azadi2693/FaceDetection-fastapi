import cv2

def face_detection(path_save_image):
    desired_size = (100, 100)
    cap = cv2.VideoCapture(0)  
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    captured_count = 0
    while captured_count < 20:
        ret, frame = cap.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            face_cropped = frame[y:y+h, x:x+w]
            face_resized = cv2.resize(face_cropped, desired_size, interpolation=cv2.INTER_AREA)
            image_filename = f"{path_save_image}/image_{captured_count + 1}.jpg"
            cv2.imwrite(image_filename, face_resized)
            captured_count += 1

        cv2.imshow("Face Detection", frame)
        cv2.waitKey(500)

    cap.release()
    cv2.destroyAllWindows()
