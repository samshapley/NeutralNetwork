class AI:
    def __init__(self, openai_module, system="",rate=150):
        self.system = system
        self.openai = openai_module
        self.messages = [{"role": "system", "content": system}]        
        
    def generate_response(self, prompt):
        self.messages.append({"role": "user", "content": prompt})
        
        response_json = self.openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
        )

        response_text = response_json["choices"][0]["message"]["content"]

        # Print the AI's response as it's being read out
        print(f"User: {prompt}\nAssistant: {response_text}\n")

        self.messages.append({"role": "assistant", "content": response_text})

        return response_text, self.messages