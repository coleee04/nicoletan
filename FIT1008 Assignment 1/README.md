# FIT1008 A1 - Card Game Simulation using Custom Data Structures
## Overview
- Developed a Python-based multiplayer card game simulation as part of FIT1008 – Introduction to Computer Science.
- The project focused on applying object-oriented programming, algorithms and abstract data structures under restricted implementation constraints. Python built-in collections such as lists, dictionaries, tuples and sets were not permitted, so the game logic was implemented using the custom data structures provided in the project scaffold.
- The objective of the game is for players to be the first to empty their hand by playing cards that match the current colour or label, while handling special card effects.

## What I Implemented
- Built the core game flow including deck generation, card dealing, player turn progression and winner detection.
- Managed player hands using a sorted abstract data structure and implemented card comparison based on colour and label.
- Implemented draw and discard pile management, including reshuffling discarded cards back into the draw pile when required.
- Implemented gameplay rules for special cards including Skip, Reverse, Draw Two, Crazy and Draw Four.
- Implemented card-drawing and playable-card selection logic based on the current colour and label.
- Analysed and documented the best- and worst-case time complexity of key operations.

## Key Concepts
- Object-Oriented Programming
- Abstract Data Types
- Sorted data structures
- Algorithm design
- Searching and insertion
- Time complexity analysis
- Game-state management

## Technologies
- Python
- Custom data structures provided through the FIT1008 scaffold

## Project Structure
- card.py – represents cards and defines card comparison behaviour
- player.py – manages player information, sorted hands and card selection
- game_board.py – manages the draw pile, discard pile and reshuffling
- game.py – controls game initialisation, turn progression, special-card behaviour and overall game flow

## Academic Context
This project was completed for FIT1008 – Fundamentals of Algorithms at Monash University. The repository contains the files implemented from the provided assignment scaffold.
