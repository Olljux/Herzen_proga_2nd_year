from flask import Flask, render_template, request, redirect
from model import CurrencyRatesFetcher, CurrencyRate, SessionLocal

app = Flask(__name__)


fetcher = CurrencyRatesFetcher(['USD', 'EUR'])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        codes_str = request.form.get('codes')

        codes = [code.strip().upper() for code in codes_str.split(',')]
        fetcher.set_tracked(codes)
        try:
            fetcher.fetch_and_store()
        except Exception as e:
            return render_template('index.html', error=str(e), currencies=[])

        return redirect('/')


    session = SessionLocal()
    currencies = session.query(CurrencyRate).all()
    session.close()

    return render_template('index.html', currencies=currencies)


if __name__ == '__main__':
    app.run(debug=True)