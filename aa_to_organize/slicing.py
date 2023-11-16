

s = "0123456789"
start_marker, stop_marker = "b", "e"
print(f"'{start_marker}': start/beginning(inizio) '{stop_marker}': end (fine) NB. ")


"""
def show_slicing(start_range_inf: int, start_range_sup: int):
    for start in range(start_range_inf,0, -1):
        for stop in range(len(s)):
            # print(start, stop)
            print(f'{s}[{start}:{stop}:-1]: "{s[start:stop:-1]}"')
            markers = [' ']*10
            markers[start] = start_marker
            markers[stop] = stop_marker
            print("".join(markers)+"\n")
"""




for start in range(len(s)-1,0, -1):
    for stop in range(len(s)):
        # print(start, stop)
        print(f'{s}[{start}:{stop}:-1]: "{s[start:stop:-1]}"')
        markers = [' ']*10
        markers[start] = start_marker
        markers[stop] = stop_marker
        print("".join(markers)+"\n")

print("-"*50)
for stop in range(-1,-len(s)+1, -1):
    for start in range(len(s)):
        # print(start, stop)
        print(f'{s}[{start}:{stop}:-1]: "{s[start:stop:-1]}"')
        markers = [' ']*10
        markers[start] = start_marker
        markers[stop] = stop_marker
        print("".join(markers))
        print("")
