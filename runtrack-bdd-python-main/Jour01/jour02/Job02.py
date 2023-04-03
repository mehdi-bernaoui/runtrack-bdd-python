# mysql> create table etage (
#     -> id int primary key auto_increment,
#     -> nom varchar(255),
#     -> numero int,
#     -> superficie int
#     -> );
# Query OK, 0 rows affected (0.08 sec)
#
# mysql> select * from etage
#     -> ;
# Empty set (0.01 sec)
#
# mysql> show tables;
# +------------------------+
# | Tables_in_laplateforme |
# +------------------------+
# | etage                  |
# | etudiants              |
# +------------------------+
# 2 rows in set (0.01 sec)
#
# mysql> show fields from etage;
# +------------+--------------+------+-----+---------+----------------+
# | Field      | Type         | Null | Key | Default | Extra          |
# +------------+--------------+------+-----+---------+----------------+
# | id         | int          | NO   | PRI | NULL    | auto_increment |
# | nom        | varchar(255) | YES  |     | NULL    |                |
# | numero     | int          | YES  |     | NULL    |                |
# | superficie | int          | YES  |     | NULL    |                |
# +------------+--------------+------+-----+---------+----------------+
# 4 rows in set (0.01 sec)
#
# mysql> create table salles (
#     -> id int primary key auto_increment,
#     -> nom varchar(255),
#     -> id_etage int,
#     -> capacite int
#     -> );
# Query OK, 0 rows affected (0.04 sec)
#
# mysql> show fields from salles;
# +----------+--------------+------+-----+---------+----------------+
# | Field    | Type         | Null | Key | Default | Extra          |
# +----------+--------------+------+-----+---------+----------------+
# | id       | int          | NO   | PRI | NULL    | auto_increment |
# | nom      | varchar(255) | YES  |     | NULL    |                |
# | id_etage | int          | YES  |     | NULL    |                |
# | capacite | int          | YES  |     | NULL    |                |
# +----------+--------------+------+-----+---------+----------------+
# 4 rows in set (0.01 sec)