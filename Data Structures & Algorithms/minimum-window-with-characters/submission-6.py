class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""
        len_s = len(s)
        t_count, window = Counter(t), {}
        have, need = 0, len(t_count)
        res,resLen = [-1,-1], math.inf

        l=0
        for r in range(len_s):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            
            if c in t_count and window[c]==t_count[c]:
                have+=1
            
            while have==need:
                if (r-l+1) < resLen:
                    res=[l,r]
                    resLen=r-l+1
                window[s[l]]-=1
                if s[l] in t_count and window[s[l]]<t_count[s[l]]:
                    have-=1
                l+=1
        l,r = res[0],res[1]
        return s[l:r+1] if resLen !=math.inf else ""





        
        
        
        
        # if t=="": return ""
        # t_map = Counter(t)
        # t_len = len(t)
        # s_len = len(s)
        # res, resLen=[0,0], math.inf
        # s_map={}
        # # sliding window
        # l,r = 0, 0

        # def compare_map(s_map,t_map):
        #     for char,count in t_map.items():
        #         if not (char in s_map and s_map[char]>=count):
        #             return False
        #     return True
        
        # s_map={}
        
        # while l<=r and r<s_len:
        #     s_map[s[r]] = s_map.get(s[r], 0) + 1
        #     while compare_map(s_map,t_map):
        #         if r-l+1<resLen:
        #             res=[l,r]
        #             resLen=r-l+1
        #         s_map[s[l]] = s_map.get(s[l], 0) - 1
        #         l+=1
        #     r+=1
        # return s[res[0]:res[1]+1] if resLen!=math.inf else ""
            


                
            

        
        
        # brute force
        # for curr_len in range(t_len,s_len+1):
        #     for i in range(s_len):
        #         if i+curr_len>s_len:
        #             break
        #         s_map = Counter(s[i:i+curr_len])

        #         # compare both the hm
        #         flag=True
        #         for char,count in t_map.items():
        #             if not (char in s_map and s_map[char]>=count):
        #                 flag=False
        #                 break
        #         if flag:
        #             return s[i:i+curr_len]
        # return ""