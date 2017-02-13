This is the submission for the vieo intern code challenge. It is for Tianyu Yang (ty2345@columbia.edu)

In my implementation, I assumed the csv file can be quite large. So the validation tool would read the input file line by line instead of reading all content at once, even this would sacrifice some performance. IDs were put in memory and write to file at the end of the program to avoid frequent IO request. 

Usage: 

py ValidClips.py [-h]
                 [--validoutputfilename Optional valid output filename]
                 [--invalidoutputfilename Optional invalid output filename]
                 inputFilename

Python version: 3.6

Thank you for your time!