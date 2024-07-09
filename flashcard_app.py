
# Samoan Language Flashcard App! 

import random 

# Here's the list of dictionaries, but I'm putting them in a function so they're reusable 
def get_flashcards():
    return[
        # Samoan word, English word
        {"Samoan": "tālofa", "English": "hello"},
        {"Samoan": "fa'afetai", "English": "thank you"},
        {"Samoan": "aiga", "English": "family"},
        {"Samoan": "fa'amalie atu", "English": "sorry"},
        {"Samoan": "siva", "English": "dance"},
        {"Samoan": "vai", "English": "water"},
        {"Samoan": "ta'avale", "English": "car"},
        {"Samoan": "fale", "English": "house"},
        {"Samoan": "pua'a", "English": "pig"},
        {"Samoan": "fanua", "English": "land"},
        {"Samoan": "lā", "English": "sun"},
        {"Samoan": "vaiaso", "English": "week"},
        {"Samoan": "tausaga", "English": "year"},
        {"Samoan": "manu", "English": "bird"},
        {"Samoan": "tamaloa", "English": "man"},
        {"Samoan": "fafine", "English": "woman"},
        {"Samoan": "tama", "English": "boy"},
        {"Samoan": "teine", "English": "girl"},
        {"Samoan": "nofoa", "English": "chair"},
        {"Samoan": "vasa", "English": "ocean"}
    ]

def generate_choices(correct_answer, all_flashcards):
    choices = [correct_answer]
    while len(choices) < 3:
        choice = random.choice(all_flashcards)['English']
        if choice not in choices:
            choices.append(choice)
    random.shuffle(choices)
    return choices

def get_user_choice(flashcard, all_flashcards):
    choices = generate_choices(flashcard['English'], all_flashcards)
    print(f"Samoan: {flashcard['Samoan']}")
    for idx, choice in enumerate(choices):
        print(f'{idx + 1}. {choice}')
    return choices

def run_quiz(flashcards):
    score = 0
    trouble_words = []
    sampled_flashcards = random.sample(flashcards, 10) # Limit to 10 questions
    for index, flashcard in enumerate(sampled_flashcards):
        choices = get_user_choice(flashcard, flashcards)
        user_input = int(input("Enter the number of your choice: ")) - 1
        if choices[user_input] == flashcard['English']:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect. Try again.")
            trouble_words.append((index + 1, flashcard))
            user_input = int(input("Enter the number of your choice: ")) - 1
            if choices[user_input] == flashcard['English']:
                print("Correct!\n")
                score += 1
            else:
                print(f"Incorrect. The correct translation is: {flashcard['English']}\n")
    return score, trouble_words

def main():
    print()
    print("Welcome to the Samoan Flashcard Quiz App!\n Let's get started!")
    print()
    flashcards = get_flashcards()
    score, trouble_words = run_quiz(flashcards)
    print(f"Quiz complete! You got {score} out of 10 words correct!")
    if trouble_words:
        print("\nYou had some trouble with the following questions:")
        for index, word in trouble_words:
            print(f"Question {index}: Remember that '{word['Samoan']}' means '{word['English']}'.")
    print()


if __name__ == "__main__":
    main()