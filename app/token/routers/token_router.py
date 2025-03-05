from fastapi import APIRouter, Depends, HTTPException,status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

import jwt
from jwt import PyJWTError
from app.token.token import create_access_token,verify_token,create_refresh_token
from app.core.config import settings


token = APIRouter(
    prefix="/token",
    tags=["token"],

)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@token.get("/protected")
async def veryfi_token(token:str =Depends(oauth2_scheme)):
    verify_user_token = verify_token(token=token)
    return verify_user_token

@token.post("/refresh")
async def refresh_access_token(refresh_token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise JWTError("Invalid refresh token")

       
        access_token = create_access_token(data={"sub": username})
        new_refresh_token = create_refresh_token(data={"sub": username})
        response = JSONResponse(content={"message": "Login successful"})
        response.set_cookie(
            key="refresh_token", 
            value=new_refresh_token, 
            httponly=True, 
            secure=True, 
            samesite="Strict"  
        )
        return {"access_token": access_token,
                "refresh_token":new_refresh_token,
                "token_type": "bearer"}
    

    except PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
            headers={"WWW-Authenticate": "Bearer"},
        )