class TrafficAnalyzer:

    def __init__(self):
        self.total_frames = 0
        self.total_objects = 0
        self.max_objects = 0

    def update(self, result):

        self.total_frames += 1

        current_objects = 0

        if result.boxes is not None:
            current_objects = len(result.boxes)

        self.total_objects += current_objects

        if current_objects > self.max_objects:
            self.max_objects = current_objects

    def get_average_objects(self):

        if self.total_frames == 0:
            return 0

        return self.total_objects / self.total_frames

    def get_traffic_level(self):

        average = self.get_average_objects()

        if average < 3:
            return "LOW"

        elif average < 7:
            return "MEDIUM"

        else:
            return "HIGH"

    def get_statistics(self):

        return {
            "frames": self.total_frames,
            "average_objects": round(
                self.get_average_objects(), 2
            ),
            "maximum_objects": self.max_objects,
            "traffic_level": self.get_traffic_level()
        }