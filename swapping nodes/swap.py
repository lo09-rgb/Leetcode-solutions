class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # Save the node after the pair
            temp = second.next

            # Swap the two nodes
            second.next = first
            first.next = temp
            prev.next = second

            # Move to the next pair
            prev = first

        return dummy.next
