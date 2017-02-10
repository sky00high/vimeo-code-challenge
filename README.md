Backend Intern Exercise: (csv included in Google Drive folder)
 
Your job is to write code that will load in clips.csv and analyze the data against the rules listed below. Your code should output the results into two files: valid.csv will contain a list of clip_ids's that passed the tests and invalid.csv will contain a list of clip_id's that failed the tests. You may use the SPL FilterIterator if you're using PHP or any standard library if you're using a different language. You may reference the language's official documentation. Your code should handle exceptions if a file cannot be read in or written to.

Rules for a clip to be considered "valid":

1. The clip must be public (privacy == anybody)
2. The clip must have over 10 likes and over 200 plays
3. The clip title must be under 30 characters
 

