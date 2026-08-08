import asyncio
import sys

import lmstudio as lms
from dotenv import load_dotenv


async def main():
    prompt = ""
    if len(sys.argv) > 1:
        prompt = sys.argv[1]
        print(f"Prompt: {prompt}")

        load_dotenv()

        try:
            # Connect to your running LM Studio application
            # By default, it looks for the local server at localhost:1234
            async with lms.AsyncClient() as client:
                # Dynamically fetch the model currently loaded in LM Studio
                # You can also pass a specific model key, e.g., client.llm.model("llama-3")
                model = await client.llm.model()

                # Generate a prediction/response
                response = await model.respond(prompt)

                # Print the generated text response
                print(response.content)

                # Extract token usage metadata

                prompt_token = ""
                response_token = ""
                if response is not None and response.stats is not None:
                    prompt_token = response.stats.prompt_tokens_count
                    response_token = response.stats.predicted_tokens_count
                else:
                    print(
                        "There were some issues retrieving metadata from the response."
                    )

                if len(sys.argv) > 2:
                    if sys.argv[2] == "--verbose":
                        verbose(prompt, prompt_token, response_token)

        except Exception as e:
            print(f"An error occurred connecting to LM Studio: {e}")
            print("Make sure LM Studio is open and the Developer Server is started.")

    else:
        print("No prompt given")
        verbose("", "", "")
        sys.exit(1)


def verbose(prompt, prompt_token, response_token):
    print("\n--- VERBOSE METRICS ---")
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {prompt_token}")
    print(f"Response tokens: {response_token}")


if __name__ == "__main__":
    # Execute the asynchronous main function
    asyncio.run(main())
