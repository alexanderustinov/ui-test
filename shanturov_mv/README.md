программа калькулятор с двумя функциями,
написана под виндувс пользователя,
использует Tkinker

Теперь, чтобы установить и запустить пакет на другой машине:
1. Убедитесь, что Python установлен.
2. Установите пакет, выполнив следующую команду в командной строке (добавьте ключ --user для установки для текущего пользователя или выполните ее с правами администратора для установки глобально):

```
pip install -e path_to_calculator_package_directory
```

Замените `path_to_calculator_package_directory` на путь к каталогу вашего пакета на другой машине.

После установки вы можете выполнить ваш пакет в командной строке:

```
python -m calculator.calculator_app
```
