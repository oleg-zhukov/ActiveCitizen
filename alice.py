from flask import  request
import logging
import json
from data import db_session
from data.calls import Call

logging.basicConfig(level=logging.INFO)

sessionStorage = {}

SERVICES = {"fire": "пожарная охрана", "police": "полиция", "ambulance":  "скорая помощь"}


def call_process():
    logging.info(f'Request: {request.json!r}')
    # Начинаем формировать ответ, согласно документации
    # мы собираем словарь, который потом при помощи
    # библиотеки json преобразуем в JSON и отдадим Алисе
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }

    # Отправляем request.json и response в функцию handle_dialog.
    # Она сформирует оставшиеся поля JSON, которые отвечают
    # непосредственно за ведение диалога
    handle_dialog(request.json, response)

    logging.info(f'Response:  {response!r}')

    # Преобразовываем в JSON и возвращаем
    return json.dumps(response, ensure_ascii=False, indent = 2)


def handle_dialog(req, res):
    user_id = req['session']['user_id']

    if req['session']['new']:
        # Это новый пользователь.
        # Инициализируем сессию и поприветствуем его.
        sessionStorage[user_id] = {
            'message': '',
            'address': ''
        }
        # Заполняем текст ответа
        res['response']['text'] = 'Вы обратились в Единую дежурно-диспетчерскую службу 112. Кратко расскажите, что случилось!'
        return

    # Сюда дойдем, если пользователь не новый,
    # и разговор с Алисой уже был начат
    # Обрабатываем ответ пользователя.
    # Это может быть сообщение - тогда нужно его запомнить и спросить адрес
    # Если сообщение меньше 8 токенов переспрашиваем

    if not sessionStorage[user_id]['message']:
        if len(req['request']['nlu']['tokens']) < 8:
            res['response']['text'] = 'Пожалуйста, опишите происшествие немного подробнее'
        else:
            sessionStorage[user_id]['message'] = req['request']['original_utterance']
            res['response']['text'] = 'Сообщите точный адрес происшествия'
        return
    else:
        if check_address(req):
            sessionStorage[user_id]['address'] = req['request']['original_utterance']
            # создать вызов
            call = Call()
            call.message = sessionStorage[user_id]['message']
            call.address = sessionStorage[user_id]['address']
            try:
                call.recognize_call()
            except:
                res['response']['text'] = f'Пожалуйста, уточните адрес. Возможно вы ошиблись или не указали полное название населенного пункта'
            else:
                db_sess = db_session.create_session()
                db_sess.add(call)
                db_sess.commit()
                res['response']['text'] = f'Вызов принят. К Вам отправилась {SERVICES[call.service]} по адресу: {call.address}'
                res['response']['end_session'] = True
        else:
            res['response']['text'] = f'Пожалуйста, уточните адрес. Возможно вы ошиблись или не указали полное название населенного пункта'
        return


def check_address(req):
    for entity in req['request']['nlu']['entities']:
        if entity['type'] == 'YANDEX.GEO':
            if 'city' in entity['value'] and 'street' in entity['value'] and 'house_number' in entity['value']:
                return True
    return False
