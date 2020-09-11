import csv
import sys

file = sys.argv[1]
output_file = sys.argv[2]

totals = {}
totals ['Athar'] = 0
totals ['DFKI'] = 0
totals ['Liu'] = 0
totals ['IMS'] = 0
totals ['CFC'] = 0
totals ['Concit'] = 0

negatives = {}
negatives ['Athar'] = 0
negatives ['DFKI'] = 0
negatives ['Liu'] = 0
negatives ['IMS'] = 0
negatives ['CFC'] = 0
negatives ['Concit'] = 0

with open(file) as csv_object: 
    csv_reader = csv.reader(csv_object, delimiter = '\t') 
    next (csv_reader) # skip the first line (headers)
    for row in csv_reader:

        totals [row[1]] +=1 # row 1 indicates the data source; we can count the total of contexts that come from this source
        if row[6] == '1':   # identify the contexts that have negative polarity
            negatives [row[1]] += 1 # count how many contexts are negative

results = []

for key in totals:
    percentage = round(((negatives[key] * 100)/totals[key]) ,2)
    results.append ({'dataSource' : key, 'contextsTotal' : totals[key], 'contextNeg' : negatives[key], '%' : percentage})

#compute grand totals
sum_total = 0
for count in totals.values():
    sum_total += count # get the total of contexts (adding the amount of contexts that come from each of the sources)

sum_neg = 0
for count in negatives.values():
    sum_neg += count # get the total of negative contexts

Percentage_neg = round(((sum_neg * 100)/sum_total) ,2) # calculate the percentage of contexts 

results.append({ 'dataSource' : 'overall', 'contextsTotal' : sum_total, 'contextNeg' : sum_neg, '%' : Percentage_neg})


with open(output_file, mode='w', newline='') as csvfile:
    fieldnames=['dataSource','contextsTotal','contextNeg','%']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter= '\t')
    writer.writeheader()   
    for line in results:  
        writer.writerow(line)

   