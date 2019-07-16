-- converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
--import DATABASE
USE hbtn_0c_0;
--converts field to utf-8 format
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4;
--converts table to utf-8 format
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

--converts database to utf-8 format
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
