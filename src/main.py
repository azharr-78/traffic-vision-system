import argparse
import cv2

from detector import ObjectDetector
from counter import ObjectCounter
from traffic_analyzer import TrafficAnalyzer
from report_generator import ReportGenerator
from performance_monitor import PerformanceMonitor


def main():

    parser = argparse.ArgumentParser(
        description="Intelligent Object Detection, Tracking and Counting System"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to input video"
    )

    parser.add_argument(
        "--output",
        default="output/analytics.mp4",
        help="Path to output video"
    )

    parser.add_argument(
        "--confidence",
        type=float,
        default=0.5,
        help="YOLO confidence threshold"
    )

    parser.add_argument(
        "--line-y",
        type=int,
        default=None,
        help="Y-coordinate of counting line"
    )

    args = parser.parse_args()

    # YOLO detector
    detector = ObjectDetector(
        model_name="yolo11n.pt",
        confidence=args.confidence
    )

    # Open video
    cap = cv2.VideoCapture(args.input)

    if not cap.isOpened():
        raise FileNotFoundError(
            f"Could not open input video: {args.input}"
        )

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 30

    # Counting line
    if args.line_y is not None:
        line_y = args.line_y
    else:
        line_y = int(height * 0.60)

    if line_y <= 0 or line_y >= height:
        raise ValueError(
            f"Invalid line position: {line_y}. "
            f"Choose a value between 1 and {height - 1}."
        )

    # Initialize modules
    counter = ObjectCounter(line_y)
    analyzer = TrafficAnalyzer()
    performance = PerformanceMonitor()
    performance.start()

    # Output video
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    writer = cv2.VideoWriter(
        args.output,
        fourcc,
        fps,
        (width, height)
    )

    if not writer.isOpened():
        raise RuntimeError(
            f"Could not create output video: {args.output}"
        )

    print("Starting intelligent traffic analysis...")
    print(f"Input: {args.input}")
    print(f"Output: {args.output}")
    print(f"Video size: {width}x{height}")
    print(f"Counting line Y: {line_y}")

    frame_count = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        # YOLO detection + tracking
        result = detector.track(frame)

        # Object counting
        counter.update(result)

        # Traffic analytics
        analyzer.update(result)

        # Draw YOLO boxes and IDs
        annotated_frame = detector.draw_detections(
            frame,
            result
        )

        # Draw counting line
        cv2.line(
            annotated_frame,
            (0, line_y),
            (width, line_y),
            (0, 0, 255),
            3
        )

        cv2.putText(
            annotated_frame,
            "COUNTING LINE",
            (20, line_y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2
        )

        # Get statistics
        counts = counter.get_counts()
        statistics = analyzer.get_statistics()

        # Display total count
        cv2.putText(
            annotated_frame,
            f"Total Count: {counts['total']}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        # Display traffic level
        cv2.putText(
            annotated_frame,
            f"Traffic Level: {statistics['traffic_level']}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 0),
            2
        )

        # Display average objects
        cv2.putText(
            annotated_frame,
            f"Average Objects: {statistics['average_objects']}",
            (20, 115),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        # Display maximum objects
        cv2.putText(
            annotated_frame,
            f"Maximum Objects: {statistics['maximum_objects']}",
            (20, 150),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        # Display class counts
        y_position = 190

        for class_name, count in counts["by_class"].items():

            text = f"{class_name}: {count}"

            cv2.putText(
                annotated_frame,
                text,
                (20, y_position),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 255),
                2
            )

            y_position += 30

        # Save frame
        writer.write(annotated_frame)

        frame_count += 1
        performance.update()

        if frame_count % 30 == 0:

            print(
                f"Processed {frame_count} frames | "
                f"Counted: {counts['total']} | "
                f"Traffic: {statistics['traffic_level']}"
            )
    performance.stop()
    performance_stats = performance.get_statistics()
    # Release resources
    cap.release()
    writer.release()

    # Final statistics
    final_counts = counter.get_counts()
    final_statistics = analyzer.get_statistics()

    print("\n================================")
    print("Traffic Analysis Completed!")
    print("================================")

    print(f"Processed frames: {frame_count}")

    print(
        f"Total objects counted: "
        f"{final_counts['total']}"
    )

    print(
        f"Class counts: "
        f"{final_counts['by_class']}"
    )

    print(
        f"Average objects per frame: "
        f"{final_statistics['average_objects']}"
    )

    print(
        f"Maximum objects in a frame: "
        f"{final_statistics['maximum_objects']}"
    )

    print(
        f"Traffic level: "
        f"{final_statistics['traffic_level']}"
    )
        # Generate reports
    report_generator = ReportGenerator()

    report = report_generator.generate_report(
        final_counts,
        final_statistics
    )

    json_path = report_generator.save_json(report)
    csv_path = report_generator.save_csv(report)

    print(f"JSON report: {json_path}")
    print(f"CSV report: {csv_path}")
    print(
    f"Processing time: "
    f"{performance_stats['processing_time']} seconds"
    )

    print(
        f"Processing FPS: "
        f"{performance_stats['fps']}"
    )
    print(f"Saved to: {args.output}")


if __name__ == "__main__":
    main()