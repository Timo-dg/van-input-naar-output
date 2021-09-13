# Timo de Gruiter Pizza Calculator 

# pizzaSmall = 6.95
# pizzaMedium = 8.70
# pizzaLarge = 11.95

#pizza prijzen en formaat
beschikbaarFormaat =  ['small', 'medium', 'large']
pizza_prijs = {'small': 6.95, 'medium': 8.70, 'large': 11.95}
sub_total = []
final_order = {}
customer_adress = {}

#Bestel systeem
order_pizza = True
while order_pizza:    
    print(                        )
    print("Kies je pizza: ")
    print('prijzen: small €6,95, medium €8,70, large €11,95')
    print('---------------------------')
    print()
    for pizzas in beschikbaarFormaat:
        print(pizzas)
        print()
        print('---------------------------')
    while True:
        pizza = input("Welke pizza wilt u bestellen?")
        if pizza in beschikbaarFormaat:
            print(f"Je hebt een {pizza} besteld.")
            sub_total.append(pizza_prijs[pizza])
            break
        if pizza not in beschikbaarFormaat:
            print(f"We hebben geen {pizza}.")
    extra_pizza = input("Wilt u nog een pizza bestellen?")
    if extra_pizza == "nee":
        for key, value in final_order.items():
            print(f"\nje hebt een {key} pizza met {value}")
        check_order = True
        while check_order:
            print()
            order_correct = input("Klopt dit? ja/nee ")
            if order_correct == "ja":
                check_order = False
                order_pizza = False
            if order_correct == "nee":
                print(final_order)
                add_remove = input("Wilt u een pizza verwijderen of toevoegen? ")
                if add_remove == "verwijderen":
                    remove = input("Welke pizza wilt u verwijderen? ")
                    del final_order[remove]
                    print(final_order)
                if add_remove == "toevoegen":
                    check_order = False
print(f"\nde totaal prijs: €{sum(sub_total)}")