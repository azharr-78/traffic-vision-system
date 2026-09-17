import csv
import json


class ReportGenerator:

    def __init__(self, output_directory="output"):
        self.output_directory = output_directory

    def generate_report(self, counts, statistics):

        report = {
            "total_objects_counted": counts["total"],
            "class_counts": counts["by_class"],
            "average_objects_per_frame": statistics["average_objects"],
            "maximum_objects_in_frame": statistics["maximum_objects"],
            "traffic_level": statistics["traffic_level"]
        }

        return report

    def save_json(self, report):

        path = f"{self.output_directory}/traffic_report.json"

        with open(path, "w") as file:
            json.dump(report, file, indent=4)

        return path

    def save_csv(self, report):

        path = f"{self.output_directory}/traffic_report.csv"

        with open(path, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(["Metric", "Value"])

            writer.writerow([
                "Total Objects Counted",
                report["total_objects_counted"]
            ])

            writer.writerow([
                "Average Objects Per Frame",
                report["average_objects_per_frame"]
            ])

            writer.writerow([
                "Maximum Objects In Frame",
                report["maximum_objects_in_frame"]
            ])

            writer.writerow([
                "Traffic Level",
                report["traffic_level"]
            ])

            writer.writerow([])

            writer.writerow([
                "Object Class",
                "Count"
            ])

            for class_name, count in report["class_counts"].items():

                writer.writerow([
                    class_name,
                    count
                ])

        return path