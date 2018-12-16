
def bank(a, years):
    ten_proc = a * 0.1
    for i in range(years):
        a = a + ten_proc
    return(a)
print(bank(100,2))