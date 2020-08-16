# pywork14.py start
# <<강의 복습 7. 시작>>





all = [var for var in globals() if var[0] != "_"]
for var in all:
    del globals()[var]
del(all)
del(var)

import sys
sys.modules[__name__].__dict__.clear()

# <<강의 복습 7. 끝>>
# pywork14.py end