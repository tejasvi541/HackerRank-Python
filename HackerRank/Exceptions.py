# Enter your code here. Read input from STDIN. Print output to STDOUT
def div(n):
    for i in range(n):
        ls = list(map(int, input().split()))
        a = ls.pop(0)
        b = ls.pop(0)
        try:
            print(a / b)
        except ZeroDivisionError:
            print("Error Code: integer division or modulo by zero")
        except ValueError as e:
            print("Error Code:", e)


n = int(input())
div(n)
