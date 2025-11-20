import os
import google.generativeai as genai

# Configure API Key
if "GOOGLE_API_KEY" not in os.environ:
    print("Please set the GOOGLE_API_KEY environment variable.")
    exit(1)

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# --- 1. Define the Tool ---

def convert_currency(amount: float, currency_from: str, currency_to: str) -> dict:
    """
    Converts an amount from one currency to another.
    
    Args:
        amount: The amount to convert (e.g., 100.0).
        currency_from: The source currency code (e.g., 'USD').
        currency_to: The target currency code (e.g., 'EUR').
    
    Returns:
        A dictionary with the converted amount, rate, and details.
    """
    # Mock data for demonstration
    rates = {
        "USD": {"EUR": 0.92, "GBP": 0.78, "JPY": 150.0},
        "EUR": {"USD": 1.09, "GBP": 0.85, "JPY": 163.0},
        "GBP": {"USD": 1.28, "EUR": 1.18, "JPY": 192.0},
        "JPY": {"USD": 0.0067, "EUR": 0.0061, "GBP": 0.0052},
    }
    
    # Normalize inputs
    c_from = currency_from.upper()
    c_to = currency_to.upper()
    
    if c_from == c_to:
        return {
            "original_amount": amount,
            "original_currency": c_from,
            "converted_amount": amount,
            "target_currency": c_to,
            "exchange_rate": 1.0
        }
        
    if c_from in rates and c_to in rates[c_from]:
        rate = rates[c_from][c_to]
        converted = amount * rate
        return {
            "original_amount": amount,
            "original_currency": c_from,
            "converted_amount": round(converted, 2),
            "target_currency": c_to,
            "exchange_rate": rate
        }
    
    return {
        "error": f"Exchange rate not available for {c_from} to {c_to}",
        "original_amount": amount,
        "original_currency": c_from,
        "target_currency": c_to
    }

# --- 2. Initialize Model with Tools ---

def create_tool_agent():
    # Create the tool dictionary/list for Gemini
    tools = [convert_currency]
    
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        tools=tools,
        system_instruction="You are a helpful assistant with access to currency conversion tools. When users ask to convert amounts, use the convert_currency function to calculate the converted amount. Always provide the final converted amount clearly in your response."
    )
    return model

# --- 3. Chat Loop ---

def main():
    print("Welcome to the Tool-Empowered Agent")
    print("Try asking: 'Convert 100 USD to EUR' or 'What is 5000 JPY in USD?'")
    print("The agent will calculate the final converted amount for you!")
    print("---------------------------------------------------------------")

    model = create_tool_agent()
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

