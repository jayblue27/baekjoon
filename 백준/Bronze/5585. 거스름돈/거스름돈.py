n = int(input())

def changes(n = n):
    money = 1000 - n
    coin_list = [500, 100, 50, 10, 5, 1]

    count_dict = {}

    while money != 0:
        for coin in coin_list:
            count_bool = 0
            count_bool = money // coin

            if count_bool != 0:
                count_dict[coin] = count_bool
                money = money - (coin * count_bool)
    
    return sum(count_dict.values())

print(changes())