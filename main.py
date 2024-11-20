def enter_three_sentances():

    # Takes inut form user t oset three sentances
    sentance_one = input("Enter sentance 1: ")
    sentance_two = input("Enter sentance 2: ")
    sentance_three = input("Enter sentance 3: ")
    splitter = "-----------"

    # Opens user_sentance.txt file for writing
    f = open('user_sentances.txt', 'w')


    # Writes list to open file and closes file
    f.write(f"{sentance_one}\n")
    f.write(f"{splitter}\n")
    f.write(f"{sentance_two}\n")
    f.write(f"{splitter}\n")
    f.write(f"{sentance_three}")
    f.close()
    print("Sentances have been saved to user_sentances.txt.")

enter_three_sentances()