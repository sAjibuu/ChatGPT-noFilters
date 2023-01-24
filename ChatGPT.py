from API import key
import requests
import sys
import optparse

def main():
    help_text=f"""\n\n{sys.argv[0]} Hello how are you?"""
    parser = optparse.OptionParser(usage=help_text)
                    
    (options, arguments) = parser.parse_args()

    if len(sys.argv) < 2:
       print(f"Try: {sys.argv[0]} Hello how are you?") 
       exit(1)

    else:
        print("\nThinking, please wait...")
        url = "https://api.openai.com/v1/completions"

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}"
            }

        data = {
            "model": "text-davinci-003",
            "prompt": f"{sys.argv[1]}",
            "max_tokens": 4000,
            "temperature": 1.0
            }

        req = requests.post(url, headers = headers, json = data)
        answer = req.json()

        print(answer["choices"][0]["text"])


if __name__ == "__main__":
    main()
