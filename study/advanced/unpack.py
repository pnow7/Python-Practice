def print_numbers(a, *args):
     print(a)
     print(args)

print(print_numbers(1))

print(print_numbers(1, 10, 20))

print(print_numbers(*[10, 20, 30]))

# def print_numbers(*args, a):처럼 
# *args가 고정 매개변수보다 앞쪽에 오면 안 됩니다. 
# 매개변수 순서에서 *args는 반드시 가장 뒤쪽에 와야 합니다.