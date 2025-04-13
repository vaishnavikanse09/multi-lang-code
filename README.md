# Hypothesis Generator Chatbot

A Flask-based web application that uses Google's Gemini AI to generate detailed hypotheses for research topics. This tool is designed to help students create well-structured hypotheses for their academic work.

## Features

- Modern and user-friendly interface
- Detailed hypothesis generation including:
  - Main hypothesis statement
  - Supporting sub-hypotheses
  - Key variables
  - Research methods
  - Expected outcomes
  - Limitations

## Setup Instructions

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Replace the API key in `app.py`:
   - Open `app.py`
   - Replace `"YOUR_API_KEY_HERE"` with your actual Gemini API key

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## Usage

1. Enter your research topic in the input field
2. Click the "Generate Hypothesis" button
3. Wait for the AI to generate a detailed hypothesis
4. Review the generated hypothesis and use it for your research

## Note

Make sure you have a valid Gemini API key from Google AI Studio. The application will not work without a valid API key. 
