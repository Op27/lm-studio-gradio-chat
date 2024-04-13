import gradio as gr  # to create the web UI for the application
from openai import OpenAI  # to interact with LM Studio models
import re  # for text manipulation

# ANSI escape code for colors
RESET_COLOR = '\033[0m'
NEON_GREEN = '\033[92m'

client = OpenAI(base_url="http://[add_local_host_here]", api_key="lm-studio")

# Initialize an empty list to store conversation history
conversation_history = []

def format_response_text(text):
    """
    Formats the response text for improved readability.
    :param text: The raw response text.
    :return: Formatted text.
    """
    # New paragraphs after each period, question mark, or exclamation point
    text = re.sub(r'(?<=[.!?])\s+(?=[A-Z])', '\n\n', text)
    
    # Properly indent bullet points and numbered lists
    text = re.sub(r'(\n)?(\s*)?([•\-*]|\d+\.)\s+', r'\n    \3 ', text)
    
    return text

def mistral_streamed_interaction(user_input, conversation_history):
    """
    Interacts with the mistral model via LM Studio, maintaining conversation context.
    :param user_input: String, user's input.
    :param conversation_history: List, the conversation history.
    :return: Tuple, containing the response and updated conversation history.
    """
    # Add user's input to conversation history
    conversation_history.append({"role": "user", "content": user_input})

    streamed_completion = client.chat.completions.create(
        model="TheBloke/dolphin-2.2.1-mistral-7B-GGUF/dolphin-2.2.1-mistral-7b.Q4_K_S.gguf",
        messages=conversation_history,
        stream=True  # Enable streaming
    )

    full_response = ""
    line_buffer = ""

    for chunk in streamed_completion:
        delta_content = chunk.choices[0].delta.content
        if delta_content:
            line_buffer += delta_content
            if '\n' in line_buffer:
                lines = line_buffer.split('\n')
                full_response += '\n'.join(lines[:-1])
                line_buffer = lines[-1]

    if line_buffer:
        full_response += line_buffer

    full_response = format_response_text(full_response)

    # Add model's response to conversation history
    conversation_history.append({"role": "system", "content": full_response})

    return full_response, conversation_history

def clear_conversation_history():
    """
    Clears the conversation history.
    """
    global conversation_history
    conversation_history = []
    print("Conversation history cleared.")


def gradio_interface_interaction(user_input):
    """
    This function acts as the bridge between the Gradio interface and the chat logic.
    It processes the user input via the existing chat logic and returns the response.
    
    :param user_input: User input from the Gradio interface.
    :return: Response text to be displayed in the Gradio interface.
    """
    # Call the existing chat interaction function with the global conversation history
    response, _ = mistral_streamed_interaction(user_input, conversation_history)
    return response


# Modify the Gradio interface to use the new interaction function
iface = gr.Interface(
    fn=gradio_interface_interaction,
    inputs=gr.Textbox(lines=2, placeholder="Enter your prompt here"),
    outputs=gr.Textbox(),
)

# Launch the Gradio interface
iface.launch()

