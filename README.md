# CompetitiePlanner
Competitie planner voor badminton

## App usage
The app uses [Streamlit](https://streamlit.io/) to run a web application. The app can be run locally and in a cloud environment. To run locally use the following commands:
```bash
streamlit run .\main.py
```

## Requirements
To use the environment, the `requirements.txt` file can be used to install the dependencies needed. Install the requirements using pip:
```bash
pip install -r ".\requirements.txt"
```

## Release Notes

### v1.2.0
- Competition selection page added. Makes it possible to select different competitions.
- Dynamically load the competitions based on the selected competitions.
- Display selected competitions.
- When there are duplicated teams, combine them instead of creating a new object.
- Add functions to add multiple teams/players instead of only one.

### v1.1.1
- Fix JSONHandler import references to also call directory.

### v1.1.0
- JSONHandler accepts a file name and directory in separate parameters.
- JSONHandler checks if directory exists before creating/reading file.

### v1.0.1
- Add some debugging info
- Fix issue where index out of range if time did not exist in match.

### v1.0.0
- Basic functionality for planning badminton competitions added
- Support for teams, matches, and schedules for both youth and senior teams
