import cv2
import mediapipe as mp
import pyautogui
import winsound

x1 = y1 = x2 = y2 = 0

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    refine_landmarks=True,
    max_num_faces=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

camera = cv2.VideoCapture(0)

while True:
    success, image = camera.read()

    if not success:
        break

    image = cv2.flip(image, 1)

    # Get image width and height
    fh, fw, _ = image.shape

    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    output = face_mesh.process(rgb_image)

    landmark_points = output.multi_face_landmarks

    if landmark_points:
        landmarks = landmark_points[0].landmark

        for id, landmark in enumerate(landmarks):

            x = int(landmark.x * fw)
            y = int(landmark.y * fh)

            # Draw every landmark
            cv2.circle(image, (x, y), 1, (0, 255, 0), -1)

            if id == 43:
                x1, y1 = x, y

            if id == 287:
                x2, y2 = x, y

        # Draw line between smile points
        cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 2)

        dist = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)

        cv2.putText(image, f"Distance: {int(dist)}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2)

        print(dist)
        if dist > 80:
            cv2.imwrite("selfie.png",image)
            cv2.waitKey(100)

    cv2.imshow("Auto Selfie", image)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()