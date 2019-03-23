import nltk
import re

# Describe the class of strings matched by the following regular expressions.
print("Regular Expression Validator")
print("**************************************************************************")
print("[a-zA-Z]+")
print("Alphabet at least and more than at one time")
print("Example : ")
nltk.re_show(r'[a-zA-Z]+', 'a abc aBcd ABcd ABCD a1234 12A34 aB1234')

print("**************************************************************************")
print("[A-Z][a-z]*")
print("Start with upper case after that lower case is coming but lower cases can be omitted")
print("Example : ")
nltk.re_show(r'[A-Z][a-z]*', 'a abc aBcd ABcd ABCD a1234 12A34 aB1234')

print("**************************************************************************")
print("p[aeiou]{,2}t")
print("start with ‘p’ and end with ‘t’ between them 0 to 2 vowels(aeiou) can be inserted")
print("Example : ")
nltk.re_show(r'p[aeiou]{,2}t', 'pit pet peat pool good puuut pt')

print("**************************************************************************")
print("\d+(\.\d+)?")
print("‘\d’ means numbers, therefore numbers with decimals and under decimal point is optional")
print("Example : ")
nltk.re_show(r'\d+(\.\d+)?', '0 0.2 12.0003 -4 -5.2 5,000')

print("**************************************************************************")
print("a([^aeiou][aeiou][^aeiou])*")
print("- Exactly once: All of:")
print("-1. Exactly once: Match 'a'")
print("- 2.Zero or more times: Subexpression: Exactly once: All of: ")
print("1. Exactly once: Match '[^aeiou]'")
print(" 2. Exactly once: Match '[aeiou]'")
print("3. Exactly once: Match '[^aeiou]'")
print("Example : ")
nltk.re_show(r'a([^aeiou][aeiou][^aeiou])*', 'pit pet peat pool good puuut pt')

print("**************************************************************************")
print("\w+|[^\w\s]+")
print("- Exactly once: One of:")
print("-1. One or more times: Match '\w'")
print("-2. One or more times: Match '[^\w\s]'")
print("Example : ")
nltk.re_show(r'\w+|[^\w\s]+', 'roshan.ramanan@gmail.com')
print("#######################################################################################")
print("Create Regular Expression# 1")
print("**************************************************************************")
###
### Write regular expressions to match the following classes of strings:
###    1. A single determiner (assume that a, an, and the are the only determiners).
###    2. An arithmetic expression using integers, addition, and multiplication,
###       such as 2*3+8.
###
print("Get a sample word list")
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
print(wordlist)
[w for w in wordlist if re.search(r'^(an?|the)$', w)]
['a', 'an', 'the']

### Arithmetic

nltk.re_show(r'8', ' I can\'t do 2*8+4 in my head')
nltk.re_show(r'[\d+*]+', ' I can\'t do 2*8+4 in my head')
nltk.re_show(r'[\d+*-/]+', ' I can\'t do 2*8+4 in my head')

print("The matching text Regular Expression for item 1: '\b([Aa][Nn]?|[Tt][Hh][Ee])\b'")
print("Arhithamatic : '([\d+*][\d+*-/]+)")
