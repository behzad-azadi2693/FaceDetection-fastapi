import os
from fastapi import APIRouter


router = APIRouter(prefix='', tags=['core'])


@router.get('/')
async def index_view():
    return {"messges", "Hello World!"}


