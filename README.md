# SD8-23: AI-Powered Spatial Face Locking System

## Table of Contents
- [Description](#description)
- [Overall Structure and Interaction](#overall-structure-and-interaction)
- [Key Components and Data Structures/Algorithms](#key-components-and-data-structuresalgorithms)
- [Logic Flow Across Files](#logic-flow-across-files)
- [Inputs/Outputs Across the Codebase](#inputsoutputs-across-the-codebase)
- [Dependencies](#dependencies)
- [Limitations](#limitations)
- [Further Development](#further-development)


## Description

This project, SD8-23, is an AI system designed for face detection and depth estimation. Utilizing a webcam for live video input, the system identifies individuals and estimates their distance from the camera. This information is then displayed on screen in real-time. 

## Overall Structure and Interaction

At the heart of this codebase lies the `FaceDetection.py` script. It manages the capture of video data from the webcam via the `cv2.VideoCapture` object and leverages the `FaceMeshDetector` class from the `cvzone` library to detect facial landmarks. In a continuous loop, the script processes incoming frames, identifies faces, calculates depth, and visualizes the results.

## Key Components and Data Structures/Algorithms

### Key Components:
- **FaceMeshDetector (`cvzone`)**: This class is instrumental in detecting and localizing facial landmarks within each frame.
- **`faces` List**: Acting as storage, this list holds the detected faces from the current frame. Each face is represented as a collection of landmark coordinates.

### Data Structures and Algorithms:
- **Landmark Coordinates**: Represented by (x, y) coordinates, these landmarks serve as the foundation for face detection and depth estimation.
- **Euclidean Distance**:  The `findDistance` method from the `FaceMeshDetector` class is used to determine the distance between the left and right eye corners.
- **Depth Estimation**: By utilizing the calculated eye-corner distance, a predefined average face width (6.3cm), and a fixed focal length (477), depth is estimated using a simplified formula based on the pinhole camera model.

## Logic Flow Across Files
The codebase is self-contained within a single file, `FaceDetection.py`, and follows a linear flow:

1. **Initialization:**  Establishes a connection with the webcam using `cv2.VideoCapture(0)` and instantiates a `FaceMeshDetector` object.
2. **Processing Loop:**
   - Captures a frame from the webcam.
   - Utilizes `detector.findFaceMesh(img)` to detect faces within the captured frame.
   - For every detected face:
     - A visual indicator (circle) is drawn at a specific head landmark (landmark 151).
     - Calculates the distance between landmark 145 (left eye corner) and landmark 374 (right eye corner).
     - Estimates depth based on the predefined face width, focal length, and the calculated eye-corner distance.
     - Displays the estimated depth on the image.
3. **Termination:** The loop ceases upon detecting the user pressing the 'T' or 't' key.

## Inputs/Outputs Across the Codebase

- **Input:**  Live video stream sourced from the connected webcam.
- **Output:**  A window displaying the live video feed enhanced with the following:
   - Identified faces overlaid with a circle positioned on the head.
   - Estimated depth for each detected face, presented on the display.

## Dependencies
- **OpenCV**: The cornerstone for image and video manipulation, including tasks such as webcam access and image processing.
- **cvzone**: Provides the `FaceMeshDetector` class, crucial for facial landmark detection, along with other utility functions.
- **Python 3.x**: The codebase is written and intended for execution within a Python 3.x environment.

## Limitations
- **Depth Estimation Accuracy**:  Relying on predefined values for face width and focal length can introduce inaccuracies, particularly when dealing with variations in actual face sizes and differing camera configurations.
- **Calibration Requirements**: For enhanced depth estimation precision, calibration becomes essential. This process should account for the camera's intrinsic parameters and the true dimensions of the faces being analyzed.

## Further Development
- **Calibration Implementation**:  Introducing a calibration step can significantly improve depth estimation accuracy by tailoring the system to specific camera and subject characteristics.
- **Real-time Expression Tracking**: Augmenting the system with the ability to track facial expressions in real-time opens up possibilities for more nuanced interactions and applications.
- **Integration with Advanced Applications**: The depth estimation capabilities can be integrated with other technologies, such as gesture recognition or augmented reality systems, to create more immersive and interactive experiences.
