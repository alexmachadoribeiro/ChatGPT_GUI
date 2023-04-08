import openai
import os

openai.api_key = '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'

while True:

    model_engine = "text-davinci-003"

    prompt = input('Enter new prompt: ')

    if 'exit' in prompt or 'quit' in prompt:
        break

    o_robo = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = o_robo.choices[0].text
    
    print(response)