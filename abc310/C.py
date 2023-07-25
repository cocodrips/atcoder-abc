N = int(input())
unique = set()
sub = set()
for i in range(N):
    s = input()
    if s not in unique:
        if s not in sub:
            # どっちにもない
            unique.add(s)
            sub.add(s[::-1])

print(len(unique))