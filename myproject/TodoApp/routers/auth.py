from fastapi import APIRouter # Import APIRouter to create a router for authentication endpoints


router = APIRouter()


@router.get("/auth/")
async def get_user():
    return {'user': 'authenticated'} 