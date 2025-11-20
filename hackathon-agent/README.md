# Study Buddy Agent (Hackathon Project)

## Overview
This project is an implementation of a "Study Buddy" agent, inspired by the "Awesome ADK Agents" hackathon projects. It helps users learn new topics by providing summaries and interactive quizzes.

## Features
- **Topic Summarization**: Explains complex topics in simple terms.
- **Interactive Quiz**: Generates a 3-question multiple-choice quiz based on the topic.
- **Real-time Feedback**: Evaluates user answers and provides explanations.

## Prerequisites
- Python 3.9+
- Google API Key

## Setup
1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Set your API Key**:
   ```bash
   export GOOGLE_API_KEY="your_api_key_here"
   ```

## Usage
Run the agent:
```bash
python study_buddy.py
```

## Code Walkthrough
- The `StudyBuddy` class manages the conversation state.
- It uses structured prompting to ask Gemini to return valid JSON for the quiz questions, ensuring reliable parsing.
- The interaction loop handles the user's answers and scores them.

## Video Walkthrough
[Link to YouTube Video - To be added by user]

