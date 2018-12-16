'''
Правило для почты, по теме. Отработывается по  определенным тригерам.

по условию, чтобы отработало правило:
	Все буквы заглавные
	Имеются триггеры в виде слов, в любом виде
	Если 3 последних символа строки - знаки припинания


Пример быстрого рещения:
import re


def is_stressful(subj):

    return (subj.isupper() or

            subj.endswith('!!!') or

            any(re.search('+[.!-]*'.join(word), subj.lower())

                for word in ['help', 'asap', 'urgent']))


'''


# -*- coding: utf-8 -*-
def is_stressful(subj):
	import re

	# Тригеры
	symbol = ['!', '?']
	alarm_words = ["help", "asap", "urgent"]

	#Массив всех заглавных букв с пробелами и символами
	all_chr_is_up = [x for x in subj if x.isupper() or x in symbol or x ==" "]

	#все елементы в нижний регистр
	subj = subj.lower()
	# Разделяем по прбелам
	array_words = subj.split(" ")
	# Оставляем только буквы
	array_words = list(re.findall("[A-z]", x) for x in array_words)
	# print(array_words)
	# Проверка совпадения наборов букв из фразы и тригера
	for x in array_words:
		for y in alarm_words:
			# Если совпали наборы букв, правило  отработало)
			if set(x) == set(y):
				# print(set(x), set(y))
				return True

	# Массив символов в последние из последних 3х елементов	
	lasts_3_symbol = [x for x in subj[-3:] if x in symbol]
	print(lasts_3_symbol, len(lasts_3_symbol))

	# Если 3 и более последних эл-та строки стмволы или длина строки заглавными буквами, правило отработало
	if len(lasts_3_symbol) >= 3 or len(subj) == len(all_chr_is_up):
		return True
	else:
		return False
# print(is_stressful("Hi"))
# print(is_stressful("I’m REALLY happy on my vacation!")) - ok
# print(is_stressful("UUUURGGGEEEEENT here"))
# print(is_stressful("I neeed HELP")) - ok
# print(is_stressful("Heeeeeey!!! I’m having so much fun!”"))
# print(is_stressful("HI HOW ARE YOU?"))