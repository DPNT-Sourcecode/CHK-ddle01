

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if skus == "":
        return -1
    prices = {
        "A":50,
        "B":30,
        "C":20,
        "D":15
    }
    count = [0,0,0,0]
    res = 0
    for sku in skus:
        if sku == "A":
            count[0] += 1
        elif sku == "B":
            count[1] += 1
        elif sku == "C":
            count[2] += 1
        elif sku == "D":
            count[3] += 1
    return -1



