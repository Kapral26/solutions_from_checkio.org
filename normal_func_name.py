def from_camel_case(name):
	print(name.lower())
	res = [x if x.islower() or x == name[0] else '_' + x for x in name]
	name = ''.join(res).lower()
	return name

exem = "MyFunctionName"
print(from_camel_case(exem))