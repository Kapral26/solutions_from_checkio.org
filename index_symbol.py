def index_sym(text,ind):
    try:
        return text.index(ind)
    except:
        return None

text = 'kalatuha'
ind = 'k'
print(
    index_sym(text, ind)
)