from task.app.main import run

# TODO:
#  Try `max_tokens` parameter. It sets the maximum length of the AI's response. The AI will stop generating text once it hits this limit.
#  User massage: What is token when we are working with LLM?

def main():
    # Limit the response to a small number of tokens to observe `finish_reason: length` and truncated text.
    run(
        deployment_name='gpt-4o',
        max_tokens=10,
        print_only_content=False,
    )


if __name__ == '__main__':
    main()

# Previously, we have seen that the `finish_reason` in choice was `stop`, but now it is `length`, and if you check the
# `content,` it is clearly unfinished.