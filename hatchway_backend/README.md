Setup: Using Python Pandas data structures for reading csv files.
Workflow: 1) A directory for storing csv files.
          2) A Python file consisiting of fileClass having class variable  data file folder path and a list of files having csv extensions.
          3) Some prior knowledge of csv files is necessary for using filters for error checking such as hire date in one of the data files is stored as string where as while
            performing analysis one would need it to be in date format . 
          4) Error checking: compares the path of files with that of root folder to check if file exists in that location.
          5) Based on the file , reads the file in pandas and performs the required analysis. (function read_file())
          6) Test Analysed here: a) Find max salary of employee in empdata.csv
                                 b) Find Highest Score in Highscore.csv
          7) Pandas provide better performance when compared to csv reader of python in case of large files.
        
          

          