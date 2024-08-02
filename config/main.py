from fastapi import FastAPI
from core.routers import router as CoreRouters
from account.routers import router as AccountRouters
from . import settings


app = FastAPI()

app.include_router(CoreRouters)
app.include_router(AccountRouters)