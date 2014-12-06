if __name__ == "__main__":
    m,d = map(int, raw_input().split())
    if m % d == 0:
        print "YES"
    else:
        print "NO"

