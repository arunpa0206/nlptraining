import re

input_txt = """This       is a      white         car """
# THIS REGEX REMOVES EXTRA WHITESPACES:
output_txt = re.sub("\s+"," ", input_txt)
print(output_txt)