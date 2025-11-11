# AI Engineer Skill Matcher

A modern Flask web application for matching user skills to AI Engineer requirements and displaying a match score.

## Features

- User submits their name, email, and skills
- Backend compares submitted skills against a set of AI engineering requirements (TensorFlow, Keras, PyTorch, LLM, RAG, scikit-learn)
- Displays a visually appealing results card with match score
- Clean, centered, and responsive UI with a green-themed color palette

## File Structure

| File         | Description                                |
|--------------|--------------------------------------------|
| main.py      | Main Flask app and logic                   |
| base.html    | Base site layout template                  |
| form.html    | Skill submission form template             |
| result.html  | Results display template                   |
| base.css     | Core styles and layout                     |
| form.css     | Form-specific styles                       |
| result.css   | Result card and page styles                |

## Requirements

- Python 3.7 or newer
- Flask

Install dependencies:
```bash
pip install Flask
```

## Running the App

1. Clone or download the project files.
2. In your terminal, run:
```bash
puthon main.py
```
3. Open your browser and visit `http://127.0.0.1:5000`.

