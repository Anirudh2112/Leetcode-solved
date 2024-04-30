class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        result = []
        carry = 0
        for i in range(max_len - 1, -1, -1):
            total = carry
            if a[i] == '1':
                total += 1
            if b[i] == '1':
                total += 1

            if total % 2 == 1:
                result.append('1')
            else:
                result.append('0')

            carry = total // 2

        if carry != 0:
            result.append('1')

        return ''.join(reversed(result))

