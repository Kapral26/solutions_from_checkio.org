
## Old version
# def between_markers3(text: str, begin: str, end: str) -> str:
#     """
#         returns substring between two given markers
#     """
#     if len(begin) == 1 or len(end) == 1:
#         id_begin = text.index(end)
#         id_end = text.index(begin)
#         result = text[id_end+1:id_begin]
#     else:
#         list1 = text.split(end)
#         list2 = list1[0].split(begin)
#         result = list2[-1]
#     return result

def between_markers3(text: str, begin: str, end: str) -> str:
    return text.split(begin)[1].split(end)[0]

text = 'What is >apple<'
begin = ">"
end = "<"

print(between_markers3(text, begin, end))

del text
del begin
del end

text = "<head><title>My new site</title></head>"
begin = "<title>"
end = "</title>"

print(between_markers3(text, begin, end))

del text
del begin
del end


text = "No <hi>"
begin = '>'
end = '<'
print(between_markers3(text, begin, end))
