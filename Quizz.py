questions = {
    "What is the capital of India?" : "delhi",
    "How many states does India have?" : "29",
    "What is the capital of Maharashtra?" : "mumbai",
    "Ranchi is the capital of which Indian state?" : "jharkhand",
    "How many union territories are there in india?" : "7"
}

def ask_question(question, answer):
    user = input(f"{question} ").strip().lower()
    return user == answer

score = 0
for q,a in questions.items():
    if ask_question(q,a):
        print("Correct!!")
        score+=1
    else:
        print(f"Noo! the answer was {a}.")

print(f"\nYour Final Score: {score}/{len(questions)}")