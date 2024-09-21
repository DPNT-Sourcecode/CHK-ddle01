

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
    res = 0
    for sku in skus:
        res += prices[sku]
    return -1


