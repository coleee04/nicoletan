# FIT1008 A2 - Football Season Management using Hash Tables & Custom Data Structures

## Overview

Developed components of a Python-based football season management system as part of **FIT1008 – Introduction to Computer Science**.

The project focused on applying data structures and algorithmic techniques to manage players, teams, match results, season standings and date-based information. A major component involved implementing custom hash-table behaviour, including **double hashing, collision resolution, lazy deletion and dynamic rehashing**.

## What I Implemented

* Implemented a custom **double-hashing hash table** with probing for collision resolution.
* Added **lazy deletion**, allowing deleted hash-table positions to be reused while preserving valid probe sequences.
* Implemented automatic **rehashing and table resizing** as the hash table grows.
* Designed a second hash function and ensured valid probing step sizes for the table.
* Developed a specialised **date hashing function** supporting multiple date formats and accounting for leap years.
* Managed football players and their statistics, including stat retrieval, updates, resetting and age calculation.
* Organised team players by playing position and implemented player addition, removal and retrieval.
* Maintained bounded team match histories and updated team points based on game results.
* Implemented team post storage using date-based key-value records.
* Processed simulated season results to update team outcomes, player goals and an ordered league leaderboard.
* Implemented functionality for rescheduling an existing week of games.
* Analysed and documented the best- and worst-case time complexity of key operations.

## Key Concepts

* Hash Tables
* Double Hashing
* Collision Resolution
* Lazy Deletion
* Dynamic Rehashing
* Hash Function Design
* Abstract Data Types
* Object-Oriented Programming
* Algorithmic Complexity
* Searching and Data Management

## Technologies

* Python
* Custom data structures supplied through the FIT1008 scaffold

## Project Structure

* `lazy_double_table.py` – implements a hash table using double hashing, lazy deletion and resizing
* `hashy_date_table.py` – implements a specialised hash function for date-formatted string keys
* `player.py` – manages player information and statistics
* `team.py` – manages players, team results, points, match history and posts
* `season.py` – processes season results, maintains the leaderboard and supports schedule changes

## Academic Context

This project was completed for **FIT1008 – Fundamentals of Algorithms** at Monash University. The repository contains the files I implemented from the provided assignment scaffold.
