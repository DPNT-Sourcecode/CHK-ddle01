

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if skus == "":
        return 0
    
    indexs = {
        "A":0,
        "B":1,
        "C":2,
        "D":3,
        "E":4,
        "F":5,
    }
    count = [0,0,0,0,0,0]
    prices = [50,30,20,15,40,10]

    res = 0
    for sku in skus:
        if sku not in indexs.keys():
            return -1
        count[indexs[sku]] += 1

    # Checking for offers, reducing count if offer found
    
    #Offers for A
    if count[0] >= 5:
        offersA = count[0] // 5
        res += offersA * 200
        count[0] = count[0] % 5
    
    if count[0] >= 3:
        offersA = count[0] // 3
        res += offersA * 130
        count[0] = count[0] % 3

    #Offer for E
    if count[4] >= 2:
        offersE = count[4] // 2
        count[1] = max(0, count[1] - offersE)

    #Offer for B
    if count[1] >= 2:
        offersB = count[1] // 2
        res += offersB * 45
        count[1] = count[1] % 2

    #Offer for F
    if count[5] >= 3:
        offersF = count[5] // 3
        count[5] = count[5] - offersF

    # adding the remaining non-offer itemss
    for index in range(len(count)):
        res += count[index] * prices[index]
    return res

print(checkout("FFFFF"))