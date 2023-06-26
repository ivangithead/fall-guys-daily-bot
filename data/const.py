from io import BytesIO
from PIL import Image
from requests import get

"""
API from https://fallguys-db.pages.dev/store
"""

URL = "https://api2.fallguysdb.info/api/symphony-store"

"""
Image assets
"""


subtitles = {
    "cosmetics_nameplates": "Табличка для имени",
    "costumes_faceplates":  "Лицо",
    "costumes_patterns":    "Название на табличке",
    "cosmetics_emotes":     "Эмоция",
    "costumes_lower":       "Нижняя часть костюма",
    "costumes_upper":       "Верхняя часть костюма",
    # Need: Win scene
}