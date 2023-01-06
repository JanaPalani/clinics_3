import cv2
from cv2 import VideoCapture
import mediapipe as mp




mp_draw = mp.solutions.drawing_utils
mp_styles = mp.solutions.drawing_styles
my_pose = mp.solutions.pose
pose = my_pose.Pose(static_image_mode = True , model_complexity = 1 ,enable_segmentation = True,min_detection_confidence = 0.6)



        
video = cv2.VideoCapture(0)
while True:
    cap,frame = video.read()
    frame=cv2.resize(frame,(749, 720))
    hight_frame , width_frame,_ = frame.shape
    frame = cv2.flip(frame,1)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    height_frame , width_frame,_ = frame.shape
    results = pose.process(frame)
    
    if results.pose_landmarks:
        
        mp_draw.draw_landmarks(frame,results.pose_landmarks,my_pose.POSE_CONNECTIONS,
                            landmark_drawing_spec=mp_draw.DrawingSpec(color=(255,255,255),thickness=3, circle_radius=3),
                            connection_drawing_spec=mp_draw.DrawingSpec(color=(49,125,237) ,thickness=2, circle_radius=2))

        
        body_landmarks = results.pose_landmarks.landmark
        
        
        right_eye = (round(body_landmarks[my_pose.PoseLandmark.LEFT_EAR.value].x*width_frame),round(body_landmarks[my_pose.PoseLandmark.LEFT_EAR.value].y*height_frame))
        
        left_eye = (round(body_landmarks[my_pose.PoseLandmark.RIGHT_EAR.value].x*width_frame),round(body_landmarks[my_pose.PoseLandmark.RIGHT_EAR.value].y*height_frame))

        right_ankle = (round(body_landmarks[my_pose.PoseLandmark.LEFT_ANKLE.value].x*width_frame),round(body_landmarks[my_pose.PoseLandmark.LEFT_ANKLE.value].y*height_frame))
        
        left_ankle = (round(body_landmarks[my_pose.PoseLandmark.RIGHT_ANKLE.value].x*width_frame),round(body_landmarks[my_pose.PoseLandmark.RIGHT_ANKLE.value].y*height_frame))
        
        cv2.line(img=frame,pt1 = (right_eye[0] - 300 , right_eye[1] - 280),pt2 = (left_eye[0] + 300,left_eye[1] - 280),thickness=3,color=(255,0,0))
        
        cv2.line(img=frame,pt1 = (right_eye[0] - 300 , right_eye[1] - 280),pt2 = (right_ankle[0] - 300 , right_ankle[1] + 80),thickness=3,color=(255,0,0))
    
        cv2.line(img=frame,pt1 = (left_ankle[0] + 300,left_ankle[1] + 80),pt2 = (left_eye[0] + 300,left_eye[1] - 280),thickness=3,color=(255,0,0))
        
        cv2.line(img=frame,pt1 = (right_ankle[0] - 300 , right_ankle[1] + 80),pt2 = (left_ankle[0] + 300,left_ankle[1] + 80),thickness=3,color=(255,0,0))
        
        
        cv2.putText(frame,"Human detected",(100,450),cv2.FONT_HERSHEY_PLAIN,4,(0,255,0),4,cv2.LINE_AA)


        
    cv2.imshow("image",frame)
    key =  cv2.waitKey(1)
    if key == 81:
        break
  
video.release()

cv2.destroyAllWindows()