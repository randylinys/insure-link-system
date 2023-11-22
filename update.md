### Question

1. 在不限資料庫的情況下，如何不用程式的 recursive 透過 SQL 快速找出 4 層的組織樹?
2. 如果一個人的組織有 100+  層以上的時後，如何快速取得左線或右線的人數?

### sql重建(以下使用postgresql)
```sql
-- 建立資料表
CREATE TABLE IF NOT EXISTS policyholders (
    code TEXT UNIQUE,
    name TEXT,
    registration_date DATE NOT NULL,
    introducer_code TEXT,
    tree_child_direction TEXT,
    FOREIGN KEY (introducer_code) REFERENCES policyholders(code)
);

-- 建立索引
CREATE INDEX IF NOT EXISTS idx_policyholders ON policyholders (code);

-- 建立10筆資料
INSERT INTO policyholders (code, name, registration_date) VALUES("0000000001", "保戶1", "2023-11-21");
INSERT INTO policyholders (code, name, registration_date, introducer_code, tree_child_direction) VALUES("0000000002", "保戶2", "2023-11-22", "0000000001", "left");
INSERT INTO policyholders (code, name, registration_date, introducer_code, tree_child_direction) VALUES("0000000003", "保戶3", "2023-11-23", "0000000001", "right");
INSERT INTO policyholders (code, name, registration_date, introducer_code, tree_child_direction) VALUES("0000000004", "保戶4", "2023-11-24", "0000000002", "left");
INSERT INTO policyholders (code, name, registration_date, introducer_code, tree_child_direction) VALUES("0000000005", "保戶5", "2023-11-25", "0000000002", "right");
INSERT INTO policyholders (code, name, registration_date, introducer_code, tree_child_direction) VALUES("0000000006", "保戶6", "2023-11-26", "0000000003", "left");
INSERT INTO policyholders (code, name, registration_date, introducer_code, tree_child_direction) VALUES("0000000007", "保戶7", "2023-11-27", "0000000003", "right");
INSERT INTO policyholders (code, name, registration_date, introducer_code, tree_child_direction) VALUES("0000000008", "保戶8", "2023-11-28", "0000000004", "left");
INSERT INTO policyholders (code, name, registration_date, introducer_code, tree_child_direction) VALUES("0000000009", "保戶9", "2023-11-29", "0000000004", "right");
INSERT INTO policyholders (code, name, registration_date, introducer_code, tree_child_direction) VALUES("0000000010", "保戶10", "2023-11-30", "0000000009", "left");
```

### 給定code，取出階層4以內的保戶清單(以0000000001為例)
```sql
WITH RECURSIVE Tree AS (
    SELECT code, name, registration_date, introducer_code, 1 AS level
    FROM policyholders
    WHERE code = '0000000001'
    UNION
    SELECT p.code, p.name, p.registration_date, p.introducer_code, t.level+1
    FROM policyholders AS p
    JOIN Tree AS t ON p.introducer_code = t.code
)
SELECT code, name, registration_date, introducer_code FROM Tree WHERE level <= 4 ORDER BY introducer_code NULLS FIRST;
```

### 給定code，取出上階節點的階層4以內保戶清單(以0000000004為例)
```sql
WITH RECURSIVE Tree AS (
    SELECT code, name, registration_date, introducer_code, 1 AS level
    FROM policyholders
    WHERE code = (SELECT introducer_code FROM policyholders WHERE code = '0000000004')
    UNION
    SELECT p.code, p.name, p.registration_date, p.introducer_code, t.level+1
    FROM policyholders AS p
    JOIN Tree AS t ON p.introducer_code = t.code
)
SELECT code, name, registration_date, introducer_code FROM Tree WHERE level <= 4 ORDER BY introducer_code NULLS FIRST;
```

### 給定code，取出左線或右線的人數(以0000000002為例，取出左線總數)
```sql
WITH RECURSIVE Tree AS (
    SELECT code, name, registration_date, introducer_code, 1 AS level
    FROM policyholders
    WHERE code = (SELECT code FROM policyholders WHERE introducer_code = '0000000002' AND tree_child_direction = 'left')
    UNION
    SELECT p.code, p.name, p.registration_date, p.introducer_code, t.level+1
    FROM policyholders AS p
    JOIN Tree AS t ON p.introducer_code = t.code
)
SELECT COUNT(*) FROM Tree;
```