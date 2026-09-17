from src.traffic_analyzer import TrafficAnalyzer


def test_empty_analyzer():
    analyzer = TrafficAnalyzer()

    assert analyzer.get_average_objects() == 0
    assert analyzer.get_traffic_level() == "LOW"


def test_analyzer_statistics():
    analyzer = TrafficAnalyzer()

    assert analyzer.total_frames == 0
    assert analyzer.total_objects == 0
    assert analyzer.max_objects == 0