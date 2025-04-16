from fastapi import APIRouter
from services.scripture_service import get_random_bible_verse, get_random_gita_chapter

router = APIRouter()

@router.get("/bible-verse")
def bible_verse():
    return get_random_bible_verse()

@router.get("/gita-chapter")
def gita_chapter():
    return get_random_gita_chapter()