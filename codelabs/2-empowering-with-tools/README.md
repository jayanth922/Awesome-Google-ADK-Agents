# Building AI Agents with ADK: Empowering with Tools

## Overview
This project demonstrates how to enhance an AI agent by integrating tools (Function Calling). This corresponds to the "Empowering with Tools" codelab.

## Description
The agent is capable of performing tasks that require external data or computation. In this example, we integrate a **Currency Converter** tool. The agent can answer questions like "How much is 100 USD in EUR?" by calling the defined function.

## Prerequisites
- Python 3.9+
- Google API Key

## Setup
1. **Install dependencies**:
   ```bash
   pip install google-generativeai
   ```
2. **Set your API Key**:
   ```bash
   export GOOGLE_API_KEY="your_api_key_here"
   ```

## Usage
Run the agent:
```bash
python main.py
```

## Code Walkthrough
- **Tools Definition**: We define a Python function `get_exchange_rate` that acts as a mock currency API.
- **Tool Registration**: We pass this function to the `tools` parameter of the Gemini model.
- **Automatic Execution**: The model decides when to call the tool, and the script executes it and passes the result back to the model for the final answer.

## Video Walkthrough
[Link to YouTube Video - To be added by user]

