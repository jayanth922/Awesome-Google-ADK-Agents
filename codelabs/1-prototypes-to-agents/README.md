# From Prototypes to Agents with ADK

## Overview
This project implements the "From Prototypes to Agents with ADK" codelab. The goal is to build an AI agent that generates a renovation proposal document based on user input.

## Description
The agent takes a user's renovation request (e.g., "I want to renovate my kitchen with a modern Italian style") and generates a structured proposal including:
- Design Concept
- Material Suggestions
- Estimated Budget Range
- Timeline

## Prerequisites
- Python 3.9+
- Google Cloud Project with Vertex AI API enabled (or Google AI Studio API Key)
- `google-generativeai` library

## Setup
1. **Clone the repository** (if applicable) or navigate to this directory.
2. **Install dependencies**:
   ```bash
   pip install google-generativeai
   ```
3. **Set your API Key**:
   ```bash
   export GOOGLE_API_KEY="your_api_key_here"
   ```

## Usage
Run the agent:
```bash
python main.py
```

## Code Walkthrough
The `main.py` file initializes the Gemini model with a specific system instruction to act as a Renovation Expert. It then takes user input and generates a formatted proposal.

## Video Walkthrough
[Link to YouTube Video - To be added by user]

