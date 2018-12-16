'''
Поиск заданных слов, в тарабарщине

'''

def count_words(text: str, words: set) -> int:
    import re
    ll = [re.findall(x, text.lower()) for x in words if re.findall(x, text.lower())]
    return len(ll)

print(count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}))
