# Requirements
## Language
- Python 3.6.6 :: Anaconda, Inc.
## Packages
All packages are found in requirements.txt, you can install them using: pip install -r requirements.txt__
Depending on your your Anaconda settings you might need to install pip: conda install -c anaconda pip
- spacy==2.0.16
- wikipedia-api==0.4.3
### Spacy corpus: download en_core_web_sm
To install download en_core_web_sm use: python -m spacy download en_core_web_sm
## Description
A more detailed description can be found in SNLP.pdf
- reduceNames.py extracts all entities from test.tsv and train.tsv and saves them in reducedNames.csv
- buildFactChecker.py requests the wikipedia pages for all entities in reducedNames.csv and extracts all nouns and proper nouns from the wikipedia page of an entity and saves these in knowledge_matrix.csv
- factChecker.py checks the facts in test.tsv, train.tsv and impossible.tsv and writes the prediction in results_test.ttl, results_train.ttl and results_impossible.ttl
## Usage
- python reduceNames.py
- python buildFactChecker.py
- python factChecker.py
## Facts that are not working (Impossible.tsv)
- FactID	Fact_Statement	True/False
- 0	Michelle Trachtenberg stars in 17 Again	1.0
- 1	Zac Efron owns an Instagram Account	1.0
- 2	Margot Robbie stars in Suicide Squad	1.0
- 3	Margot Robbie was born in Gold Coast	1.0
- 4	Leonardo DiCaprio is an actor	1.0
- 5	Zac Efron acts as Mitch Buchannon in the film Baywatch	0.0
- 6	Kurt Cobain's death place is unknown	0.0
- 7	Justin Timberlake's birth place is Nashville, Tennessee	0.0
- 8	Avril Lavigne's sister is called Matthew	0.0
- 9	Avril Lavigne's brother is called Michelle	0.0
## Participants
Nino Schnitker
## Team
NotReallyAGroup