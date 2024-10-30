import random

LETTER_SCORES = {
    "А": 1,
    "Б": 3,
    "В": 1,
    "Г": 3,
    "Д": 2,
    "Е": 1,
    "Ё": 3,
    "Ж": 5,
    "З": 5,
    "И": 1,
    "К": 2,
    "Л": 2,
    "M": 2,
    "H": 1,
    "О": 1,
    "П": 2,
    "Р": 1,
    "С": 1,
    "Т": 1,
    "У": 1,
    "Ф": 10,
    "X": 5,
    "Ц": 5,
    "Ч": 5,
    "Ш": 8,
    "Щ": 10,
    "Ъ": 10,
    "Ы": 4,
    "Ь": 3,
    "Э": 8,
    "Ю": 8,
    "Я": 3,
}


def get_random_letter():
    converted_dictionary = list(LETTER_SCORES.keys())
    random_letter = random.choice(converted_dictionary)
    return random_letter


def get_word_with_letter(letter):
    status = False
    while status == False:
        word = input("Введите слово на букву " + letter + ":")
        if word[0].upper() == letter:
            return word
        else:
            print("Слово должно начинаться с буквы " + letter + " .Попробуйте снова")


def calculate_score(word):
    all_scores = []
    for letters in range(len(word)):
        let = word[letters].upper()
        all_scores.append(LETTER_SCORES.get(let))
    sum_scores = sum(all_scores)
    return sum_scores


if __name__ == "__main__":
    letter = get_random_letter()
    print("Начальная буква " + letter)
    print("Игрок 1")
    word_one = get_word_with_letter(letter)
    print("Игрок 2")
    word_two = get_word_with_letter(letter)
    score1 = calculate_score(word_one)
    score2 = calculate_score(word_two)
    print("Игрок 1 ввсел слово", word_one, "и набрал", score1, "очков")
    print("Игрок 2 ввсел слово", word_two, "и набрал", score2, "очков")
    if score1 > score2:
        print("Выиграл игрок 1")
    elif score1 < score2:
        print("Выиграл игрок 2")
    elif score1 == score2:
        print("Ничья")
