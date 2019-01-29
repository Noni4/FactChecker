# Requirements
## Language
- Python 3.6.6 :: Anaconda, Inc.
## Packages
All packages are found in requirements.txt, you can install them using: pip install -r requirements.txt
- spacy==2.0.16
- wikipedia-api==0.4.3
### Spacy corpus: download en_core_web_sm
To install download en_core_web_sm use: python -m spacy download en_core_web_sm
## Description
- reduceNames.py extracts all entities from test.tsv and train.tsv and saves them in reducedNames.csv
- buildFactChecker.py requests the wikipedia pages for all entities in reducedNames.csv and extracts all nouns and proper nouns from the wikipedia page of an entity and saves these in 

