from flask import Flask, request
import model
import logic

app = Flask(__name__)

_event_logic = logic.EventLogic()


class ApiException(Exception):
    pass


def _from_raw(raw_event: str) -> model.Event:
    parts = raw_event.split('|')
    if len(parts) == 3:
        event = model.Event()
        event.e_id = None
        event.date = parts[0]
        event.title = parts[1]
        event.text = parts[2]
        return event
    elif len(parts) == 4:
        event = model.Event()
        event.e_id = parts[0]
        event.date = parts[1]
        event.title = parts[2]
        event.text = parts[3]
        return event
    else:
        raise ApiException(f"invalid RAW event data {raw_event}")


def _to_raw(event: model.Event) -> str:
    if event.e_id is None:
        return f"{event.date}|{event.title}|{event.text}"
    else:
        return f"{event.e_id}|{event.date}|{event.title}|{event.text}"


API_ROOT = "/api/v1"
EVENT_API_ROOT = API_ROOT + "/calendar"


@app.route(EVENT_API_ROOT + "/", methods=["POST"])
def create():
    try:
        data = request.get_data().decode('utf-8')
        event = _from_raw(data)
        e_id = _event_logic.create(event)
        return f"new id: {e_id}", 201
    except Exception as ex:
        return f"failed to CREATE with: {ex}", 404


@app.route(EVENT_API_ROOT + "/", methods=["GET"])
def list_events():
    try:
        events = _event_logic.list()
        raw_events = ""
        for event in events:
            raw_events += _to_raw(event) + '\n'
        return raw_events, 200
    except Exception as ex:
        return f"failed to LIST with: {ex}", 404


@app.route(EVENT_API_ROOT + "/<e_id>/", methods=["GET"])
def read(e_id: str):
    try:
        event = _event_logic.read(e_id)
        raw_event = _to_raw(event)
        return raw_event, 200
    except Exception as ex:
        return f"failed to READ with: {ex}", 404


@app.route(EVENT_API_ROOT + "/<e_id>/", methods=["PUT"])
def update(e_id: str):
    try:
        data = request.get_data().decode('utf-8')
        event = _from_raw(data)
        _event_logic.update(e_id, event)
        return "updated", 200
    except Exception as ex:
        return f"failed to UPDATE with: {ex}", 404


@app.route(EVENT_API_ROOT + "/<e_id>/", methods=["DELETE"])
def delete(e_id: str):
    try:
        _event_logic.delete(e_id)
        return "deleted", 200
    except Exception as ex:
        return f"failed to DELETE with: {ex}", 404
