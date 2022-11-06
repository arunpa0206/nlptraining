input_txt = "Nice 2 see you. I will3 join you."
output_txt = ''
for token in input_txt.split():
    isDigitFound = False #If isDigitFound == true for a token, then that token contains digit.
    for char in token:
        if(char.isdigit()):
            isDigitFound = True
            break
    if(isDigitFound == True):
        isDigitFound = False
    else:    
        output_txt += " " + token 

print(output_txt)
