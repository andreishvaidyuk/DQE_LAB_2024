import time
import pytest


@pytest.fixture(scope="session", autouse=True)
def track_suite_time():
    start_time = time.time()
    yield # Run some test
    end_tine = time.time()
    total_time = end_tine - start_time
    print(f"Total suite execution time: {total_time:.4f} seconds")


@pytest.fixture(autouse=True)
def track_test_time(request):
    if request.node.name != "test_last":
        start_time = time.time()
        yield  # Run some test
        end_time = time.time()
        total_time = end_time - start_time
        print(f"\nTest {request.node.name} execution time: {total_time:.4f} seconds")


def add_numbers(a, b):
    return a + b


def test_add_two_positive_numbers():
    a, b = 3, 5
    result = add_numbers(a, b)
    time.sleep(2)
    assert result == 8


def test_add_two_negative_numbers():
    a, b = -3, -5
    result = add_numbers(a, b)
    time.sleep(3)
    assert result == -8


def test_add_negative_and_positive_numbers():
    a, b = -3, 5
    result = add_numbers(a, b)
    time.sleep(10)
    assert result == 2
