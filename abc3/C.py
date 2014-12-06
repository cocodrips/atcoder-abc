N, K = map(int, raw_input().split())
Rs = map(int, raw_input().split())

rating = 0
for r in sorted(Rs)[N - K:]:
    rating = (r + rating) / 2.0
print rating