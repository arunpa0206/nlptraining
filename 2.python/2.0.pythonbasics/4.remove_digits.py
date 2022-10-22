input_txt = "Nice 2 see you. I will3 join you."
output_txt = ' '.join(s for s in input_txt.split() 
                     if not any(c.isdigit() for c in s))
print(output_txt)