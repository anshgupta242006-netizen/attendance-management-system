# AI Attendance Management System

## Project Overview
The AI Attendance Management System is a Python-based project that uses the OpenRouter API to understand natural-language instructions and manage student attendance records.

## Features
- View attendance details for an individual student.
- Display attendance records for all students.
- Calculate individual attendance percentages.
- Calculate the class average attendance.
- Update attendance status for a particular day.
- Remove an attendance record for a specified day.

## Technologies Used
- Python
- OpenRouter API
- JSON for storing attendance data
- Requests library
- Python-dotenv library

## Project Files
- `main.py` – Main program.
- `ai_attendance.py` – Interprets user instructions using an AI model.
- `attendance_tools.py` – Performs attendance-related operations.
- `students.json` – Stores sample student attendance records.
- `test_openrouter.py` – Tests the API connection.
- `test_attendance.py` – Tests attendance calculations.
- `requirements.txt` – Lists Python dependencies.

## Setup Instructions
1. Install Python.
2. Clone or download this repository.
3. Create and activate a Python virtual environment.
4. Install the dependencies using `pip install -r requirements.txt`.
5. Create a `.env` file in the project directory.
6. Add your OpenRouter API key:

   `OPENROUTER_API_KEY=your_api_key_here`

7. Run the program using `python main.py`.

## Security
Never upload your `.env` file or expose your API key publicly. Use fictional sample student data when sharing this project.

## Learning Objective
This project demonstrates API integration, natural-language instruction processing, JSON data handling, and Python-based attendance calculations.
