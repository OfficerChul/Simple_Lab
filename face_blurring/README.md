# Face Blurring

## Notes
```
- Should use GPU in the server
    - Failed to use GPU of Retinaface due to the dependency issues
        - Driver updates automatically
- Should try multiple ways of face blurring method to use GPU
- Differences between Deepface and Retinaface
    - DeepFace is better suited for large-scale facial recognition tasks, while RetinaFace is ideal for detecting and analyzing faces in complex and dynamic environments.
```

## Method 1: Using Haar-cascade algorithm in OpenCV
```
Haar-cascade algorithm couldn't detect the face in the video
```

## Method 2: Using Mediapipe Face Detection Algorithm
```angular2html
It cannot detect the face.
```

## Method 3: Using DeepFace()
DeepFace is the most lightweight face recognition and facial attribute analysis library for Python.
```

```

## Method 4: Using Retinaface
RetinaFace is a deep learning based cutting-edge facial detector for Python coming with facial landmarks.
```angular2html
Reference: https://github.com/elliottzheng/face-detection
```
landmarks in Retinaface
- right_eye
- left_eye
- nose
- mouth_right
- mouth_left
