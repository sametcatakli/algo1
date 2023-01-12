book_price = 24.95
discount = 40
delivery_fees_first = 3
delivery_fees_extra = 0.75


def price(quantity):
    book_price_after_discount = (book_price / 100) * 60
    if quantity == 1:
        to_pay = float(book_price_after_discount) + float(delivery_fees_first)
        print(to_pay)
    elif quantity > 1:
        extra_book = quantity - 1
        extra_book_total_delivery = extra_book * delivery_fees_extra
        to_pay = extra_book_total_delivery + 3 + (quantity * book_price_after_discount)
        print(to_pay)


number = input('Nombre de livre: ')
price(int(number))
