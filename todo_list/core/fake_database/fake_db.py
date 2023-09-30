from collections import defaultdict, Counter

from todo_list.core.fake_database.model_base import BaseModel


class FakeDB:

    def __init__(self):
        self.id_counter = Counter()
        self.db = defaultdict(list)

    def check_model(self, model: BaseModel):
        if not model.initialized:
            raise ValueError("Model is not initialized")

    def add_table(self, model: BaseModel):
        self.check_model(model)
        table_name = model.get_table_name()
        model.set_id(self.id_counter[table_name])
        self.id_counter.update({table_name: 1})
        self.db[table_name].append(model)


    def update_data(self,
                    table: str,
                    idx: int,
                    data: BaseModel):
        data.set_id(self.db[table][idx].id)
        self.db[table][idx] = data


    def delete_data(self, table: str, idx: int):
        self.db[table].pop(idx)


    def get_table(self, table):
        return self.db[table]
