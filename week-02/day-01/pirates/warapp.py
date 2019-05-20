import 
A1_Ship1 = Ship()
A1_Ship1.fill_ship()
A1_Ship2 = Ship()
A1_Ship2.fill_ship()
A1_Ship3 = Ship()
A1_Ship3.fill_ship()
A1_Ship4 = Ship()
A1_Ship4.fill_ship()

A2_Ship1 = Ship()
A2_Ship1.fill_ship()
A2_Ship2 = Ship()
A2_Ship2.fill_ship()
A2_Ship3 = Ship()
A2_Ship3.fill_ship()

A1 = Armada(A1_Ship1, A1_Ship2, A1_Ship3, A1_Ship4)
A2 = Armada(A2_Ship1, A2_Ship2, A2_Ship3)

print(A1.war(A2))