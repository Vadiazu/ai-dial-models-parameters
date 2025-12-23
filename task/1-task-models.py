from task.app.main import run

# HINT: All available models you can find here: https://ai-proxy.lab.epam.com/openai/models

# TODO:
#  Try different models (`deployment_name`) with such user request:
#  User massage: What LLMs can do?

# Models to try:
# - gpt-4o
# - claude-3-7-sonnet@20250219
# - gemini-2.5-pro

def main():
    # Example: try different deployment names listed in README. Change this value to explore other models.
    run(
        deployment_name='gpt-4o',
        print_request=True,
        print_only_content=False,
    )


if __name__ == '__main__':
    main()

# The main goal of this task is to explore the functional capabilities of DIAL to be able to work with different
# LLMs through unified API