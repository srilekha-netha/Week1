import requests

API_KEY = " "
ENDPOINT = "https://bedrock-runtime.ap-south-1.amazonaws.com/model/meta.llama3-8b-instruct-v1:0/invoke"

def clean_llama_output(raw_output):
    cleaned = raw_output.replace("[/INST]", "").replace("[INST]", "")
    if "You are a certified dietician" in cleaned:
        cleaned = cleaned.split("You are a certified dietician")[0]
    if "Question:" in cleaned:
        cleaned = cleaned.split("Question:")[0]
    return cleaned.strip()

def get_diet_advice(user_input):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
        "X-Amzn-Bedrock-Accept": "application/json",
        "X-Amzn-Bedrock-Content-Type": "application/json"
    }

    prompt = (
        f"[INST] You are a certified dietician. Answer this question clearly and briefly: "
        f"{user_input} Do not repeat the question. Do not generate another question. Do not add extra prompts. Just give one helpful answer. [/INST]"
    )

    payload = {
        "prompt": prompt,
        "max_gen_len": 512,
        "temperature": 0.7,
        "top_p": 0.9
    }

    response = requests.post(ENDPOINT, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        raw_text = result.get("generation", "")
        return clean_llama_output(raw_text)
    else:
        return f"Error {response.status_code}: {response.text}"

# Optional test
if __name__ == "__main__":
    print(get_diet_advice("How can I reduce belly fat naturally?"))

