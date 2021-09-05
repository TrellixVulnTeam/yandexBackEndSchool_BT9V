test = input() # "market_1.csv billing_1.csv" # to input change
marketFilename, billingFilename = test.split(" ")

print("order_id,shop_name,shop_id,cost") # i am Headings

shopMap = {}
billArr = []

billNum = 0
test = []

with open(marketFilename) as market:
    market.readline() #header
    for lineMarket in market:
        # billArr.append(lineMarket.strip("\n"))
        billNum = billNum + 1

def get_line_by_number(num):
    with open(marketFilename) as market:
        market.readline() #header
        i = 0
        for lineMarket in market:
            if i == num:
                return lineMarket
            i = i + 1

def binary_search(low, high, x):
    if high >= low:
        mid = (high + low) // 2
        (shop_id_bill, shop_name_bil) = get_line_by_number(mid).strip("\n").split(",")
        if shop_id_bill == x:
            return shop_name_bil
        elif shop_id_bill > x:
            return binary_search(low, mid - 1, x)
        else:
            return binary_search(mid + 1, high, x)
    else:
        return None

with open(billingFilename) as billing:
    billing.readline() #header
    for lineBilling in billing:
        (order_id, shop_id, cost) = lineBilling.strip("\n").split(",")
        shop_name = binary_search(0, billNum - 1, shop_id)
        if shop_name is not None:
            print(",".join([order_id, shop_name, shop_id, cost]))
