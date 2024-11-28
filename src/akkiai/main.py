#!/usr/bin/env python
import sys
import warnings

from akkiai.crew import Akkiai

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'BUSINESS_DETAILS': 'Business details',
        'PRODUCT_DESCRIPTION': 'Product Description'
    }
    Akkiai().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'BUSINESS_DETAILS': 'Business details',
        'PRODUCT_DESCRIPTION': 'Product Description'
    }
    try:
        Akkiai().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Akkiai().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'BUSINESS_DETAILS': 'Business details',
        'PRODUCT_DESCRIPTION': 'Product Description'
    }
    try:
        Akkiai().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

if __name__ =="__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py [COMMAND] [OPTIONS]")
        sys.exit(1)
    command = sys.argv[1]
    if command == "run":
        run()