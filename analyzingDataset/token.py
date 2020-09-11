class Token ():

    def __init__ (self):

        self.index = 0
        self.wordForm = ''
        self.lemma = ''
        self.pos = ''
        self.upos = ''
        self.feature = ''
        self.governor = 0
        self.dependency = ''

    def checkFeature (self, feature_name, value_checked):  # Verify if the token has a feature
        feature_list = self.feature.split('|')
        for feature in feature_list:
            split_feature = feature.split('=')
            if split_feature[0]==feature_name:
                if split_feature[1] == value_checked:
                    return True
                else: 
                    return False
            
        return False


###############################################################################################
# Exemple of a sentence analysed by Stanza. The data is presented as a list of dictionnaries.
# See https://stanfordnlp.github.io/stanza/index.html or reference below
#
#  [
#         {
#             "id": 1,                                 ** id = The index of this token in the sentence, 1-based  
#             "text": "See",                              (index 0 is reserved for an artificial symbol that represents the root of the syntactic tree). 
#             "lemma": "see",                          ** text = The text (the word form) of this token 
#             "upos": "VERB",                          ** lemma = the lemma of this word 
#             "xpos": "VB",                            ** upos = The universal part-pf-speech of this word (e.g. NOUN, VERB) 
#             "feats": "Mood=Imp|VerbForm=Fin",        ** xpos = The treebank-specific part-of-speech of this word 
#             "head": 0,                               ** features = The morphological features of this word 
#             "deprel": "root",                        ** head = The id of the syntactic head of this word in the sentence, 1-based for actual words in the sentence (
#             "misc": "start_char=1|end_char=4",            0 is reserved for an artificial symbol that represents the root of the syntactic 	tree).
#             "ner": "O"                               ** deprel = The dependency relation between this word and its syntactic head        
#         },                                           ** miscelaneus : Miscellaneous annotations with regard to this word. 
#         {                                                 The pipeline uses this field to store character offset information internally, for instance.
#             "id": 2,                                 ** ner = The NER tag of this token (named entity recognition)
#             "text": "CITATION",
#             "lemma": "citation",
#             "upos": "NOUN",
#             "xpos": "NN",
#             "feats": "Number=Sing",
#             "head": 1,
#             "deprel": "obj",
#             "misc": "start_char=5|end_char=13",
#             "ner": "S-ORG"
#         },
#         {
#             "id": 3,
#             "text": "for",
#             "lemma": "for",
#             "upos": "ADP",
#             "xpos": "IN",
#             "head": 5,
#             "deprel": "case",
#             "misc": "start_char=14|end_char=17",
#             "ner": "O"
#         },
#         {
#             "id": 4,
#             "text": "more",
#             "lemma": "more",
#             "upos": "ADJ",
#             "xpos": "JJR",
#             "feats": "Degree=Cmp",
#             "head": 5,
#             "deprel": "amod",
#             "misc": "start_char=18|end_char=22",
#             "ner": "O"
#         },
#         {
#             "id": 5,
#             "text": "details",
#             "lemma": "detail",
#             "upos": "NOUN",
#             "xpos": "NNS",
#             "feats": "Number=Plur",
#             "head": 2,
#             "deprel": "nmod",
#             "misc": "start_char=23|end_char=30",
#             "ner": "O"
#         },
#         {
#             "id": 6,
#             "text": ".",
#             "lemma": ".",
#             "upos": "PUNCT",
#             "xpos": ".",
#             "head": 1,
#             "deprel": "punct",
#             "misc": "start_char=31|end_char=32",
#             "ner": "O"
#         }
#     ]
# ]


## Reference

# Peng Qi, Yuhao Zhang, Yuhui Zhang, Jason Bolton and Christopher D. Manning. 2020. Stanza: 
# A Python Natural Language Processing Toolkit for Many Human Languages. In Association for 
# Computational Linguistics (ACL) System Demonstrations. 2020.
    
