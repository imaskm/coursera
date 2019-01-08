# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        #print(current)
        previous, current = int(str(current)[-1]), str(int(str(previous)[-1]) + int(str(current)[-1]))[-1]

    return str(current)[0]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
