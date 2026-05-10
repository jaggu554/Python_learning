words = ["cat", "dog", "elephant", "bat", "tiger"]

dicts={}
def group_word_length(words):
    for i in words:
        if len(i) not in dicts:
            dicts[len(i)]=[]
            dicts[len(i)].append(i)
        else:
            dicts[len(i)].append(i)

    return dicts

print(group_word_length(words))
        

