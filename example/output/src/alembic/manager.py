from typing import Any, List, Type

from sqlalchemy.orm import Session


class ModelManager:
    def __init__(self, db_session: Session):
        self.db = db_session

    def insert(self, model_instance):
        try:
            self.db.add(model_instance)
            self.db.commit()
            return model_instance
        except Exception as e:
            self.db.rollback()
            raise e

    def get(self, model: Type[Any], **kwargs):
        return self.db.query(model).filter_by(**kwargs).first()

    def get_all(self, model: Type[Any], **kwargs) -> List[Any]:
        return self.db.query(model).filter_by(**kwargs).all()

    def update(self, model: Type[Any], identifier, **kwargs):
        try:
            obj = self.db.query(model).filter_by(id=identifier).first()
            if not obj:
                raise ValueError("Item not found")

            for key, value in kwargs.items():
                setattr(obj, key, value)

            self.db.commit()
            return obj
        except Exception as e:
            self.db.rollback()
            raise e

    def delete(self, model: Type[Any], identifier):
        try:
            obj = self.db.query(model).filter_by(id=identifier).first()
            if not obj:
                raise ValueError("Item not found")

            self.db.delete(obj)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            raise e
