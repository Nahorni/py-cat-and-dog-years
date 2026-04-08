import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cate_age, dog_age,expected",
    [
        (14, 14, [0, 0]),
        (23, 23, [1, 1]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ], ids=["zero_before_threshold",
            "age_limit_of_dog_and_cat",
            "age_limit_of_cat",
            "age_limit_of_dog",
            "all_ages_dog_and_cat"])
def test_age(cate_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cate_age, dog_age) == expected
