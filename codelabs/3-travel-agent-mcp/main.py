import os
import google.generativeai as genai
import database

# Configure API Key
if "GOOGLE_API_KEY" not in os.environ:
    print("Please set the GOOGLE_API_KEY environment variable.")
    exit(1)

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Initialize DB
database.setup_database()

def create_travel_agent():
    # Register the search_hotels function as a tool
    tools = [database.search_hotels]
    
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        tools=tools,
        system_instruction="""
        You are a helpful Travel Agent. 
        Use the `search_hotels` tool to find hotel information for users.
        Always present the results in a friendly and readable way.
        If no hotels are found, apologize and suggest alternative parameters.
        """
    )
    return model

def main():
    print("Welcome to the MCP Travel Agent")
    print("Ask me about hotels in Paris, Tokyo, New York, etc.")
    print("--------------------------------------------------")

    model = create_travel_agent()
    chat = model.start_chat(enable_automatic_function_calling=True)

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['exit', 'quit']:
            break
            
        try:
            response = chat.send_message(user_input)
            print(f"Agent: {response.text}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

