
s = "0123456789"
for i in range(-1,-len(s)+2, -1):
    s_sliced = f'"{s[ :i: -1]}"'
    print( f'{s_sliced:12}', f" is {s}[:{str(i)}:{-1}]")
for i in range(-1,-len(s)+2, -1):
    s_sliced = f'"{s[ i:: -1]}"'
    print( f'{s_sliced:12}', f" is {s}[{str(i)}::{-1}]")

exit(0)

starts  = range(0, l-1)
s = "0123456789"
for start in range(0, len(s)-1):
    # print(f'{s}[{start}:{stop}:{steps}]')
    s_sliced = f'"{s[start::-1]}"'
    print(f'{s_sliced:11} is ', f'{s:10}[{start}::-1]')
