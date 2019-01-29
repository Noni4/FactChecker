# csv to read csv/tsv files
import csv

# spacy to extract entities
import spacy

# Writes a row in correct form to a result.tll file
def write(row, value, set_name):
    with open(f"result_{set_name}.ttl", 'a') as ttl_file:
        ttl_file.write(f"<http://swc2017.aksw.org/task2/dataset/{row[0]}> <http://swc2017.aksw.org/hasTruthValue> \"{value}\"^^<http://www.w3.org/2001/XMLSchema#double> .\n")

# Checks facts from data and writes it to a result.tll file
def check_facts(data, set_name):
    results = []

    # Create new result.tll file and delete old one
    with open(f"result_{set_name}.ttl", 'w') as ttl_file:
        pass

    for i, row in enumerate(data):

        print("")
        print(f"Line {i}")

        entities = []
        try:
            summary = nlp(row[1])
        except IndexError:
            continue

        for word in summary.ents:
            try:
                if word.label_ == 'PERSON' or word.label_ == 'ORG' or word.label_ == 'WORK_OF_ART' or word.label_ == 'FAC' or word.label_ == 'GPE' or word.label_ == 'LOC':
                    if '\'s' in word.text:
                        insert = word.text.replace('\'s', '')
                    elif '\'' in word.text:
                        insert = word.text.replace('\'', '')
                    else:
                        insert = word.text
                    if insert not in entities:
                        entities.append(insert)
            except Exception as e:
                print(e)

        all_entities = []
        for word in summary.ents:
            try:
                if True:
                    if '\'s' in word.text:
                        insert = word.text.replace('\'s', '')
                    elif '\'' in word.text:
                        insert = word.text.replace('\'', '')
                    else:
                        insert = word.text
                    if insert not in all_entities:
                        all_entities.append(insert)
            except Exception as e:
                print(e)

        token_to_keep = []
        token_to_keep = token_to_keep + all_entities


        for token in summary:
            if token.pos_ == 'NOUN' or token.pos_ == 'PROPN':
                if token.lemma_ is not None and token.lemma_ != '':
                    token_to_keep.append(token.lemma_)

        all_token_known = []

        for i in range(len(entities)):

            token_to_keep.remove(entities[i])

            known = None

            with open('knowledge_matrix.csv', encoding='utf-8') as csv_file:
                for rows in list(csv.reader(csv_file)):
                    if rows[0] == entities[i]:
                        known = rows[1:]
                        break
                else:
                    pass

            if known is None:
                continue

            local_tokens_known = []

            for j in range(len(token_to_keep)):
                local_token_known = False
                for _id in known:
                    if token_to_keep[j].lower() == _id.lower():
                        local_token_known = True
                local_tokens_known.append(local_token_known)

            all_token_known = all_token_known + local_tokens_known
            token_to_keep.append(entities[i])

        trues = 0
        for value in all_token_known:
            if value is True:
                trues += 1
        if trues == 0:
            results.append('0.0')
            print(f"Prediction: {0.0}")
            write(row, '0.0', set_name)
        elif trues * 1.8 < len(all_token_known):
            results.append('0.0')
            print(f"Prediction: {0.0}")
            write(row, '0.0', set_name)
        else:
            results.append('1.0')
            print(f"Prediction: {1.0}")
            write(row, '1.0', set_name)
        try:
            print(f"Real: {row[2]}")
        except Exception:
            pass
        print("")


    real = []
    for row in data:
        try:
            real.append(row[2])
        except IndexError:
            continue

    eins_null = 0
    null_null = 0
    null_eins = 0
    eins_eins = 0

    try:
        print(real)
    except Exception:
        pass
    print(results)

    try:
        for i in range(len(real)):
            if real[i] == '1.0' and results[i] == '1.0':
                eins_eins += 1
            elif real[i] == '0.0' and results[i] == '1.0':
                null_eins += 1
            elif real[i] == '1.0' and results[i] == '0.0':
                eins_null += 1
            elif real[i] == '0.0' and results[i] == '0.0':
                null_null += 1

        print(f"EinsEins: {eins_eins}")
        print(f"NullEins: {null_eins}")
        print(f"EinsNull: {eins_null}")
        print(f"NullNull: {null_null}")
    except Exception:
        pass

nlp = spacy.load('en_core_web_sm')

with open('test.tsv', encoding='utf-8') as csv_file:
    test = list(csv.reader(csv_file, delimiter='\t'))[1:]
check_facts(test, 'test')

with open('train.tsv', encoding='windows-1252') as csv_file:
    train = list(csv.reader(csv_file, delimiter='\t'))[1:]
check_facts(train, 'train')

with open('impossible.tsv', encoding='utf-8') as csv_file:
    impossible = list(csv.reader(csv_file, delimiter='\t'))[1:]
check_facts(impossible, 'impossible')
