print("======================================")
print("       AI REGISTRATION ASSISTANT")
print("======================================")
print("Hello! I can help you with course registration.")
print("Type 'register' to start registration.")
print("Type 'exit' to stop.\n")


def get_intent(message):
    message = message.lower()

    if any(word in message for word in ["register", "registration", "join", "enroll"]):
        return "registration"

    elif any(word in message for word in ["course", "courses", "available", "program"]):
        return "courses"

    elif any(word in message for word in ["eligible", "eligibility", "qualification"]):
        return "eligibility"

    elif any(word in message for word in ["status", "application"]):
        return "status"

    elif any(word in message for word in ["hello", "hi", "hey"]):
        return "greeting"

    elif any(word in message for word in ["help"]):
        return "help"

    elif any(word in message for word in ["exit", "bye", "goodbye"]):
        return "exit"

    else:
        return "unknown"


def registration_process():

    print("\nAssistant: Let's complete your registration.")

    name = input("Assistant: What is your name?\nYou: ")

    while not name.strip():
        print("Assistant: Name cannot be empty.")
        name = input("Assistant: Please enter your name.\nYou: ")

    while True:
        age_input = input("Assistant: What is your age?\nYou: ")

        try:
            age = int(age_input)

            if age <= 0:
                print("Assistant: Please enter a valid age.")
            else:
                break

        except ValueError:
            print("Assistant: Please enter your age as a number.")

    while True:
        email = input("Assistant: Enter your email address.\nYou: ")

        if "@" in email and "." in email:
            break
        else:
            print("Assistant: Please enter a valid email address.")

    print("\nAssistant: Available courses:")
    print("1. Python")
    print("2. Data Science")
    print("3. Artificial Intelligence")

    while True:
        choice = input("Assistant: Select a course (1-3).\nYou: ")

        if choice == "1":
            course = "Python"
            break
        elif choice == "2":
            course = "Data Science"
            break
        elif choice == "3":
            course = "Artificial Intelligence"
            break
        else:
            print("Assistant: Please select 1, 2 or 3.")

    print("\n======================================")
    print("        REGISTRATION SUMMARY")
    print("======================================")
    print("Name   :", name)
    print("Age    :", age)
    print("Email  :", email)
    print("Course :", course)
    print("======================================")

    if age >= 18:
        print("Eligibility : ELIGIBLE")
        print("Status      : REGISTRATION SUCCESSFUL")
    else:
        print("Eligibility : NOT ELIGIBLE")
        print("Status      : REGISTRATION FAILED")

    print("======================================")


while True:

    user_input = input("\nYou: ")

    intent = get_intent(user_input)

    if intent == "greeting":
        print("Assistant: Hello! How can I help you?")

    elif intent == "registration":
        registration_process()

    elif intent == "courses":
        print("Assistant: Available courses are:")
        print("1. Python")
        print("2. Data Science")
        print("3. Artificial Intelligence")

    elif intent == "eligibility":
        print("Assistant: Students aged 18 or above are eligible for registration.")

    elif intent == "status":
        print("Assistant: Please provide your registration ID to check your status.")

    elif intent == "help":
        print("Assistant: You can ask about courses, registration, eligibility or status.")

    elif intent == "exit":
        print("Assistant: Thank you! Goodbye.")
        break

    else:
        print("Assistant: Sorry, I didn't understand.")
        print("Assistant: Try asking about courses, registration or eligibility.")
