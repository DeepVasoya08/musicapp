from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/{id}")
async def getUser(id):
    pass
