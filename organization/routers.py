import os
from fastapi import APIRouter
from opencv.camera import face_detection
from config.settings import MEDIA_ROOT


router = APIRouter(prefix='', tags=['organization'])


@router.get("/camera/{organizatio_name}/{user_id}")
async def read_items(organizatio_name:str, user_id:int):
    paht_save_image = os.path.join(MEDIA_ROOT, organizatio_name, f"{user_id}").replace('./', '')
    os.makedirs(paht_save_image, exist_ok=True)
    print(paht_save_image)
    face_detection(paht_save_image)
    return {"messages", "end images"}


