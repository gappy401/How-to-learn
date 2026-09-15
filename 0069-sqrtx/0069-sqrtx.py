class Solution:
    def mySqrt(self, x: int) -> int:
        low=0
        high=x
        ans=1


        if x <=1:
            return x

        while low <= high :
            mid = low + (high-low)//2
            if (mid*mid) == x:
                return mid
            
            elif (mid*mid) > x:
                high = mid -1
                ans=mid-1
            

            else:
                low = mid+1
                
        return ans

        
                
                


    
        