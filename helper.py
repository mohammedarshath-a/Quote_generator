from g4f.client import Client

client = Client()

def generate_quote(mood):
    prompt= "prompt: You are a motivator, given the users feelings you should help them with a quote that emphasise their feeling and make them feel better"
    query = prompt + f"User feeling: {mood}"
    chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": query}],
    )

    return chat_completion.choices[0].message.content or ""

#generate_quote("happy")