class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # freq map
        n1,n2 = len(s1), len(s2)
        
        if n2<n1:
            return False

        count_s1 = [0]*26
        curr=[0]*26
        for i in range(n1):
            print(ord(s1[i]))
            count_s1[ord('z')-ord(s1[i])]+=1
            curr[ord('z')-ord(s2[i])]+=1
        
        for i in range(0,n2):
            if curr==count_s1:
                return True
            else:
                curr[ord('z')-ord(s2[i])]-=1
                if i+n1<n2:
                    curr[ord('z')-ord(s2[i+n1])]+=1
                else:
                    break

        return False

        
            



        # # sorting
        # n1,n2 = len(s1), len(s2)
        # if n2<n1:
        #     return False
        # s1 = sorted(s1)
        # for i in range(n2):
        #     if i+n1<=n2:
        #         if  sorted(s2[i:i+n1])==s1:
        #             return True
        #     else:
        #         break
        # return False
