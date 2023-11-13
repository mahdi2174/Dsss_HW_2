import random


def random_intiger_generator(min_value, max_value):
    """
    Generates a random integer between min_value and max_value (inclusive).
    """
    return random.randint(min_value, max_value)


def choose_operator():
    """
    Chooses a random arithmetic operator: '+', '-', or '*'.
    """
    return random.choice(['+', '-', '*'])


def evaluate_calculation(number1, number2, operator):
    """
    Evaluates the calculation formed by number1, number2, and operator.
    Returns the calculation and the result.
    """
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    else:
        result = number1 * number2

    calculation = f"{number1} {operator} {number2}"
    return calculation, result


def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        number1 = random_intiger_generator(1, 10)
        number2 = random_intiger_generator(1, 5)
        operator = choose_operator()

        problem, answer = evaluate_calculation(number1, number2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()