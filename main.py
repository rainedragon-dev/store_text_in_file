def collect_sentences():
    """
    Collects three sentences from the user and returns them as a list.
    """
    sentences = []
    for i in range(1, 4):
        sentence = input(f"Enter sentence {i}: ")
        sentences.append(sentence)
    return sentences


def save_sentences_to_file(sentences, file_name="user_sentences.txt"):
    """
    Saves the provided sentences to a text file with dash lines in between.
    """
    splitter = "-----------"
    with open(file_name, 'w') as file:
        for i, sentence in enumerate(sentences):
            file.write(sentence + '\n')
            # Add splitter after each sentence except the last
            if i < len(sentences) - 1:
                file.write(splitter + '\n')
    print(f"Sentences have been saved to {file_name}.")


def main():
    """
    Main function to handle the process flow.
    """
    sentences = collect_sentences()
    save_sentences_to_file(sentences)


# Run the program
main()