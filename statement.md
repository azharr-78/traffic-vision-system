# Project Statement

Project Title

**Intelligent Object Detection, Tracking and Counting System Using Computer Vision**

Problem Statement

In traffic videos, it can be difficult to manually keep track of every vehicle and person, especially when several objects are present at the same time. Manual counting also takes time and may not always give consistent results.

The aim of this project is to build a computer vision system that can analyze a traffic video automatically. The system detects objects in the video, gives them tracking IDs, and counts them when they cross a predefined line. It also calculates some basic traffic statistics and saves the results for further analysis.

Objectives

The main objectives of this project are:

* Detect objects from a traffic video.
* Track detected objects across different frames.
* Assign IDs to individual objects.
* Count objects crossing a selected counting line.
* Display class-wise counts such as cars and persons.
* Calculate the average and maximum number of objects in the video.
* Give a basic traffic level based on the detected objects.
* Measure the processing time and FPS.
* Save the analysis results in CSV and JSON formats.
* Generate an output video with the detection and analysis information.

Scope of the Project

The project works with recorded traffic videos. The video is processed frame by frame using Python and OpenCV.

A pretrained YOLO model is used for object detection, so the project does not require training a new model. The detected objects are tracked using the tracking functionality provided by the YOLO framework.

The counting is done using a horizontal virtual line. The position of this line can be changed according to the camera view by using the `--line-y` option.

The current project focuses on basic traffic analysis rather than a complete traffic management system.

Main Features

1. Video Processing

The system reads the input video and processes it frame by frame. The processed frames are then combined into a new output video.

2. Object Detection

YOLO is used to detect objects in each frame. The system can identify classes supported by the pretrained model, such as cars, motorcycles, and persons.

3. Object Tracking

Each detected object is assigned a tracking ID. The ID helps the system follow the same object across multiple frames.

4. Object Counting

A virtual horizontal line is placed in the video. When a tracked object crosses the line, it is counted.

The system also keeps separate counts for different object classes.

5. Traffic Analysis

The system calculates basic statistics from the video, including:

* Average number of objects per frame
* Maximum number of objects in a frame
* Traffic level

The traffic level is currently classified into three categories:

* LOW
* MEDIUM
* HIGH

6. Performance Monitoring

The system records the total processing time and calculates the processing FPS.

7. Report Generation

After processing the video, the system generates:

* `traffic_report.json`
* `traffic_report.csv`

These files contain the counting and traffic analysis results.

8. Output Video

The final video contains the YOLO bounding boxes and tracking IDs along with the counting line and traffic statistics.

Target Users

This project can be useful for:

* Students learning computer vision
* Students working on video processing projects
* Researchers experimenting with object detection and tracking
* Developers building simple traffic-analysis applications

Technologies Used

* Python
* OpenCV
* YOLO
* Ultralytics
* Computer Vision
* CSV
* JSON
* Git and GitHub

Expected Output

The main output of the system is an annotated video showing detected and tracked objects.

The system also produces CSV and JSON files containing the final counting and traffic-analysis results.

For example, during testing, one of the processed videos produced the following results:

* Processed frames: 456
* Total objects counted: 6
* Cars counted: 5
* Persons counted: 1
* Average objects per frame: 7.25
* Maximum objects in a frame: 11
* Traffic level: HIGH
* Processing time: 82.89 seconds
* Processing FPS: 5.5

These values are dependent on the input video and system performance.
