from openai import OpenAI
from dotenv import load_dotenv
import os

#%%

class Agent:
    def __init__(self):

        load_dotenv()
        self.client = OpenAI(os.getenv("OPENAI_API_KEY"))
        self.system_prompt = (
            "You are an expert Python developer. "
            "You will help the user by providing clear and concise code examples."
        )
        self.messages = []
        self.messages.append({"role": "system", "content": self.system_prompt})

    def send_message(self, message):
        
        self.messages.append({"role": "user", "content": message})
        response = self.client.chat.completions.create(model="gpt-4o", messages=self.messages)

        return response.choices[0].message.content
    
if __name__ == "__main__":

    agent = Agent()
    message = "How do I read a file in Python?"
    response = agent.send_message(message)
    print(response)
