from context import *
from evaluator import *

import glob
import os
import sys

path = os.path.join(sys.argv[1],'*')  
output_filename = os.path.join(sys.argv[2],'results.csv')
original_corpus_name = sys.argv[3]

dict_parsed_contexts = {} # dictionary to store the elements of the parsed context

for file in glob.glob(path):

    new_context =  Context(file) # Create a new context from each file

    dict_parsed_contexts[new_context.id] = new_context # Store each new context in the dictionary 
                                                       #using the id as key

evaluator = Evaluator (dict_parsed_contexts, original_corpus_name)

## fetaure_list: list that contains the id of the features found
#GF1: General feature 1 - number of sentences in the contexts 
#GF2: General feature 2 - presence of a real citation in the contexts 
#GF3: General feature 3 - presence of the words lack, fail and failure and their synonyms (nouns and verbs)
feature_index = ['GF1', 'GF2', 'GF3']

## rule_index: list that contains the id of the rules applied
# WF1: Weakness Feature 1 - presence of the verbs lack or fail
#WF2: Weakness Feature 2 - presence of an adjective that has a negative meaning; the adjective must follow a verb 
rule_index = ['WF1', 'WF2']

evaluator.apply (feature_index) # It is possible to apply the features and rules on the whole list
evaluator.apply (['WF1', 'WF2'])    # or chose a specific feature/rule

evaluator.evaluateResultsForMultipleMethods (['WF1','WF2'])
evaluator.evaluteResultsForSingleMethod('WF2')

evaluator.exportAsCSV (output_filename)
    