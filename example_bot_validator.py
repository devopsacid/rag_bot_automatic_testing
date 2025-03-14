import json
import time
import os
import pytest
import requests
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY") or "your_api_key")

# def ask_bot(question: str) -> str:
#     """
#     Sends a question to the RAG chatbot API and retrieves the answer.

#     Args:
#         question (str): The user's question.

#     Returns:
#         str: The answer from the chatbot or an error message if the request fails.
#     """
#     url = "https://dev.agentkovac.sk/api/rag/get_rag_answer"
#     payload = [{"role": "user", "content": question}]
#     headers = {"Content-Type": "application/json"}

#     try:
#         response = requests.post(
#             url,
#             json=payload,
#             headers=headers,
#             timeout=60
#         )
#         response.raise_for_status()
#         data = response.json()["answer"]
#         return data
#     except requests.exceptions.RequestException as e:
#         return "error: " + str(e)
#     except (ValueError, KeyError) as e:
#         return "error: invalid response format - " + str(e)

def ask_bot(question: str):
    """
    Sends a question to the chatbot API and retrieves the answer.

    Args:
        question (str): The user's question.

    Returns:
        str: The answer from the chatbot.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": question}]
    )
    return response.choices[0].message.content.strip()

def ask_openai(question: str):
    """
    Sends a question directly to OpenAI's GPT-4o-mini model
        and returns its response.

    Args:
        question (str): The question for GPT-4o-mini.

    Returns:
        str: The answer provided by GPT-4o-mini.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": question}]
    )
    return response.choices[0].message.content.strip()

def load_questions(file_path: str):
    """
    Loads a list of question-answer pairs from a JSON file.

    Args:
        file_path (str): Path to the JSON file containing question-answer pairs.

    Returns:
        list: A list of dictionaries with question-answer pairs.

    Raises:
        pytest.fail: If the file does not exist or contains invalid JSON.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if (
            not isinstance(data, list)
            or not all(isinstance(item, dict) for item in data)
        ):
            raise ValueError(
                "Error: JSON file must contain a list of dictionaries."
            )

        return data
    except FileNotFoundError:
        pytest.fail(f"File {file_path} not found.")
        return []
    except json.JSONDecodeError:
        pytest.fail(f"Error parsing JSON in file {file_path}.")
        return []

@pytest.mark.dependency(name="test_bot_response_format")
@pytest.mark.parametrize("question", ["Kto je dekan?"])
def test_bot_response_format(question):
    """
    Tests whether the ask_bot function returns
        a properly formatted string without errors.

    Args:
        question (str): A test question for the bot.
    """
    response = ask_bot(question)
    assert isinstance(response, str)
    assert not response.lower().startswith("error")

@pytest.mark.dependency(
    name="test_contains_key_data",
    depends=["test_bot_response_format"]
)
@pytest.mark.parametrize("file_path", ["simple_questions.json"])
def test_contains_key_data(file_path):
    """
    Checks if answers from ask_bot contain correct answers
        from predefined question-answer pairs.

    Args:
        file_path (str): Path to the JSON file with question-answer pairs.
    """
    data = load_questions(file_path)
    correct_counter = 0

    for row in data:
        question, correct_answer = list(row.items())[0]
        answer = ask_bot(question).lower()
        correct_counter += 1 if correct_answer.lower() in answer else 0

    assert correct_counter >= len(data) * (2 / 3)

@pytest.mark.dependency(depends=["test_bot_response_format"])
@pytest.mark.parametrize("question", ["Kto je dekan?"])
def test_bot_response_time(question):
    """
    Measures and validates that the bot's
        response time is within acceptable limits.

    Args:
        question (str): A test question to measure response time.
    """
    start_time = time.time()
    ask_bot(question)
    duration = time.time() - start_time
    assert duration <= 20

@pytest.mark.dependency(depends=["test_contains_key_data"])
@pytest.mark.parametrize("file_path", ["simple_questions.json"])
def test_answer_validity(file_path):
    """
    Validates correctness of the bot's answers
        by comparing them with OpenAI's GPT-4o-mini.

    Args:
        file_path (str): Path to the JSON file
            with predefined question-answer pairs.
    """
    data = load_questions(file_path)
    valid_counter = 0

    for row in data:
        question, correct_answer = list(row.items())[0]
        answer = ask_bot(question)
        validation_request = (
            f"I asked my bot question '{question}', correct answer '{correct_answer}', "
            f"and got bot answer '{answer}'. Check if the correct answer is contained "
            "in the bot's answer, and if so, write only 'YES', and if not, write only 'NO'."
        )
        validation_answer = ask_openai(validation_request)
        valid_counter += 1 if "YES" in validation_answer.strip().upper() else 0

    assert valid_counter >= len(data) * (2 / 3)
