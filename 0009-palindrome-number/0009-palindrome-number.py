class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else :
            str_num=str(x)
            for i in range(len(str_num)):
                if str_num[i]==str_num[len(str_num)-1-i]:
                    continue

                else:
                    return False

        return True
                