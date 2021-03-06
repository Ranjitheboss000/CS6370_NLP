# CS6370_NLP

Development of search engine using vector space model

The goal of the assignment is to build a search engine from scratch, which is an example of an information retrieval system. 
Codes associated with basic text processing module that implements sentence segmentation, tokenization, stemming/lemmatization and stopword removal are provided. 
Codes implementing an Information Retrieval system using the Vector Space Model are provided.

Cranfiled dataset has been used for this purpose.

main.py - The main module that contains the outline of the Search Engine. Do not change anything in this file.

To test the code, run main.py as before with the appropriate arguments.
Usage: main.py [-custom] [-dataset DATASET FOLDER] [-out_folder OUTPUT FOLDER]
               [-segmenter SEGMENTER TYPE (naive|punkt)] [-tokenizer TOKENIZER TYPE (naive|ptb)] 

When the -custom flag is passed, the system will take a query from the user as input. For example:
> python main.py -custom
> Enter query below
> Papers on Aerodynamics
This will print the IDs of the five most relevant documents to the query to standard output.

When the flag is not passed, all the queries in the Cranfield dataset are considered and precision@k, recall@k, f-score@k, nDCG@k and the Mean Average Precision are computed.

In both the cases, *queries.txt files and *docs.txt files will be generated in the OUTPUT FOLDER after each stage of preprocessing of the documents and queries.

