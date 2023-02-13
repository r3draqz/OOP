import insectClass as ic

def main():
    mosquito = ic.insect('mosquito', 2, 4)
    housefly = ic.insect('housefly', 2, 4)

    mosquito.lenflight()
    housefly.lenflight()

    print(f'the {mosquito.get_name()} can fly up to, {mosquito.get_miles()} miles')
    print(f'the {housefly.get_name()} can fly up to, {housefly.get_miles()} miles')

    print()

    print('I am going to calculate the flight 10 times:')
    print()

    for count in range(10):
        mosquito.lenflight()
        print(f'This is the length of the flight of the {mosquito.get_name()}:', mosquito.get_miles())
        housefly.lenflight()
        print(f'This is the length of the flight of the {housefly.get_name()}:', housefly.get_miles())

main()