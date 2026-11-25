---
name: cascade-traceability
summary: Проверить двустороннюю причинную трассировку TOP → СРО → продукт → инициатива и назад.
---
# Cascade Traceability
Для каждого ребра составить `parent ID`, `child ID`, `mechanism of influence`, `shared observed quantity`, `evidence path`, `link grade` (DIRECT_MEASURED / DIRECT_PENDING / CONTRIBUTORY / HYPOTHESIS / NONE), `assumption`, `counter-evidence`, `owner`.
Два обхода: TOP→DOWN: у каждого заявленного KR СРО есть достижимые contributors; BOTTOM→UP: у каждого Product KR ясная стратегическая причина. Покажи orphan и dangling edges; если СРО обещает снизить длительность плохих решений, а команда только диагностирует, это GAP, а не DIRECT.
Отдельный флаг `causality_status`: `cooccurrence`, `expert_validated`, `counterfactual_validated`. Совпадение двух маркеров на одном событии не доказывает причинность. Число затронутых вычислений не равно числу уникальных решений, пока это не проверено. Технический uptime не обязательно отражает корректность бизнес-результата; клиентскую удовлетворённость следует подтверждать данными.
**Выход:** `traceability_matrix` + coverage_summary + gap register + предложенная поправка на конкретном уровне. Не ставить PASS по одному тематическому соответствию.
