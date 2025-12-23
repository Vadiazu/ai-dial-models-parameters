from task.app.main import run

# TODO:
#  Try the `temperature` parameter that controls the randomness of the output. It's a parameter for balancing creativity
#        and determinism. Range: 0.0 to 2.0, Default: 1.0
#  User massage: Describe the sound that the color purple makes when it's angry

def main():
    # Set temperature between 0.0 and 1.0 to control randomness. Try 0.0, 0.5, 1.0.
    run(
        deployment_name='gpt-4o',
        print_only_content=True,
        temperature=0.5,
    )


if __name__ == '__main__':
    main()