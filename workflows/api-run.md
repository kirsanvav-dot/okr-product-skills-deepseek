# API execution example

```bash
python -m pip install openai openpyxl
python scripts/extract_xlsx.py 'OKR_2027.xlsx' > okr_source.txt
# Применять только в согласованном контуре. Файл будет отправлен на внешний API.
export DEEPSEEK_API_KEY='...'
python scripts/run_api.py --source okr_source.txt --stage 00-source-intake --out stage00.md --confirm-external-upload
# Просмотри вывод; исправь противоречия или сохрани approved_stage00.md
python scripts/run_api.py --source okr_source.txt --prior approved_stage00.md --stage 01-discovery-questions --out stage01.md --confirm-external-upload
```

Другие стадии запускаются аналогично. Для анализа пересечений обязательно добавь экспорт **общего** файла с чужими KR. Опция `--prior` передаёт только подтверждённые людьми результаты. Это намеренно не бесконтрольный автоматический агент.

`--model` — модель, доступная в вашем тарифе/аккаунте. Проверяйте актуальные идентификаторы и возможности по официальной документации.
