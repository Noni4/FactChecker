# wikipediaapi to easily query wikipedia.com
import wikipediaapi

# csv to read csv/tsv files
import csv

# spacy to recognize nouns and get their lemmas
import spacy

# re split entire articles in sentences for easier progressing
import re

# Get wikipediaapi object for wikipedia in english
wiki = wikipediaapi.Wikipedia("en")

# Load small english corpus
nlp = spacy.load('en_core_web_sm')

knowledge = {}

# Open file with known entities
with open('reducedNames.csv', encoding='utf-8') as file:
    data = file.read().split('\n')

print(data)

all_know_words = []

for title in data:
    print(title)

    # Query the text of an entity from wikipedia.com
    try:
        important_sentences = []
        print('search for ' + str(title))
        summary = wiki.article(title).text

        # Some entities were falsely recognized with an 's' at the end. (E.g. Zac Efrons instead of Zac Efron)
        if len(summary) == 0:
            print('NOT FOUND')
            cutted_title = title[:-1]
            print('search for ' + str(cutted_title))
            summary = wiki.article(cutted_title).text
            if len(summary) == 0:
                print('NOT FOUND AGAIN')
                cutted_title = title.replace('s ', ' ')
                print('search for ' + str(cutted_title))
                summary = wiki.article(cutted_title).text
                if len(summary) == 0:
                    print('REALLY NOT FOUND')
                    continue
    except Exception as e:
        print(e)
        continue

    # Delete token that made some problems during processing and split the text by sentences
    summary = summary.replace(title, '')
    summary = summary.replace('"', '')
    summary = summary.replace('\t', '')
    summary = summary.replace('\n', '')
    summary = re.split('\. |! | \?', summary)

    knowledge_of_title = []

    # Save every noun and proper noun of every text
    token_to_keep = []
    for i in range(len(summary)):
        summary[i] = nlp(summary[i])
        for token in summary[i]:
            if token.pos_ == 'NOUN' or token.pos_ == 'PROPN':
                if token.lemma_ is not None and token.lemma_ != '' and token.lemma_ not in token_to_keep:
                    token_to_keep.append(token.lemma_)
        if len(token_to_keep) > 0:
            knowledge_of_title.append(token_to_keep)

    if knowledge_of_title is not None:
        knowledge[title] = knowledge_of_title

# Write nouns and proper nouns for every entity to a file
with open('knowledge_matrix.csv', 'w', encoding='utf-8', newline='') as csv_file:
    pass
for key in knowledge:
    matrix_as_array = [key]
    for splitted in knowledge[key]:
        for i in range(len(splitted)):
            if splitted[i] != '' and splitted[i] not in matrix_as_array:
                matrix_as_array.append(splitted[i])
    with open(f"knowledge_matrix.csv", 'a', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        print(matrix_as_array)
        csv_writer.writerow(matrix_as_array)