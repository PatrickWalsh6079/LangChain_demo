
from langchain.llms import OpenAI
from langchain.llms import HuggingFaceHub
from application.models import secret_key


def large_lang(model_name='google/flan-t5-large', key=secret_key.HUGGINGFACEHUB_API_TOKEN):
    """
    model_name='text-davinci-003'
    key=secret_key.openai_api_key

    model_name = 'google/flan-t5-large'
    key=secret_key.HUGGINGFACEHUB_API_TOKEN
    :param key:
    :param model_name:
    :return: execute run
    """
    # setup model
    # llm = OpenAI(openai_api_key=key, model_name=model_name)
    llm = HuggingFaceHub(huggingfacehub_api_token=key, repo_id=model_name)

    # construct query
    query = 'What is the capital of Sweden?'

    # execute query
    run = llm(query)

    return query, run

