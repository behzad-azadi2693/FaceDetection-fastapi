from fastapi import APIRouter

router = APIRouter(prefix='/account', tags=['account'])

async def login():
    return {"messages", "Acounts View"}