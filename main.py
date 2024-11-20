def enter_three_sentances():

    # Takes input form user for three sentances
    sentence_one = input("Enter sentence 1: ")
    sentence_two = input("Enter sentence 2: ")
    sentence_three = input("Enter sentence 3: ")
    splitter = "-----------"

    # Opens user_sentance.txt file for writing
    f = open('user_sentances.txt', 'w')


    # Writes list to open file
    with open('user_sentences.txt', 'w') as file:
        file.write(f"{sentence_one}\n")
        file.write(f"{splitter}\n")
        file.write(f"{sentence_two}\n")
        file.write(f"{splitter}\n")
        file.write(f"{sentence_three}")

    print("Sentances have been saved to user_sentances.txt.")

enter_three_sentances()