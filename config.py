SQLITE = "sqlite:///project.db"
POSTGRESQL = "postgresql+psycopg2://postgres:123456@localhost:5432/blogPosts_db"

class Config:
    DEBUG = False
    SECRET_KEY = "aplicacionDePosteosEnBlog"
    SQLALCHEMY_DATABASE_URI = POSTGRESQL
    CKEDITOR_PKG_TYPE = 'full'
    
 