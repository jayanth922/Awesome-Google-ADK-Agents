# Build a Travel Agent using MCP Toolbox for Databases and ADK

## Overview
This project implements a Travel Agent that uses a database to answer user queries. It simulates the "Model Context Protocol" (MCP) pattern where the model is given tools to access structured data (a Hotel Database).

## Description
The agent can answer questions like:
- "Find me a hotel in Paris under $200."
- "What hotels do you have in Tokyo with a pool?"
- "Is there a luxury hotel in New York?"

It uses a local SQLite database (`hotels.db`) populated with sample data.

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
On the first run, it will automatically create and populate the `hotels.db` file.

## Code Walkthrough
- **Database Simulation**: `database.py` handles the SQLite connection and provides a `search_hotels` function.
- **MCP Pattern**: The `search_hotels` function is exposed as a tool to the Gemini model. The model converts natural language queries into function arguments (location, price range, amenities), retrieves the data, and generates a natural language response.

## Video Walkthrough
[Link to YouTube Video - To be added by user]

