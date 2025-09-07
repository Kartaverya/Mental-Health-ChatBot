from pydantic import BaseModel
#structure and validate incoming data to fastAPI endpoint

class ChatRequest(BaseModel):
    session_id: str
    query : str 
#standard structure of JSON request body 