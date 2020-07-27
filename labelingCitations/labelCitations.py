#!/usr/sfw/bin/python
# -*- coding: utf-8 -*-

import glob, os, re, sys, requests

# store in the folder variable the address of the folder containing this program
folder = os.path.abspath(os.path.dirname(sys.argv[0]))

input = open(os.path.join(folder,"input.txt"),"r",encoding="utf-8")
output = open(os.path.join(folder,"output.txt"),"w",encoding="utf-8")

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
            while res:
               end = res.group(3)
               newLineSegments.append(res.group(1))
               newLineSegments.append("<cite>"+res.group(2)+"</cite>")
               res = re.search('(.*'+regex+'.*)',end)
               # We repeat this as long as we find other citations
            newLineSegments.append(end)
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
   lineSegments = labelReference(lineSegments,")([A-Z][^ ]+ and [A-Z][^ ]+[, ]* [(][12][0-9][0-9][0-9][a-f]*[)])(")   
   lineSegments = labelReference(lineSegments,")([A-Z][^ ]+ and [A-Z][^ ]+[, ]* [12][0-9][0-9][0-9][a-f]*)(")   
   lineSegments = labelReference(lineSegments,")([A-Z][^ ]+ et al[., ]*[(][12][0-9][0-9][0-9][a-f]*[)])(")   
   lineSegments = labelReference(lineSegments,")([A-Z][^ ]+ et al[., ]*[12][0-9][0-9][0-9][a-f]*)(")   
   lineSegments = labelReference(lineSegments,")([A-Z][^ ]+ and [A-Z][^ ]+ [12][0-9][0-9][0-9][a-f]*)(")   
   lineSegments = labelReference(lineSegments,")([A-Z][^ ]+[, ]*[12][0-9][0-9][0-9][a-f]*)(")   
   lineSegments = labelReference(lineSegments,")([A-Z][^ ]+ [(][12][0-9][0-9][0-9][a-f]*[)])(")   
   citationFound = False
   # Reconstruct the context with labeled citations by putting together all segments
   for segment in lineSegments:
      output.writelines(segment)
      if segment[0:6] == "<cite>":
         citationFound = True
   output.writelines("\n")
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