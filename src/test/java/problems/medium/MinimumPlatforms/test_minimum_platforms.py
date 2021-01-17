from src.main.java.problems.medium.MinimumPlatforms.minimum_platforms_shorter import minimumPlatform
from typing import List
from src.main.java.problems.medium.MinimumPlatforms.minimum_platforms import is_earlier, is_interval_in, is_interval_in_schedule, is_time_in, is_later, minimumPlatformSlow
import pytest


test_data = [
    (6, ['0900', '0940', '0950', '1100', '1500', '1800'],
     ['0910', '1200', '1120', '1130', '1900', '2000'], 3),
    (3, ['0900', '1100', '1235'], ['1000', '1200', '1240'], 1)
]


@pytest.mark.parametrize("number,arrival_times,departure_times,expected_result", test_data)
def test_minimum_platforms(number: int, arrival_times: List[str], departure_times: List[str], expected_result: int):
    assert expected_result == minimumPlatformSlow(
        number, arrival_times, departure_times)


@pytest.mark.parametrize("number,arrival_times,departure_times,expected_result", test_data)
def test_minimum_platforms_shorter(number: int, arrival_times: List[str], departure_times: List[str], expected_result: int):
    assert expected_result == minimumPlatform(
        number, arrival_times, departure_times)


test_data_is_later = [
    ([9, 50], [9, 40], True),
    ([10, 0], [9, 50], True),
    ([9, 0], [9.40], False),
    ([8, 50], [9, 50], False)
]


@pytest.mark.parametrize("time,base_time,expected_result", test_data_is_later)
def test_is_later(time: List[int], base_time: List[int], expected_result: bool):
    assert expected_result == is_later(time, base_time)


test_data_is_earlier = [
    ([9, 30], [9, 40], True),
    ([8, 50], [9, 0], True),
    ([10, 0], [9.40], False),
    ([9, 55], [9, 50], False)
]


@pytest.mark.parametrize("time,base_time,expected_result", test_data_is_earlier)
def test_is_earlier(time: List[int], base_time: List[int], expected_result: bool):
    assert expected_result == is_earlier(time, base_time)


test_data_is_time_in = [
    ([[9, 30], [9, 40]], [9, 0], False),
    ([[8, 50], [9, 0]], [8, 50], False),
    ([[8, 50], [9, 0]], [9, 0], False),
    ([[9, 0], [9.40]], [8, 0], False),
    ([[8, 45], [9, 50]], [9, 0], True),
    ([[8, 45], [9, 50]], [9, 40], True),
    ([[8, 45], [9, 50]], [8, 50], True)
]


@pytest.mark.parametrize("interval,time,expected_result", test_data_is_time_in)
def test_is_time_in(interval: List[List[int]], time: List[int], expected_result: bool):
    assert expected_result == is_time_in(interval, time)


test_data_is_interval_in = [
    ([[9, 30], [9, 40]], [[9, 0], [9, 20]], False),
    ([[8, 50], [9, 0]], [[8, 40], [8, 50]], False),
    ([[8, 50], [9, 0]], [[9, 0], [9, 20]], False),
    ([[9, 0], [9.40]], [[8, 0], [8, 30]], False),
    ([[8, 45], [9, 50]], [[9, 0], [10, 0]], True),
    ([[8, 45], [9, 50]], [[9, 40], [9, 45]], True),
    ([[8, 45], [9, 50]], [[8, 50], [8, 55]], True)
]


@pytest.mark.parametrize("interval,interval_to_test,expected_result", test_data_is_interval_in)
def test_is_interval_in(interval: List[List[int]], interval_to_test: List[List[int]], expected_result: bool):
    assert expected_result == is_interval_in(interval, interval_to_test)


test_data_is_interval_in_schedule = [
    ([[[9, 30], [9, 40]], [[10, 0], [10, 20]]], [[9, 0], [9, 20]], False),
    ([[[8, 50], [9, 0]], [[10, 0], [10, 20]]], [[8, 40], [8, 50]], False),
    ([[[8, 50], [9, 0]], [[10, 0], [10, 20]]], [[9, 0], [9, 20]], False),
    ([[[9, 0], [9.40]], [[10, 0], [10, 20]]], [[8, 0], [8, 30]], False),
    ([[[8, 45], [9, 50]], [[18, 0], [18, 20]]], [[9, 0], [10, 0]], True),
    ([[[8, 45], [9, 50]], [[18, 0], [18, 20]]], [[9, 40], [9, 45]], True),
    ([[[8, 45], [9, 50]], [[18, 0], [18, 20]]], [[8, 50], [8, 55]], True),
    ([[]], [[8, 50], [8, 55]], False)
]


@ pytest.mark.parametrize("schedule,interval_to_test,expected_result", test_data_is_interval_in_schedule)
def test_is_interval_in_schedule(schedule: List[List[List[int]]], interval_to_test: List[List[int]], expected_result: bool):
    assert expected_result == is_interval_in_schedule(
        schedule, interval_to_test)
