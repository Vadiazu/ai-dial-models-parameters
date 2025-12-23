from task.app.main import run

# TODO:
#  Try `max_tokens` parameter. It sets the maximum length of the AI's response. The AI will stop generating text once it hits this limit.
#  User massage: What is token when we are working with LLM?

if __name__ == "__main__":
    # Limit responses to 10 tokens to observe truncated outputs (finish_reason == 'length')
    run(
        deployment_name='gpt-4o',
        max_tokens=10,
        print_request=False,
    )

# Previously, we have seen that the `finish_reason` in choice was `stop`, but now it is `length`, and if you check the
# `content,` it is clearly unfinished.