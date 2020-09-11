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

            elif method_id in traits:

                applied_function = traits [method_id]
            
            else:
                print('Method not identified')
            
        
            for context_key in self.contexts_dict:

                context_id = context_key
                context = self.contexts_dict[context_id]

                self.results[context_id][method_id] = applied_function(context)
                #print(context_id + method_id)

    
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
               
        print ('true negatives : '+str(true_negatives)+', true positives : '+str(true_positives))
        print ('false negatives : '+str(false_negatives)+', false positives : '+str(false_positives))
        recall = (true_positives / (true_positives + false_negatives))
        precision = (true_positives / (true_positives + false_positives))
        f1score = 2*(precision*recall)/(precision+recall)
        print ('For the method '+method_id+', precision is: ' + str(precision)+ ' and recall is : ' + str (recall)+'. The F1-score is '+str(f1score))
      
        return (true_negatives, true_positives, false_negatives, false_positives)


    def evaluateResultsForMultipleMethods (self, method_ids):
        number_of_matches = 0
        number_of_annotated_negatives = 0
        number_of_negatives_found = 0

        for context_id in self.results:
            method_polarities = []
            for method_id in method_ids:
                method_polarities.append(self.results[context_id][method_id])
            
            original_polarity = self.results[context_id]['original_polarity']

            matches = False
            negative_found = False

            if original_polarity == '1':
                number_of_annotated_negatives += 1

            #If at least one method finds a negative, then we consider that the group of methods
            #has identified the context as negative
            for method_polarity in method_polarities:
                if method_polarity == '1' and original_polarity == '1':
                    matches = True

                if method_polarity == '1':
                    negative_found = True
            
            if matches:
                number_of_matches += 1
            
            if negative_found:
                number_of_negatives_found +=1

        
        recall = number_of_matches / number_of_annotated_negatives
        precision = number_of_matches / number_of_negatives_found 

        names = ''
        for method_id in method_ids:
            if names == '':
                names = method_id
            else:
                names = names+', '+method_id

        print ('For the methods '+names)
        print ('Precision is : '+str(precision)+' and recall is : '+str (recall))

        
        return (recall, precision)


    def checkForNoRecall (self, list_of_methods_compared):
	# This funciton identifies the contexts that were not identified

        if list_of_methods_compared == None:
            methods_checked = self.methods_applied
        else:
            methods_checked = list_of_methods_compared

        for context_id in self.results:
            found_a_match = False
            for method_id in methods_checked:
                if self.results[context_id][method_id] == '1':
                    found_a_match = True

            if not found_a_match:
                self.results[context_id]['no_recall'] = '1'
            else:
                self.results[context_id]['no_recall'] = '0'

    def checkForNoPrecision (self, list_of_methods_compared):
	# This funciton identifies the contexts that were wrongly identified

        if list_of_methods_compared == None:
            methods_checked = self.methods_applied
        else:
            methods_checked = list_of_methods_compared

        for context_id in self.results:
            found_a_match = False

            for method_id in methods_checked:
                if self.results[context_id][method_id] == '1':
                    found_a_match = True
            
            if found_a_match and self.results[context_id]['original_polarity'] == '0':
                self.results[context_id]['no_precision'] = '1'
            else:
                self.results[context_id]['no_precision'] = '0'
    
    #Optional parameter list_of_exported_methods 
    #If not given, the file will have the results for all the methods applied

    def exportAsCSV (self, output_file_name, list_of_exported_methods = None):
        list_to_export = []
        self.checkForNoRecall(list_of_exported_methods)
        self.checkForNoPrecision(list_of_exported_methods)

        for context_id in self.results:
            if list_of_exported_methods != None:
                new_item = {}
                for method_id in list_of_exported_methods:
                    new_item[method_id]=self.results[context_id][method_id]
                new_item['no_precision'] = self.results[context_id]['no_precision']
                new_item['no_recall'] = self.results[context_id]['no_recall']
                new_item['context_text'] = self.results[context_id]['context_text']
                new_item['original_polarity'] = self.results[context_id]['original_polarity']
            else:
                new_item = self.results[context_id].copy()

            new_item['context_id'] = context_id
            list_to_export.append (new_item)         
        
        ## Write the results on a csv file 
        with open(output_file_name, mode='w', newline='') as csvfile:
            #check if the optional parameter was given
            if (list_of_exported_methods == None):
                fieldnames = ['context_id', 'context_text']+self.methods_applied+ ['no_recall','no_precision','original_polarity']
            else:
                fieldnames = ['context_id', 'context_text']+list_of_exported_methods+ ['no_recall','no_precision','original_polarity']
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter= '\t')
            writer.writeheader()

            for dict in list_to_export:
                writer.writerow(dict)
    
    def exportForWeka (self, output_file_name2, list_of_exported_methods = None):
        list_to_export = []

        for context_id in self.results:
            if list_of_exported_methods != None:
                new_item = {}
                for method_id in list_of_exported_methods:
                    new_item[method_id]=self.results[context_id][method_id]

                new_item['original_polarity'] = self.results[context_id]['original_polarity']
            else:
                new_item = self.results[context_id].copy()
                del new_item['context_text']

            list_to_export.append (new_item)         
        
        ## Write the results on a csv file 
           
        with open(output_file_name2, mode='w', newline='') as csvfile:
            #check if the optional parameter was given
            if (list_of_exported_methods == None):
                fieldnames = self.methods_applied+ ['original_polarity']
            else:
                fieldnames = list_of_exported_methods+ ['original_polarity']
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter= ',')
            writer.writeheader()

            for dict in list_to_export:
                writer.writerow(dict)


