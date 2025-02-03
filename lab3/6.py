def reverse_words(sentense):
    words = sentense.split()
    reverse_sentence = " ".join(words[::-1])
    return reverse_sentence

user_input=input("soilem_engz")
print("kery_retpen:" , reverse_words(user_input))