import re

input_txt_1 = "Hello, how may I help you?"
input_txt_2 = "Hello, how may I help you ?"

output_txt_1 = re.sub(r'[^\w\s]', '', input_txt_1) 
output_txt_2 = re.sub(r'[^\w\s]', '', input_txt_2)

print(output_txt_1)
print(output_txt_2)