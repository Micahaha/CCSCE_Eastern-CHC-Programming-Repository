WCK = [2, 7, 9, 3, 3, 3] # small burger, large burger, specialty burger, fries, drink, dessert
WCK_COMBO_1 = 9 # large + fries + drink

CMS = [3, 6, 10, 3, 2, 4] # small burger, large burger, speciality burger, fries, drink, dessert
CMS_COMBO_1 = 11 # Speciality + desert
CMS_COMBO_2 = 4 # small + fries

def order():
    order = input("Enter item numbers separated by spaces: ").split(" ")
    order_to_int = [int(i) for i in order] # [1 2 3 2 0 1]
    return order_to_int


def calculate_WCK_total(customer_order):
    wck_total = 0
    temp_order = customer_order.copy()

    ## combo 1: large + fries + drink

    ## just grab smallest value of the three

    # grabs smallest value because that is the max number of combos possible
    
    combo_1 = min(temp_order[1], temp_order[3], temp_order[4]) # large + fries + drink

    wck_total += combo_1 * WCK_COMBO_1

    ## subtract combo items from temp order
    temp_order[1] -= combo_1
    temp_order[3] -= combo_1
    temp_order[4] -= combo_1

    for i in range(len(temp_order)):
        quantity = temp_order[i]
        price = WCK[i]
        wck_total += quantity * price
    return wck_total

def calculate_CMS_total(customer_order):
    cms_total = 0
    temp_order = customer_order.copy()

    combo_1 = min(temp_order[2], temp_order[5]) # speciality + dessert
    combo_2 = min(temp_order[0], temp_order[3]) # small + fries

    cms_total += combo_1 * CMS_COMBO_1

    temp_order[2] -= combo_1
    temp_order[5] -= combo_1
    temp_order[0] -= combo_2
    temp_order[3] -= combo_2

    for i in range(len(temp_order)):
        quantity = temp_order[i]
        price = CMS[i]
        cms_total += quantity * price
    return cms_total

def compare_orders(cms_total, wck_total):
    if cms_total < wck_total:
        return f"CMS  ${cms_total}"
    elif wck_total < cms_total:
        return f"WCK  ${wck_total}"




def main():
    print("Welcome to the Combo Deal Calculator!")

    user_order = order() # [1 2 3 2 0 1]
    print(user_order)
    wck_total = calculate_WCK_total(user_order)
    cms_total = calculate_CMS_total(user_order)

    print(compare_orders(cms_total, wck_total))


main()
