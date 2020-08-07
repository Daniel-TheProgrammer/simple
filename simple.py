<!--Created by Daniel theProgrammer-->

import re
text = str(input())
result = re.sub(r"[^\w\s]", "", text)
res = re.sub(r"\d", "", result)

def reverse(res):
    res = res[::-1]
    return res

print (reverse(res))
