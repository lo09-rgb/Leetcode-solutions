def generate_permutations(chars, index):
    # Base case
    if index == len(chars):
        print("".join(chars))
        return

    for i in range(index, len(chars)):
        # Swap
        chars[index], chars[i] = chars[i], chars[index]

        # Recurse
        generate_permutations(chars, index + 1)

        # Backtrack
        chars[index], chars[i] = chars[i], chars[index]


word = input("Enter a string: ")

generate_permutations(list(word), 0)
