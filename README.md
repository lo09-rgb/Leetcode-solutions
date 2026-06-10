# Leetcode-solutions
it is a repo where i push the solved leetocode answers


# Group Anagrams - Thought Process

### Initial Observation

Anagrams are words that contain the same letters but in a different order. Therefore, there must be a common representation that all words in an anagram group share.

For example:

* eat → aet
* tea → aet
* ate → aet

After sorting the characters of each word, all anagrams produce the same result.

### Key Insight

The sorted version of a word can be used as a unique signature (or key) for its anagram group.

Examples:

* "eat", "tea", "ate" → "aet"
* "tan", "nat" → "ant"
* "bat" → "abt"

Words with the same sorted signature belong to the same group.

### Using a HashMap

A dictionary is used where:

* Key = sorted version of the word
* Value = list of words belonging to that anagram group

Example:

{
"aet": ["eat", "tea", "ate"],
"ant": ["tan", "nat"],
"abt": ["bat"]
}

### Algorithm

1. Iterate through each word in the input list.
2. Sort the characters of the word.
3. Convert the sorted characters into a string to create a key.
4. If the key is not present in the dictionary, create an empty list for it.
5. Append the original word to the list corresponding to that key.
6. Return all dictionary values.

### Understanding the Append Operation

For every word, a key is generated independently.

Example:

* eat → key = "aet"
* tea → key = "aet"

When processing "tea", Python checks whether the key "aet" already exists in the dictionary. Since it does, Python appends "tea" to the existing list stored under that key.

This is not based on the position of the word in the input list. It works because words that are anagrams always generate the same key after sorting.

### Pattern Learned

When a problem requires:

* Grouping similar items
* Counting frequencies
* Fast lookups based on a property

A HashMap (Dictionary) is often the right data structure.

For Group Anagrams, the pattern is:

Find a unique signature → Use it as a HashMap key → Group elements under that key.

