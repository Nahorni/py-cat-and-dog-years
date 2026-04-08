from app.main import get_human_age


def test_get_human_age_should_be_min_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_be_zero_before_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_be_the_first_age_limit_of_dog_and_cat() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_be_end_of_the_first_age_limit_of_dog_and_cat() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_be_the_second_age_limit_of_dog_and_cat() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_be_end_of_the_second_age_limit_of_cat() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_should_be_end_of_the_second_age_limit_of_dog() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_be_all_ages_dog_and_cat() -> None:
    assert get_human_age(100, 100) == [21, 17]
