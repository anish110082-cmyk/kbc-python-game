import time
questions = [
    (
        "What is the capital of India?",
        ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        ("B", "New Delhi", "Delhi")
    ),
    (
        "Who is the CM of Bihar?",
        ["A. Nitish Kumar", "B. Narendra Modi", "C. Arvind Kejriwal", "D. Yogi Adityanath"],
        ("A", "Nitish Kumar")
    ),
    (
        "Which player scored the highest runs in a single IPL season?",
        ["A. Rohit Sharma", "B. Virat Kohli", "C. MS Dhoni", "D. KL Rahul"],
        ("B", "Virat Kohli")
    ),
    (
        "Who said: 'Better to die standing than live on your knees'?",
        ["A. Mahatma Gandhi", "B. Che Guevara", "C. Bhagat Singh", "D. Subhash Chandra Bose"],
        ("B", "Che Guevara", "Che Guevara")
    ),
    (
        "The only Indian captain to win all ICC trophies?",
        ["A. Virat Kohli", "B. Rohit Sharma", "C. MS Dhoni", "D. Kapil Dev"],
        ("C", "MS Dhoni", "Mahendra Singh Dhoni")
    ),
    (
        "Who was the biggest drug lord of Colombia?",
        ["A. El Chapo", "B. Pablo Escobar", "C. Amado Carrillo", "D. Griselda Blanco"],
        ("B", "Pablo Escobar")
    ),
    (
        "Which Punjabi singer was shot dead in 2022?",
        ["A. AP Dhillon", "B. Sidhu Moosewala", "C. Honey Singh", "D. Badshah"],
        ("B", "Sidhu Moosewala", "Moosewala")
    ),
    (
        "Which language is used for web styling?",
        ["A. HTML", "B. Python", "C. CSS", "D. Java"],
        ("C", "CSS")
    ),
    (
        "Which data structure uses key-value pairs?",
        ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
        ("C", "Dictionary", "dict")
    ),
    (
        "Who is known as the Father of Computers?",
        ["A. Alan Turing", "B. Charles Babbage", "C. Bill Gates", "D. Steve Jobs"],
        ("B", "Charles Babbage", "Babbage")
    )
]
prize = [1000,2000,5000,15000,25000,50000,75000,100000,250000,500000]
money = 0
safe_money = 0
lifeline_used = False


for i in range(len(questions)):
    question, options, answer = questions[i]

    print("\n----------------------------")
    print(f"Question {i+1} for ₹{prize[i]}")
    print(question)

    for opt in options:
        print(opt)

    user = input("Enter your answer (A/B/C/D or text): ")
    # 🔹 50-50 Lifeline
    if user == "50" and not lifeline_used:
        lifeline_used = True
        print("\nUsing 50-50 lifeline...\n")

        # show only correct + one wrong
        correct_option = answer[0]
        print(f"Correct option is among: {correct_option} and one other")

        user = input("Now enter your answer: ")

    if user.strip().lower() in [a.lower() for a in answer]:
        print("✅ Correct Answer!")
        money = prize[i]
     # safe level
        if i == 1:
            safe_money = money

        time.sleep(1)

    else:
        print("❌ Wrong Answer!")
        print(f"You take home ₹{safe_money}")
        break
    
else:
       
   print("\n🎉 Congratulations! You won the game!")

print("\n💰 Total Winning:", money)
print("Thanks for playing KBC!")