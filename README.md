# StealthBoard

**StealthBoard** is a Python-based tool designed to interact with OpenAI's GPT models and cl1p.net directly via the clipboard. It operates discreetly in the background, enabling users to query GPT or fetch and update shared content from cl1p.net without opening a browser.

## ⚡ Features

- **GPT Integration**: Send prompts prefixed with `gpt:` and get instant responses in your clipboard.
- **cl1p.net GET**: Retrieve shared content from cl1p.net by copying `cl1p_get:{ID}`.
- **cl1p.net PUT**: Update content on cl1p.net by copying `cl1p_put:{ID}:{content}`.
- **Clipboard Monitoring**: Continuously monitors the clipboard for specific prefixes to trigger actions.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Andrei-Iosifescu123/StealthBoard.git
   cd StealthBoard
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. (Optional) Set OpenAI API key
4. Run the tool:
   ```
   python3 main.py
   ```

## Usage

### GPT Integration
To query GPT, copy text starting with `gpt:`, followed by your prompt. 

Example: `gpt:Explain how recursion works.`

The tool will process the prompt and replace your clipboard content with GPT's response.

### cl1p.net GET
To retrieve content from cl1p.net, copy text starting with `cl1p_get:`, followed by the cl1p ID.

Example: `cl1p_get:example_clip`

The tool will fetch the content from `https://cl1p.net/example_clip` and place it in your clipboard. If the cl1p is empty, the clipboard will say: `Empty cl1p!`. 

### cl1p.net PUT
To upload content to cl1p.net, copy text starting with `cl1p_put:`, followed by the cl1p ID and content, separated by `:`. 

Example: `cl1p_put:example_clip:This is a test note.`

The tool will send a POST request to `https://cl1p.net/example_clip` with the content `This is a test note.`. You’ll be notified if the update was successful or if an error occurred.

## Dependencies

To run **StealthBoard**, you need the following:

- **Python**: Version 3.7 or higher
- **Requests**: For handling HTTP requests
- **Pyperclip**: For clipboard monitoring and manipulation
- **OpenAI Python Library**: For GPT API integration

Install all dependencies using the following command:
```bash
pip3 install -r requirements.txt
```

## License
StealthBoard is licensed under the MIT License. 

