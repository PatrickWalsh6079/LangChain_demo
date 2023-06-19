

from langchain import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from application.models import secret_key


def openai_model():
    """

    :return:
    """
    model_name = 'text-davinci-003'
    llm = OpenAI(openai_api_key=secret_key.openai_api_key, model_name=model_name)
    query = 'What is my name and how many awards do I have?'
    result_without_context = llm(query)
    print('Result without context:')
    print(result_without_context)

    # get text file for context
    with open('application/data/my_data.txt', 'r') as f:
        content = f.read()

    # use text splitter
    text_splitter = CharacterTextSplitter(
        separator='\n',
        chunk_size=200,
        chunk_overlap=20,
        length_function=len,
    )
    split = text_splitter.split_text(content)

    # FAISS embeddings for similarity search
    embeddings = OpenAIEmbeddings(openai_api_key=secret_key.openai_api_key)
    doc_search = FAISS.from_texts(split, embeddings)

    # chain
    chain = load_qa_chain(OpenAI(openai_api_key=secret_key.openai_api_key), chain_type="stuff")
    same_query = 'What is my name and how many awards do I have?'
    docs = doc_search.similarity_search(same_query)
    print('Run with document context:')
    run = chain.run(input_documents=docs, question=same_query)

    return run


# print(openai_model())
