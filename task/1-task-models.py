from task.app.main import run

# HINT: All available models you can find here: https://ai-proxy.lab.epam.com/openai/models

# TODO:
#  Try different models (`deployment_name`) with such user request:
#  User massage: What LLMs can do?

# Models to try:
# - gpt-4o
# - claude-3-7-sonnet@20250219
# - gemini-2.5-pro

if __name__ == "__main__":
    # Default example: replace deployment_name with any available deployment to try different models
    run(
        deployment_name='gpt-4o',
        print_request=False,  # Set to False to hide request payload in console
        print_only_content=False,  # Set to True to print only the model content
    )

# The main goal of this task is to explore the functional capabilities of DIAL to be able to work with different
# LLMs through unified API