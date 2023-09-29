class BaseModel:
    __tablename__ = None

    def init(self):
        self.initialized = True
        if not self.__tablename__:
            raise ValueError("Model must have a __tablename__")

    def set_id(self, id: int):
        self.id = id

    @classmethod
    def get_table_name(cls):
        return cls.__tablename__
