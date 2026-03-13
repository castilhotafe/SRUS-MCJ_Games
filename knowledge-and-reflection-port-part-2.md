# Overview

These questions are designed to accompany the task "Implementing a Hash Map in Python" in the "Data Structures and Algorithms" module. The questions are intended to test your understanding of hash maps, their implementation in Python, and the process of integrating data from a double linked list into a hash map. You will also be asked to reflect on your learning and the challenges you faced during the task.

# Knowledge questions

The following are all examples of hash functions:

```python
# (1) the simplest hash function (Stupidly Simple Hash)
def ssh(key):
    return 1
```

```python
# (2) hash function that sums the ASCII values of the characters in the key
def sum_of_ascii_values(key: str, size: int) -> int:
    total = 0
    for char in key:
        total += ord(char)
    return total % size
```

A more Pythonic version

```python
# (2a)
def sum_of_ascii_values(key: str, size: int) -> int:
    return sum(ord(char) for char in key) % size
```

A Pearson Hash function

```python
# (3) Pearson hash function
# https://en.wikipedia.org/wiki/Pearson_hashing
import random

random.seed(42)

# This is INCORRECT:
# pearson_table = [random.randint(0, 255) for _ in range(256)]
pearson_table = list(range(256))
random.shuffle(pearson_table)

def pearson_hash(key: str, size: int) -> int:
    hash_ = 0
    for char in key:
        hash_ = pearson_table[hash_ ^ ord(char)]
    return hash_ % size
```

The following is a hash function that uses the built-in `hash` function in Python

```python
# (4) hash function that uses the built-in hash function
def built_in_hash(key: str, size: int) -> int:
    return hash(key) % size
```

Finally, the following is a hash function that uses the `SHA256` hash function from the `hashlib` module

```python
# (5) hash function that uses the SHA256 hash function
# https://docs.python.org/3/library/hashlib.html
# https://en.wikipedia.org/wiki/SHA-2
# https://en.wikipedia.org/wiki/SHA-2#Pseudocode
import hashlib

def sha256_hash(key: str, size: int) -> int:
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % size
```

1. All of the above functions are hash functions. Explain how so - what key properties do they all share?

> All the funnctions above are hash functions because they all have the same pattern where it receives a key value
> as input and returns numeric value that can be used to determine an index in a hash map 

2. What are the advantages and disadvantages of each of the above hash functions? Evaluate in terms of uniformity, determinism, efficiency, collision resistance, sensitivity to input changes, and security[1](#Reference). You may need to do some reasearch to answer this question 😱

> The first function always returns the same value, so it has very poor uniformity and many collisions. It is deterministic and very fast, but it is not useful fo a hash map because all keys will go to the same index.
> 
> The ASCII sum function is deterministic and efficient because it simply adds the ASCII values of the characters. It distributes values better than the first function, but collisions can still happen because different strings may produce the same total value.
> Zelenski, J. (n.d.). Hashing (Lecture 25). Stanford University, CS106B: Programming Abstractions. https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1262/lectures/25-hashing/
> 
> The Pearson hash function improves uniformity and collision resistance because it mixes the input values using a lookup table and XOR operations.
It is deterministic and efficient because it uses simple operations and can run very fast.
Another advantage is that small changes in the input usually produce very different hash values.
The disadvantage is that it is not secure for cryptographic purposes and requires a lookup table that may consume extra memory.
> Reference (APA)
Pearson, P. K. (1990). Fast hashing of variable-length text strings. Communications of the ACM. - https://www.epaperpress.com/vbhash/download/p677-pearson.pdf
> 
> The built-in Python hash function is deterministic within the same execution and very efficient because it is implemented in the Python runtime.
It usually provides good distribution of values, which helps reduce collisions in hash tables.
The advantage is that it is fast and already optimized for Python objects.
The disadvantage is that its result may change between program executions and it is not designed for cryptographic security.
> Reference:
Python Software Foundation. (2024). Built-in Functions — hash(). Python Documentation.
Concept of hash table distribution: https://www.cs.cornell.edu/courses/cs312/2008sp/lectures/lec21.html
> 
> The SHA256 hash function has very strong collision resistance and high sensitivity to input changes.
A small modification in the input produces a completely different output.
The advantage is strong security and resistance to attacks.
The disadvantage is that it is slower and computationally heavier than simple hash functions, so it is usually not used for hash tables.
> Reference:
NIST. (2015). Secure Hash Standard (SHS).https://www.linkedin.com/pulse/understanding-sha-family-cryptographic-hash-functions-manjhu-bzyzc

3. List the three most important attributes (arranged from most to least) in the context of a hash map? Justify your answer.
>
>The most important attribute is uniformity because a hash function should distribute keys evenly across the hash map. This helps reduce collisions and keeps the structure efficient.
>
>The second attribute is efficiency because the hash function must be fast to compute. If the hash function is slow, it can affect the performance of the hash map.
>
>The third attribute is determinism because the same key must always produce the same hash value. This ensures the program can always find the correct index for the stored data.

4. Which of the above hash functions would you choose to implement the requirements of the task? Why?

> I used an ASCII based hash function for the player uid so if the key is a string the Player.hash() method is used, and if the key is a Player object  the __hash__ methodis called, but both use the same hashing logic.

5. In your own words, explain each line in the pearson hash function above in terms of the criteria you listed in question 2.
>
> random.seed(42) ensures the shuffle always produces the same table
>
>pearson_table = list(range(256)) creates a lookup table/list with values from 0 to 255
>
>random.shuffle(pearson_table) mixes the table values to reduce collisions, following seed(42)
>
>hash_ = 0 initializes the hash value before processing the key.
>
>for char in key: processes each character so the entire key influences the final hash.
>
>hash_ ^ ord(char) converts the character to its ASCII value and mixes it with the current hash using XOR mixing their bit values
>
>pearson_table[...] uses the XOR result as an index in the table and the value found becomes the new hash value to compute the next char
>
>return hash_ % size ensures the final hash fits within the hash map range.
>
6. Write pseudocode of how you would store Players in PlayerLists in a hash map.

Start

    Create a PlayerHashMap with size 10 
    create 10 empty PlayerLists inside the hash map

    When storin a player:
    receive key and name
    if key is a Player object:
        calculat index using hash(player) % size
    else:
        calculate index using Player.hash(key) % size
    go to the PlayerList on that index
    search the PlayerList by its key

    If player is not found:
        create a new Player with key and name
        append the new Player to the PlayerList
    Else:
        update the existing player's name

## Reflection

1. What was the most challenging aspect of this task?

> maintaining a good separation of responsibilities between the classes was a huge challenge because 
>i had to think carefully about what each method should return so the values could be reused by other functions.
>Another challenge was researching Python magic methods and understanding how they interact through polymorphism. 
>This helped keep the hash map interface more natural and maintainable.

2. If you didn't have to use a PlayerList, how would you have changed them implementation of the hash map and why?

> I would probably use a Python dictionary as it already work as hash map and handle hashing and collisions internally.
>This would make the implementation simpler because players could be stored directly using their uid as the key.

## Reference

### Key Dimensions of Hash Functions

1. **Uniformity**: the probability of any given hash value within the range of possible hash values should be approximately equal.

2. **Determinism**: a given input will always produce the same output.

3. **Efficiency**: the time complexity of computing the hash value should be constant, the hash function should be fast to compute, and utilize the architecture of the computer effectively

4. **Collision Resistance:** minimize the probability of collisions, through a variety of mechanisms.

5. **Sensitivity to input changes:** small changes in the input should produce large changes in the output.

6. **Security**
   - It should be computationally infeasible to find an input key that produces a specific hash value (non-reversibility)
   - The output hash values should appear random and unpredictable.
