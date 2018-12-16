from collections import Counter
'Подсчет в тексте указаных слов'


def new_count(text: str, words: list) -> dict:
    main_doct = Counter(text.lower().replace('\n', ' ').split(' '))
    return {x: y for x, y in main_doct.items() if x in words}


text = '''
When I was One
I had just begun
When I was Two
I was nearly new
'''

words = ['i', 'was', 'three', 'near']


print(
    new_count(text, words)
)
