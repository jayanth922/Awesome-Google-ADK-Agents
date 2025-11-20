import os
import google.generativeai as genai

# Configure the API key
# Ensure you have the GOOGLE_API_KEY environment variable set
if "GOOGLE_API_KEY" not in os.environ:
    print("Please set the GOOGLE_API_KEY environment variable.")
    exit(1)

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def create_renovation_agent():
    """
    Creates a Renovation Proposal Agent using Gemini.
    """
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        system_instruction="""
        You are an expert Renovation Consultant. 
        Your goal is to generate professional renovation proposals based on client needs.
        The proposal should include:
        1. Design Concept (Creative and aligned with style)
        2. Material Suggestions (Specific and durable)
        3. Estimated Budget Range (Realistic estimates)
        4. Timeline (Phased approach)
        
        Format the output as a clean, structured text document.
        """
    )
    return model

def generate_proposal(agent, request):
    """
    Generates a proposal based on the user request.
    """
    print(f"Generating proposal for: {request}...\n")
    response = agent.generate_content(request)
    return response.text

def main():
    print("Welcome to the Renovation Agent (ADK Demo)")
    print("-----------------------------------------")
    
    request = input("Describe your renovation project (e.g., 'Kitchen renovation, modern style, $20k budget'): ")
    
    if not request:
        request = "Kitchen renovation, modern Italian style, budget $25,000"
        print(f"No input provided. Using default: {request}")

    agent = create_renovation_agent()
    proposal = generate_proposal(agent, request)
    
    print("\n--- Renovation Proposal ---\n")
    print(proposal)
    print("\n---------------------------\n")

    # Save to file (simulating document generation)
    with open("renovation_proposal.txt", "w") as f:
        f.write(proposal)
    print("Proposal saved to 'renovation_proposal.txt'")

if __name__ == "__main__":
    main()

