from ultralytics import YOLO


class ObjectDetector:
    def __init__(self, model_name="yolo11n.pt", confidence=0.5):
        self.model = YOLO(model_name)
        self.confidence = confidence

    def detect(self, frame):
        results = self.model(
            frame,
            conf=self.confidence,
            verbose=False
        )

        return results[0]

    def track(self, frame):
        results = self.model.track(
            frame,
            conf=self.confidence,
            persist=True,
            verbose=False
        )

        return results[0]

    def draw_detections(self, frame, result):
        return result.plot()