import requests
import dotenv
import os

dotenv.load_dotenv()
llama_api_url = os.getenv("LLAMA_API_URL")


def explain_command(command):
    prompt = f"Explain this shell command in simple English:\n{command}"
    headers = {
        "Authorization": f"Bearer {os.getenv('LLAMA_API_KEY')}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "llama3-70b-chat",
        "messages": [
            {
                
            "role": "system", 
            "content": prompt
            }
        ],
    }
    
    response = requests.post(
        os.getenv("LLAMA_API_URL"), 
        headers=headers, 
        json=data)
    response.raise_for_status()
    result = response.json()
    print(result)


if __name__ == "__main__":
    command = input("Enter a shell command to explain: ")
    explain_command(command)
