
from application.models import bot
from application.models import large_lang_model

if __name__ == "__main__":

    # chatbot = bot.openai_model()
    # print(chatbot)
    llm = large_lang_model.large_lang()
    print(llm)
