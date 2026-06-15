def canJump(nums):
    farthest = 0

    for i in range(len(nums)):
        # If current position is unreachable
        if i > farthest:
            return False

        # Update the farthest reachable position
        farthest = max(farthest, i + nums[i])

    return True


# Example
nums = [2, 3, 1, 1, 4]
print(canJump(nums))  # True
