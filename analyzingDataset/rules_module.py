import context
import re
from features_module import *

### Functions to identify the different patterns that constitute a rule
    ### Typology patterns

    ## Class: Weakness
    # Look for features that characterize the class 'Weakness'

## Weakness Feature 1 (WF1): presence of the verbs lack or fail
def findingVerbFail (context): 

    for sentence in context.sentences:
        for token in sentence:
        
            if (token.lemma =='lack') or (token.lemma =='fail'):
                if re.search (r"^V", token.pos):
                    return '1' # True
        
    # If you get to this point, it means the pattern was not found; therefore, return false
    return '0' # False

############################################################################################

    ## Class: Weakness
        # Look for features that characterize the class 'Weakness'

# Weakness Feature 2 (WF2): presence of words (nouns and verbs) that indicate limitation or problem
def findingLimitation (context): 
    
    list_of_words = ['caveat','deficiency','deficit', 'difficulty','degradation','failure', 'flaw',
                    'inadequacy', 'inconsistency','insufficiency','issue','limit', 'limitation',
                    'malfunction','mistake','problem','restrict', 'restriction', 'scarceness',
                    'scarcity','scantiness','shortage','shortcoming','weakness']
    
    for sentence in context.sentences:
        for token in sentence:
        
            if token.lemma in list_of_words:
                return '1' #True

    return '0'


############################################################################################

    ## Class: Weakness
        # Look for features that characterize the class 'Weakness'

# Weakness Feature 3 (WF3): presence of the adjective low
def findingLow (context): 
    
    for sentence in context.sentences:
        for token in sentence:
        
            if token.lemma == 'low':
                return '1' # True

    return '0'

############################################################################################

    ## Class: Weakness
        # Look for features that characterize the class 'Weakness'

# Weakness Feature 4 (WF4): presence of the adjective/adverb only
def findingOnly (context): 
    
    for sentence in context.sentences:
        for token in sentence:
        
            if token.lemma == 'only':
                return '1' # True

    return '0'

############################################################################################

    ## Class: Weakness
        # Look for features that characterize the class 'Weakness'

# Weakness Feature 5 (WF5): presence of the adjective difficult
def findingDifficult (context): 
    
    for sentence in context.sentences:
        for token in sentence:
        
            if token.lemma == 'difficult':
                return '1' # True

    return '0'
############################################################################################

        ## Class: Weakness
        # Look for features that characterize the class 'Weakness'

## Weakness Feature 6 (WF6): presence of an adjective that has a negative meaning; the adjective must follow a verb 
def findingNegativeAdjectives (context): 
            
    list_of_adjectives = ['coarse','costly','debatable','defficient','erroneous','flawed','impossible', 
                            'impractical','irregular', 'limited','problematic','questionable', 'scarce',  
                            'shallow', 'slow','small','stumbling','suspect']
    for sentence in context.sentences:
        for token in sentence:
            if (token.pos =='JJ') and (token.lemma in list_of_adjectives or re.search (r"^in|^un", token.lemma)):
                token_list = sentence
                gov_index = (token.governor)-1
                governor = token_list[gov_index]

                if governor.upos =='VERB' and governor.dependency =='root':
                   return '1' # True  
    
    return '0' 
## Weakness Feature 7 (WF7):
def findingNegativeAdjectives2 (context): 
            
    list_of_adjectives = ['coarse','costly','debatable','defficient','erroneous','flawed','impossible', 
                            'impractical','irregular', 'limited','problematic','questionable', 'scarce',  
                            'shallow', 'slow','small','stumbling','suspect']
    for sentence in context.sentences:
        for token in sentence:
            if token.upos =='AUX' and token.dependency =='cop':
                token_list = sentence
                gov_index = (token.governor) -1
                governor = token_list[gov_index]

                if (governor.pos =='JJ') and (governor.lemma in list_of_adjectives or re.search (r"^in|^un", governor.lemma)):
                    return '1' # True  
    
    return '0' 
   
############################################################################################

        ## Class: Weakness
        # Look for features that characterize the class 'Weakness'

# Weakness Feature 8 (WF8): presence of the structure copular verb + not + (adverb) adjective
def findingNegPhrase1 (context): 
    for sentence in context.sentences:
        token_index = 0
        copular_verb_not_found = True
        while token_index < len (sentence) and copular_verb_not_found:
            if sentence[token_index].dependency == 'cop':
                copular_verb_not_found = False
            else:
                token_index +=1

        if not copular_verb_not_found:
            if sentence [token_index+1].lemma =='not' or sentence [token_index+1].lemma =='rarely' or sentence [token_index+1].lemma =='never':
                adjective_search_index = token_index+2
                has_not_found_adjective = True
                still_searching_adjective = True
                while adjective_search_index <len(sentence) and has_not_found_adjective and still_searching_adjective:
                    if sentence[adjective_search_index].pos == 'RB':
                        adjective_search_index +=1
                    elif sentence[adjective_search_index].pos == 'JJ':
                        has_not_found_adjective = False
                    else:
                        still_searching_adjective = False #Something that is not an adjective or an adverb was found

                if not has_not_found_adjective: 
                    return '1'

    return '0'

############################################################################################

        ## Class: Weakness
        # Look for features that characterize the class 'Weakness'

# Weakness Feature 9 (WF9): presence of the structure auxiliary verb [do, does, did, have, has] 
#                                                       or a modal verb [can, could, might, should] + not + (adverb) verb
def findingNegPhrase2 (context): 
    for sentence in context.sentences:
        token_index = 0
        auxiliary_verb_not_found = True
        while token_index < len (sentence) and auxiliary_verb_not_found:
            if sentence[token_index].dependency == 'aux':
                auxiliary_verb_not_found = False
            else:
                token_index +=1

        if not auxiliary_verb_not_found:
            if sentence [token_index+1].lemma =='not':
                verb_search_index = token_index+2 # look for a verb in its base form (VB) or in the past participle (VBN)
                has_not_found_verb = True
                still_searching_verb = True
                while verb_search_index <len(sentence) and has_not_found_verb and still_searching_verb:
                    if sentence[verb_search_index].pos == 'RB':
                        verb_search_index +=1
                    elif sentence[verb_search_index].pos == 'VB' or sentence[verb_search_index].pos == 'VBN':
                        has_not_found_verb = False
                    else:
                        still_searching_verb = False #Something that is not a verb or an adverb was found

                if not has_not_found_verb: 
                    return '1'

    return '0'

############################################################################################

        ## Class: Weakness
        # Look for features that characterize the class 'Weakness'

# Weakness Feature 10 (WF10): presence of a negative passive voice
def findingNegPhrase3 (context): 
    for sentence in context.sentences:
        token_index = 0
        auxiliary_verb_not_found = True
        while token_index < len (sentence) and auxiliary_verb_not_found:
            if sentence[token_index].dependency == 'aux:pass':
                auxiliary_verb_not_found = False
            else:
                token_index +=1

        if not auxiliary_verb_not_found:
            if sentence [token_index+1].lemma =='not':
                verb_search_index = token_index+2 
                has_not_found_verb = True
                still_searching_verb = True
                while verb_search_index <len(sentence) and has_not_found_verb and still_searching_verb:
                    if sentence[verb_search_index].pos == 'RB':
                        verb_search_index +=1
                    elif sentence[verb_search_index].pos == 'VBN':
                        has_not_found_verb = False
                    else:
                        still_searching_verb = False #Something that is not a verb or an adverb was found

                if not has_not_found_verb: 
                    return '1'

    return '0'

############################################################################################

        ## Class: Weakness
        # Look for features that characterize the class 'Weakness'

# Weakness Feature 11 (WF11): presence of a negative passive voice (perfect tenses and modal verbs)
def findingNegPhrase4 (context): 
    for sentence in context.sentences:
        token_index = 0
        auxiliary_verb_not_found = True
        while token_index < len (sentence) and auxiliary_verb_not_found:
            if (sentence[token_index].dependency == 'aux') and (sentence[token_index].pos == 'VBZ' or sentence[token_index].pos == 'VBD' or sentence[token_index].pos == "MD"):
                auxiliary_verb_not_found = False
            else:
                token_index +=1

        if not auxiliary_verb_not_found:
            if sentence [token_index+1].lemma =='not':
                verb_search_index = token_index+2 
                has_not_found_verb = True
                still_searching_verb = True
                while verb_search_index <len(sentence) and has_not_found_verb and still_searching_verb:
                    if sentence[verb_search_index].pos == 'RB':
                        verb_search_index +=1
                    elif sentence[verb_search_index].dependency == 'aux:pass' \
                         and sentence[verb_search_index+1].pos == 'VBN': 
                        has_not_found_verb = False
                    else:
                        still_searching_verb = False #Something that is not a verb or an adverb was found

                if not has_not_found_verb: 
                    return '1'

    return '0'

############################################################################################

        ## Class: Weakness
        # Look for features that characterize the class 'Weakness'
        
# Weakness Feature 12 (WF12): presence of the structure adj-noun
def findingAdjNoun (context):

    list_of_adjectives = ['coarse','costly','debatable','defficient','erroneous','flawed','impossible', 
                            'impractical','irregular', 'limited','problematic','questionable', 'scarce',  
                            'shallow', 'slow','small','stumbling','suspect']
                               
    for sentence in context.sentences:
        for token in sentence:
            if (token.pos =='JJ') and (token.lemma in list_of_adjectives or re.search (r"^in|^un", token.lemma)):
                token_list = sentence
                gov_index = (token.governor)-1
                governor = token_list[gov_index]

                if governor.pos =='NN':
                    return '1' # True   

    return '0'

############################################################################################

        ## Class: Weakness
        # Look for features that characterize the class 'Weakness'
        
# Weakness Feature 13 (WF13): presence of the verb degrade and synonyms
def findingVerbDegrade (context): 

    for sentence in context.sentences:
        for token in sentence:
        
            if (token.lemma =='degrade') or (token.lemma =='hinder') or (token.lemma =='jeopardize'):
                if re.search (r"^V", token.pos):
                    return '1' # True
        
    # If you get to this point, it means the pattern was not found; therefore, return false
    return '0' # False
############################################################################################

        ## Class: Compare / Contrast
        # Look for features that characterize the class 'Compare / Contrast'

# Compare Feature 1 (CF1): presence of the verb overcome and synonymes   
def findingVerbOutperform (context): 

    list_of_verbs = ['outperform', 'outdo', 'outmatch', 'outweigh', 'overcome', 'overmatch', 'surpass', 'surmount', 'exceed', 'improve']
    for sentence in context.sentences:
        for token in sentence:
        
            if token.lemma in list_of_verbs:
                if re.search (r'^V', token.pos):
                    return '1' # True
        
    
    return '0' # False

############################################################################################

        ## Class: Compare / Contrast
        # Look for features that characterize the class 'Compare / Contrast'

# Compare Feature 2 (CF2): presence of the noun improvement
def findingImprovement (context): 

    for sentence in context.sentences:
        for token in sentence:
        
            if token.lemma == 'improvement':
                return '1' # True
    
    return '0' # False

############################################################################################

        ## Class: Compare / Contrast
        # Look for features that characterize the class 'Compare / Contrast'

# Compare Feature 3 (CF3): presence of a comparison  
def findingComparison (context): 

    for sentence in context.sentences:
        for token in sentence:
            if token.pos  == 'JJR':
                return '1' # True
                    
    return '0' # False


############################################################################################

        ## Class: Compare / Contrast
        # Look for features that characterize the class 'Compare / Contrast'

# Compare Feature 4 (CF4): presence of the verbs compare and differ (and synonyms)
def findingCompare (context): 

    list_of_verbs = ['compare', 'contrast', 'differ', 'oppose' ]
    for sentence in context.sentences:
        for token in sentence:
        
            if token.lemma in list_of_verbs and re.search (r'^V', token.pos):
                    return '1' # True
        
    
    return '0' # False

############################################################################################

        ## Class: Compare / Contrast
        # Look for features that characterize the class 'Compare / Contrast'

# Compare Feature 5 (CF5): presence of the structure different from
def findingRather (context):  # this function did not have a good result (very low precision)
                                        # it is not going to be used
    for sentence in context.sentences:
        token_index = 0
        adjective_not_found = True
        while token_index < len (sentence) and adjective_not_found:
            if sentence[token_index].lemma == 'rather': 
                adjective_not_found = False
            else:
                token_index +=1

        if not adjective_not_found:
            if sentence [token_index+1].lemma =='than':
                return '1'
    
    return '0'

############################################################################################

        ## Traits: Background
        # Look for features that characterize the trait 'Background'

# Background Feature 1 (BF1): presence of time and frequency adverbs
def findingBackgroundAdverb (context):  

    background_adverbs = ['commonly', 'constantly', 'ever', 'frequently', 'generally', 'infrequently', 'never' , 'normally', 
    'occasionally', 'often', 'rarely', 'regularly', 'seldom', 'sometimes', 'regularly', 'usually', 
    'already', 'before', 'early', 'earlier', 'eventually', 'finally', 'first', 'formerly', 'initially', 'just', 'last', 
    'late', 'later', 'lately', 'next', 'previously', 'recently', 'since', 'soon', 'still', 'traditionally', 
    'typically', 'usually','yet']
    
    for sentence in context.sentences:
        for token in sentence:
        
            if token.lemma in background_adverbs and token.pos == 'RB':
                    return '1' # True
        
    return '0'

############################################################################################

        ## Traits: Background
        # Look for features that characterize the trait 'Background'

# Background Feature 2 (BF2): presence of adjectives
def findingBackgroundAjectives (context):  

    background_adjectives = ['typical', 'recent', 'traditional', 'prior', 'previously', 'past', 'existing']
    
    for sentence in context.sentences:
        for token in sentence:
        
            if token.lemma in background_adjectives and token.pos == 'JJ':
                    return '1' # True
        
    return '0'

############################################################################################

        ## Traits: Background
        # Look for features that characterize the trait 'Background'

# Background Feature 3 (BF3): presence of background verbs
def findingBackgroundVerbs (context):  

    list_of_verbs = ['use', 'propose', 'describe','observe', 'explain', 'define' ]
    for sentence in context.sentences:
        token_index = 0
        verb_not_found = True
        while token_index < len (sentence) and verb_not_found:
            if sentence[token_index].lemma in list_of_verbs and sentence[token_index].pos == 'VBN': 
                verb_not_found = False
            else:
                token_index +=1

        if not verb_not_found:
            if (sentence [token_index+1].lemma =='in' or sentence [token_index+1].lemma == 'by') and (sentence [token_index+1].pos =='IN'):
                return '1'
    
    return '0'

############################################################################################

        ## Traits: Background
        # Look for features that characterize the trait 'Background'

# Background Feature 4 (BF4): presence of examples (for example, for instance)
def findingExamples (context):  

    def findingExamples1 (context):

        for sentence in context.sentences:
            token_index = 0
            example_not_found = True
            while token_index < len (sentence) and example_not_found:
                if sentence[token_index].lemma == "for" and sentence[token_index].pos == 'IN': 
                    example_not_found = False
                else:
                    token_index +=1

            if not example_not_found:
                if (sentence [token_index+1].lemma =='example' or sentence [token_index+1].lemma == 'instance') and (sentence [token_index+1].pos =='NN'):
                    return '1'
        
        return '0'
    
    def findingExamples2 (context):  

        for sentence in context.sentences:
            token_index = 0
            example_not_found = True
            while token_index < len (sentence) and example_not_found:
                if sentence[token_index].lemma == "such" and sentence[token_index].pos == 'JJ': 
                    example_not_found = False
                else:
                    token_index +=1

            if not example_not_found:
                if sentence [token_index+1].lemma =='as' and sentence [token_index+1].pos =='IN':
                    return '1'
        
        return '0'
    
    def findingExamples3 (context):  

        for sentence in context.sentences:
            for token in sentence:
            
                if token.lemma == 'e.g.' and token.pos == 'FW':
                    return '1' # True
                
        return '0'

    if (findingExamples1(context) =='1') or (findingExamples2(context) =='1') or (findingExamples3(context) =='1'):
        return '1'
    else:
        return '0'

############################################################################################

        ## Traits: Hedges
        # Look for features that characterize the trait 'Hedges'

# Hedge Feature 1 (HF1): presence of modal verbs (may, might, could, should,  would)
def findingModalVerbs (context): 

    list_of_modal_verbs = ['may', 'might', 'could', 'should', 'would']
    for sentence in context.sentences:
            for token in sentence:
            
                if token.lemma in list_of_modal_verbs and token.pos == 'MD':
                    return '1' # True
                
    return '0' 

############################################################################################

        ## Traits: Hedges
        # Look for features that characterize the trait 'Hedges'

# Hedge Feature 2 (HF2): presence of reporting verbs (suggest, estimate, etc.)
def findingReportingVerbs (context): 

    list_of_reporting_verbs = ['suggest', 'imply', 'estimate', 'conjecture', 'suppose', 'assune', 'admit', 'speculate']
    for sentence in context.sentences:
            for token in sentence:
            
                if token.lemma in list_of_reporting_verbs and re.search (r'^V', token.pos):
                    return '1' # True
                
    return '0' 

############################################################################################

        ## Traits: Hedges
        # Look for features that characterize the trait 'Hedges'

# Hedge Feature 3 (HF3): presence of copular verbs (not be), such as appear, seem, etc.
def findingCopVerbs (context): 

    list_of_cop_verbs = ['appear', 'seem', 'tend', 'look like']
    for sentence in context.sentences:
            for token in sentence:
            
                if token.lemma in list_of_cop_verbs and re.search (r'^V', token.pos):
                    return '1' # True
                
    return '0' 

############################################################################################

        ## Traits: Hedges
        # Look for features that characterize the trait 'Hedges'

# Hedge Feature 4 (HF4): presence of modal adjectives
def findingModalAdjectives (context): 

    list_of_modal_adjectives = ['possible', 'probable', 'potential']
    for sentence in context.sentences:
            for token in sentence:
            
                if token.lemma in list_of_modal_adjectives and token.pos == 'JJ':
                    return '1' # True
                
    return '0' 

############################################################################################

        ## Traits: Hedges
        # Look for features that characterize the trait 'Hedges'

# Hedge Feature 5 (HF5): presence of modal adjectives
def findingModalAdverbs (context): 

    list_of_modal_adverbs = ['possibly', 'probably', 'potentially', 'perhaps', 'conceivably']
    for sentence in context.sentences:
            for token in sentence:
            
                if token.lemma in list_of_modal_adverbs and token.pos == 'RB':
                    return '1' # True
                
    return '0' 

############################################################################################

        ## Traits: Hedges
        # Look for features that characterize the trait 'Hedges'

# Hedge Feature 6 (HF6): presence of modal nouns
def findingModalNouns (context): 

    list_of_modal_nouns = ['possibility', 'probability', 'assumption']
    for sentence in context.sentences:
            for token in sentence:
            
                if token.lemma in list_of_modal_nouns and token.pos == 'NN':
                    return '1' # True
                
    return '0' 

############################################################################################

      
#########################################


rules = {'WF1' : findingVerbFail, 
         'WF2' : findingLimitation,
         'WF3' : findingLow, 
         'WF4' : findingOnly, 
         'WF5' : findingDifficult,     
         'WF6' : findingNegativeAdjectives,
         'WF7' : findingNegativeAdjectives2,
         'WF8' : findingNegPhrase1,
         'WF9' : findingNegPhrase2,
         'WF10' : findingNegPhrase3,
         'WF11' : findingNegPhrase4,
         'WF12' : findingAdjNoun,
         'WF13' : findingVerbDegrade,
         'CF1' : findingVerbOutperform,
         'CF2' : findingImprovement,
         'CF3' : findingComparison,
         'CF4' : findingCompare,
         'CF5' : findingRather
         }

traits = {'BF1' : findingBackgroundAdverb,
         'BF2' : findingBackgroundAjectives,
         'BF3' : findingBackgroundVerbs,
         'BF4' : findingExamples,
         'HF1' : findingModalVerbs,
         'HF2' : findingReportingVerbs,
         'HF3' : findingCopVerbs,
         'HF4' : findingModalAdjectives,
         'HF5' : findingModalAdverbs,
         'HF6' : findingModalNouns}
