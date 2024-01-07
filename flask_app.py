# Импорт необходимых библиотек из Flask
from flask import Flask, render_template, request, jsonify

# Создание экземпляра Flask-приложения
app = Flask(__name__)

# Маршрут для главной страницы
@app.route('/')
def index():
    # Отображение HTML-шаблона index.html при обращении к корневому URL
    return render_template('index.html')

# Маршрут для обработки действия (например, нажатия на кнопку)
@app.route('/perform_action', methods=['POST'])
def perform_action():
    # Простое логирование в консоль сервера
    print("ok")
    # Отправка JSON-ответа обратно на клиент
    return jsonify(result="Действие выполнено!")

# Маршрут для расчета квадрата числа
@app.route('/square', methods=['POST'])
def square():
    # Получение числа из данных формы, отправленных клиентом
    number = int(request.form.get('number', 0))
    # Расчет квадрата числа и отправка результата обратно клиенту в формате JSON
    return jsonify(result=number ** 2)

# Запуск приложения на всех интерфейсах (0.0.0.0) на порту 80
app.run(host="0.0.0.0", port=80)
