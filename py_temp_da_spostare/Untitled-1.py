import os

depth = 0
def split_fully(path):
    global depth
    depth+= 1
    parent_path, name = os.path.split(path)    
    if name == '':
        print(f"depth {depth} returning '{parent_path}' name: '{name}'")
        depth-= 1
        return (parent_path, )
    else:
        print(f"depth {depth} recursive call, input is '{parent_path}'' name: '{name}'")
        splitted  = split_fully(parent_path)
        depth-= 1
        print(f"depth {depth} returning '{splitted}' name: '{name}'")
        return splitted + (name, ) # concatenates

os.chdir(r'F:\youtube-download\downloads\small-videos\German for intermediate learners (B1 - B2)')
wdir = os.getcwd()
dir_splitted = split_fully(wdir)
print(type(dir_splitted))
print(dir_splitted)
