import time
import pyperclip
import requests
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    api_key="API_KEY_HERE"
)

def chat_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def cl1p_get(cl1p_name):
    try:
        url = f"https://api.cl1p.net/{cl1p_name}"
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text.strip()
            return content if content else "Empty cl1p!"
        else:
            return f"Error: HTTP {response.status_code}"
    except Exception as e:
        return f"Error: {e}"

def cl1p_put(cl1p_id, content):
    try:
        url = f"https://cl1p.net/{cl1p_id}"
        data = {"ttl": 10, "content": content}
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return "Cl1p updated successfully!"
        else:
            return f"Error: HTTP {response.status_code}"
    except Exception as e:
        return f"Error: {e}"

def monitor_clipboard():
    last_text = ""
    while True:
        clipboard_text = pyperclip.paste()

        if clipboard_text != last_text:
            if clipboard_text.startswith("gpt:"):
                prompt = clipboard_text[4:].strip()
                pyperclip.copy("Waiting for response...")
                print("Waiting for response...")
                try:
                    reply = chat_gpt(prompt)
                    pyperclip.copy(reply)
                    print("Response copied to clipboard.")
                except Exception as e:
                    pyperclip.copy(f"Error: {e}")
                    print(f"Error: {e}")
            elif clipboard_text.startswith("cl1p_get:"):
                cl1p_name = clipboard_text[9:].strip()
                pyperclip.copy("Fetching cl1p content...")
                print("Fetching cl1p content...")
                try:
                    result = cl1p_get(cl1p_name)
                    pyperclip.copy(result)
                    print("Cl1p content copied to clipboard.")
                except Exception as e:
                    pyperclip.copy(f"Error: {e}")
                    print(f"Error: {e}")
            elif clipboard_text.startswith("cl1p_put:"):
                try:
                    _, cl1p_id, content = clipboard_text.split(":", 2)
                    pyperclip.copy("Updating cl1p content...")
                    print("Updating cl1p content...")
                    result = cl1p_put(cl1p_id.strip(), content.strip())
                    pyperclip.copy(result)
                    print("Cl1p update result copied to clipboard.")
                except ValueError:
                    pyperclip.copy("Invalid cl1p_put format! Use cl1p_put:{ID}:{content}.")
                    print("Invalid cl1p_put format!")

        last_text = clipboard_text
        time.sleep(1)

if __name__ == "__main__":
    print("Monitoring clipboard for 'gpt:', 'cl1p_get:', and 'cl1p_put:' prefixed text...")
    monitor_clipboard()
