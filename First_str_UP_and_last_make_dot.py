'''Любая фраза должна начинаться с заглавной буквы и закачиваться точкой'''
text = "greetings, friends"
def chg_str(text):
    return text.capitalize() if text.endswith('.') is True else text.capitalize() + '.'

print(chg_str(text))