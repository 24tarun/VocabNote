def enter_data(sheet):
    print("Enter data for each field. Press Enter without typing anything to skip.")
    cont="y"
    # Prompt user for each field
    while True:
        Gender=input("Enter Gender: ").strip().capitalize()
        word = input("Enter Word: ").strip().capitalize()
        english_meaning = input("Enter English Meaning: ").strip().capitalize()
        part_of_speech = input("Enter Part of Speech: ").strip().capitalize()
        other_comments = input("Enter Other Comments: ").strip().capitalize()
        cont=input("do u want to continue entering? y / n")
        sheet.append([Gender, word, english_meaning, part_of_speech, other_comments])

        if cont !="y":
            break

sheet=[]
enter_data(sheet)