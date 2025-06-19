from sqlalchemy import create_engine, Column, Float, String
from sqlalchemy.orm import declarative_base, sessionmaker
import requests
import datetime

Base = declarative_base()
engine = create_engine("sqlite:///currency.db", echo=False)
SessionLocal = sessionmaker(bind=engine)


class CurrencyRate(Base):
    __tablename__ = 'currency_rates'
    id = Column(String(3), primary_key=True)  # код валюты
    datetime = Column(String(20), default="")
    value = Column(Float)


class CurrencyRatesFetcher:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CurrencyRatesFetcher, cls).__new__(cls)
        return cls._instance

    def __init__(self, tracked=['USD', 'EUR', 'GBP']):
        self.tracked = tracked
        Base.metadata.create_all(engine)

    def set_tracked(self, codes):
        self.tracked = list(set(codes))

    def get_rates(self):
        session = SessionLocal()
        rates = session.query(CurrencyRate).all()
        session.close()
        return rates

    def fetch_and_store(self):
        url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()['Valute']
        except Exception as e:
            print("Ошибка при получении данных от ЦБ РФ:", e)
            raise

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        session = SessionLocal()
        for code in self.tracked:
            if code in data:
                value = float(data[code]['Value'])
                obj = session.query(CurrencyRate).filter_by(id=code).first()
                if obj:
                    obj.value = value
                    obj.datetime = now
                else:
                    session.add(CurrencyRate(id=code, value=value, datetime=now))
        session.commit()
        session.close()