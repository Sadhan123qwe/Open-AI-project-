from dotenv import load_dotenv 
import cohere 
import os 

load_dotenv()
api_key = os.getenv('COHERE_API_KEY')
co = cohere.Client(api_key)

def get_budget_insights(user_query, transactions_text):
    prompt = f""" =User query: {user_query}\nTransactions list: {transactions_text}\n 
    You are SynBot, a financial AI assistant developed by Sakshi & Shahn for the Syntego Finance Tracker and Respond to 
    Your job is **ONLY** to assist users with their ***financial queries**, including budgeting, expense tracking, and said
    "I can only assist with financial-related questions. Please ask me something about your finances."
    If user asks about making changes his expenses or incoe to delete or add , simply respond:""I can assist you with my chatBot"" 
    If the user asks about **yourself**, simply respond:
    "I am SynBot, a financial assistant built by Sakshi & Shanu to help with budgeting and expense management."""

    response = co.generate(
        model = 'command-xlarge-nightly',
        prompt=prompt,
        max_tokens=100
    )

    # Return the responsefrom Cohere API 
    return response.generations[0].text.strip()

