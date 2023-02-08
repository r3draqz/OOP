import insectClass as ic

def main():
    my_insect = ic.insect()

    print('This is the length of the flight of the insect:', my_insect.get_lenflight())

    print('I am going to calculate the flight 10 times:')
    for count in range(10):
        my_insect.lenflight()
        print('This is the length of the flight of the insect:', my_insect.get_lenflight())

main()