import sys
from typing import cast

from openai.types.chat import ChatCompletionMessageParam

from config import MODEL_TEMPERATURE
from etc.call_functions import available_functions, call_function


def process_request(messages, i_token, o_token, ai_client ):

    response = None
    response = ai_client.chat.completions.create(
        model="local-model",  # LM Studio routes this to whichever model is loaded
        messages=cast(list[ChatCompletionMessageParam], messages),
        temperature=MODEL_TEMPERATURE,
        tools=available_functions,
    )

    assert response is not None

    message_response = response.choices[0].message

    if message_response.content == "" and message_response.reasoning_content == "" and message_response.tool_calls == []:
        return False

    messages.append(dict(message_response))
    if message_response.tool_calls:
        for tool_call in message_response.tool_calls:
            try:
                result_message = call_function(tool_call, "--verbose" in sys.argv)

                messages.append({
                    "role": "tool",
                    "content": result_message["content"],
                    "tool_call_id": result_message["tool_call_id"]
                })
                messages.append(result_message)
            except Exception as e:
                return f"Error: executing Python file: {e}"

    return True
