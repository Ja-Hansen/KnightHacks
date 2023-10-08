

if __name__ == "__main__":
    print("Thank you for using Morgan&Morgan's AI system.")
    print("Please select the prompt that best suits your selection")
    print("1. Submit a Document\n2. Summarize a Document\n3. General Inquiries")
    while True:
        user_input = input("Enter a number between 1 and 4: ")

    # Check if the input is a valid integer
        if user_input.isdigit():
            user_input = int(user_input)
        
            # Check if the input is between 1 and 4
            if 1 <= user_input <= 4:
                break  # Exit the loop if the input is valid
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        else:
            print("Invalid input. Please enter a valid integer.")


    print("You entered:", user_input)
    if user_input == 1:
        ## Function 1
    elif user_input == 2:
        ## Function 2
    elif user_input == 3:
        # Function 3
    else: