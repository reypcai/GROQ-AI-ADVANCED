import requests
from app.config import GROQ_API_KEY, GROQ_MODEL
from app.memory import save_memory, get_last_messages
from app.rag import retrieve_context

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

def generate_response(prompt: str):

    history = get_last_messages()
    context = retrieve_context(prompt)

    messages = [
        {"role": "system", "content": "Use provided context if relevant."},
        {"role": "system", "content": f"Context: {context}"}
    ]

    for user, ai in history[::-1]:
        messages.append({"role": "user", "content": user})
        messages.append({"role": "assistant", "content": ai})

    messages.append({"role": "user", "content": prompt})

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": GROQ_MODEL,
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 1024
    }

    response = requests.post(GROQ_URL, headers=headers, json=payload)

    if response.status_code != 200:
        return f"Error: {response.text}"

    output = response.json()["choices"][0]["message"]["content"]
    save_memory(prompt, output)

    return output