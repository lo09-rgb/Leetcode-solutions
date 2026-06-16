def opposite_direction_template(nums: list[int]) -> None:
    left = 0
    right = len(nums) - 1

    while left < right:
        # Calculate or check current state
        current = calculate_something(nums, left, right)

        if found_answer(current, nums, left, right):
            # Process and possibly return
            return
        elif need_to_increase_value(current, nums, left, right):
            left += 1
        else:
            right -= 1
