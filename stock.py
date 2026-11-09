from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
import os

groq_api = os.getenv("GROQ_API_KEY") 

model = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=groq_api
)

from pydantic import BaseModel,Field
class Section(BaseModel):
    