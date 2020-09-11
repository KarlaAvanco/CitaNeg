from context import *
from evaluator import *
from newFeature import *

import glob
import os
import sys

path = os.path.join(sys.argv[1],'*')  
output_filename = os.path.join(sys.argv[2],'results.csv')
output_filename2 = os.path.join(sys.argv[3],'resultsForWeka.csv')
original_corpus_name = sys.argv[4]
specificities = sys.argv[5]

dict_parsed_contexts = {} # dictionary to store the elements of the parsed context

for file in glob.glob(path):

    new_context =  Context(file) # Create a new context from each file

    dict_parsed_contexts[new_context.id] = new_context # Store each new context in the dictionary 
                                                       #using the id as key

evaluator = Evaluator (dict_parsed_contexts, original_corpus_name)


## fetaure_list: list that contains the id of the features found
#GF1: General feature 1 - number of sentences in the contexts 
#GF2: General feature 2 - presence of a real citation in the contexts 
#GF3: General feature 3 - presence of the adverb not
#GF4: General feature 4 - presence of the conjunction but
#GF5: General feature 5 - presence of however
#GF6: General feature 6 - presence of the words lack, fail and failure and their synonyms (nouns and verbs)
#GF7: General feature 7 - presence of the verb overcome 
#GF8: General feature 8 - verify if the citation is the subject of the sentence
#GF9: General feature 9 - verify if the the subject is first person
#GF10: General feature 10 - verify if the the subject is third person
#GF11: General feature 11 - verify if the noun 'method' is in the context
#GF12: General feature 12 - verify if the words 'model' and 'modeling' are in the context
#GF13: General feature 13 - verify if the noun 'approach' is in the context
#GF14: General feature 14 - verify if the noun 'result' is in the context
feature_index = ['GF1', 'GF2', 'GF3', 'GF4', 'GF5', 'GF6', "GF7", 'GF8', 'GF9', 'GF10', 'GF11','GF12','GF13','GF14']

## rule_index: list that contains the id of the rules applied
# WF1: Weakness Feature 1 - look for the verbs lack or fail
# WF2: Weakness Feature 2 - look for words (nouns and verbs) that indicate limitation or problem
# WF3: Weakness Feature 3 - look for the adjectif low
# WF4: Weakness Feature 4 - look for the adjectif/adverb only
# WF5: Weakness Feature 5 - look for the adjectif difficult
# WF6: Weakness Feature 6 - look for an adjective that has a negative meaning; the adjective must follow a verb 
# WF7: Weakness Feature 7 - look for an adjective that has a negative meaning; the adjective must follow a copular verb 
# WF8: Weakness Feature 8 - look for the structure copular verb + not + (adverb) adjective
# WF9: Weakness Feature 9 - look for the structure auxiliary verb [do, does, did, have, has] + not + (adverb) verb
# WF10: Weakness Feature 10 - look for a negative passive voice (verb be + not + past participle)
# WF11: Weakness Feature 11 - look for a negative passive voice (perfect tenses and modal verbs)
# WF12: Weakness Feature 12 - look for the structure adj-noun
# WF13: Weakness Feature 13 - look for the verb degrade and synonyms
# CF1: Compare Feature 1 - look for the structure copular verb + not + (adverb) adjective   
# CF2: Compare Feature 2 - look for the noun improvement
# CF3: Compare Feature 3 - look for a comparison in the context 
# CF4: Compare Feature 4 - look for the verbs compare and differ (and synonyms)
# CF5: Compare Feature 5 - look for presence of the structure different from
rule_index = ['WF1', 'WF2', 'WF3', 'WF4', 'WF5', 'WF6', 'WF7', 'WF8', 'WF9', 'WF10', 'WF11', 'WF12','WF13',
                'CF1', 'CF2', 'CF3', 'CF4','CF5']

# BF1: Background Feature 1 - look for time and frequency adverbs
# BF2: Background Feature 2 - look for adjectives
# BF3: Background Feature 3 - look for background verbs
# BF4: Background Feature 4 - look for examples 
# HF1: Hedge Feature 1 - look for modal verbs (may, might, could, should, would)
# HF2: Hedge Feature 2 - look for reporting verbs (suggest, estimate, etc.)
# HF3: Hedge Feature 3 - look for copular verbs (not be), such as appear, seem, etc.
# HF4: Hedge Feature 4 - look for modal adjectives
# HF5: Hedge Feature 5 - look for modal adjectives
# HF6: Hedge Feature 6 - look for of modal nouns
trait_index = ['BF1', 'BF2', 'BF3', 'BF4',
                'HF1', 'HF2', 'HF3', 'HF4', 'HF5', 'HF6']

evaluator.apply(feature_index) # It is possible to apply the features and rules on the whole list
evaluator.apply (rule_index)    # or chose a specific feature/rule
evaluator.apply (trait_index)

for method in feature_index:
    evaluator.evaluteResultsForSingleMethod(method)
   

words_list = getWordsList (specificities)

for name in words_list:
    features[name] = createWordFormSearcher(name)
    evaluator.apply([name])
    feature_index.append (name) #in order to print precision and recall


for method in rule_index+trait_index:
    evaluator.evaluteResultsForSingleMethod(method)


evaluator.evaluateResultsForMultipleMethods (rule_index)
evaluator.evaluateResultsForMultipleMethods (trait_index)
evaluator.evaluateResultsForMultipleMethods (feature_index)

evaluator.exportAsCSV (output_filename, list_of_exported_methods = rule_index+trait_index)
output_filename = os.path.join(sys.argv[2],'results2.csv')
evaluator.exportAsCSV (output_filename, list_of_exported_methods = rule_index+trait_index+feature_index)    
evaluator.exportForWeka (output_filename2, list_of_exported_methods=rule_index+trait_index+feature_index)
