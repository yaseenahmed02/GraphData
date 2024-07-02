from prompt_generation_templates import *
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import openai
import requests
import json
import time
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

prompts_list = [
    prompt_easy,
    prompt_expert,
    prompt_political,
    prompt_social,
    prompt_incident,
    prompt_friendship,
    prompt_coauthor,
    prompt_fiction,
    prompt_research,
    prompt_transport,
    prompt_ecosystem,
    prompt_corporate,
    prompt_telecom,
    prompt_family,
    prompt_supplychain
]

prompt_names = [
    "easy",
    "expert",
    "political",
    "social",
    "incident",
    "friendship",
    "coauthor",
    "fiction",
    "research",
    "transport",
    "ecosystem",
    "corporate",
    "telecom",
    "family",
    "supplychain"
]

openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai.api_key}"
}


def generate_prompts(template_prompt, num_prompts):
    """
    generates a list of prompts using the openai api.

    args:
        template_prompt (str): the base prompt to use for generating new prompts.
        num_prompts (int): number of prompts to generate.

    returns:
        list: a list of generated prompts.
    """
    prompts = []
    for i in range(num_prompts):
        print(f"Generating prompt {i+1}/{num_prompts}...")
        payload = {
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a prompt engineer tasked with generating prompts for explaining graphs described by a Graph Description Language (GDL). "
                               "Ensure the prompt includes a placeholder <GDL> and guides the model to explain the graph in an easy-to-understand manner."
                },
                {"role": "user", "content": template_prompt},
            ],
            "max_tokens": 500,  # ensures detailed prompts without cutting off information
            "temperature": 0.8,  # encourages creative and diverse responses
            "top_p": 0.8,  # balances diversity and relevance by considering top 80% probability mass
            "frequency_penalty": 0.0,  # allows repeated important terms for clarity and relevance
            # ensures central terms are not avoided, maintaining prompt clarity
            "presence_penalty": 0.0,
        }

        retry_attempts = 5
        for attempt in range(retry_attempts):
            try:
                response = requests.post(
                    "https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
                response.raise_for_status()
                response_json = response.json()
                generated_prompt = response_json["choices"][0]["message"]["content"].strip(
                )
                print(f"Generated prompt: {generated_prompt}")
                prompts.append(generated_prompt)
                break
            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")
                if response.status_code == 429:
                    retry_delay = (2 ** attempt) + \
                        (np.random.randint(0, 1000) / 1000)
                    print(
                        f"Rate limit hit. Retrying in {retry_delay:.2f} seconds...")
                    time.sleep(retry_delay)
                else:
                    break
            except json.JSONDecodeError:
                print("Error: Could not decode JSON response.")
                print(f"Response: {response.text}")
                break
            except KeyError:
                print("Unexpected response format.")
                print(f"Response JSON: {json.dumps(response_json, indent=2)}")
                break
    return prompts


def get_embedding(text, model="text-embedding-3-small"):
    """
    retrieves the embedding for the given text using the specified model.

    args:
        text (str): the text to get the embedding for.
        model (str): the model to use for generating embeddings.

    returns:
        list: the embedding vector for the text.
    """
    print(f"Getting embedding for text: {text[:60]}...")
    response = client.embeddings.create(
        input=[text], model=model).data[0].embedding
    print(f"Received embedding of length {len(response)}")
    return response


def evaluate_prompts(prompts):
    """
    evaluates the given prompts by calculating their embeddings and determining mean similarity.

    args:
        prompts (list): the prompts to evaluate.

    returns:
        list: mean similarity scores for the prompts.
    """
    print("Evaluating prompts...")
    embeddings = [get_embedding(prompt) for prompt in prompts]
    similarity_matrix = cosine_similarity(embeddings)
    mean_similarities = similarity_matrix.mean(axis=1)
    print("Evaluation completed.")
    return mean_similarities


def save_top_prompts(template_name, prompts, mean_similarities, top_n=50):
    """
    saves the top N prompts based on mean similarity scores to a file.

    args:
        template_name (str): the name of the template to use for naming the file.
        prompts (list): the list of generated prompts.
        mean_similarities (list): the mean similarity scores for the prompts.
        top_n (int): the number of top prompts to save.
    """
    print(f"Sorting prompts based on mean similarity for {template_name}...")
    sorted_indices = np.argsort(mean_similarities)[::-1]
    top_prompts = [prompts[i] for i in sorted_indices[:top_n]]

    if not os.path.exists('top_prompts'):
        os.makedirs('top_prompts')

    file_path = os.path.join('top_prompts', f'{template_name}_prompts.txt')
    print(f"Saving top {top_n} prompts to '{file_path}'...")
    with open(file_path, 'w') as file:
        for prompt in top_prompts:
            file.write(f"{prompt}\n")
    print(f"Top {top_n} prompts saved to '{file_path}'")


def main():
    num_prompts_per_template = 10
    top_n = 10

    for template, template_name in zip(prompts_list, prompt_names):
        print(f"Generating prompts for template: {template_name}")
        generated_prompts = generate_prompts(
            template, num_prompts_per_template)

        print(f"Evaluating prompts for template: {template_name}")
        mean_similarities = evaluate_prompts(generated_prompts)

        save_top_prompts(template_name, generated_prompts,
                         mean_similarities, top_n)


if __name__ == "__main__":
    main()
