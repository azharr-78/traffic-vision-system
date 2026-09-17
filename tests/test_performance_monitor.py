from src.performance_monitor import PerformanceMonitor


def test_performance_monitor():
    monitor = PerformanceMonitor()

    monitor.start()
    monitor.update()
    monitor.stop()

    statistics = monitor.get_statistics()

    assert statistics["processing_time"] >= 0
    assert statistics["fps"] >= 0


def test_initial_performance_statistics():
    monitor = PerformanceMonitor()

    statistics = monitor.get_statistics()

    assert statistics["processing_time"] == 0
    assert statistics["fps"] == 0