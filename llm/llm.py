import os
from dotenv import load_dotenv
from together import Together
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

client = Together(api_key=os.getenv("TOGETHER_API_KEY"))

def generate_actionables(insights_data):
    """Summarize and extract actionables from insights."""
    
    # Get the current date
    current_date = datetime.now().strftime("%Y-%m-%d")
    
# Structured prompt for generating actionables

    prompt = f"""
    📅 *Date:* {current_date}

    Here are key insights extracted from business data:
    {insights_data}

    ### **Your task:**
    - Summarize the key insights  
    - Provide **3-5 actionable recommendations**  
    - Identify **any risks or opportunities**  
    - Format output for Slack readability  

    ### **Format:**  
    📢 *Daily Insights from @StartupAnalyst*  
    📅 *Date:* YYYY-MM-DD (time in 12 hr formst)

    ------  

    🔍 **Summary:**  
    *1*. [Brief description]  
    *2*. [Brief description]  
    *3*. [Brief description]  

    ------  

    ✅ **Actionables:**  
    *1*. [Brief description]  
    *2*. [Brief description]  
    *3*. [Brief description]  

    ------  

    ⚠️ **Risks:**  
    *1*. [Brief description]  
    *2*. [Brief description] 

    💡 **Opportunities:**  
    *1*. [Brief description]  
    *2*. [Brief description]  
    *3*. [Brief description]  

    ------  

    📈 *Stay ahead of the curve!* 🚀  

    ### **Guidelines:**  
    - **Keep it concise, and must be mobile-phone friendly** (short, punchy sentences).  
    - **Use whitespace and dividers (`------`)** to improve Slack readability.  
    - **Use emojis sparingly**, only where they enhance clarity.  
    - **Ensure Markdown formatting is valid** for proper Slack rendering.  
    """
    
    try:
        response = client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        
        result = response.choices[0].message.content.strip()
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
        return f"An error occurred: {e}"
