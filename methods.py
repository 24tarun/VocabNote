import random

def enforce_gender_rule(sheet):
    # Get all values in the sheet
    data = sheet.get_all_values()

    # Iterate through each row starting from the second row (skipping headers)
    for row in data[1:]:
        gender = row[0]  # Gender column (first column)
        part_of_speech = row[3]  # Part of Speech column (fourth column)

        # Check if Gender column has a value and Part of Speech is not already filled
        if gender and not part_of_speech:
            # Update Part of Speech to 'Noun'
            sheet.update_cell(data.index(row) + 1, 4, 'Noun')
            print(f"Updated Part of Speech for row {data.index(row) + 1} to 'Noun'.")


def enter_data(sheet):
    print("Enter data for each field. Press Enter without typing anything to skip.")
    
    # Prompt user for each field
    Gender=input("Enter Gender: ").strip().capitalize()
    word = input("Enter Word: ").strip().capitalize()
    english_meaning = input("Enter English Meaning: ").strip().capitalize()
    part_of_speech = input("Enter Part of Speech: ").strip().capitalize()
    other_comments = input("Enter Other Comments: ").strip().capitalize()

    sheet.append_row([Gender, word, english_meaning, part_of_speech, other_comments])

    
#when i was noting down the words i didnt really care about the Case Sensitivity of Nouns and others,
#so this function will run every once when the api connection is established to check and change from the last updated row

def capitalize_first_letter(worksheet):
    # Get all the data
    data = worksheet.get_all_values()

    # Capitalize the first letter of each cell
    for row_index, row in enumerate(data):
        for col_index, cell in enumerate(row):
            if cell and cell[0].islower():
                capitalized_cell = cell[0].upper() + cell[1:]
                # Update the cell in the worksheet
                worksheet.update_cell(row_index + 1, col_index + 1, capitalized_cell)


#this is getting rate limited for now



def quiz(data, num_questions):
    score = 0
    
    if num_questions:
        # Shuffle and select the required number of questions
        questions = random.sample(data, min(num_questions, len(data)))
    else:
        questions = data
    
    for entry in questions:
        word = entry['Word']
        correct_meaning = entry['English Meaning']
        
        user_answer = input(f"What is the meaning of the word '{word}'? ")
        
        if user_answer.strip().lower()== 'break':
            break
        elif user_answer.strip().lower() == correct_meaning.strip().lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct meaning of {word} is '{correct_meaning}'.")

    print(f"Your final score is {score} out of {len(questions)}")