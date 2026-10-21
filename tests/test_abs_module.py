
import pytest

from maths.abs import abs_val, abs_min, abs_max, abs_max_sort

@pytest.mark.unit
@pytest.mark.parametrize("num, expected", [
    (-5, 5),
    (5, 5),
    (0, 0),
    (-3.5, 3.5),
    (2.5, 2.5)
])
def test_abs_val(num, expected):
    assert abs_val(num) == expected

@pytest.mark.unit
@pytest.mark.parametrize("numbers, expected", [
    ([0, 5, 1, 11], 0),
    ([3, -10, -2], -2),
    ([-3, -1, 2, -11], -1),
    ([7], 7)
])
def test_abs_min(numbers, expected):
    assert abs_min(numbers) == expected

@pytest.mark.unit
@pytest.mark.parametrize("numbers, expected", [
    ([0, 5, 1, 11], 11),
    ([3, -10, -2], -10),
    ([-3, -1, 2, -11], -11),
    ([7], 7)
])
def test_abs_max(numbers, expected):
    assert abs_max(numbers) == expected

@pytest.mark.unit
@pytest.mark.parametrize("numbers, expected", [
    ([0, 5, 1, 11], 11),
    ([3, -10, -2], -10),
    ([-3, -1, 2, -11], -11),
    ([7], 7)
])
def test_abs_max_sort(numbers, expected):
    assert abs_max_sort(numbers) == expected

@pytest.mark.unit
def test_abs_min_empty_list():
    with pytest.raises(ValueError):
        abs_min([])

@pytest.mark.unit
def test_abs_max_empty_list():
    with pytest.raises(ValueError):
        abs_max([])
@pytest.mark.unit
def test_abs_max_sort_empty_list():
    with pytest.raises(ValueError):
        abs_max_sort([])

import csv
from pathlib import Path
def load_csv_data():
    file_path = Path(__file__).parent.parent / "test_data" / "abs_test_data.csv"

    with open(file_path, newline="") as file:
        reader = csv.DictReader(file)
        return [(float(row["num"]), float(row["expected"])) for row in reader]

@pytest.mark.csv_data
@pytest.mark.parametrize("num, expected", load_csv_data())
def test_abs_val_from_csv(num, expected):
    assert abs_val(num) == expected
