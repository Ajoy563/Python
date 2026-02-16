from openai import OpenAI

client = OpenAI()  # reads key from environment

completion = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis."},
        {"role": "user", "content": "What is coding?"}
    ]
)

print(completion.choices[0].message.content)