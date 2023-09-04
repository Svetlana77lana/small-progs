Кодировки - теория

* encoding - кодирование для передачи инфы.
* decoding - докодирование в читаемый вид для получателя

- Unicode (or Universal Coded Character Set) Transformation Format
- UTF-8 (8-bit Unicode Transformation Format)
UTF-8 - это один из форматов Unicod. 8 бит
- BOM (byte order mark)

в cp1251 (он же windows-1251) нету псевдографических символов.

UTF-8 - это cp65001. псевдографика есть.

Пример:
* Python отдает Bytearray в какой-то кодировке, МТ декодирует согласно кодеку,
который задан в БД для этого теста.
