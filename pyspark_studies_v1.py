# Databricks notebook source
# MAGIC %sql
# MAGIC DROP TABLE students;
# MAGIC DROP TABLE marks;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE students(name VARCHAR(64), address VARCHAR(64), student_id INT) PARTITIONED BY (student_id);
# MAGIC CREATE TABLE marks(student_id INT, subject_id VARCHAR(12), exam_date DATE, points NUMERIC(8,2), mark INT) PARTITIONED BY (student_id)

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO students VALUES 
# MAGIC ('Amy Smith', '123 Park Ave, San Jose', 1),
# MAGIC ('Bob Brown', '456 Taylor St, Cupertino', 4),
# MAGIC ('Cathy Johnson', '789 Race Ave, Palo Alto', 2),
# MAGIC ('Gwyneth Zhao', '120 Main St, Rockport', 5),
# MAGIC ('Jackson Peterson', DEFAULT, 3)

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Formula in excel to create the values
# MAGIC -- date values from date cells: ="DATE'"&TEXT(A4,"yyyy-mm-dd")&"'"
# MAGIC -- all values for the marks table: ="("&B4&",'"&C4&"',"&D4&","&TEXT(E4,"##.00")&","&F4&"),"
# MAGIC INSERT INTO marks VALUES
# MAGIC (1,'h123',DATE'2019-05-21',50.88,4),
# MAGIC (1,'g54',DATE'2019-05-22',77.72,4),
# MAGIC (1,'jy765',DATE'2019-06-01',96.78,5),
# MAGIC (1,'234t',DATE'2019-06-01',35.51,4),
# MAGIC (2,'g54',DATE'2019-05-21',92.36,5),
# MAGIC (2,'234t',DATE'2019-05-22',84.25,4),
# MAGIC (3,'g54',DATE'2019-06-01',36.80,3),
# MAGIC (3,'234t',DATE'2019-06-01',35.92,4),
# MAGIC (3,'r543',DATE'2019-05-21',24.71,2),
# MAGIC (4,'g54',DATE'2019-05-22',42.80,3),
# MAGIC (4,'r543',DATE'2019-05-21',82.58,4),
# MAGIC (4,'234t',DATE'2019-05-22',95.59,4),
# MAGIC (5,'g54',DATE'2019-06-01',99.50,4)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM students

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM marks
