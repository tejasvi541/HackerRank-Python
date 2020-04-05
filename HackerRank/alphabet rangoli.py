def print_rangoli(size):
    a = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    spl = a.split(" ")
    print(spl)
    for char in a:
        asa = spl.join("-")
    print(asa)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
