def main():
    menu_prices = {
        "Kai Thot": 25,
        "Khao Mu Krop": 50,
        "Mu Krathiam": 45,
        "Pla Nin Thot": 80,
        "Khaoniao": 5
    }
    food_1, food_2, food_3 = input(), input(), input()
    total_price = menu_prices[food_1] + menu_prices[food_2] + menu_prices[food_3]
    print(total_price, "Baht")
main()