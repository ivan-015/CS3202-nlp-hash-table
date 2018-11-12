# Ivan Vigliante
# CS2302 TR 10:20am-11:50am
# Lab 4A
# Professor Aguirre, Diego
# TA Saha, Manoj
# Date of last modification: 11/11/2018
# The purpose of this program is to read from a file containing words and
# their word embeddings, store them in a hash table, determine the average
# number of comparisons to retrieve an element, and compute the load factor
from Hash_Table import HashTable
from timeit import default_timer as timer

# Function that prompts user to perform search on hash table
def perform_search(ht, hf):
    while True:
        word = input("Enter a word you would like to look for (\"e\" to cancel and go back): ")
        if word == "e":
            print()
            return
        start = timer()
        ht.search(word, hf)
        print("Runtime of search operation:", round(timer()-start,6)*1000, "milliseconds")


# This function computes the average number of comparisons performed
# in the search() function. This is done by dividing the number of nodes
# by the number of buckets being used.
def avg_comparisons(ht):
    if ht is None or len(ht.table) == 0:
        return 0
    buckets_used = 0
    nodes = 0
    for elem in ht.table:
        if elem is None:
            continue
        # If the current index has an element, add one to
        # buckets used
        buckets_used += 1
        temp = elem
        # Count the number of elements in each bucked
        while temp is not None:
            nodes += 1
            temp = temp.next
    if buckets_used == 0:
        return 0
    # Return average number of comparisons to be performed
    return nodes // buckets_used


# Function that returns the load factor of a hash table by
# dividing the number of nodes by the total number of buckets
def load_factor(ht):
    if ht is None or len(ht.table) == 0:
        return 0
    count = 0
    # Traverse hash table and count the number of nodes
    for elem in ht.table:
        curr = elem
        while curr is not None:
            count += 1
            curr = curr.next

    return count / len(ht.table)


# Function that creates a hash table from a file
def populate_ht(filename, size, hf):
    file = open(filename, "r", encoding="utf8")
    ht = HashTable(size)
    for line in file:
        curr = line.strip().split(" ")
        # Insert word and embedding if words starts with
        # alphabetic character
        if "a" <= curr[0] <= "z":
            embedding = []
            # Populate the list with embeddings
            for num in curr[1:]:
                embedding.append(float(num))
            ht.insert(curr[0], embedding, hf)
    return ht


# Function that allows the user to decide the hashing function to use on
# the hash table and then calls the function to create the hash table
def choose_funct():
    filename = "glove.6B.50d.txt"
    # Get the size of the hash table
    try:
        size = input("Enter the size of the hash table (Press \"RETURN\" for default size of 60,000): ")
        if size == "":
            size = 60000
        elif int(size) <= 0:
            print("No negative numbers or zero allowed for size.")
            return
        else:
            size = int(size)
    except ValueError:
        print("Invalid hash table size.")
        return

    while True:
        try:

            pref = input("What kind of hashing function would you like?\n"+
                         " [1]: Power hashing function\n"
                         " [2]: Multiplicative hashing function\n"
                         " [3]: Positional hashing function\n"
                         "Input the number of the hash function to use (or \"e\" to exit): ")
            # Performs the power hashing function
            if pref == "1":
                # Create hash table
                start = timer()
                hash_table = populate_ht(filename, size, "pow")
                print("Runtime of populating hash table:", round(timer()-start, 3)*1000, "milliseconds")
                # Compute loading factor
                lf = load_factor(hash_table)
                print("Loading factor:", lf)
                # Compute average number of comparisons
                avg_comp = avg_comparisons(hash_table)
                print("Average number of comparisons when searching for a word: ", avg_comp, "\n")
                perform_search(hash_table, "pow")
            # Performs the multiplicative hashing function
            elif pref == "2":
                # Create hash table
                start = timer()
                hash_table = populate_ht(filename, size, "mult")
                print("Runtime of populating hash table:", round(timer() - start, 3) * 1000, "milliseconds")
                # Compute loading factor
                lf = load_factor(hash_table)
                print("Loading factor:", lf)
                # Compute average number of comparisons
                avg_comp = avg_comparisons(hash_table)
                print("Average number of comparisons when searching for a word: ", avg_comp, "\n")
                perform_search(hash_table, "mult")
            # Performs the positional hashing function
            elif pref == "3":
                # Create hash table
                start = timer()
                hash_table = populate_ht(filename, size, "pos")
                print("Runtime of populating hash table:", round(timer() - start, 3) * 1000, "milliseconds")
                # Compute loading factor
                lf = load_factor(hash_table)
                print("Loading factor:", lf)
                # Compute average number of comparisons
                avg_comp = avg_comparisons(hash_table)
                print("Average number of comparisons when searching for a word: ", avg_comp, "\n")
                perform_search(hash_table, "pos")
            # Exits the program
            elif pref.lower() == "e":
                return
            else:
                print("Operation not recognized. Please try again.\n")

        # If the default file was not found, give user the option to enter a file path
        except FileNotFoundError:
            print(filename + " file was not found.\n" +
                  "Provide path and name of file with word and embeddings(\"e\" to exit): ")
            prompt = input()
            if prompt.lower() == "e":
                return
            else:
                filename = prompt
        except ValueError:
            print("Value Error. Invalid embedding likely found.")
            return
        except Exception as ee:
            print(ee)


choose_funct()
