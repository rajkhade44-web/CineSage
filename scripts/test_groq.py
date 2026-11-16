import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# 1. Load environment variables
load_dotenv()

# 2. Read configuration
api_key = os.getenv("GROQ_API_KEY")
model_name = os.getenv("GROQ_MODEL")

# 3. Check API key
if not api_key:
    raise ValueError("GROQ_API_KEY is missing in .env")

# 4. Initialize the LLM
llm = ChatGroq(
    model=model_name,
    temperature=0
)

# 5. Send a message
response = llm.invoke("Explain LangChain in simple words.")

# 6. Display the response
print("\nAI Response:")
print(response.content)









# movie_text = """
#     Inception is a science fiction movie directed by Christopher Nolan.
#     It was released in 2010 and stars Leonardo DiCaprio.
# """

# response = llm.invoke(f"Identify the movie title, director and release year: {movie_text}")

# print(response.content)

