from app.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
        # devuelve uno a la vez
    finally:
        db.close()