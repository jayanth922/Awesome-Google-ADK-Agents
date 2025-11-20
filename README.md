# Google ADK - AI Agent Development Kit Projects

A comprehensive collection of projects demonstrating the Google Agent Development Kit (ADK) capabilities, featuring progressive codelabs and a hackathon project showcasing AI agent development with Google's Gemini models.

Youtube Demo's for codelabs and hackathon project : 
  - codelab 1 - from prototypes to agents - Renovation Proposal Agent - https://youtu.be/--WdzacZe1U
  - codelab 2 - empowering with tools - Currency Converter Agent - https://youtu.be/3xDdbiAgk-E
  - codelab 3 - travel agent with MCP (Model Context Protocol) - Travel Agent - https://youtu.be/tUrjq-Spu_k
  - Hackathon Project - Study Buddy Agent - https://youtu.be/E1uMaCztQY4

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Projects](#projects)
  - [Codelab 1: From Prototypes to Agents](#codelab-1-from-prototypes-to-agents)
  - [Codelab 2: Empowering with Tools](#codelab-2-empowering-with-tools)
  - [Codelab 3: Travel Agent with MCP](#codelab-3-travel-agent-with-mcp)
  - [Hackathon: Study Buddy Agent](#hackathon-study-buddy-agent)
- [Getting Started](#getting-started)
- [API Key Setup](#api-key-setup)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This repository contains a series of educational projects that progressively build your understanding of AI agent development using Google's Generative AI SDK. Each project demonstrates different aspects of building intelligent agents, from basic prototypes to tool-integrated systems.

### Key Technologies

- **Google Generative AI SDK** (`google-generativeai`)
- **Gemini 2.0 Flash** model
- **Python 3.9+**
- **SQLite** (for database examples)
- **Function Calling / Tools** (for agent capabilities)

## 📁 Project Structure

```
google-adk/
├── codelabs/
│   ├── 1-prototypes-to-agents/     # Basic agent with system instructions
│   ├── 2-empowering-with-tools/    # Agent with function calling
│   └── 3-travel-agent-mcp/         # Agent with database integration
├── hackathon-agent/                 # Study Buddy - Interactive learning agent
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

## 🔧 Prerequisites

Before you begin, ensure you have:

- **Python 3.9 or higher** installed
- A **Google API Key** from [Google AI Studio](https://makersuite.google.com/app/apikey)
- Basic knowledge of Python programming
- Familiarity with command-line interface

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/google-adk.git
   cd google-adk
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**:
   ```bash
   export GOOGLE_API_KEY="your_api_key_here"
   ```
   
   Or on Windows:
   ```cmd
   set GOOGLE_API_KEY=your_api_key_here
   ```

## 🚀 Projects

### Codelab 1: From Prototypes to Agents

**Location**: `codelabs/1-prototypes-to-agents/`

**Description**: Learn how to transform a simple prototype into a functional AI agent. This project demonstrates how to use system instructions to create a specialized agent that generates professional renovation proposals.

**Features**:
- System instruction configuration
- Structured output generation
- Document creation (saves proposals to file)

**Run it**:
```bash
cd codelabs/1-prototypes-to-agents
python main.py
```

**Example Input**: "Kitchen renovation, modern Italian style, budget $25,000"

**Output**: A structured renovation proposal with design concepts, materials, budget, and timeline.

---

### Codelab 2: Empowering with Tools

**Location**: `codelabs/2-empowering-with-tools/`

**Description**: Enhance your agent by integrating external tools through function calling. This project shows how to give your agent the ability to perform calculations and access external data.

**Features**:
- Function calling / tool integration
- Automatic function execution
- Multi-turn conversations with tool usage

**Run it**:
```bash
cd codelabs/2-empowering-with-tools
python main.py
```

**Example Queries**:
- "Convert 100 USD to EUR"
- "What is 5000 JPY in USD?"

**Key Learning**: How to define Python functions as tools and let the model decide when to use them.

---

### Codelab 3: Travel Agent with MCP

**Location**: `codelabs/3-travel-agent-mcp/`

**Description**: Build a travel agent that can query a database to answer user questions. This demonstrates the Model Context Protocol (MCP) pattern, where agents access structured data sources.

**Features**:
- SQLite database integration
- Natural language to SQL query conversion
- Hotel search with filtering (location, price, amenities)

**Run it**:
```bash
cd codelabs/3-travel-agent-mcp
python main.py
```

**Example Queries**:
- "Find me a hotel in Paris under $200"
- "What hotels do you have in Tokyo with a pool?"
- "Is there a luxury hotel in New York?"

**Database**: Automatically creates `hotels.db` on first run with sample data.

---

### Hackathon: Study Buddy Agent

**Location**: `hackathon-agent/`

**Description**: An interactive learning companion that helps students master new topics through summarization and quizzes. This project showcases a complete agent application with structured JSON output and user interaction.

**Features**:
- Topic summarization (under 200 words)
- Interactive multiple-choice quizzes
- Real-time feedback and scoring
- Structured JSON parsing from model responses

**Run it**:
```bash
cd hackathon-agent
python study_buddy.py
```

**Example Topics**:
- "Photosynthesis"
- "Quantum Physics"
- "French Revolution"

**Workflow**:
1. User provides a topic
2. Agent generates a concise summary
3. Agent creates a 3-question quiz
4. User answers questions
5. Agent provides feedback and explanations

---

## 🏁 Getting Started

### Quick Start Guide

1. **Set up your environment**:
   ```bash
   # Install dependencies
   pip install -r requirements.txt
   
   # Set API key
   export GOOGLE_API_KEY="your_key_here"
   ```

2. **Try the first codelab**:
   ```bash
   cd codelabs/1-prototypes-to-agents
   python main.py
   ```

3. **Progress through the codelabs** in order to build your understanding progressively.

4. **Explore the hackathon project** to see a complete application.

## 🔑 API Key Setup

### Getting Your API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your API key

### Setting the API Key

**Linux/macOS**:
```bash
export GOOGLE_API_KEY="your_api_key_here"
```

**Windows (Command Prompt)**:
```cmd
set GOOGLE_API_KEY=your_api_key_here
```

**Windows (PowerShell)**:
```powershell
$env:GOOGLE_API_KEY="your_api_key_here"
```

**Permanent Setup (Linux/macOS)**:
Add to your `~/.bashrc` or `~/.zshrc`:
```bash
export GOOGLE_API_KEY="your_api_key_here"
```

**Permanent Setup (Windows)**:
Add as a system environment variable through System Properties.

## 📚 Learning Path

We recommend following this order:

1. **Start with Codelab 1** - Understand basic agent setup and system instructions
2. **Move to Codelab 2** - Learn about tool integration and function calling
3. **Advance to Codelab 3** - See how agents interact with databases
4. **Explore the Hackathon Project** - Study a complete application with user interaction

## 🛠️ Development

### Project Dependencies

All projects use the `google-generativeai` library. See `requirements.txt` for the complete list.

### Code Style

- Follow PEP 8 Python style guidelines
- Use descriptive variable names
- Include docstrings for functions
- Add comments for complex logic

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Google AI Studio for providing the Gemini API
- The Google ADK team for excellent documentation and examples
- The open-source community for inspiration and feedback

## 📞 Support

If you encounter any issues or have questions:

1. Check the individual project READMEs in each directory
2. Review the [Google Generative AI documentation](https://ai.google.dev/docs)
3. Open an issue on GitHub

## 🔗 Useful Links

- [Google AI Studio](https://makersuite.google.com/)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [Python SDK Reference](https://ai.google.dev/api/python)
- [Function Calling Guide](https://ai.google.dev/docs/function_calling)

---

**Happy Coding! 🚀**

