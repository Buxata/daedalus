import sys,json
from openai import OpenAI
from etc.prompts import system_prompt
from etc.call_functions import available_functions

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
        messages_for_chat = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ]

        response = client.chat.completions.create(
            model="local-model",  # LM Studio routes this to whichever model is loaded
            messages=messages_for_chat,
            temperature=0,
            tools=available_functions,
        )

        prompt_token = ""
        response_token = ""

        message = response.choices[0].message
        if message.tool_calls:
            for tool_call in message.tool_calls:
                function_args = json.loads(tool_call.function.arguments or "{}")
                print(f"Calling function: {tool_call.function.name}({function_args})")

        if response and response.choices:
            print(response.choices[0].message.content)
            if response.usage:
                prompt_token = response.usage.prompt_tokens
                response_token = response.usage.completion_tokens
        else:
            print("There were some issues with the response.")

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
