

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if skus == "":
        return 0
    #ord("A") = 65
    valueA = 65

    count = []
    for i in range(65,91):
        count.append(0)
    
    prices = [50,30,20,15,40,10,20,10,35,60,80,90,15,40,10,50,30,50,30,20,40,50,20,90,10,50]

    res = 0
    for sku in skus:
        if ord(sku) < 65 or ord(sku) > 90:
            return -1
        count[ord(sku)-valueA] += 1

    # Checking for free items
    applyFreeOffer(count,ord("E"),ord("B"),2)


    # Checking for offers, reducing count if offer found
    res += applyDiscount(count,ord("A"),5,200)
    res += applyDiscount(count,ord("A"),3,130)
    res += applyDiscount(count,ord("B"),2,45)
    res += applyDiscount(count,ord("H"),10,80)
    res += applyDiscount(count,ord("H"),5,45)
    res += applyDiscount(count,ord("K"),2,150)
    res += applyDiscount(count,ord("P"),5,200)
    res += applyDiscount(count,ord("Q"),3,80)
    res += applyDiscount(count,ord("V"),3,130)
    res += applyDiscount(count,ord("V"),2,90)

    #Offer for E
    if count[4] >= 2:
        offersE = count[4] // 2
        count[1] = max(0, count[1] - offersE)

    #Offer for F
    if count[5] >= 3:
        offersF = count[5] // 3
        count[5] = count[5] - offersF

    # adding the remaining non-offer itemss
    for index in range(len(count)):
        res += count[index] * prices[index]
    return res

def applyDiscount(count,index,quantity,price):
    valueA = 65
    index = index - valueA
    curr = 0

    if count[index] >= quantity:
        offersA = count[index] // quantity
        curr = offersA * price
        count[index] = count[index] % quantity

    return curr

def applyFreeOffer(count,index1,index2,quantity):
    valueA = 65
    index1 = index1 - valueA
    index2 = index2 - valueA
    if count[index1] >= quantity:
        freeItems = count[index1] // quantity
        count[index2] = max(0,count[index2] - freeItems)

print(checkout("EEBBB"))