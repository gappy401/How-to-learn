class Solution:
    def isValid(self, s: str) -> bool:

        pair={"(":")",
        "[":"]",
        "{":"}"
        }

        stack=[]

        for i in range(len(s)):

            if i == 0:
                stack.append(s[i])

            else:
                if len(stack) != 0:
                    curr = stack.pop()
                    
                    if curr in pair and pair[curr] == s[i]:
                        continue
                    else:
                        stack.append(curr)
                        stack.append(s[i])
                
                
                else:
                    stack.append(s[i])
        
        if len(stack) == 0:
            return True

        return False
