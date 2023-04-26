from fastapi import APIRouter, Request

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signin")
async def Login(req: Request):
    pass


@router.post("/signup")
async def Register():
    pass
