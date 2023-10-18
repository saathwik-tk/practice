def longestKSubstr(s, k):
    # code here
    l=vc=maxLen=0
    vowels={'a','e','i','o','u','A','E','I','O','U'}
    vowelwindow=set()
    n=len(s)
    for r in range(n):
        print(s[l:r+1])
        if s[r] in vowels and s[r] not in vowelwindow:
            vc+=1
            vowelwindow.add(s[r])
            if vc==k:
                maxLen=max(maxLen,r-l+1)
            elif vc>k:
                while s[l] not in vowels:
                    l+=1
                vowelwindow.remove(s[l])
                l+=1
        else:
            maxLen=max(maxLen,r-l+1)
    return maxLen
print(longestKSubstr('',2))
