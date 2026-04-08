def get_human_age(cat_age: int, dog_age: int) -> list:
    if cat_age <= 14:
        cat_age_result = 0
    elif cat_age <= 23:
        cat_age_result = 1
    else:
        cat_age_result = 2 + (cat_age - 24) // 4
    if dog_age <= 14:
        dog_age_result = 0
    elif dog_age <= 23:
        dog_age_result = 1
    else:
        dog_age_result = 2 + (dog_age - 24) // 5

    return [cat_age_result, dog_age_result]
