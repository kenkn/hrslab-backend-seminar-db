from fastapi import FastAPI
from db import database
from routers.router import router
from starlette.requests import Request

app = FastAPI()


# DB 接続
@app.on_event("startup")
async def startup():
    await database.connect()


# DB 切断
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# router 登録
app.include_router(router)


# middleware state.connection に database オブジェクトをセット
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.connection = database
    response = await call_next(request)
    return response
