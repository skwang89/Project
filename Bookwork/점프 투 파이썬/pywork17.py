# pywork17.py start
# <<강의 복습 10. 시작>>


















all = [var for var in globals() if var[0] != "-"]
for var in all:
    del globals()[var]
del(all)
del(var)

import sys
sys.modules[__name__].__dict__.clear()


# <<강의 복습 10. 끝>>
# pywork17.py end