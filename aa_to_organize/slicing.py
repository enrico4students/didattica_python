

s = "0123456789"
for start in range(len(s)-1,0, -1):
    for stop in range(len(s)):
        # print(start, stop)
        print(f'{s}[{start}:{stop}:-1]: "{s[start:stop:-1]}"')
        markers = [' ']*10
        markers[start] = "b"
        markers[stop] = "e"
        print("".join(markers))
        print("")
