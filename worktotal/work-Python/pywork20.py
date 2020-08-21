# pywork20.py start
# <<강의 복습 13. 시작>>




all = [var for var in globals() if var[0] != "-"]
for var in all:
    del globals()[var]
del(all)
del(var)

import sys
sys.modules[__name__].__dict__.clear()


# <<강의 복습 13. 끝>>
# pywork20.py end