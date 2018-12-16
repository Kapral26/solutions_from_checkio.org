''' Мое решение по сортировки словарей внутри списка '''
def bigger_price1(limit: int, data: list) -> list:
    main_dict = []
    l = []
    for price in data:
        lists = list(price.values())[0]
        try:
            int(lists)
        except:
            lists = list(price.values())[1]
        main_dict.append(lists)
    main_dict.sort()
    main_dict.reverse()
    main_dict = main_dict[:limit]
    print(main_dict)
    del lists
    
    for it in data:
        lists = list(it.values())[0]
        try:
            int(lists)
        except:
            lists = list(it.values())[1]
        print(lists)
        for i in range(len(main_dict)):
            if lists == main_dict[i]:
                l.insert(i, it)
    return(l)


''' Как надо было писать '''
def bigger_price(limit, data):

    return sorted(data, key=lambda x: x['price'], reverse=True)[:limit]


# print(bigger_price(2,top_price))

print(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

print( bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]))

print(bigger_price(2,[{"price":10,"name":"bread"},{"price":138,"name":"wine"},{"price":15,"name":"meat"},{"price":25,"name":"milk"}]))