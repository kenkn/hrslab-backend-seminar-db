from pydantic import BaseModel

class PostSchema(BaseModel):
    post_id: int
    user_id: str
    body: str