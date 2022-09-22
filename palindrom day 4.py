strs=""
strs=strs.casefold()
rev_strs = reversed (strs)
if list(strs)==list(rev_strs):
    print("true")
else:
    print("false")
