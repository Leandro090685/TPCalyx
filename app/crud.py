from sqlalchemy.orm import Session


from app import models, schemas


def get_provinces(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Province).offset(skip).limit(limit).all()