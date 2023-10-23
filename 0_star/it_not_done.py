def main():
    sentence = input()
    new_sentence = ""
    for i in range(0, len(sentence)):
        if sentence[i].isupper():
            new_sentence += sentence[i].lower()
        else:
            new_sentence += sentence[i].upper()
    print(new_sentence)
main()