class Solution():
    def multiply(self, num1, num2):
        if int(len(num1)) and int(len(num2)) <= 200:
            return str(int(num1)*int(num2))

sol = Solution()
sol.multiply("123","456")