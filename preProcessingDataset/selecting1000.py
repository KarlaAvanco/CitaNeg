import csv
from random import sample
import sys

file = sys.argv[1]
output_file_sampled = sys.argv[2]
output_file_remainder = sys.argv[3]

with open(file) as csv_object: 
    with open(output_file_sampled, mode='w', newline='') as csvfile:
        csv_reader = csv.reader(csv_object, delimiter = '\t') 
        csv_writer = csv.writer(csvfile, delimiter= '\t')
    
        header = next (csv_reader) 
        csv_writer.writerow(header) 

        neg_contexts = []
        other_contexts = []
        for row in csv_reader:
        
            if row[6] == '1':
                neg_contexts.append(row)
            
            else:
                other_contexts.append(row)
                
        
        sample_neg = sample(neg_contexts, 500)

        remaining_neg = []
        for item in neg_contexts:
            if not item in sample_neg:
                remaining_neg.append(item)

        number_of_negatives_remaining = len (remaining_neg)

        sample_other = sample(other_contexts, 500)

        remaining_other = []
        number_of_remaining_other = 1
        for item in other_contexts:
            if not item in sample_other:
                remaining_other.append(item)
                number_of_remaining_other += 1
                if number_of_remaining_other == number_of_negatives_remaining:
                    break

        for context in sample_neg:
            csv_writer.writerow(context)
                
        for context in sample_other:
            csv_writer.writerow(context)
       
                       
    with open(output_file_remainder, mode='w', newline='') as remainder_csv:
        csv_writer = csv.writer(remainder_csv, delimiter= '\t')
        
        csv_writer.writerow(header) 
        for context in remaining_neg:
            csv_writer.writerow(context)
                
        for context in remaining_other:
            csv_writer.writerow(context)
                   

       




   