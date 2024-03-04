#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
Changed_name = "[name]"

with open("/GitHub Repos/Projects of 100 Days of Python Programming/Day24- Mail Merge/Input/Names/invited_names.txt") as Names:
    names = Names.readlines()
    with open("/GitHub Repos/Projects of 100 Days of Python Programming/Day24- Mail Merge/Input/Letters/starting_letter.txt") as Starting_letter:
        content = Starting_letter.read()
        for name in names:
            stripped_name = name.strip()
            personalized_content = content.replace(Changed_name, stripped_name)
            print(personalized_content)
            with open(f"F:\GitHub Repos\Projects of 100 Days of Python Programming\Day24- Mail Merge\Output\letter_for_{stripped_name}.txt", mode="w") as Final_letters:
                Final_letters.write(personalized_content)
