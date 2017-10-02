#!/usr/bin/env python
import re


hand = open('regex_sum_42.txt')
str_list =[];
for line in hand:
   num = re.findall('[0-9]+', line);
   if num != []:
      str_list.extend(num);

print str_list;
int_list = [];
int_list = map(int,str_list);

print int_list;
print(sum(int_list));

