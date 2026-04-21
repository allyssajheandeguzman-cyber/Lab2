# Lab Activity 2: Strings, Lists, Tuples, and Dictionaries
**Student Name:** Allyssa Jhean F. De Guzman
**Professor:** Dr. John De Guzman Tarampi

# Description 
This laboratory activity focuses on developing a menu-driven Python program to manage a structured hardware inventory system. The program demonstrates the practical application of core Python data types:
- **Strings:** Used for user input (item names, tags) and formatted data display.
- **Lists:** Used as the primary "database" to store multiple inventory records, as well as to hold the dynamic tags for each item.
- **Tuples:** Used for immutable data, specifically representing fixed warehouse locations (e.g., Aisle and Rack).
- **Dictionaries:** Used to structure individual hardware profiles, grouping the name, quantity, location, and tags together.

# Program Features (CRUD Operations)
- **Create:** Allows the user to input new hardware items, including stock quantity and initial tags.
- **Read/Display:** Lists all hardware components currently stored in the system, utilizing index-based numbering.
- **Update:** Specifically allows appending new descriptive tags to an existing item's record.

# Project Structure

- src/: Contains main.py (the menu-driven inventory logic).
- tests/: Contains screenshots of the required test runs (Create, Read, Update).
- README.md: Documentation and execution instructions

# How to Run the Activity

This activity was developed and tested using OneCompiler.
1. Copy the code from src/main.py.
2. In OneCompiler, you must use the STDIN box to provide inputs before clicking 'Run'.
    Example STDIN input:
    1 (to Create Item)
    RTX 4090 Graphics Card (Name)
    15 (Quantity)
    gpu, component (Tags)
    2 (to Display)
    4 (to Exit)
3. View the output in the console to verify the CRUD operations.
# Test Case Summary
**Test 1:** Successful creation of a single hardware inventory record.
**Test 2:** Displaying multiple hardware records to verify list storage and loop formatting.
**Test 3:** Updating an existing item's tags to verify dictionary and nested list modification.
