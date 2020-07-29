#!/usr/sfw/bin/python
# -*- coding: utf-8 -*-

import glob, os, re, sys, requests

# store in the folder variable the address of the folder containing this program
folder = os.path.abspath(os.path.dirname(sys.argv[0]))

input = open(os.path.join(folder,"input.txt"),"r",encoding="utf-8")
output = open(os.path.join(folder,"output.txt"),"w",encoding="utf-8")
outputHtml = open(os.path.join(folder,"output.html"),"w",encoding="utf-8")
outputHtml.writelines("<html><head></head><body>")

def repeatSearch(lineSegments, regex):
   oldLength = -1
   length = len(lineSegments)
   # Look for the regular expression in all segments as long as we find occurrences:
   while length != oldLength:
      lineSegments = labelReference(lineSegments, regex)
      oldLength = length
      length = len(lineSegments)      
   return lineSegments

# For each segment in lineSegment which is not already labeled as a citation
# check if the regex is found, in which case we have found a new citation segment
def labelReference(lineSegments, regex):
   newLineSegments = []
   for segment in lineSegments:
      if segment[0:6] == "<cite>":
         # A citation was already found in the segment so no need to check the regex on this segment
         newLineSegments.append(segment)
      else:
         # No citation was found yet, try to apply the regex to find a citation
         #print("Looking for regex in "+segment)
         res = re.search('(.*'+regex+'.*)',segment)
         if res:
            # A citation was found, add the segment before, the labeled citation, and the segment after, into newLineSegments
            #print("found!")
            newLineSegments.append(res.group(1))
            newLineSegments.append("<cite>"+res.group(2)+"</cite>")
            newLineSegments.append(res.group(3))
         else:
            # No citation was found
            #print("not found!")
            newLineSegments.append(segment)
   return newLineSegments
   

foundCitations = 0
contextNb = 0

for line in input:
   # For each context
   lineSegments = [line]
   # Look for citations using the following expressions
   # each found citation will cut the context into several segments, one of which containing the citation
   lineSegments = repeatSearch(lineSegments,")([A-Z][^ ]+ and [A-Z][^ ]+[, ]* [(][12][0-9][0-9][0-9][a-f]*[)])(")   
   lineSegments = repeatSearch(lineSegments,")([A-Z][^ ]+ and [A-Z][^ ]+[, ]* [12][0-9][0-9][0-9][a-f]*)(")   
   lineSegments = repeatSearch(lineSegments,")([A-Z][^ ]+ & [A-Z][^ ]+[, ]* [(][12][0-9][0-9][0-9][a-f]*[)])(")   
   lineSegments = repeatSearch(lineSegments,")([A-Z][^ ]+ & [A-Z][^ ]+[, ]* [12][0-9][0-9][0-9][a-f]*)(")   
   lineSegments = repeatSearch(lineSegments,")([A-Z][^ ]+ et al[., ]*[(][12][0-9][0-9][0-9][a-f]*[)])(")   
   lineSegments = repeatSearch(lineSegments,")([A-Z][^ ]+ et al[., ]*[12][0-9][0-9][0-9][a-f]*)(")   
   #lineSegments = repeatSearch(lineSegments,")([A-Z][^ ]*[a-zàâäéèêëìîöòôùûüç][^ ]*[, ]*[12][0-9][0-9][0-9][a-f]*)(")   
   lineSegments = repeatSearch(lineSegments,")([A-Z][^ ]+[, ]*[12][0-9][0-9][0-9][a-f]*)(")   
   lineSegments = repeatSearch(lineSegments,")([A-Z][^ ]+ [(][12][0-9][0-9][0-9][a-f]*[)])(")   
   citationFound = False
   # Reconstruct the context with labeled citations by putting together all segments
   for segment in lineSegments:
      output.writelines(segment)
      outputHtml.writelines(segment.replace("<cite>","<b><u>").replace("</cite>","</u></b>"))
      if segment[0:6] == "<cite>":
         citationFound = True
   output.writelines("\n")
   outputHtml.writelines("<br>\n")
   # Update the number of found citations
   contextNb += 1
   if citationFound:
      foundCitations += 1
   else: 
      print("No citation found in:\n"+line)

# Print the total number of contexts and the number of contexts containing a citation
print(str(contextNb)+" contexts, "+str(foundCitations)+" citations.")
input.close()
output.close()

outputHtml.writelines("</body></html>")
outputHtml.close()