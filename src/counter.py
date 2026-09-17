class ObjectCounter:

    def __init__(self, line_y):
        self.line_y = line_y

        self.counted_ids = set()
        self.previous_positions = {}

        self.total_count = 0
        self.class_counts = {}

    def update(self, result):

        if result.boxes is None:
            return

        boxes = result.boxes

        if boxes.id is None:
            return

        ids = boxes.id.int().cpu().tolist()
        classes = boxes.cls.int().cpu().tolist()
        coordinates = boxes.xyxy.cpu().tolist()

        for object_id, class_id, box in zip(
            ids,
            classes,
            coordinates
        ):

            x1, y1, x2, y2 = box

            center_y = int((y1 + y2) / 2)

            previous_y = self.previous_positions.get(object_id)

            self.previous_positions[object_id] = center_y

            if previous_y is None:
                continue

            # Check if object crossed the line
            crossed_down = (
                previous_y < self.line_y
                and center_y >= self.line_y
            )

            crossed_up = (
                previous_y > self.line_y
                and center_y <= self.line_y
            )

            crossed = crossed_down or crossed_up

            if crossed and object_id not in self.counted_ids:

                self.counted_ids.add(object_id)

                self.total_count += 1

                class_name = result.names[class_id]

                self.class_counts[class_name] = (
                    self.class_counts.get(class_name, 0) + 1
                )

    def get_counts(self):

        return {
            "total": self.total_count,
            "by_class": self.class_counts.copy()
        }