input_txt = "Nice 2 see you. I will3 join you."
#tokenize the input sentence using white spaces
#check if the token contain digits
#Join the tokens which do not contain digits using white space
output_txt = ' '.join(s for s in input_txt.split() 
                     if not any(c.isdigit() for c in s))
print(output_txt)