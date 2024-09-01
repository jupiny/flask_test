create database test_db;
create user 'testuser'@'%' identified by 'testuser123';
flush privileges;
show grants for testuser@'%';
grant all privileges on test_db.* to testuser@'%';
show grants for testuser@'%';
