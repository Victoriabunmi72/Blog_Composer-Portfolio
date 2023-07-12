from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai_generate import OpenAIService

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Data(BaseModel):

    """ Data class for data validation
    """
    keyword: str


@app.post("/api/compose")
def compose_article(data: Data) -> str:
    openai_service = OpenAIService()

    # generate article using the OpenAI API
    article = openai_service.generate_article(
        data.keyword)

    return article
