class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def peek(self):
        if self.stack:
            return self.stack[-1]
        return None

    def isEmpty(self):
        return len(self.stack) == 0


def NGE():
    n = int(input("Enter the number of elements: "))
    arr = []

    for i in range(n):
        arr.append(int(input("Enter element: ")))

    st = Stack()
    ans = [-1] * n

    # Traverse from right to left
    for i in range(n - 1, -1, -1):

        # Remove all smaller or equal elements
        while not st.isEmpty() and st.peek() <= arr[i]:
            st.pop()

        # If stack is not empty, top is the answer
        if not st.isEmpty():
            ans[i] = st.peek()

        # Push current element
        st.push(arr[i])

    print("\nNext Greater Elements:")
    for i in range(n):
        print(f"{arr[i]} -> {ans[i]}")


NGE()
