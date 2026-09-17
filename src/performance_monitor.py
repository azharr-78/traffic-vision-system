import time


class PerformanceMonitor:

    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.frame_count = 0

    def start(self):
        self.start_time = time.time()

    def update(self):
        self.frame_count += 1

    def stop(self):
        self.end_time = time.time()

    def get_statistics(self):

        if self.start_time is None or self.end_time is None:
            return {
                "processing_time": 0,
                "fps": 0
            }

        processing_time = self.end_time - self.start_time

        if processing_time > 0:
            fps = self.frame_count / processing_time
        else:
            fps = 0

        return {
            "processing_time": round(processing_time, 2),
            "fps": round(fps, 2)
        }