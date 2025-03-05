from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db.engine import create_table
from app.user.router.user_router import user_router
from app.product.router.product_router import product_router
from app.token.routers.token_router import token
from app.auth.auth_router import auth_router
import uvicorn




@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_table()
    yield
    
    
app = FastAPI(lifespan=lifespan)

app.include_router(user_router)
app.include_router(product_router)
app.include_router(token)
app.include_router(auth_router)






if __name__ == '__main__':
    uvicorn.run("main:app",reload=True)