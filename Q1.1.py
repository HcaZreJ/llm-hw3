import openai

client = openai.OpenAI(
    api_key="sk-3K_qPRoWxmiYBT-A62oweg",
    base_url="https://cmu.litellm.ai",
)
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "Give me ONLY the answer of 1 point 1 times 3 million 2 thousand thirty-six plus 2.5 billion divided by 4.44444 hundred million minus 3 point 2"
        }
    ]
)

print(response.choices[0].message.content)