/*
Navicat SQLite Data Transfer

Source Server         : food_manage
Source Server Version : 30714
Source Host           : :0

Target Server Type    : SQLite
Target Server Version : 30714
File Encoding         : 65001

Date: 2017-11-24 09:45:12
*/

PRAGMA foreign_keys = OFF;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS "main"."auth_group";
CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(80) NOT NULL UNIQUE);

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS "main"."auth_group_permissions";
CREATE TABLE "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id"), "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"));

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS "main"."auth_permission";
CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id"), "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO "main"."auth_permission" VALUES (1, 1, 'add_logentry', 'Can add log entry');
INSERT INTO "main"."auth_permission" VALUES (2, 1, 'change_logentry', 'Can change log entry');
INSERT INTO "main"."auth_permission" VALUES (3, 1, 'delete_logentry', 'Can delete log entry');
INSERT INTO "main"."auth_permission" VALUES (4, 2, 'add_permission', 'Can add permission');
INSERT INTO "main"."auth_permission" VALUES (5, 2, 'change_permission', 'Can change permission');
INSERT INTO "main"."auth_permission" VALUES (6, 2, 'delete_permission', 'Can delete permission');
INSERT INTO "main"."auth_permission" VALUES (7, 3, 'add_group', 'Can add group');
INSERT INTO "main"."auth_permission" VALUES (8, 3, 'change_group', 'Can change group');
INSERT INTO "main"."auth_permission" VALUES (9, 3, 'delete_group', 'Can delete group');
INSERT INTO "main"."auth_permission" VALUES (10, 4, 'add_user', 'Can add user');
INSERT INTO "main"."auth_permission" VALUES (11, 4, 'change_user', 'Can change user');
INSERT INTO "main"."auth_permission" VALUES (12, 4, 'delete_user', 'Can delete user');
INSERT INTO "main"."auth_permission" VALUES (13, 5, 'add_contenttype', 'Can add content type');
INSERT INTO "main"."auth_permission" VALUES (14, 5, 'change_contenttype', 'Can change content type');
INSERT INTO "main"."auth_permission" VALUES (15, 5, 'delete_contenttype', 'Can delete content type');
INSERT INTO "main"."auth_permission" VALUES (16, 6, 'add_session', 'Can add session');
INSERT INTO "main"."auth_permission" VALUES (17, 6, 'change_session', 'Can change session');
INSERT INTO "main"."auth_permission" VALUES (18, 6, 'delete_session', 'Can delete session');
INSERT INTO "main"."auth_permission" VALUES (19, 7, 'add_table_manage', 'Can add table_manage');
INSERT INTO "main"."auth_permission" VALUES (20, 7, 'change_table_manage', 'Can change table_manage');
INSERT INTO "main"."auth_permission" VALUES (21, 7, 'delete_table_manage', 'Can delete table_manage');
INSERT INTO "main"."auth_permission" VALUES (22, 8, 'add_table_status', 'Can add table_status');
INSERT INTO "main"."auth_permission" VALUES (23, 8, 'change_table_status', 'Can change table_status');
INSERT INTO "main"."auth_permission" VALUES (24, 8, 'delete_table_status', 'Can delete table_status');
INSERT INTO "main"."auth_permission" VALUES (25, 9, 'add_user_group', 'Can add user_group');
INSERT INTO "main"."auth_permission" VALUES (26, 9, 'change_user_group', 'Can change user_group');
INSERT INTO "main"."auth_permission" VALUES (27, 9, 'delete_user_group', 'Can delete user_group');
INSERT INTO "main"."auth_permission" VALUES (28, 10, 'add_user_info', 'Can add user_info');
INSERT INTO "main"."auth_permission" VALUES (29, 10, 'change_user_info', 'Can change user_info');
INSERT INTO "main"."auth_permission" VALUES (30, 10, 'delete_user_info', 'Can delete user_info');
INSERT INTO "main"."auth_permission" VALUES (31, 11, 'add_food_manage', 'Can add food_manage');
INSERT INTO "main"."auth_permission" VALUES (32, 11, 'change_food_manage', 'Can change food_manage');
INSERT INTO "main"."auth_permission" VALUES (33, 11, 'delete_food_manage', 'Can delete food_manage');
INSERT INTO "main"."auth_permission" VALUES (34, 12, 'add_foodtype_manage', 'Can add foodtype_manage');
INSERT INTO "main"."auth_permission" VALUES (35, 12, 'change_foodtype_manage', 'Can change foodtype_manage');
INSERT INTO "main"."auth_permission" VALUES (36, 12, 'delete_foodtype_manage', 'Can delete foodtype_manage');
INSERT INTO "main"."auth_permission" VALUES (37, 13, 'add_food_choose', 'Can add food_choose');
INSERT INTO "main"."auth_permission" VALUES (38, 13, 'change_food_choose', 'Can change food_choose');
INSERT INTO "main"."auth_permission" VALUES (39, 13, 'delete_food_choose', 'Can delete food_choose');
INSERT INTO "main"."auth_permission" VALUES (40, 14, 'add_order', 'Can add order');
INSERT INTO "main"."auth_permission" VALUES (41, 14, 'change_order', 'Can change order');
INSERT INTO "main"."auth_permission" VALUES (42, 14, 'delete_order', 'Can delete order');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS "main"."auth_user";
CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "username" varchar(150) NOT NULL UNIQUE);

-- ----------------------------
-- Records of auth_user
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS "main"."auth_user_groups";
CREATE TABLE "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "group_id" integer NOT NULL REFERENCES "auth_group" ("id"));

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS "main"."auth_user_user_permissions";
CREATE TABLE "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"));

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for backapp_foodtype_manage
-- ----------------------------
DROP TABLE IF EXISTS "main"."backapp_foodtype_manage";
CREATE TABLE "backapp_foodtype_manage" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "foodtypename" varchar(32) NOT NULL);

-- ----------------------------
-- Records of backapp_foodtype_manage
-- ----------------------------
INSERT INTO "main"."backapp_foodtype_manage" VALUES (3, '西北菜');
INSERT INTO "main"."backapp_foodtype_manage" VALUES (4, '粤菜');

-- ----------------------------
-- Table structure for backapp_food_choose
-- ----------------------------
DROP TABLE IF EXISTS "main"."backapp_food_choose";
CREATE TABLE "backapp_food_choose" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "food_cho_id" integer NOT NULL REFERENCES "backapp_food_manage" ("id"), "order_n_id" integer NOT NULL REFERENCES "backapp_order" ("id"), "ou_id" integer NOT NULL, "food_count" integer NOT NULL);

-- ----------------------------
-- Records of backapp_food_choose
-- ----------------------------
INSERT INTO "main"."backapp_food_choose" VALUES (15, 8, 17, 2017112211483211, 1);
INSERT INTO "main"."backapp_food_choose" VALUES (16, 8, 18, 2017112211494441, 2);

-- ----------------------------
-- Table structure for backapp_food_manage
-- ----------------------------
DROP TABLE IF EXISTS "main"."backapp_food_manage";
CREATE TABLE "backapp_food_manage" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "foodname" varchar(16) NOT NULL, "price" decimal NOT NULL, "foodtype_id" integer NOT NULL REFERENCES "backapp_foodtype_manage" ("id"), "vip_price" decimal NOT NULL);

-- ----------------------------
-- Records of backapp_food_manage
-- ----------------------------
INSERT INTO "main"."backapp_food_manage" VALUES (8, '酱猪蹄', 22, 3, 19);

-- ----------------------------
-- Table structure for backapp_order
-- ----------------------------
DROP TABLE IF EXISTS "main"."backapp_order";
CREATE TABLE "backapp_order" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "table_id" integer NOT NULL REFERENCES "backapp_table_manage" ("id"), "all_price" decimal NOT NULL, "vip_type" integer NOT NULL, "orderstatus" integer NOT NULL, "ou_id" integer NOT NULL, "ordertime" datetime NOT NULL);

-- ----------------------------
-- Records of backapp_order
-- ----------------------------
INSERT INTO "main"."backapp_order" VALUES (17, 4, 19, 1, 0, 2017112211483211, '2017-11-21 11:12:22');
INSERT INTO "main"."backapp_order" VALUES (18, 8, 44, 0, 1, 2017112211494441, '2017-11-22 11:12:22');

-- ----------------------------
-- Table structure for backapp_table_manage
-- ----------------------------
DROP TABLE IF EXISTS "main"."backapp_table_manage";
CREATE TABLE "backapp_table_manage" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "tablename" varchar(32) NOT NULL);

-- ----------------------------
-- Records of backapp_table_manage
-- ----------------------------
INSERT INTO "main"."backapp_table_manage" VALUES (4, '中顺');
INSERT INTO "main"."backapp_table_manage" VALUES (8, '吉祥');

-- ----------------------------
-- Table structure for backapp_user_group
-- ----------------------------
DROP TABLE IF EXISTS "main"."backapp_user_group";
CREATE TABLE "backapp_user_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "groupname" varchar(12) NOT NULL);

-- ----------------------------
-- Records of backapp_user_group
-- ----------------------------
INSERT INTO "main"."backapp_user_group" VALUES (1, 'admin');
INSERT INTO "main"."backapp_user_group" VALUES (2, 'waiter');

-- ----------------------------
-- Table structure for backapp_user_info
-- ----------------------------
DROP TABLE IF EXISTS "main"."backapp_user_info";
CREATE TABLE "backapp_user_info" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "username" varchar(16) NOT NULL, "password" varchar(32) NOT NULL, "email" varchar(32) NOT NULL, "grouptype_id" integer NOT NULL REFERENCES "backapp_user_group" ("id"));

-- ----------------------------
-- Records of backapp_user_info
-- ----------------------------
INSERT INTO "main"."backapp_user_info" VALUES (1, 'temp', 123, 'temp@qq.com', 1);
INSERT INTO "main"."backapp_user_info" VALUES (4, 'phpcms', 123, 'w1@ct.cn', 2);
INSERT INTO "main"."backapp_user_info" VALUES (8, 'zhangsi', 123456, 'zhangsi@qq.com', 2);
INSERT INTO "main"."backapp_user_info" VALUES (9, 'wangwu', 123, 'wangwu@163.com', 1);

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS "main"."django_admin_log";
CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL, "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id"), "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "action_time" datetime NOT NULL);

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS "main"."django_content_type";
CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO "main"."django_content_type" VALUES (1, 'admin', 'logentry');
INSERT INTO "main"."django_content_type" VALUES (2, 'auth', 'permission');
INSERT INTO "main"."django_content_type" VALUES (3, 'auth', 'group');
INSERT INTO "main"."django_content_type" VALUES (4, 'auth', 'user');
INSERT INTO "main"."django_content_type" VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO "main"."django_content_type" VALUES (6, 'sessions', 'session');
INSERT INTO "main"."django_content_type" VALUES (7, 'backapp', 'table_manage');
INSERT INTO "main"."django_content_type" VALUES (8, 'backapp', 'table_status');
INSERT INTO "main"."django_content_type" VALUES (9, 'backapp', 'user_group');
INSERT INTO "main"."django_content_type" VALUES (10, 'backapp', 'user_info');
INSERT INTO "main"."django_content_type" VALUES (11, 'backapp', 'food_manage');
INSERT INTO "main"."django_content_type" VALUES (12, 'backapp', 'foodtype_manage');
INSERT INTO "main"."django_content_type" VALUES (13, 'backapp', 'food_choose');
INSERT INTO "main"."django_content_type" VALUES (14, 'backapp', 'order');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS "main"."django_migrations";
CREATE TABLE "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO "main"."django_migrations" VALUES (1, 'contenttypes', '0001_initial', '2017-09-18 15:46:01.720809');
INSERT INTO "main"."django_migrations" VALUES (2, 'auth', '0001_initial', '2017-09-18 15:46:01.749935');
INSERT INTO "main"."django_migrations" VALUES (3, 'admin', '0001_initial', '2017-09-18 15:46:01.771311');
INSERT INTO "main"."django_migrations" VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2017-09-18 15:46:01.787863');
INSERT INTO "main"."django_migrations" VALUES (5, 'contenttypes', '0002_remove_content_type_name', '2017-09-18 15:46:01.810610');
INSERT INTO "main"."django_migrations" VALUES (6, 'auth', '0002_alter_permission_name_max_length', '2017-09-18 15:46:01.829827');
INSERT INTO "main"."django_migrations" VALUES (7, 'auth', '0003_alter_user_email_max_length', '2017-09-18 15:46:01.856163');
INSERT INTO "main"."django_migrations" VALUES (8, 'auth', '0004_alter_user_username_opts', '2017-09-18 15:46:01.890874');
INSERT INTO "main"."django_migrations" VALUES (9, 'auth', '0005_alter_user_last_login_null', '2017-09-18 15:46:01.928004');
INSERT INTO "main"."django_migrations" VALUES (10, 'auth', '0006_require_contenttypes_0002', '2017-09-18 15:46:01.948154');
INSERT INTO "main"."django_migrations" VALUES (11, 'auth', '0007_alter_validators_add_error_messages', '2017-09-18 15:46:01.997308');
INSERT INTO "main"."django_migrations" VALUES (12, 'auth', '0008_alter_user_username_max_length', '2017-09-18 15:46:02.025402');
INSERT INTO "main"."django_migrations" VALUES (13, 'backapp', '0001_initial', '2017-09-18 15:46:02.055781');
INSERT INTO "main"."django_migrations" VALUES (14, 'sessions', '0001_initial', '2017-09-18 15:46:02.069339');
INSERT INTO "main"."django_migrations" VALUES (15, 'backapp', '0002_auto_20170926_1405', '2017-11-16 09:37:52.535937');
INSERT INTO "main"."django_migrations" VALUES (16, 'backapp', '0003_auto_20170929_1645', '2017-11-16 09:37:52.568608');
INSERT INTO "main"."django_migrations" VALUES (17, 'backapp', '0004_order_detail', '2017-11-16 09:37:52.588210');
INSERT INTO "main"."django_migrations" VALUES (18, 'backapp', '0005_auto_20170930_1358', '2017-11-16 09:37:52.608515');
INSERT INTO "main"."django_migrations" VALUES (19, 'backapp', '0006_order_order_d', '2017-11-16 09:37:52.634947');
INSERT INTO "main"."django_migrations" VALUES (20, 'backapp', '0007_remove_order_order_d', '2017-11-16 09:37:52.659180');
INSERT INTO "main"."django_migrations" VALUES (21, 'backapp', '0008_order_detail', '2017-11-16 09:37:52.678352');
INSERT INTO "main"."django_migrations" VALUES (22, 'backapp', '0009_auto_20170930_1437', '2017-11-16 09:37:52.698378');
INSERT INTO "main"."django_migrations" VALUES (23, 'backapp', '0010_order_detail', '2017-11-16 09:37:52.720176');
INSERT INTO "main"."django_migrations" VALUES (24, 'backapp', '0011_auto_20170930_1452', '2017-11-16 09:37:52.742658');
INSERT INTO "main"."django_migrations" VALUES (25, 'backapp', '0012_remove_order_detail_food_cho', '2017-11-16 09:37:52.764395');
INSERT INTO "main"."django_migrations" VALUES (26, 'backapp', '0013_remove_order_detail_order_d', '2017-11-16 09:37:52.788350');
INSERT INTO "main"."django_migrations" VALUES (27, 'backapp', '0014_auto_20170930_1535', '2017-11-16 09:37:52.813445');
INSERT INTO "main"."django_migrations" VALUES (28, 'backapp', '0015_auto_20171110_1111', '2017-11-16 09:37:52.838335');
INSERT INTO "main"."django_migrations" VALUES (29, 'backapp', '0016_auto_20171110_1120', '2017-11-16 09:37:52.870059');
INSERT INTO "main"."django_migrations" VALUES (30, 'backapp', '0017_auto_20171110_1739', '2017-11-16 09:37:52.902276');
INSERT INTO "main"."django_migrations" VALUES (31, 'backapp', '0018_auto_20171113_0922', '2017-11-16 09:37:52.957771');
INSERT INTO "main"."django_migrations" VALUES (32, 'backapp', '0019_remove_order_order_s', '2017-11-16 09:37:52.984149');
INSERT INTO "main"."django_migrations" VALUES (33, 'backapp', '0020_remove_order_table', '2017-11-16 09:37:53.005691');
INSERT INTO "main"."django_migrations" VALUES (34, 'backapp', '0021_order_table', '2017-11-16 09:37:53.031398');
INSERT INTO "main"."django_migrations" VALUES (35, 'backapp', '0022_remove_order_table', '2017-11-16 09:37:53.053053');
INSERT INTO "main"."django_migrations" VALUES (36, 'backapp', '0023_auto_20171113_1131', '2017-11-16 09:37:53.079873');
INSERT INTO "main"."django_migrations" VALUES (37, 'backapp', '0024_auto_20171113_1131', '2017-11-16 09:37:53.105898');
INSERT INTO "main"."django_migrations" VALUES (38, 'backapp', '0025_auto_20171113_1147', '2017-11-16 09:37:53.132019');
INSERT INTO "main"."django_migrations" VALUES (39, 'backapp', '0026_auto_20171113_1148', '2017-11-16 09:37:53.154076');
INSERT INTO "main"."django_migrations" VALUES (40, 'backapp', '0027_auto_20171113_1346', '2017-11-16 09:37:53.185928');
INSERT INTO "main"."django_migrations" VALUES (41, 'backapp', '0028_auto_20171114_0912', '2017-11-16 09:37:53.215028');
INSERT INTO "main"."django_migrations" VALUES (42, 'backapp', '0029_table_manage_tlevel_type', '2017-11-16 09:37:53.236919');
INSERT INTO "main"."django_migrations" VALUES (43, 'backapp', '0030_auto_20171115_1439', '2017-11-16 09:37:53.280907');
INSERT INTO "main"."django_migrations" VALUES (44, 'backapp', '0031_auto_20171115_1447', '2017-11-16 09:37:53.300758');
INSERT INTO "main"."django_migrations" VALUES (45, 'backapp', '0032_remove_order_ordertime', '2017-11-16 09:37:53.331852');
INSERT INTO "main"."django_migrations" VALUES (46, 'backapp', '0033_order_ordertime', '2017-11-16 09:37:53.355812');
INSERT INTO "main"."django_migrations" VALUES (47, 'backapp', '0034_auto_20171115_1617', '2017-11-16 09:37:53.383805');
INSERT INTO "main"."django_migrations" VALUES (48, 'backapp', '0035_auto_20171115_1649', '2017-11-16 09:37:53.409870');
INSERT INTO "main"."django_migrations" VALUES (49, 'backapp', '0036_auto_20171116_0937', '2017-11-16 09:37:53.434454');
INSERT INTO "main"."django_migrations" VALUES (50, 'backapp', '0037_auto_20171120_0927', '2017-11-20 09:27:16.118737');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS "main"."django_session";
CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO "main"."django_session" VALUES ('jowzsj7gf77qf79ap7u3cp0le36sh5g7', 'NzVhODU1OTZjNDgwZTNlNThlMTI3OGZkYzhiNjY5ZmNkMmMyMWRmMTp7fQ==', '2017-10-03 11:29:24.097180');
INSERT INTO "main"."django_session" VALUES ('gowf0as4cvqi4lyuctgxsuig3d8zlmw2', 'NzVhODU1OTZjNDgwZTNlNThlMTI3OGZkYzhiNjY5ZmNkMmMyMWRmMTp7fQ==', '2017-10-03 16:23:46.709418');
INSERT INTO "main"."django_session" VALUES ('e6cx0l65511zsjgnff52bn1ruhxgxrwj', 'MTc5MTUyMWY3ZjcxMWMxOWFhMjI2NmVjMTcyNGM3NTJiMTNmMzUxNjp7InVzZXJuYW1lIjoidGVtcCIsImlzX2xvZ2luIjp0cnVlLCJfc2Vzc2lvbl9leHBpcnkiOjg2NDAwfQ==', '2017-11-17 09:35:42.190152');
INSERT INTO "main"."django_session" VALUES ('tlh5brjntmn7kyizsjcyejfl5d3heezd', 'Y2MxMjc0ODVkMDU2Y2UwZWI4MDUzMDFkMDU2YzU3Mzc4MWY4ZjM5Mjp7InVzZXJuYW1lIjoidGVtcCIsImlzX2xvZ2luIjp0cnVlLCJfc2Vzc2lvbl9leHBpcnkiOjYwNDgwMH0=', '2017-11-29 16:29:52.619252');
INSERT INTO "main"."django_session" VALUES ('0ci5k9shglqhcj71rzr55c8jue8edtpv', 'MTc5MTUyMWY3ZjcxMWMxOWFhMjI2NmVjMTcyNGM3NTJiMTNmMzUxNjp7InVzZXJuYW1lIjoidGVtcCIsImlzX2xvZ2luIjp0cnVlLCJfc2Vzc2lvbl9leHBpcnkiOjg2NDAwfQ==', '2017-11-18 14:55:03.103488');
INSERT INTO "main"."django_session" VALUES ('2lws6zpnxwba8sncau0btiwrsjcgisyq', 'ZjRiZWE2NTk2YmI4ZDFkZTkxYWU3ODFkZjM1YWIwOWVlYmM1OWMxNTp7InVzZXJuYW1lIjoicGhwY21zIiwiaXNfbG9naW4iOnRydWUsIl9zZXNzaW9uX2V4cGlyeSI6ODY0MDB9', '2017-11-23 16:42:11.425487');
INSERT INTO "main"."django_session" VALUES ('1572n7a24lwfht4qjdbdk5bn4fn3qbaf', 'Y2MxMjc0ODVkMDU2Y2UwZWI4MDUzMDFkMDU2YzU3Mzc4MWY4ZjM5Mjp7InVzZXJuYW1lIjoidGVtcCIsImlzX2xvZ2luIjp0cnVlLCJfc2Vzc2lvbl9leHBpcnkiOjYwNDgwMH0=', '2017-11-29 18:01:49.612281');

-- ----------------------------
-- Table structure for sqlite_sequence
-- ----------------------------
DROP TABLE IF EXISTS "main"."sqlite_sequence";
CREATE TABLE sqlite_sequence(name,seq);

-- ----------------------------
-- Records of sqlite_sequence
-- ----------------------------
INSERT INTO "main"."sqlite_sequence" VALUES ('django_migrations', 50);
INSERT INTO "main"."sqlite_sequence" VALUES ('django_admin_log', 0);
INSERT INTO "main"."sqlite_sequence" VALUES ('django_content_type', 14);
INSERT INTO "main"."sqlite_sequence" VALUES ('auth_permission', 42);
INSERT INTO "main"."sqlite_sequence" VALUES ('auth_user', 0);
INSERT INTO "main"."sqlite_sequence" VALUES ('backapp_user_group', 3);
INSERT INTO "main"."sqlite_sequence" VALUES ('backapp_user_info', 9);
INSERT INTO "main"."sqlite_sequence" VALUES ('backapp_food_manage', 9);
INSERT INTO "main"."sqlite_sequence" VALUES ('backapp_table_manage', 8);
INSERT INTO "main"."sqlite_sequence" VALUES ('backapp_foodtype_manage', 4);
INSERT INTO "main"."sqlite_sequence" VALUES ('backapp_food_choose', 16);
INSERT INTO "main"."sqlite_sequence" VALUES ('backapp_order', 18);

-- ----------------------------
-- Indexes structure for table auth_group_permissions
-- ----------------------------
CREATE INDEX "main"."auth_group_permissions_group_id_b120cbf9"
ON "auth_group_permissions" ("group_id" ASC);
CREATE UNIQUE INDEX "main"."auth_group_permissions_group_id_permission_id_0cd325b0_uniq"
ON "auth_group_permissions" ("group_id" ASC, "permission_id" ASC);
CREATE INDEX "main"."auth_group_permissions_permission_id_84c5c92e"
ON "auth_group_permissions" ("permission_id" ASC);

-- ----------------------------
-- Indexes structure for table auth_permission
-- ----------------------------
CREATE INDEX "main"."auth_permission_content_type_id_2f476e4b"
ON "auth_permission" ("content_type_id" ASC);
CREATE UNIQUE INDEX "main"."auth_permission_content_type_id_codename_01ab375a_uniq"
ON "auth_permission" ("content_type_id" ASC, "codename" ASC);

-- ----------------------------
-- Indexes structure for table auth_user_groups
-- ----------------------------
CREATE INDEX "main"."auth_user_groups_group_id_97559544"
ON "auth_user_groups" ("group_id" ASC);
CREATE INDEX "main"."auth_user_groups_user_id_6a12ed8b"
ON "auth_user_groups" ("user_id" ASC);
CREATE UNIQUE INDEX "main"."auth_user_groups_user_id_group_id_94350c0c_uniq"
ON "auth_user_groups" ("user_id" ASC, "group_id" ASC);

-- ----------------------------
-- Indexes structure for table auth_user_user_permissions
-- ----------------------------
CREATE INDEX "main"."auth_user_user_permissions_permission_id_1fbb5f2c"
ON "auth_user_user_permissions" ("permission_id" ASC);
CREATE INDEX "main"."auth_user_user_permissions_user_id_a95ead1b"
ON "auth_user_user_permissions" ("user_id" ASC);
CREATE UNIQUE INDEX "main"."auth_user_user_permissions_user_id_permission_id_14a6b632_uniq"
ON "auth_user_user_permissions" ("user_id" ASC, "permission_id" ASC);

-- ----------------------------
-- Indexes structure for table backapp_food_choose
-- ----------------------------
CREATE INDEX "main"."backapp_food_choose_food_cho_id_3c0957d1"
ON "backapp_food_choose" ("food_cho_id" ASC);
CREATE INDEX "main"."backapp_food_choose_order_n_id_ba07c49d"
ON "backapp_food_choose" ("order_n_id" ASC);

-- ----------------------------
-- Indexes structure for table backapp_food_manage
-- ----------------------------
CREATE INDEX "main"."backapp_food_manage_foodtype_id_269db5fb"
ON "backapp_food_manage" ("foodtype_id" ASC);

-- ----------------------------
-- Indexes structure for table backapp_order
-- ----------------------------
CREATE INDEX "main"."backapp_order_table_id_a711aede"
ON "backapp_order" ("table_id" ASC);

-- ----------------------------
-- Indexes structure for table backapp_user_info
-- ----------------------------
CREATE INDEX "main"."backapp_user_info_grouptype_id_a297571e"
ON "backapp_user_info" ("grouptype_id" ASC);

-- ----------------------------
-- Indexes structure for table django_admin_log
-- ----------------------------
CREATE INDEX "main"."django_admin_log_content_type_id_c4bce8eb"
ON "django_admin_log" ("content_type_id" ASC);
CREATE INDEX "main"."django_admin_log_user_id_c564eba6"
ON "django_admin_log" ("user_id" ASC);

-- ----------------------------
-- Indexes structure for table django_content_type
-- ----------------------------
CREATE UNIQUE INDEX "main"."django_content_type_app_label_model_76bd3d3b_uniq"
ON "django_content_type" ("app_label" ASC, "model" ASC);

-- ----------------------------
-- Indexes structure for table django_session
-- ----------------------------
CREATE INDEX "main"."django_session_expire_date_a5c62663"
ON "django_session" ("expire_date" ASC);
