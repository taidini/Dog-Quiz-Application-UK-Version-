# Dog Quiz Application (UK Version)

def welcome_message():
    """Display a welcome message."""
    print("Welcome to the Ultimate UK Dog Quiz!")
    print("Test your knowledge about dogs in the UK and see how well you score.\n")

def display_question(question, options):
    """Display a single question and its options."""
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    print()

def get_user_answer(num_options):
    """Get the user's answer and ensure it's valid, without displaying the input prompt."""
    while True:
        try:
            answer = int(input())  # No prompt message, just waiting for the user to input a number
            if 1 <= answer <= num_options:
                return answer
            else:
                print(f"Please enter a number between 1 and {num_options}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_score(answers, correct_answers):
    """Calculate the user's score."""
    score = 0
    for user_answer, correct_answer in zip(answers, correct_answers):
        if user_answer == correct_answer:
            score += 1
    return score

def display_results(score, total_questions):
    """Display the user's score and performance message."""
    print(f"\nYour total score is: {score}/{total_questions}")
    
    # Performance message based on score
    if score == total_questions:
        print("Excellent! You're a UK dog expert!")
    elif score >= total_questions // 2:
        print("Good job! You know a fair amount about UK dogs.")
    else:
        print("Keep learning! There's still more to discover about UK dogs.")

def thank_you_message():
    """Display a thank you message."""
    print("\nThank you for taking the UK Dog Quiz!")

def play_again():
    """Ask if the user wants to play again."""
    while True:
        again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if again == 'yes':
            dog_quiz()  # Restart the quiz
            break
        elif again == 'no':
            print("Goodbye!")
            break
        else:
            print("Please enter 'yes' or 'no'.")

def dog_quiz():
    """Main function to run the dog quiz."""
    welcome_message()

    # List of questions, each with options and the correct answer (index starts at 1 for answers)
    questions = [
        ("What is the most popular dog breed in the UK?", 
        ["Labrador Retriever", "French Bulldog", "Cocker Spaniel", "Staffordshire Bull Terrier"], 
        1),
        
        ("Which dog breed is known as the Queen's favourite?", 
        ["Dalmatian", "Corgi", "Beagle", "Dachshund"], 
        2),
        
        ("Which breed originated in Scotland and is known for its herding ability?", 
        ["Border Collie", "Golden Retriever", "West Highland Terrier", "Cairn Terrier"], 
        1),
        
        ("Which dog breed is commonly associated with British fox hunting?", 
        ["Beagle", "Greyhound", "English Foxhound", "Whippet"], 
        3),
        
        ("Which breed is known for its wrinkled face and is originally from England?", 
        ["French Bulldog", "Bulldog", "Pug", "Shih Tzu"], 
        2)
    ]

    # Check if there are any questions available
    if not questions:
        print("There are no questions available.")
        return

    user_answers = []
    correct_answers = [q[2] for q in questions]
    
    # Display each question
    for i, (question, options, _) in enumerate(questions, 1):
        print(f"\nQuestion {i}:")
        display_question(question, options)
        answer = get_user_answer(len(options))  # Now no visible prompt
        user_answers.append(answer)
        print("-" * 40)  # Separator between questions

    # Calculate and display the score
    score = calculate_score(user_answers, correct_answers)
    display_results(score, len(questions))

    thank_you_message()
    play_again()

# Run the dog quiz
if __name__ == "__main__":
    dog_quiz()
