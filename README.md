# Traffic Vision System

This project processes recorded traffic video to detect, track, and count objects such as cars, motorcycles, and people. It uses a pretrained YOLO model for detection and a simple line-crossing rule to count objects as they pass a selected point in the frame.

The goal is to automate the traffic-counting process without manual frame-by-frame review. The system also calculates basic traffic statistics and saves the results in CSV and JSON format.


## Features

- Read and process a traffic video
- Detect objects using YOLO
- Track objects with unique IDs
- Count objects when they cross a predefined horizontal line
- Keep separate counts for each object class
- Measure average and maximum objects per frame
- Classify traffic as LOW, MEDIUM, or HIGH
- Overlay detection data on the output video
- Monitor processing time and FPS
- Generate JSON and CSV reports


## Workflow

```text
Input video
   ↓
Video processing
   ↓
YOLO detection
   ↓
Object tracking
   ↓
Line crossing count
   ↓
Traffic analysis
   ↓
Performance monitoring
   ↓
Output video + reports
```

## Technologies

- Python 3.12
- OpenCV
- Ultralytics YOLO
- NumPy
- CSV
- JSON
- Pytest


## Project Structure

```text
traffic-vision-system/
├── input/
│   └── README.md
├── output/
│   └── README.md
├── src/
│   ├── __init__.py
│   ├── counter.py
│   ├── detector.py
│   ├── main.py
│   ├── performance_monitor.py
│   ├── report_generator.py
│   ├── tracker.py
│   ├── traffic_analyzer.py
│   └── video_processor.py
├── tests/
│   ├── test_counter.py
│   ├── test_performance_monitor.py
│   └── test_traffic_analyzer.py
├── .gitignore
├── README.md
├── requirements.txt
└── statement.md


## Main Modules

### `main.py`
This is the entry point of the project. It connects the video-processing pipeline, detection, tracking, counting, reporting, and output generation.

### `detector.py`
This module loads the YOLO model and performs object detection and tracking.

### `counter.py`
This module checks each tracked object and decides whether it crossed the counting line. Each tracking ID is counted only once.

### `traffic_analyzer.py`
This module calculates the number of processed frames, average objects per frame, maximum objects in one frame, and the overall traffic level.

### `performance_monitor.py`
This module tracks processing time and FPS for the video analysis.

### `report_generator.py`
This module creates the final CSV and JSON reports based on the counting results.

## `tracker.py`

This module is part of the project's tracking-related source structure.

The object tracking used by the main pipeline is provided through the Ultralytics YOLO tracking functionality.

## Requirements

Install the required packages with:

```powershell
pip install -r requirements.txt
```

The project depends on:

```text
ultralytics
opencv-python
numpy
```

## Installation

### 1. Clone the project

```powershell
git clone https://github.com/azharr-78/traffic-vision-system.git
cd traffic-vision-system
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

### 3. Activate it

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```


## Running the Project

Place the input video in the `input` folder, then run:

```powershell
python src/main.py --input input/traffic.mp4 --output output/final.mp4 --line-y 900
```

This produces:

```text
output/final.mp4
output/traffic_report.json
output/traffic_report.csv
```

---

## Command-line Arguments

The program supports the following arguments:

| Argument | Description |
| --- | --- |
| `--input` | Path to the input video |
| `--output` | Path for the processed output video |
| `--confidence` | Detection confidence threshold |
| `--line-y` | Y-position of the counting line |

Example:

```powershell
python src/main.py \
    --input input/traffic.mp4 \
    --output output/final.mp4 \
    --confidence 0.5 \
    --line-y 800
```

The counting line should be within the height of the input video.

## EXAMPLE
python src/main.py --input input/traffic.mp4 --output output/final.mp4 --confidence 0.5 --line-y 800

## How Counting Works

The system uses the center point of each detected bounding box. If the center of an object crosses the horizontal line, it is counted once for that tracking ID.

The logic is simple:
1.The current center Y-coordinate is calculated.
2.The previous center Y-coordinate is stored.
3.The current and previous positions are compared with the counting line.
4.If the object moves across the line, it is counted.
5.The tracking ID is stored in a set.
6.If the same tracking ID crosses the line again, it is not counted again.

## Traffic Analysis

The system calculates:

- total processed frames
- average objects per frame
- maximum number of objects in one frame
- traffic level

The current classification rules are:

```text
Average objects < 3   -> LOW
Average objects < 7   -> MEDIUM
Average objects >= 7  -> HIGH
```

These thresholds are simple project-defined rules and are not an official traffic standard.


## Generated Reports

### JSON report
The JSON file includes summary values such as:

```json
{
  "total_objects_counted": 6,
  "class_counts": {
    "car": 5,
    "person": 1
  },
  "average_objects_per_frame": 7.25,
  "maximum_objects_in_frame": 11,
  "traffic_level": "HIGH"
}
```

### CSV report
The CSV report contains the same main statistics in a table format that can be opened in spreadsheet software.

### Testing

The project contains unit tests for the main supporting modules.

Run the tests using:

      python -m pytest

The tests cover:

Object counter initialization
Counting-line configuration
Traffic analyzer initialization
Traffic analyzer statistics
Performance monitor initialization
Performance monitor execution

The tests verify the basic behavior of the supporting modules without requiring the complete video-processing pipeline for every test.

## Example Result

A successful test run produced the following output:

```text
Processed frames: 456
Total objects counted: 6
Class counts: car = 5, person = 1
Average objects per frame: 7.25
Maximum objects in a frame: 11
Traffic level: HIGH
Processing time: 82.89 seconds
Processing FPS: 5.5
```

The final annotated video and both report files were generated successfully.


## Limitations

This version is intentionally simple and has a few limitations:

1. The counting line is set with the `--line-y` argument.
2. It works with recorded video, not a live camera feed.
3. Processing speed depends on the hardware used.
4. It uses a pretrained YOLO model rather than a custom-trained one.
5. Each object is counted only once after crossing the line.
6. Traffic classification is based on project-defined thresholds.


## Possible Improvements

Some useful next steps could include:

- interactive counting-line selection
- separate incoming and outgoing counts
- vehicle speed estimation
- lane-based analysis
- real-time camera input
- a web dashboard for viewing results
- historical data storage
- custom model training for specific environments
- more detailed traffic-density analysis


## Conclusion

This project demonstrates a practical way to combine object detection, tracking, and traffic analysis in a single Python pipeline. It is a lightweight computer-vision solution for counting and summarizing movement in recorded traffic footage.

It is useful as a learning project and as a starting point for more advanced traffic-monitoring systems.
