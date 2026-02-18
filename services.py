from db import engine
from tables import users, posts
from sqlalchemy import insert, select,update,delete


# INSERT OR CREATE USER
def create_user(name: str,email:str):
    with engine.connect() as conn:
        stmt = insert(users).values(name=name,email=email)
        conn.excute(stmt)
        conn.commit()

# INSERT OR CREATE USER
def create_user(name: str,email:str):
    with engine.connect() as conn:
        stmt = insert(users).values(name=name,email=email)
        conn.excute(stmt)
        conn.commit()
    
# GET SINGLE USER BY ID
def get_user_by_id(user_id: int):
    with engine.connect() as conn:
        stmt = select(user).where(user.c.id == user_id)
        result = conn.excute(stmt).first()
        return result
        
# GET POST BY USER
def get_posts_by_user(user_id: int):
    with engine.connect() as conn:
        stmt = select(posts).where(posts.c.user_id == user_id)
        result = conn.execute(stmt).fetchall()
        return result

#update user email
def update_user_email(user_id:int, new_email: str):
    with engine.connect() as conn:
        stmt = update(user).where(user.c.id == user_id).values(email=new_email)
        conn.execute(stmt)
        conn.commit()

#delete post
def delete_post(post_id: int):
    with engine.connect() as conn:
        stmt = delete(posts).where(posts.c.id == post_id)
        conn.execute(stmt)
        conn.commit( )