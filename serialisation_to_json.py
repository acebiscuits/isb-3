import json
import logging

def serialisation_to_json(filename: str, key: bytes)->None:
    '''
    str сериализуется в json файл

    Args:
        filename (str): имя файла в который сериализуется str
        key (bytes): объект, который сериализуется в json
    '''
    try:
        with open(filename, "w") as f:
            json.dump(list(key), f)
    except FileNotFoundError:
        logging.error(f"{filename} not found")

def deserialisation_from_json(filename: str)->bytes:
    '''
    десериализует данные из файла, возвращает байтовую строку

    Args:
        filename (str): имя файла в который сериализуется str
        key (bytes): объект, который сериализуется в json
    '''
    try:
        with open(filename) as f:
            data = bytes(json.load(f))
            return data
    except FileNotFoundError:
        logging.error(f"{filename} not found")