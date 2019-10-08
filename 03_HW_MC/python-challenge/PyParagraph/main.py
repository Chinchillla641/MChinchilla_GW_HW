# -*- coding: UTF-8 -*-
"""PyParagraph Homework Solution."""

# Incorporate regular expressions (helpful for splitting by punctuation)
import re
import os

# Files to load and output (Remember to change these)
p = "paragraph_1"
#p = "paragraph_2"

file_to_load = os.path.realpath(f"D:\\Git\\GWU-ARL-DATA-PT-09-2019-U-C\\02-Homework\\03-Python\\Instructions\\Part-3\\PyParagraph\\raw_data\\{p}.txt")
file_to_output = os.path.realpath(f"D:\\Git\\MChinchilla_GW_HW\\03_HW_MC\\python-challenge\\PyParagraph\\output_{p}.txt")

# String variable to hold the paragraph contents
paragraph = ""

# Read the text file
with open(file_to_load) as txt_data:

    # Store the contents as a string (with no new lines)
    paragraph = txt_data.read().replace("\n", " ")

# Split the paragraph based on spaces to calculate word count
word_split = paragraph.split(" ")
#print(word_split)
word_count = len(word_split)

# Create a list for holding all the letter counts
letter_counts = []

# Loop through the word array and calculate the length of each word
for word in word_split:

    # Add each letter count into the letter_counts list
    word = re.sub("[.]", "", word)
    word = re.sub("[!]", "", word)
    word = re.sub("[?]", "", word)
    letter_counts.append(len(word))

# Calculate the avg letter count
avg_letter_count = sum(letter_counts) / float(len(letter_counts))

# Re-split the original paragraph based on punctuation (. ? !)
sentence_split = re.split("(?<=[.!?]) +", paragraph)
#print(sentence_split)
sentence_count = len(sentence_split)

words_per_sentence = []

# Loop through the sentence array and calculate the number of words in each
for sentence in sentence_split:

    # Calculate the number of words in each sentence and add to the list
    words_sentence = re.findall("[.!?]", sentence)
    words_sentence2 = re.findall(" ", sentence)
    words_sentence.extend(words_sentence2)
    
    print(words_sentence)
    
    num_words = len(words_sentence)
    words_per_sentence.append(num_words)
print(words_per_sentence)
# Calculate the avg word count (per sentence)
avgwc = sum(words_per_sentence) / float(sentence_count)
    
# Generate Paragraph Analysis Output
output = (f"Paragraph Analysis ({p})\n"
          "-----------------\n"
          f"Approximate Word Count: {word_count} words\n"
          f"Approximate Sentence Count: {sentence_count} sentences\n"
          f"Average Letter Count: {round(avg_letter_count, 2)} letters\n"
          f"Average Sentence Length: {round(avgwc, 2)} words")

# Print all of the results (to terminal)
print(output)
    
# Save the results to analysis text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
