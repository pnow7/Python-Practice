import numpy as np

# c 문자가 몇개인지?
x = np.array([['a', 'b', 'c', 'd'],
              ['c', 'c', 'g', 'h']])

# ~~~.sum() 방식, np.sum(~~~) 방식
print(f"'c' 문자가 {(x == 'c').sum()}개 있음\n")

c_mask = (x == 'c')
count_c = np.sum(c_mask)

print(f"'c' 문자가 {count_c}개 있음")
