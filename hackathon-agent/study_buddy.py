import os
import json
import google.generativeai as genai

# Configure API Key
if "GOOGLE_API_KEY" not in os.environ:
    print("Please set the GOOGLE_API_KEY environment variable.")
    exit(1)

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

class StudyBuddy:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        self.chat = self.model.start_chat(history=[])

    def start_session(self):
        print("\n🎓 Welcome to your AI Study Buddy! 🎓")
        print("Tell me a topic you want to learn about (e.g., 'Photosynthesis', 'Quantum Physics', 'French Revolution').")
        
        topic = input("\nTopic: ")
        self.teach_topic(topic)

    def teach_topic(self, topic):
        print(f"\nGenerating summary for '{topic}'... Please wait.\n")
        
        # 1. Get Summary
        prompt_summary = f"Provide a clear, concise, and engaging summary of '{topic}' suitable for a student. Keep it under 200 words."
        response = self.chat.send_message(prompt_summary)
        print("--- 📖 Summary ---")
        print(response.text)
        print("------------------\n")
        
        input("Press Enter when you are ready for a quick quiz...")
        self.run_quiz(topic)

    def run_quiz(self, topic):
        print(f"\nGenerating quiz for '{topic}'...\n")
        
        # 2. Get Quiz (Structured JSON)
        quiz_prompt = f"""
        Create a 3-question multiple-choice quiz about '{topic}' based on the summary provided earlier.
        Return ONLY a valid JSON array of objects. Do not use Markdown code blocks.
        Each object should have:
        - "question": string
        - "options": array of 4 strings (A, B, C, D)
        - "answer": string (the correct option letter, e.g., "A")
        - "explanation": string (why it is correct)
        """
        
        try:
            response = self.chat.send_message(quiz_prompt)
            # Clean up potential markdown formatting
            text = response.text.replace("```json", "").replace("```", "").strip()
            quiz_data = json.loads(text)
        except Exception as e:
            print("Error generating quiz. Please try again.")
            print(f"Debug info: {e}")
            return

        score = 0
        for i, q in enumerate(quiz_data):
            print(f"\nQuestion {i+1}: {q['question']}")
            for opt in q['options']:
                print(opt)
            
            user_ans = input("\nYour Answer (A/B/C/D): ").strip().upper()
            
            if user_ans == q['answer']:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Incorrect. The correct answer was {q['answer']}.")
            
            print(f"Explanation: {q['explanation']}")
            
        print(f"\n--- 🏁 Quiz Completed! Score: {score}/{len(quiz_data)} ---")
        if score == len(quiz_data):
            print("Excellent work! You mastered this topic.")
        elif score >= 1:
            print("Good effort! Review the summary and try again.")
        else:
            print("Don't worry, learning takes time. Read the summary again!")

if __name__ == "__main__":
    buddy = StudyBuddy()
    buddy.start_session()

