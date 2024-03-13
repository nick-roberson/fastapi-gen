from generate.models import ModelDefinitionList
from generate.generate import generate


SAMPLE_INPUT: str = "examples/models.yaml"


def run(input: str = SAMPLE_INPUT):
    generate(input)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
