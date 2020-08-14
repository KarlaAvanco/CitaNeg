import context
import re

### Functions to identify the different patterns that constitute a rule
    ### Typology patterns

    ## Class: Weakness
    # Look for features that characterize the class 'Weakness'

## Weakness Feature 1 (WF1): presence of the verbs lack or fail
def findingVerbFail (context): 

    for token in context.token_list:
    
        if (token.lemma =='lack') or (token.lemma =='fail'):
            if re.search (r"^V", token.pos):
                return '1' # True
        
    # If you get to this point, it means the pattern was not found; therefore, return false
    return '0' # False

        
#####################################################################################################################

        ## Class: Weakness
        # Look for features that characterize the class 'Weakness'

## Weakness Feature 2 (WF2): presence of an adjective that has a negative meaning; the adjective must follow a verb 
def findingNegativeAdjectives (context): 
        
    list_of_adjectives = ['problematic','questionable','debatable']
    
    for token in context.token_list:
    
        if token.pos =='JJ':
            token_list = context.token_list
            gov_index = int(token.governor)-1
            governor = token_list[gov_index]
            gov_pos = governor.pos

            if ((re.search (r"^in|^un|^im", token.lemma)) or (token.lemma in list_of_adjectives)) and (re.search (r"^V", gov_pos)):        
                return '1' # True                    
        
    return '0' # False

rules = {'WF1' : findingVerbFail, 
         'WF2' : findingNegativeAdjectives}
