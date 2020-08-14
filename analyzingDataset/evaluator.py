from  rules_module import *
from  features_module import *

import csv


class Evaluator():

    def __init__ (self, contexts_dict, original_csv):

        self.contexts_dict = contexts_dict
        self.results = {}
        self.methods_applied = []

        for context_key in self.contexts_dict: # Initialize the dictionary that takes the id of the context as key
            self.results[context_key] = {}

        # Open the original corpus file (csv format) to recover the text of the context and the polarity
        with open(original_csv, mode='r') as contexts_file:
            reader = csv.DictReader(contexts_file, delimiter='\t')
            for row in reader:
                self.results[row['id']]['context_text']=row['citeContext']
                self.results[row['id']]['original_polarity']=row ['polarity']

    
    
    def apply (self, method_ids):
        self.methods_applied += method_ids
        for method_id in method_ids:
            if method_id in features:

                applied_function = features[method_id]
            
            elif method_id in rules:

                applied_function = rules[method_id]
            
            else:
                print('Method not identified')
            
        
            for context_key in self.contexts_dict:

                context_id = context_key
                context = self.contexts_dict[context_id]

                self.results[context_id][method_id] = applied_function(context)

    
    def evaluteResultsForSingleMethod (self, method_id):
        
        # The goal is to find "negative polarity" citations
        # A method gives a true positive when the annotated citations is negative and the automatic check is also negative
        # A method gives a false positive when the annotated citations is not negative and the automatic check is negative
        # A method gives a false negative when the annotated citations is negative and the automatick check is not negative
        # A method gives a true negative when the annotated citations is not negative and the automatic check is not negative
        true_negatives = 0
        true_positives = 0
        false_negatives = 0
        false_positives = 0

        for context_id in self.results:
            original_polarity = self.results[context_id]['original_polarity']
            method_polarity = self.results[context_id][method_id] 
            if method_polarity == '0' and original_polarity == '0':
                true_negatives +=1
            elif method_polarity == '0' and  original_polarity == '1':
                false_negatives +=1
            elif method_polarity == '1' and  original_polarity == '1':
                true_positives +=1
            elif method_polarity == '1' and  original_polarity == '0':
                false_positives += 1
               

        recall = (true_positives / (true_positives + false_negatives))
        precision = (true_positives / (true_positives + false_positives))
        print ('For the method '+method_id+', precision is: ' + str(precision)+ ' and recall is : ' + str (recall))
        #print ('true negatives : '+str(true_negatives)+', true positives : '+str(true_positives))
        #print ('false negatives : '+str(false_negatives)+', false positives : '+str(false_positives))
        return (true_negatives, true_positives, false_negatives, false_positives)


    #Optional parameter list_of_exported_methods 
    #If not given, the file will have the results for all the methods applied

    def exportAsCSV (self, output_file_name, list_of_exported_methods = None):
        list_to_export = []
        for key in self.results:
            new_item = self.results[key].copy()
            new_item['context_id'] = key
            list_to_export.append (new_item)
            

        ## Write the results on a csv file 
        with open(output_file_name, mode='w', newline='') as csvfile:
            #check if the optional parameter was given
            if (list_of_exported_methods == None):
                fieldnames = ['context_id', 'context_text']+self.methods_applied+ ['original_polarity']
            else:
                fieldnames = ['context_id', 'context_text']+list_of_exported_methods+ ['original_polarity']
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter= '\t')
            writer.writeheader()

            for dict in list_to_export:
                writer.writerow(dict)

        