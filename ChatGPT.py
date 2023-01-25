from API import key
import requests
import sys
import optparse


def main():
    help_text = f"""\n\n{sys.argv[0]} Hello how are you?"""
    parser = optparse.OptionParser(usage=help_text)

    parser.parse_args()

    if len(sys.argv) < 2:
        print(f"\nMaybe you should try: {sys.argv[0]} Hello how are you?")
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

        req = requests.post(url, headers=headers, json=data)
        answer = req.json()

        if "error" in answer:
            print("\n" + answer["error"]["message"])

        else:
            if "choices" in answer:
                print(answer["choices"][0]["text"])
            else:
                print("ChatGPT did not understand your question, please try again...")


if __name__ == "__main__":
    main()
