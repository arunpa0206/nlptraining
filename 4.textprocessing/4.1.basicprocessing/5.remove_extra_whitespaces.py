import re

input_txt = """This       is a      white         car """
# THIS REGEX REMOVES EXTRA WHITESPACES:
#./s matches single white space
#/s+ matches substring of all white spaces
output_txt = re.sub("\s+"," ", input_txt)
print(output_txt)