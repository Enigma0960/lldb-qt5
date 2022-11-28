# lldb-qt5

## Description

В этом репозитории я выкладываю свою версию LLDB форматера для QT5.

## Install

Клонируем этот репозиторий, для удобства его можно поместить в папку `~/.lldb`. Создаем и открываем файл `~/.lldbinit` (если он уже есть, то просто открываем). Добавляем в него следующие строки, путь к файлам может отличаться:

```
command script import ~/.lldb/lldb-qt5/Qt5Formatters.py
command source ~/.lldb/lldb-qt5/Qt5Formatters.lldb
```

## Tested

Моя система:

- Kubuntu 22.10
- Qt 5.15.6
- LLDB 14.0.6