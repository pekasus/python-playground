#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt", 'r') as namefile:
    names = namefile.readlines()

for i in range(len(names)):
    names[i] = names[i].strip()

with open("Input/Letters/starting_letter.txt", 'r') as letterfile:
    source_text = letterfile.read()

for name in names:
    output_text = source_text.replace("[name]", name)
    with open(f"Output/ReadyToSend/{name}.txt", 'w') as outfile:
        outfile.write(output_text)
