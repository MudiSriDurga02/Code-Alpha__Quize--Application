import random
# Define a list of questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "answer": "Blue Whale"
    }
]

# Shuffle the questions to randomize their order
random.shuffle(questions)

# Initialize the user's score
score = 0

# Function to display a question and check the user's answer
def ask_question(question, options, answer):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    
    user_answer = input("Your answer (enter the number): ")
    
    if user_answer.isdigit():
        user_answer = int(user_answer)
        if 1 <= user_answer <= len(options):
            if options[user_answer - 1] == answer:
                print("Correct!\n")
                return True
    print(f"Wrong! The correct answer is {answer}.\n")
    return False

# Main quiz loop
for question in questions:
    question_text = question["question"]
    options = question["options"]
    answer = question["answer"]
    if ask_question(question_text, options, answer):
        score += 1

# Display the user's score
print(f"You got {score} out of {len(questions)} questions correct.")