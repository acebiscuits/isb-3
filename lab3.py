import argparse
from decrypting import decrypting
from encrypting import encrypting
from generating_keys import generating_keys
import json
import logging
from tqdm import tqdm


if __name__ == "__main__":   
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--settings_path',default='files\\settings.json',help='Путь к json файлу с путями, default = files\\settings.json', action='store')
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('-gen','--generation',help='Запускает режим генерации ключей', action="store_true")
    group.add_argument('-enc','--encryption',help='Запускает режим шифрования', action="store_true")
    group.add_argument('-dec','--decryption',help='Запускает режим дешифрования', action="store_true")
    args = parser.parse_args()
    logging.info(args)
    settings_path = args.settings_path

    try:
        with open(settings_path) as jf:
            settings = json.load(jf)
    except FileNotFoundError:
        logging.error(f"{settings_path} not found")

    mode = (args.generation, args.encryption, args.decryption)
    logging.info(mode)

    match mode:
        case (True, False, False):
            with tqdm(total=4) as pbar:
                logging.info('Generation keys\n')
                generating_keys(settings, pbar)
        case (False, True, False):
            with tqdm(total=2) as pbar:
                logging.info('Encryption the file\n')
                encrypting(settings, pbar)
        case (False, False, True):
            with tqdm(total=2) as pbar:
                logging.info('Decryption the file\n')
                decrypting(settings, pbar)
        case _:
            logging.error("wrong mode")