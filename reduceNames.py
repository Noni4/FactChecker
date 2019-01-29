# csv to read csv/tsv files
import csv

# spacy to recpgnize entities
import spacy

# Load small english corpus
nlp = spacy.load('en_core_web_sm')

# Rest test.tsv
with open('test.tsv', 'r', encoding='utf-8') as file:
    test = list(csv.reader(file, delimiter='\t'))[1:]

# Read train.tsv
with open('train.tsv', 'r', encoding='windows-1252') as file:
    train = list(csv.reader(file, delimiter='\t'))[1:]

# Unite facts from train and test
test = train + test

words_from_given_data = []
old_words = []

for row in test:
    # continue if row is empty
    if row == []:
        continue

    # Convert fact to doc
    row_to_inspect = nlp(row[1])
    print(row_to_inspect)

    # Extract all persons, organisations, words of art, buildings, locations
    for word in row_to_inspect.ents:
        try:
            if word.label_ == 'PERSON' or word.label_ == 'ORG' or word.label_ == 'WORK_OF_ART' or word.label_ == 'FAC' or word.label_ == 'GPE' or word.label_ == 'LOC':
                if '\'s' in word.text:
                    insert = word.text.replace('\'s', '')
                elif '\'' in word.text:
                    insert = word.text.replace('\'', '')
                else:
                    insert = word.text
                if insert not in words_from_given_data:
                    words_from_given_data.append(insert)
        except Exception as e:
            print(e)

for word in words_from_given_data:
    print(word)
print(len(words_from_given_data))

important_names = []

# Save the extracted entities
with open('reducedNames.csv', 'w', encoding='utf-8', ) as file:
    for row in words_from_given_data:
        print(row)
        file.write(row)
        file.write('\n')