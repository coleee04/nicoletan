# FIT1008 A3 - Mining Simulation using Binary Search Trees & Graph Traversal

## Overview

Developed components of a Python-based Minecraft-inspired mining simulation as part of FIT1008 – Fundamentals of Algorithms.

The project focused on applying tree-based data structures, graph traversal and algorithmic decision-making to explore a cave system and select valuable blocks for mining. Blocks were evaluated using their **item value relative to mining time (hardness)**, allowing different mining strategies to be implemented.

## What I Implemented

* Implemented a **balanced Binary Search Tree (BST)** by sorting key–item pairs using merge sort and recursively inserting middle elements.
* Added BST filtering functionality to retrieve elements whose keys satisfy multiple criteria.
* Built a mining checklist backed by the balanced BST, using each block's **value-to-hardness ratio** as part of its key.
* Implemented checklist operations for adding, removing, searching and retrieving blocks in sorted order.
* Implemented **Depth-First Search (DFS)** using an explicit stack to explore interconnected caves and collect available blocks.
* Developed objective-based mining logic that filters blocks according to value-to-hardness thresholds and mines eligible blocks in priority order.
* Implemented a time-constrained mining strategy that repeatedly selects the highest-value-per-mining-time block that can still be mined within the remaining time.
* Managed miner inventory, including collecting mined items and clearing inventory.
* Analysed and documented the best- and worst-case time complexity of key algorithms and data-structure operations.

## Key Concepts

* Binary Search Trees
* Balanced BST Construction
* Depth-First Search
* Stack-Based Graph Traversal
* Merge Sort
* Filtering and Searching
* Greedy Selection
* Abstract Data Types
* Object-Oriented Programming
* Algorithmic Complexity

## Technologies

* Python
* Custom data structures and algorithms supplied through the FIT1008 scaffold

## Project Structure

* `betterbst.py` – constructs and filters a balanced Binary Search Tree
* `minecraft_checklist.py` – manages mineable blocks using the BST and value-to-hardness ratios
* `not_minecraft.py` – controls cave exploration and objective/time-constrained mining strategies
* `miner.py` – manages the miner and collected inventory
* `minecraft_block.py` – represents mineable blocks and their associated items

## Academic Context

This project was completed for **FIT1008 – Fundamentals of Algorithms** at Monash University. The repository contains the files I implemented from the provided assignment scaffold.
