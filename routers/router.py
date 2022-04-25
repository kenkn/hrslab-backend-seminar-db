from fastapi import APIRouter, Depends
from schemas.post_schema import PostSchema
from databases import Database
from utils.db_utils import get_connection
from models.posts import posts

router = APIRouter()


@router.get("/post/")
async def get_post(
    post_id: int,
    database: Database=Depends(get_connection)
):
    # クエリ(SELECT * FROM posts WHERE post_id = post_id);
    query = posts.select().where(posts.columns.post_id==post_id)
    res = await database.fetch_one(query)
    if res == None:
        return {
            "message": "なかったよ～"
        }
    return res


@router.post("/post/")
async def post(req: PostSchema, database: Database=Depends(get_connection)):
    # クエリ(INSERT INTO posts (post_id, user_id, body) values ( , , ));
    query = posts.insert()
    # ( , , )の部分(値)
    values = {
        "post_id": req.post_id,
        "user_id": req.user_id,
        "body": req.body
    }
    # SQL実行
    await database.execute(query, values)

    return {
        "message": "成功ンゴ"
    }
