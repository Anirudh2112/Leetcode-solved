class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        char_to_bit = {chr(i): 1 << (i - ord('a')) for i in range(ord('a'), ord('j') + 1)}
        mask_count = {0: 1}
        current_mask = 0
        wonderful_count = 0
        
        for char in word:
            current_mask ^= char_to_bit[char]
            if current_mask in mask_count:
                wonderful_count += mask_count[current_mask]

            for i in range(10):  
                test_mask = current_mask ^ (1 << i)
                if test_mask in mask_count:
                    wonderful_count += mask_count[test_mask]
            
            if current_mask in mask_count:
                mask_count[current_mask] += 1
            else:
                mask_count[current_mask] = 1
                
        return wonderful_count