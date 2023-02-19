import FoodClass as fc

# trans = fc.Transaction()

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}

order_total = 0

cid = 570
name = 'Danni Sellyar'
address = '97 Mitchell Way Hewitt Texas 76712'
email = 'dsellyarft@gmpg.org'
phone = '254-555-9362'
memstat = False

cust = fc.Customer(cid, name, address, email, phone, memstat)

if cid == 569:
    print('Customer Name:', cust.getname())
    print('Phone:', cust.getphone())
    cid = 570
else:
    print('Customer Name:', cust.getname())
    print('Phone:', cust.getphone())
    cid = 569

for ok, ov in dict.items():
    for info in ov:
        if ov[3] == cust.getcid():
            trans = fc.Transaction(ov[0], ov[1], ov[2], ov[3])
            order_total += trans.getcost()
            print('Order Item: ', trans.getitemnm(), '  ', 'Price: $', format(trans.getcost(), '.2f'), sep = '')
            break

print('Total Cost: $', format(order_total, '.2f'), sep= '')

if cust.get_memstat() == True:
    discount = .2 * order_total
    grandtotal = order_total - (discount)
    print('Member Discount: $', format(discount, '.2f'), sep = '')
    print('Total Cost After Discount: $', format(grandtotal, '.2f'), sep = '')