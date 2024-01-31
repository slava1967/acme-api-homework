from typing import List

import model


class StorageException(Exception):
    pass


class LocalStorage:
    def __init__(self):
        self._id_counter = 0
        self._storage = {}

    def create(self, event: model.Event) -> str:
        self._id_counter += 1
        event.e_id = str(self._id_counter)
        self._storage[event.e_id] = event
        return event.e_id

    def list(self) -> List[model.Event]:
        return list(self._storage.values())

    def read(self, e_id: str) -> model.Event:
        if e_id not in self._storage:
            raise StorageException(f"{e_id} not found in storage")
        return self._storage[e_id]

    def update(self, e_id: str, event: model.Event):
        if e_id not in self._storage:
            raise StorageException(f"{e_id} not found in storage")
        event.e_id = e_id
        self._storage[event.e_id] = event

    def delete(self, e_id: str):
        if e_id not in self._storage:
            raise StorageException(f"{e_id} not found in storage")
        del self._storage[e_id]
