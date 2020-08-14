README

I. buildingDataset

DESCRIPTION:

This directory contains two scripts.
- buildingCitaNeg.py
- buildingCitaNeg_main.py


FUNCTION:

The function of the scripts is twofold: 
- to pre-process individual datasets to retrieve citation contexts and their respective metadata;
- to create a new dataset combining all the individual datasets.


HOW TO USE THE SCRIPTS:

- Each dataset should be in their respective directory.
- Indicate the path to each directory on the buildingCitaNeg_main.py script in the respective variable.
- Indicate the file name/path for the output files.


REFERENCES:

Athar, Awais.(2011. Sentiment Analysis of Citations using Sentence Structure-Based Features. Proceedings of the ACL 2011 Student Session, Portland, OR, USA, 81-87.

Athar, Awais.(2011). Citation Sentiment Corpus. Disponible https://cl.awaisathar.com/citation-sentiment-corpus/

Dong, C., Schäfer, U. (2011). Ensemble-style Self-training on Citation Classification. Proceedings of the 5th International Joint Conference on Natural Language Processing, 623–631.

Dong, C., Schäfer, U. (2011). Citation classification dataset. Disponible sur https://aclbib.opendfki.de/repos/trunk/citation_classification_dataset/

Liu, Haixia. (2017).Sentiment Analysis of Citations Using Word2vec

-------------------------------------------------------------------------------------------------------------------------------------------

II. analyzingDataset


DESCRIPTION 
The script to analyze the CitaNEg dataset comprises the following:
- 6 different codes, being three classes, two function modules and a main code.

The codes are:

1. token.py
This code (class Token) stores the tokens that come from the Talismane parsed files.

2. contexts.py
This code (class Context) reads each Talismane parsed file, identifies the tokens, counts how many sentences there are in the context and verifies the presence of a citation.

3. features_module.py
This module presents a collection of funcitons to identify different negative features present in the contexts. The presence of the features is indicated by a boolean.

4. rules_module.py
This module presents a collection of funcitons to identify the patterns that constitute the different rules. The presence of the rule patters is indicated by a boolean.

5. evaluator.py
This function (class Evaluator) stores the results from the features and rules modules in a dictionary which takes the id of the context as key. ALso, the text of the context and the original polarity, both coming from the CitaNeg dataset file, are stored in this dictionary. The text of the context is useful to analyze the rules result and the original polarity to verify precision and recall.
This class also applies the rules and features and evaluates their results (result of a single rule/feature or of a collection of rules/features). 
Finaly, the class exports the results under csv format.

6. main.py
The main code opens the directory where the Talismane parsed files are stored. It allow to apply the features/rules and evaluate them by calling the class Evaluator.


FUNCTION
The function of the script is twofold:
- to identify features and applie rules to the contexts;
- to evaluate the results regarding precision and recall.


HOW TO USE THE SCRIPTS:
The script takes two inputs and produces an output.
(a) input 1: directory with the Talismane parsed files
(b) input 2: CitaNeg datased (csv file)
(c) output: results table (csv file)

- indicate the path to the file / directory at the moment of calling the main.py script as follows:
python3 main.py (a) (c) (b)

