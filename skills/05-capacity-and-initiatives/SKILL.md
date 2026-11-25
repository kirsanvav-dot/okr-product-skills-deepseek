---
name: capacity-and-initiatives
summary: Декомпозировать KR в укрупнённые инициативы и проверить загрузку по ролям и зависимости.
---
# Capacity & Initiatives
От KR → value milestone → инициативы → эпики (не stories; отдельный workflow позже). Для каждой: contributing KR, expected change, epic/owner, DoD measurable, dependencies, role capacity ranges, assumptions, risk, quarter, cut order. Не плодить микросервисы до проверки AS-IS архитектуры.
Ёмкость считать по ролям: N engineers × iterations × focus factor, отдельно backend/frontend/QA/PM/DevOps; не дублировать резерв RUN, если он уже в focus factor; не считать неоценённые эпики нулём; AI ускорение верифицировать net throughput, а не gross code typing.
Сценарии: base / conservative / stretch. При превышении 100% = CONDITIONAL или FAIL, пока не выбран scope cut. Для external dependency нужен fallback без обещаний чужого результата.
Не создавать автоматом epics в Jira; только экспортируемое предложение. **Выход:** таблица KR→инициативы→эпики, role capacity, dependency critical path, release gates, scope-cut.
