from fastapi import FastAPI
from api.routes import astrology, quotes, scriptures

app = FastAPI()

app.include_router(astrology.router, prefix="/astrology", tags=["Astrology"])
app.include_router(quotes.router, prefix="/quotes", tags=["Quotes"])
app.include_router(scriptures.router, prefix="/scriptures", tags=["Scriptures"])

