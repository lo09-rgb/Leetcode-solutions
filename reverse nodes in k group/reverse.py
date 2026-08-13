class Solution:
    def reverseKGroup(self, head, k):
        # Dummy node makes reconnecting groups easier
        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy

        while True:
            # 1. Find the kth node
            kth = group_prev

            for _ in range(k):
                kth = kth.next

                # Fewer than k nodes remain
                if kth is None:
                    return dummy.next

            # 2. Save the node after this group
            group_next = kth.next

            # 3. Reverse the k nodes
            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # 4. Connect previous group to reversed group
            old_group_start = group_prev.next
            group_prev.next = kth

            # 5. Move group_prev to the end of the reversed group
            group_prev = old_group_start
