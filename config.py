import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://aallp_kupy_user:CAUPrFB8UeWtFAsu7uWF3dWYm43diFuO@dpg-ctor5u0gph6c73d8vp80-a.ohio-postgres.render.com/aallp_kupy')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
