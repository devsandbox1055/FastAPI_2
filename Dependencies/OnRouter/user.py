from fastapi import APIRouter


router = APIROUTER(
    prefix="/users",
    dependencies =[Depends(verify_token)]
)