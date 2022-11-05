input_txt = "Nice 2 see you. I will3 join you."
output_txt = ''
for token in input_txt.split():
    flag = False #If flag == true for a token, then that token contains digit.
    for char in token:
        if(char.isdigit()):
            flag = True
            break
    if(flag == True):
        flag = False
    else:    
        output_txt += " " + token 

print(output_txt)
