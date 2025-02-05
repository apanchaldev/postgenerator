from langchain_groq import ChatGroq
import os

llm = ChatGroq(
    groq_api_key = os.environ.get('GROQ'),
    model="deepseek-r1-distill-llama-70b",
    temperature=0.6,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

if __name__ == "__main__":
    response = llm.invoke('who was the first person to step on moon?')
    print(response.content)