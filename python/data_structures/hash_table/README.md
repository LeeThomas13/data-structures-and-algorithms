# Hashtables
A hash table is a data structure that, in a way, combines arrays and linked lists. It has a big o of O(1) for time complexity(kinda) and a space complexity of O(n).

## Challenge
Implement a Hash table with the following methods:

add: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
get: takes in the key and returns the value from the table.
contains: takes in the key and returns a boolean, indicating if the key exists in the table already.
hash: takes in an arbitrary key and returns an index in the collection.

## Approach & Efficiency
I took JB's approach during lecture. Make a Hash table class that imports my Linked List class from another file. Add the necessary methods from there.

## API
The add function called set in my class takes in a key and a value, which then makes a bucket for the input params if it doesn't have a bucket for it already. The bucket utilizes my linked lists class.

The get takes in a given key, and finds it in the hash table, then returns its value.

The hash takes in a random key, multiplies it by a prime number, then gets the modulo of that result over 1024. This gives it a unique key and 'hashisizes' it

The contains method will go through the table, and if a value exists, will return True, if not it will return False.

## Tests
Adding a key/value to your hashtable results in the value being in the data structure
Retrieving based on a key returns the value stored
Successfully returns null for a key that does not exist in the hashtable
Successfully handle a collision within the hashtable
Successfully retrieve a value from a bucket within the hashtable that has a collision
Successfully hash a key to an in-range value
