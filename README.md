# find-political-donors-for-insight

This is the coding challenge insight data engineering program. This challenge has been exciting and brainstorming. I have tried to perform well in this coding challenge.

Above project files contain specific folders related to a specific process.

Input folder contains the input file that was specified in the challenge. This file is a text file with records seperated by '|'. This file is named as itcont.txt. I recommend to put a custom file under this name before running a program.

The input folder also contains a cleanedfile folder which has the cleaned.txt file. This text file contains the records/data which can be considered for processing. This file is obtained in order to follow Input file considerations provided in the challenge. This file provides necessary data for individual entities. The data in this file is as follows:
1. CMTE_ID
2. Zip code
3. Date of transaction
4. Amount of the transaction
5. Fifth field is empty and is ignored while obtaining the outputs.

my_testsuite folder contains a folder called tests. This folder contain all the tests that were performed. It also contains a shell file to run the tests.

The output folder gives the final output named as follows:
medianvals_by_zip.txt
medianvals_by_date.txt
These files can be used as an input to create a dashboard.

The src folder contains the sourcecode for this project. This python file is well structured and commented. It is very easy to understand.

The run.sh file in the top-most directory compiles and execute the source code.