import os
import time
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import OpenAI
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('SECRET')


def safe_openai_call(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except openai.BadRequestError:
        print('Please request again, you made a bad request')
    except openai.PermissionDeniedError:
        print('Permission not given try another key')
    except openai.APITimeoutError:
        print("Time out occurred try again later")
    except openai.RateLimitError:
        print("Sorry, but the API rate limit has been reached. Please try again later.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# Take input from the user
query = f'how many chinese words can i make with the chinese words in this file'

# Load the specific file using TextLoader and specify UTF-8 encoding
loader = TextLoader('chinese_vocabulary.txt', encoding='utf-8')
docs = loader.load()

# Initialize embeddings and vector store
embedding = OpenAIEmbeddings(openai_api_key=openai.api_key)

# Create a FAISS vector store (in-memory vector database)
vectorstore = safe_openai_call(FAISS.from_documents, docs, embedding)

if vectorstore is None:
    print("Failed to create the vector store.")
else:
    # Perform the query using the vector store
    retrieved_docs = safe_openai_call(vectorstore.similarity_search, query)

    if retrieved_docs is None:
        print("Failed to perform the similarity search.")
    else:
        # Use OpenAI to generate a response to the retrieved documents
        llm = OpenAI(temperature=0, openai_api_key=openai.api_key)
        response = safe_openai_call(llm, retrieved_docs[0].page_content)

        if response is None:
            print("Failed to generate a response.")
        else:
            # Print the result to a new text file
            with open('result.txt', 'a') as file:
                file.write(response + "\n")

            print(f"Query result written to 'result.txt'.")
