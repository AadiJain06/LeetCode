class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the last digit and move backwards
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, it becomes 0 and we carry over to the next loop
            digits[i] = 0
        
        # If we finished the loop, it means we had a carry out of the most significant digit
        # e.g., [9, 9] -> [0, 0] -> [1, 0, 0]
        return [1] + digits