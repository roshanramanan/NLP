import nltk
from nltk.corpus import brown, stopwords
from nltk.book import *
from nltk.probability import FreqDist
from collections import Counter

print("**************************************************************")
print("Chapter1 Question 1")
print("**************************************************************")
fd_list = FreqDist([w for w in text5 if len(w) == 4])
vocab1 = fd_list.keys()
print("Distribution based on frequency from text5:")
print(vocab1)
print("**************************************************************")
print("Chapter1 Question 2")
print("**************************************************************")
print("Uppercase words from text6:")
for word in text6:
    if word.isupper():
        print(word)
print("**************************************************************")
print("Chapter1 Question 3")
print("**************************************************************")


def percent(word, text):
    total_words = len(Counter(text.lower().split()))
    total_occurrence_of_given_word = text.lower().split().count(word.lower())
    print("Total words:", total_words)
    print("Total occurrence of given word :", total_occurrence_of_given_word)
    print("Percentage of occurrence :", (total_occurrence_of_given_word * total_words) / 100)


percent("Roshan", "Roshan is writhing a Roshan program in Roshan file")

print("**************************************************************")
print("Chapter2 Question 1")
print("**************************************************************")

all_unique_words_brown = set(brown.words())
brown_fd = nltk.FreqDist(brown.words())
atleast_3times = [word for word in all_unique_words_brown if brown_fd[word] > 2]
print("Word Occur at least 3 times", atleast_3times)

print("**************************************************************")
print("Chapter2 Question 2")
print("**************************************************************")

most_freq_50_words = nltk.FreqDist(brown.words(categories='news'))
print(most_freq_50_words.most_common(50))
words = [word for word in most_freq_50_words]
for word in words:
    if word in stopwords.words('english') or not word.isalpha():
        most_freq_50_words.pop(word)
print("Most frequent 50 words as stop words", most_freq_50_words.most_common(50))

print("**************************************************************")
print("Chapter2 Question 3 output")
print("**************************************************************")


def word_freq(word, category):
    category_text = brown.words(categories=category)
    return sum(1 for wd in category_text if wd == word)


print("Frequency of the given word", word_freq("work", "learned"))
