# Ivan Vigliante
# CS2302 TR 10:20am-11:50am
# Lab 3A
# Professor Aguirre, Diego
# TA Saha, Manoj
# Date of last modification: 11/10/2018
# This program represents a hash table to use in another program


class HTNode:
    def __init__(self, word, embedding, next):
        self.word = word
        self.embedding = embedding
        self.next = next


class HashTable:

    def __init__(self, size=60000):
        self.table = [None] * size

    # Function that raises a value to the position of the letter
    # and multiplies it times its unicode value to hash the word
    def pos_hash(self, word):
        # Arbitrary initial value
        value = 56
        for i in range(len(word)):
            value = value + 9**i * ord(word[i])
        return value % len(self.table)

    # Function that hashes a word by looking at each character, determining
    # if its unicode number is even or odd, and performing operations
    # based on that
    def pow_hash(self, word):
        value = 0
        for i in range(len(word)):
            if ord(word[i]) % 2 == 0:
                value += ord(word[i]) ** 4 + i
            else:
                value += ord(word[i]) ** 3 + i
        return value % len(self.table)

    # Multiplicative hashing function that uses each character
    # in the word and adds to a multiplier to return a hash.
    def mult_char_hash(self, word):
        hash_num = 4321

        for char in word:
            # Multiply hash_num by 36 and add the unicode value of the alphabetic char
            hash_num = (hash_num * 36) + ord(char)
        return hash_num % len(self.table)

    def insert(self, word, embedding, hash_f="pow"):
        word = word.lower()
        # Choose hashing function
        if hash_f == "pow":
            index = self.pow_hash(word)
        elif hash_f == "mult":
            index = self.mult_char_hash(word)
        elif hash_f == "py":
            index = hash(word) % len(self.table)
        elif hash_f == "pos":
            index = self.pos_hash(word)
        else:
            print("Hashing function not recognized.")
            return

        self.table[index] = HTNode(word, embedding, self.table[index])

    def search(self, word, hash_f="pow"):
        index = -1
        if hash_f == "pow":
            index = self.pow_hash(word)
        elif hash_f == "mult":
            index = self.mult_char_hash(word)
        elif hash_f == "pos":
            index = self.pos_hash(word)
        else:
            print("Hashing function given not recognized.")
            return None
        count = 0
        temp = self.table[index]
        while temp is not None:
            count += 1
            if temp.word == word:
                print("Value found. Comparisons:", count)
                return self.table[index]
            temp = temp.next
        print("Value not found. Comparisons: ", count)
        return None
