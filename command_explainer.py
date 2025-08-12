import requests
import dotenv
import os
# import json

dotenv.load_dotenv()
llama_api_url = os.getenv("LLAMA_API_URL")


def explain_command(command):
    # with open("sample_response.json", "r") as f:
    #     sample_response = json.load(f)
    # print(sample_response["completion_message"]["content"]["text"])

    prompt = f"Explain this cli command in simple English:\n{command}"
    headers = {
        "Authorization": f"Bearer {os.getenv('LLAMA_API_KEY')}",
        "Content-Type": "application/json",
    }
    data = {
        "model" : os.getenv('LLAMA_MODEL'),
        "messages": [
            {
                
            "role": "system", 
            "content": prompt
            }
        ],
        "max_completion_tokens": 256,
    }
    
    response = requests.post(
        os.getenv("LLAMA_API_URL"), 
        headers=headers, 
        json=data)
    response.raise_for_status()
    result = response.json()
    print(f"Explanation: {result["completion_message"]["content"]["text"]}")


if __name__ == "__main__":
    command = input("Enter a command to explain: ")
    explain_command(command)
