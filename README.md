# Phishing-Attack-Scenario-Generator

Overview

The Phishing Attack Scenario Generator is a web application designed to generate realistic phishing scenarios using a GPT-2 language model. It serves as a training tool for awareness against phishing threats.

Features

API Endpoint: Generate phishing scenarios based on user-defined prompts.

GPT-2 Integration: Utilizes a pre-trained GPT-2 model for text generation.

CORS Support: Allows interaction with frontend applications.

Logging: Captures generated scenarios for auditing and debugging.

Prompt Testing: Automated testing of various prompts to ensure appropriate outputs.

Technologies Used

Flask: Web framework for building the API.

Hugging Face Transformers: For the GPT-2 language model.

Python: Programming language for the application.

Logging: Python’s logging module for tracking generated scenarios.

Getting Started

Prerequisites
Python 3.x
Virtual environment (recommended)

Installation

Create a virtual environment:

python -m venv .venv

Activate the virtual environment:

.venv\Scripts\activate

Install the required packages:

pip install -r requirements.txt

Running the Application

Start the Flask server: python app.py

Access the API at http://127.0.0.1:5000/generate_scenario?prompt=<your_prompt>.

Testing

To test the prompt generation, run: python test_prompts.py

Feel free to customize the README according to your preferences and project details!
