import sys

from openai import OpenAI

from etc.prompts import system_prompt
from etc.utilities import process_request


def main():
    prompt = ""
    if len(sys.argv) > 1:
        prompt = sys.argv[1]
        print(prompt)

        # Connect to local LM Studio server
        client = OpenAI(
            base_url="http://localhost:1234/v1",
            api_key="lm-studio",  # Required parameter, but any string works
        )



        message_history= [{"role": "system", "content": system_prompt}, {"role": "user", "content": prompt}]
        prompt_token = ""
        response_token = ""

        i = 0
        while process_request(message_history, prompt_token, response_token, client):
            if i > 20:
                sys.exit(1)
            i = i+1

        for message in message_history:
            if message.get("content"):
                print(f"{message["role"]}: {message["content"]}")
            if message.get("reasoning_content"):
                print(f"Reasoning...{message["role"]}: {message["reasoning_content"]}")

        if i == 1:
            print (f"The response was prompted {i} time" )
        else:
            print (f"The response was prompted {i} times" )

        if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
            verbose(prompt, prompt_token, response_token)

    else:
        print("No prompt given")
        verbose("", "", "")
        sys.exit(1)


def verbose(prompt, prompt_token, response_token):
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {prompt_token}")
    print(f"Response tokens: {response_token}")

main()
