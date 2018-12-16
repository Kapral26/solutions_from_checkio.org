'''
Подсчет суммы за услуги связи, в день до 100 мин по 1 монете все остальное по 2, время всегда округляемся в большую сторону
'''

from math import ceil
def total_cost(calls):
	date = {x.split(' ')[0] for x in calls}
	result = [[ceil(int(x.split(' ')[2])/60) for x in calls if x.split(' ')[0] == y] for y in date]
	result = [sum(x) for x in result] 
	return sum([x*1 if x < 100 else 100 + (x-100)*2 for x in result])


print(total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")))