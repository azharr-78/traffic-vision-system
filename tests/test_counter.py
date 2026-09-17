from src.counter import ObjectCounter


def test_counter_initial_state():
    counter = ObjectCounter(line_y=500)

    counts = counter.get_counts()

    assert counts["total"] == 0
    assert counts["by_class"] == {}


def test_counter_line_position():
    counter = ObjectCounter(line_y=500)

    assert counter.line_y == 500