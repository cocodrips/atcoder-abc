if __name__ == "__main__":
    a, b, c = map(int, raw_input().split())
    if a + b == c and a - b == c:
        print "?"
    elif a + b == c:
        print "+"
    elif a - b == c:
        print "-"
    else:
        print "!"
