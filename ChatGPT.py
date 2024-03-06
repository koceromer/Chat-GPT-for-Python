from openai import OpenAI
client = OpenAI()



while True:

    model_engine ="gpt-3.5-turbo"

    prompt = input("Birşeyler giriniz : ")

    if 'exit' in prompt or 'quit' in prompt:
        break


    completion = client.chat.completions.create(
        model = model_engine,
        messages=[
        {
        "role": "user", 
        "content": prompt
        }
        ]
    )

    response = completion.choices[0].text

    print(response)




























