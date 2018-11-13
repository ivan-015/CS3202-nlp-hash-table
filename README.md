# nlp-hash-table
This program uses hash tables to store words and their embeddings to perform quick searching and compares three hash functions.


## Important note
* Because GitHub does not allow files larger than 25MB, the glove.6B.50d.txt file had to be significantly reduced in order to be uploaded. However, you can click [here](https://nlp.stanford.edu/data/glove.6B.zip) to download the full glove file and test the program.

## Contents
* **"word_embeddings_ht.py"** - This is the main file of the function, in which the user will interact with the program. It allows the user to specify the size of the hash table they wish to work with, populates a hash table by reading words and embeddings from a file, computes the loading factor of the table, and the average comparisons to be performed when searching for a word. Additionally, the program provides the user the option to search for a word and tells the user how many comparisons were made and allows them to choose from three different hashing functions.


* **"Hash_Table.py"** - This file represents a hash table and a hash table node. It performs insertion by hashing the word with one of three different hashing functions, and chains if a collision is found. It also performs searches using the same hashing function used to insert the element, and prints the number of comparisons made.
