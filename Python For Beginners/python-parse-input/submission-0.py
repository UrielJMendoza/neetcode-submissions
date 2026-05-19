from typing import List

def read_integers() -> List[int]:
    read = input()

    new = read.split(",")
    return [int(x) for x in new]
    


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
