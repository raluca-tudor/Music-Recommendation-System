# Music Recommendation System
Rule-Based Music Recommendation System developed in Python.

# Project Overview
This application recommends songs according to user preferences by applying a set of logical rules over a music collection that contains 100 various songs. Instead of using Machine Learning, the recommendation process is entirely knowledge-based, making use of explicit decision rules defined by the developer.
The user can search for songs using multiple criteria such as music genre, duration, target audience and emotional mood.

# Objectives
- Develop a knowledge-based recommendation system.
- Implement a rule engine for music selection.
- Model songs using objected-oriented programming.
- Allow flexible filtering based on multiple user preferences.
- Demonstrate the principles of Expert Systems and Artificial Intelligence.


# Technologies
- Python
- Object-Oriented Programming (OOP)
- Rule-Based Systems
- Artificial Intelligence Fundamentals

# Features
- Music recommendation based on logical rules
- Object-oriented song representation
- Multi-criteria filtering
- Flexible user input
- Automatic recommendation generation
- Music classification by duration
- Target audience filtering
- Mood_based recommendation
- Language filtering
- Genre filtering


# Recommendation Criteria
The recommendation engine evaluates songs according to:
- Music genre
- Song duration
- Language
- Target audience
- Emotional mood
Users may specify one, several or all criteria simultaneously.


# Rule Engine
The recommendation system applies logical IF conditions to determine whether a song satisfies the user's preferences.
Example logic:
IF
- genre matches
- duration matches
- language matches
- audience matches
- mood matches
THEN
Recommend the song.
The implementation also supports optional criteria, allowing users to leave fileds empty if they are not relevant for the current search.


# Song Model
Each song contains information such as:
- Title
- Artist
- Genre
- Duration
- Language
- Target audience
- Emotional mood
Songs are represented through a dedicated Python class following object-oriented principles.


# Project Structure
- proiectReguli.py
- images/
  - KidsMusic_English.png
  - MelancholicMusic.png
  - Music_Spanish.png
  - PopDanceMusic.png
  - PopMusic_Romanian.png
  - RapMusic_English.png
  - RockMusic.png
 
# How to Run
1. Install Python 3.
2. Clone the repository.
3. Run:
   'bash
   python proiectReguli.py'
4. Enter the desired preferences:
   - Genre
   - Duration
   - Language
   - Target audience
   - Mood
5. The application displays all matching songs.


# Concepts Used
- Rule-Based Systems
- Expert Systems
- Artificial Intelligence Fundamentals
- OOP
- Python Classes
- Conditional logic
- Data filtering

# Academic Context
Developed as a univeristy project for a Knowledge-Bases course (studying AI) , rule-based reasoning and object-oriented programming.


# Author
Raluca-Ana-Maria Tudor

University of Craiova

2026
  


