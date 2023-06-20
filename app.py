
from application.models import QnA_bot
from application.models import large_lang_model

if __name__ == "__main__":

    while True:
        user_input = input("Do you want to use the LLM or Document Q&A bot? To exit, type 'Q'\n> ")
        if user_input.lower() == 'llm':
            llm = large_lang_model.large_lang()
            print(llm)
        elif user_input.lower() == 'q&a':
            qna_bot = QnA_bot.openai_model()
            print(qna_bot)
        elif user_input.lower() == 'q':
            break
        else:
            print("Invalid response!\nPlease enter 'LLM' or 'Q&A'")
