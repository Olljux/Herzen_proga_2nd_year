class SecretDocument:  # Сервис, выполняет основную логику
    def read(self):
        return "Секретная информация."

class ProxyDocument:   # Заместитель, контролирует доступ к сервису
    def __init__(self, password):
        # Прокси хранит пароль и создаёт реальный объект
        self._password = password
        self._real_document = SecretDocument()  # Прокси хранит ссылку на сервис

    def read(self, input_password):
        # Проверка пароля перед передачей запроса реальному объекту
        if input_password == self._password:
            return "Доступ разрешён. " + self._real_document.read()  # Прокси делегирует вызов сервису
        else:
            return "Доступ запрещён: неверный пароль."  # Прокси блокирует доступ

# Клиент взаимодействует с прокси, а не с реальным объектом
proxy = ProxyDocument("1234")

print(proxy.read("0000"))  # → Доступ запрещён
print(proxy.read("1234"))  # → Доступ разрешён





