from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.user.service.user_crud import UserServices
from app.user.schema.user_schem import UserSchem
from app.token.token import create_access_token,create_refresh_token
from fastapi import Depends


auth_router = APIRouter(prefix="/auth",
          tags=["auth"])

@auth_router.post("/sing-up")
async def sing_up(schem:UserSchem):
    user =  await UserServices.add_one(schem=schem)
    verify_user = await UserServices.verify_one(username=schem.username,password=schem.password)

    access_token = create_access_token(data={"sub": verify_user.username})
    refresh_token = create_refresh_token(data={"sub": verify_user.username})

    response = JSONResponse(content={"message": "Login successful"})
    response.set_cookie(
        key="refresh_token", 
        value=refresh_token, 
        httponly=True, 
        secure=True, 
        samesite="Strict" 
    )
    
    return {"access_token": access_token,
            "message":"Ok"
}


@auth_router.post("/sign-in")
async def login(data:OAuth2PasswordRequestForm = Depends()):
    user = await UserServices.verify_one(username=data.username,password=data.password)
    
    access_token = create_access_token(data={"sub": user.username})
    refresh_token = create_refresh_token(data={"sub": user.username})

    response = JSONResponse(content={"message": "Login successful"})
    response.set_cookie(
        key="refresh_token", 
        value=refresh_token, 
        httponly=True, 
        secure=True, 
        samesite="Strict" 
    )
    
    return {"access_token": access_token,
            "token_type": "bearer"}