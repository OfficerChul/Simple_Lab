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

## Method 3: Using Retinaface
RetinaFace is a deep learning based cutting-edge facial detector for Python coming with facial landmarks.
> Reference: https://github.com/serengil/retinaface
```angular2html
1. Detect face using Retinaface in every frame of the video
2. Blur images using OpenCV
3. Do 1, 2 in every frame of videos and merge into video again
```

