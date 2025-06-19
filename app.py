from flask import Flask, render_template, request, redirect
from model import CurrencyRatesFetcher, CurrencyRate, SessionLocal

app = Flask(__name__)  # создаем Flask-приложение

# создаем объект нашей модели (синглтон)
fetcher = CurrencyRatesFetcher(['USD', 'EUR'])  # начальный список валют

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # получаем список валют от пользователя
        codes_str = request.form.get('codes')  # строка типа "USD, EUR, GBP"
        # Разделяем, убираем пробелы и переводим в верхний регистр
        codes = [code.strip().upper() for code in codes_str.split(',')]
        fetcher.set_tracked(codes)  # обновляем список валют
        try:
            fetcher.fetch_and_store()  # запрашиваем данные с ЦБ
        except Exception as e:
            return render_template('index.html', error=str(e), currencies=[])

        return redirect('/')  # перезагружаем страницу

    # читаем данные из базы данных
    session = SessionLocal()
    currencies = session.query(CurrencyRate).all()
    session.close()

    return render_template('index.html', currencies=currencies)


if __name__ == '__main__':
    app.run(debug=True)