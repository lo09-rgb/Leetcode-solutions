class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


def evaluate_prefix(expression):
    s = Stack()

    # Scan from right to left
    for ch in expression[::-1]:

        # If operand, push onto stack
        if ch.isdigit():
            s.push(int(ch))

        # If operator
        else:
            operand1 = s.pop()
            operand2 = s.pop()

            if ch == '+':
                result = operand1 + operand2

            elif ch == '-':
                result = operand1 - operand2

            elif ch == '*':
                result = operand1 * operand2

            elif ch == '/':
                result = operand1 // operand2  # Integer division

            s.push(result)

    return s.pop()


def main():
    expression = input().strip()
    print(evaluate_prefix(expression))


if __name__ == "__main__":
    main()
