class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Converting strings to lists to match your logic
        main_list = list(t)
        pattern = list(s)
        
        last_found_index = -1 
        is_subsequence = True

        for pattern_char in pattern:
            found = False
            # Scan the main list along with its actual index positions
            for index, main_char in enumerate(main_list):
                # The character must match AND its index must be greater than the last one
                if main_char == pattern_char and index > last_found_index:
                    last_found_index = index  # Update our boundary to this new index
                    found = True
                    break # Stop looking for this character and move to the next pattern letter
                    
            if not found:
                is_subsequence = False
                break

        return is_subsequence
