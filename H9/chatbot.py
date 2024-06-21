import openai


openai.api_key = 'sk-K8GLQOAaK9FEvz5n2QHuT3BlbkFJtHg0QTtArbLVy9FNQ***'

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # 使用 GPT-4 模型
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=150,  # 设置回复的最大 tokens
        n=1,
        stop=None,
        temperature=0.9,  # 控制回复的随机性
    )
    return response.choices[0].message['content'].strip()

def main():
    print("Welcome to the GPT-4 Chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = chat_with_gpt(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()