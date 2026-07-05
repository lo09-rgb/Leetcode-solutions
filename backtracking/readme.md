# Backtracking - String Permutations in Python

## Overview

This project demonstrates the Backtracking algorithm by generating all possible permutations of a given string.

Backtracking is a recursive algorithmic technique used to solve problems by trying different possibilities and undoing choices whenever a path cannot lead to a valid solution.

---

## Problem Statement

Given a string, generate every possible arrangement (permutation) of its characters.

Example:

Input:

ABC

Output:

ABC
ACB
BAC
BCA
CBA
CAB

---

## Algorithm

1. Fix one character.
2. Swap it with every remaining character.
3. Recursively generate permutations for the remaining substring.
4. Backtrack by swapping the characters back.
5. Repeat until every arrangement has been explored.

---

## Time Complexity

O(n × n!)

Reason:
There are n! permutations and each permutation requires O(n) time to print.

---

## Space Complexity

O(n)

The recursion depth reaches at most n.

---

## How Backtracking Works

Suppose the input is:

ABC

Choose A

Generate permutations of BC

ABC

ACB

Backtrack

Choose B

Generate permutations of AC

BAC

BCA

Backtrack

Choose C

Generate permutations of AB

CAB

CBA

Every recursive call restores the original string before trying the next possibility.

---

## Running the Program

Clone the repository:

```bash
git clone https://github.com/yourusername/Backtracking-Permutations.git
```

Navigate into the project:

```bash
cd Backtracking-Permutations
```

Run:

```bash
python permutations.py
```

---

## Sample Run

Input

```
DOG
```

Output

```
DOG
DGO
ODG
OGD
GOD
GDO
```

---

## Learning Objectives

- Understand recursion
- Learn the Backtracking paradigm
- Practice swapping and restoring state
- Analyze recursive tree traversal

---

## Author

Aayushman Baral
