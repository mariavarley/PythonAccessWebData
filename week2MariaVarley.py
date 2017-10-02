'''#!/usr/bin/env python'''
import re

"""
>>> get_numbers_from_file('regex_sum_42.txt');  
445822
"""

def get_numbers_from_file(fileName):
   """ This functions opens a file
       and uses regex to find all the numbers
       within the text in the file
       Returns List of integers
       >>> get_numbers_from_file('regex_sum_42.txt')
           445822
   """

   hand = open(fileName)
   strList =[];
   for line in hand:
      num = re.findall('[0-9]+', line);
      strList.extend(num);

   return(map(int,strList));

def sum_numbers(numbersList):
   """ This function totals all the numbers
       in a list
       returns the sum total
       
   """
   return sum(numbersList);


# Find Sum of Sample Data
# output: 445822
listNumbers = get_numbers_from_file('regex_sum_42.txt');
print(sum_numbers(listNumbers));

# Find Sum of Actual Data
# output: 297260
listNumbers = get_numbers_from_file('regex_sum_349870.txt');

print(sum_numbers(listNumbers));

#print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )
#print (open('regex_sum_349870.txt').read());
#print (re.findall('[0-9]+',open('regex_sum_349870.txt').read()));
#print sum((re.findall('[0-9]+',open('regex_sum_349870.txt').read())));
print sum(map(int,(re.findall('[0-9]+',open('regex_sum_349870.txt').read()))));



x = 'From: Using the : character'
y = re.findall('^F.+:',x)
print y

if __name__ == "__main__":
    import doctest
    doctest.testmod()

