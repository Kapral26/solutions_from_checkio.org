'''
Проверка текста на Панграмма ли он или нет
Панграмма - текст состоящий из всех букв алфавита

'''

import re
def check_pangram(text):
	text = text.lower()
	result = list(set(re.findall(r"[a-z]", text)))
	print(result, len(result))
	if len(result) == 26:
		return True
	else:
		return False

print(check_pangram("bnC_XuknwTlVL..wvNU/*s%)*BjXi?<Q.swXDk,T(k>X<&ZieBhy&IRvxbHtr<%c%mUEcXD$WB$m<']Wfbzecee-!miZotA=&)#TPGfjDB$nw_LIZ!#JecokQ(LQK*JXKqyDSrHJSG?YTLOPfwW}Wiq=-mAi%%N]Tc(v^[TvN:XW&=@rK~CbC}|DySivVj"))

