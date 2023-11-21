-- 建立資料表
CREATE TABLE IF NOT EXISTS policyholders (
    code TEXT NOT NULL,
    name TEXT,
    registration_date DATE NOT NULL,
    introducer_code TEXT,
    tree_parent_code TEXT,
    tree_left_code TEXT,
    tree_right_code TEXT,
    FOREIGN KEY (introducer_code) REFERENCES policyholders(code)
);

-- 建立索引
CREATE INDEX IF NOT EXISTS idx_policyholders ON policyholders (code);

-- 建立10筆資料
INSERT INTO policyholders (code, name, registration_date, tree_left_code, tree_right_code) VALUES("0000000001", "保戶1", "2023-11-21", "0000000002", "0000000003");
INSERT INTO policyholders (code, name, registration_date, introducer_code, tree_parent_code, tree_left_code, tree_right_code) VALUES("0000000002", "保戶2", "2023-11-22", "0000000001", "0000000001", "0000000004", "0000000005");
INSERT INTO policyholders (code, name, registration_date, introducer_code, tree_parent_code, tree_left_code, tree_right_code) VALUES("0000000003", "保戶3", "2023-11-23", "0000000001", "0000000001", "0000000006", "0000000007");
INSERT INTO policyholders (code, name, registration_date, introducer_code, tree_parent_code, tree_left_code, tree_right_code) VALUES("0000000004", "保戶4", "2023-11-24", "0000000001", "0000000002", "0000000008", "0000000009");
INSERT INTO policyholders (code, name, registration_date, introducer_code, tree_parent_code) VALUES("0000000005", "保戶5", "2023-11-25", "0000000002", "0000000002");
INSERT INTO policyholders (code, name, registration_date, introducer_code, tree_parent_code) VALUES("0000000006", "保戶6", "2023-11-26", "0000000003", "0000000003");
INSERT INTO policyholders (code, name, registration_date, introducer_code, tree_parent_code) VALUES("0000000007", "保戶7", "2023-11-27", "0000000003", "0000000003");
INSERT INTO policyholders (code, name, registration_date, introducer_code, tree_parent_code) VALUES("0000000008", "保戶8", "2023-11-28", "0000000001", "0000000004");
INSERT INTO policyholders (code, name, registration_date, introducer_code, tree_parent_code, tree_left_code) VALUES("0000000009", "保戶9", "2023-11-29", "0000000004", "0000000004", "0000000010");
INSERT INTO policyholders (code, name, registration_date, introducer_code, tree_parent_code) VALUES("0000000010", "保戶10", "2023-11-30", "0000000009", "0000000009");
