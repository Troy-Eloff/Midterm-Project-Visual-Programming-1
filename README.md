
# Remnant 2 Item Tracker | Python Midterm Project

## Project Overview

This project was created for my Coding 1 midterm assignment. We were given the freedom to design any program we wanted, as long as it demonstrated the Python programming concepts covered in Chapters 1–8 of our textbook.

Since I enjoy playing Remnant 2, I decided to create an item tracker that would help players keep track of the weapons they have collected throughout the game.

The goal was to build a working program while applying the programming skills I had learned during the first half of the semester.

## Project Features

The program focuses on tracking weapons found on Earth in Remnant 2.

### 1. Weapon Tracking
- Organizes weapons into Primary, Secondary, and Melee categories.
- Stores weapon names, collection status, category, and location.
- Allows users to mark weapons as "collected" or "not found."
- Saves updated collection statuses to a text file.

### 2. Item Organization
- Reads weapon information from a text file.
- Parses text into lists and dictionaries.
- Sorts weapons alphabetically.
- Uses dictionaries to organize weapon information.

### 3. Collection Statistics
- Calculates how many weapons have been collected in each category.
- Displays the number of collected weapons compared to the total available.
- Identifies which weapon category contains the most and fewest items.

### 4. Interactive Menu
The program includes a menu that allows users to:

1. Initialize the Earth item list.
2. Display collection progress.
3. Update weapon collection statuses.
4. View weapon category statistics.
5. Exit the program.

### 5. Data Storage
- Uses a text file to store weapon information.
- Organizes records using comma-separated values.
- Saves changes so collection progress can be accessed later.
- Includes error handling for missing files and invalid user inputs.

## Python Concepts Demonstrated

This project allowed me to apply several concepts covered throughout Chapters 1–8 of my introductory programming course.

- **Functions:** Dividing the program into smaller sections that handle specific tasks.
- **Loops:** Repeating the menu and processing weapon collections.
- **Conditional Statements:** Responding to menu selections and weapon statuses.
- **Lists:** Organizing weapon names and collection information.
- **Dictionaries:** Storing weapon details using keys and values.
- **File Handling:** Reading, writing, and updating saved data.
- **String Parsing:** Separating text file records into individual values.
- **Sorting:** Organizing weapons alphabetically.
- **Exception Handling:** Managing invalid inputs and missing files.
- **Basic Calculations:** Calculating collection totals and comparing categories.
- **Tkinter:** Creating a basic graphical window alongside the terminal menu.

## Technologies Used

- Python 3
- Tkinter
- Text Files
- Python Standard Library

## Project Planning and Pseudocode

Before writing the program, I used handwritten notes and pseudocode to plan how I wanted everything to work.

These drafts helped me organize the different functions, figure out how information would move through the program, and decide how to store and update weapon data.

I included my original planning notes in this repository to show the process I followed while developing the project.

## How to Run the Project

1. Download or clone this repository.
2. Make sure Python 3 is installed with Tkinter support.
3. Open the project folder in your preferred Python environment.
4. Run the main Python file:

```bash
python "exam 2.py"
```

5. Follow the terminal menu to interact with the item tracker.

**Note:** The program creates or updates `earth items.txt` to store collection progress. Initializing the item list will reset previously saved statuses.

## What I Learned

This was one of my first opportunities to create a Python program based on my own idea instead of following a specific assignment example.

I started by writing out my ideas on paper and using pseudocode to plan how the program should work. From there, I broke the project into smaller functions and worked on getting each part to communicate with the others.

One of the bigger challenges was figuring out how to organize the weapon information and allow users to update their collection progress without losing their saved data.

I also gained more experience troubleshooting errors, working with dictionaries, and reading and writing information to files.

Overall, this project helped me better understand how different Python concepts can come together to create a functional application.

## Project Limitations

This was an introductory programming project, so the program has a few limitations.

- The tracker currently focuses on weapons associated with Earth.
- The main interface runs through the terminal, with a basic Tkinter window for displaying messages.
- The program uses a local text file rather than a database.
- The item list is manually maintained rather than automatically updated from the game.

These are areas I could expand on as I continue developing my programming skills.

## Project Background

This project was completed as my Coding 1 midterm assignment. The assignment required us to demonstrate programming concepts from Chapters 1–8 of our textbook while allowing us to choose our own project idea.

I decided to build a Remnant 2 item tracker because it gave me the opportunity to combine my interest in gaming with what I was learning about Python programming.
