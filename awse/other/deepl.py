import logging
from random import randint
from time import time

import regex
import requests_cache

logger = logging.getLogger(__name__)
session = requests_cache.CachedSession(backend='memory', cache_name='deepl_get', expire_after=259200)


def translate_text(text, lang=None, lang_to='EN') -> str:
    """
    Translate text
    :param text: text string
    :param lang: original lang (optional)
    :param lang_to: exit text
    :return: translated text
    """
    for _ in range(1):  # Делаем только одну попытку
        if not lang:
            lang = "auto"
        json_body = {
            "jsonrpc": "2.0",
            "method": "LMT_handle_jobs",
            "params": {
                "jobs": [
                    {
                        "kind": "default",
                        "raw_en_sentence": str(text),
                        "raw_en_context_before": [
                        ],
                        "raw_en_context_after": [
                        ],
                        "preferred_num_beams": 4,
                        "quality": "fast"
                    }
                ],
                "lang": {
                    "user_preferred_langs": [
                        "DE",
                        "RU",
                        "EN"
                    ],
                    "source_lang_user_selected": lang,
                    "target_lang": lang_to
                },
                "priority": -1,
                "commonJobParams": {
                },
                "timestamp": int(str(time()).replace('.', '')[:13])
            },
            "id": randint(1000000, 9999999)
        }
        headers = {
            "Content-Type": "application/json",
            "Content-Length": str(len(str(json_body))),
            "cache-control": "no-cache",
            "origin": "https://www.deepl.com",
            "pragma": "no-cache",
            "referer": "https://www.deepl.com/",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4491.6 Safari/537.36",
        }
        host_api = 'https://www2.deepl.com/jsonrpc'
        cookies_get = session.post(
            host_api, headers=headers, json=json_body,
        ).headers['Set-Cookie']
        cookies_get = {
            'cookie': cookies_get
        }
        headers.update(cookies_get)
        data = session.post(
            host_api, headers=headers, json=json_body,
        )
        logger.warning("%s\n%s" % (data.text[:128], headers))
        return data.json()['result']['translations'][0]['beams'][0]['postprocessed_sentence']


def latin_detect(text) -> str:
    """
    Detect latin text and translate
    :param text: text string
    :return: translated text (to russian)
    """
    result = regex.sub(r'[^.,-`\'":;\?! \p{Latin}]', '', text)
    latin_words = regex.sub(r'[^\p{Latin}]', '', text)
    if result and latin_words:
        return translate_text(result, lang_to="RU")


def cyrillic_detect(text) -> str:
    """
    Detect cyrillic text and translate
    :param text: text string
    :return: translated text (to english)
    """
    result = regex.sub(r'[^.,-!?:;\p{Cyrillic}]', '', text)
    return translate_text(result)


def translate_simple(text) -> str:
    """
    Auto translate detect function
    :param text: text string
    :return: result (String)
    """
    if text:
        try:
            latin = latin_detect(text)
            if latin:
                return latin
        except Exception as e:
            logger.warning(e)
