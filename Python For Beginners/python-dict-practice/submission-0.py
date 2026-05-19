from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    dicts = {}
    for i in range(len(word)):
        if word[i] not in dicts:
            dicts[word[i]] = 1
        else:
            dicts[word[i]] +=1
    return dicts




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
