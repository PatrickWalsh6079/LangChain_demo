
from PyPDF2 import PdfReader
from langchain import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import openai
import os
import secret_key

llm = OpenAI(openai_api_key=secret_key.openai_api_key, model_name='text-davinci-003')
print('done')
