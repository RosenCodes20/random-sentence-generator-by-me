import random
names = ["Rosen", "Ioan", "Ivelin", "Kristiqn", "Georgi", "Kaloqn"]
places = ["Sofia", "Plovdiv", "Varna", "Burgas", "Botevgrad", "Pravec"]
verbs = ["eats", "holds", "sees", "plays with", "brings", "jump", "sleep"]
nouns = ["stones", "cake", "apple", "laptop", "bikes", "computer", "playstation"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly","fast"]
details = ["near the river", "at home", "in the park", "on the basketball court", "at school"]


def random_word(words):
    return random.choice(words)


print("Hello this is your first random sentence:")
while True:
    random_names = random_word(names)
    random_places = random_word(places)
    random_verbs = random_word(verbs)
    random_nouns = random_word(nouns)
    random_adverbs = random_word(adverbs)
    random_details = random_word(details)

    print(f"{random_names} from {random_places} {random_adverbs} {random_verbs} {random_nouns} {random_details}.")
    input("Click [Enter] to create new sentence.")
