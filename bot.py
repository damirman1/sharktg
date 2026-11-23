import os 
import requests
from flask import Flask, request
from google import genai

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", "")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")

GEMINI_MODEL = "gemini-3.5-flash-lite"

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def home():
    return "Startup Shark Bot is running!", 200
    # tpc/ip --> 
    # udp -->
    
    # 1xx --> информационные
    # 100 Continue --> сервер получил начало запроса
    # и ждет остальную часть данных
    # 101 --> Switch Protocols --> серер готов сменить протокол
    
    # 2xx
    # 200 --> OK --> УСПЕШНЫЙ РЕЗУЛЬТАТ
    # 201 --> Created --> запрос выполнен, создан новый ресурс
    # 202 --> Accepted --> запрос принят в обработку, но еще не завершен
    # 204 --> Not Content --> запрос выполнен,  но тело ответа отсутствует 
    
    # 3хх --> перенапровление (редиректоры)
    # 302 --> Found --> временный перенос ресурса
    
    # 4xx --> Ошибки клиента
    # 400 --> Bad Request --> некорректный запрос
    # 401 --> Unauthorized --> требуется аутентификация
    # 403 --> Forbidden --> доступ к ресурсу запрещен, даже при наличии аутентификации
    # 404 --> Not Found --> запрошенный ресурс не найден
    # 408 --> Request Timeout --> сервер не дождался полного запроса под клиента за отведенное время
    # 429 --> Too Many Requests --> превышен лимит запросов за единицу время
    
    # 5хх --> Ошибки сервера 
    # 500 --> Internal Server Error --> внутренняя ошибка сервера
    # 502 --> Bad Gateway --> шлюз получил некорректный ответ от вышестоящего сервера
    # 503 --> Service Unavailable --> сервис временно недоступен: техработы, перезагрузка сервера

class StartupSharkBot:
    def __init__(self, author, idea, score, verdict, comment):
        self.author = author
        self.idea = idea
        self.score = score
        self.verdict = verdict
        self.comment = comment

    def format_card(self):
        return(
            f"СТАРТАП-ПИТЧ ОТ: {self.author}\n",
            f"Идея: {self.idea}\n\n",
            f"Оценка инвестора: {self.score}/100\n",
            f"Вердикт: {self.verdict}\n",
            f"Разбор от инвестора: {self.comment}"
        )
    