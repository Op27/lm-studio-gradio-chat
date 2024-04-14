# LM Studio Gradio Chat
This repository contains a web-based chat application that integrates with various AI models from LM Studio, such as Mistral, OpenAI, and Llama, via a user-friendly Gradio interface. It is designed to maintain conversation history, providing a coherent and continuous AI chat experience comparable to systems like ChatGPT or Claude.

https://github.com/Op27/lm-studio-gradio-chat/assets/39921621/357d4aaf-1ab2-45d5-ad37-6ca34959c5e0

## Features
- **Multiple AI Model Integration**: Integrates with a variety of conversational AI models hosted on LM Studio, including Mistral, OpenAI, Llama, and more, offering flexibility in choosing the AI technology.
- **Real-time Interaction**: Engage with different AI models in real-time through a Gradio interface for a dynamic chat experience.
- **Contextual Conversations**: Maintains a conversation history to provide context to the AI models, enabling more coherent and meaningful interactions, similar to advanced systems like ChatGPT or Claude.
- **User-Friendly Interface**: Simple and intuitive UI built with Gradio, making it accessible for users with any level of technical expertise.

## Installation
To get started with this project, you'll need to set up your Python environment and install the necessary dependencies.

### Prerequisites
- Python 3.8 or higher
- Access to LM Studio with a running instance of the Mistral model

### Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/lm-studio-gradio-chat.git
   cd lm-studio-gradio-chat
   ```

2. Install the required Python libraries:
   ```bash
   pip install gradio openai
   ```

3. Set up your environment variables. Replace your_base_url and your_api_key with the actual values.
   ```bash
    export OPENAI_BASE_URL="your_base_url"
    export OPENAI_API_KEY="your_api_key"
   ```

### Usage
Once you have completed the installation, you can start the application by running:
   ```bash
    python main.py
   ```
This will launch the Gradio interface in your default web browser, where you can interact with the Mistral model directly.

## Contributing
Contributions to this project are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
