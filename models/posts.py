import sqlalchemy as sa
from db import metadata, engine

posts = sa.Table(
    "posts",
    metadata,
    sa.Column("post_id", sa.Integer, primary_key=True, index=True, nullable=False),
    sa.Column("user_id", sa.String, index=True, nullable=False),
    sa.Column("body", sa.String, index=True, nullable=False),
)

metadata.create_all(bind=engine)