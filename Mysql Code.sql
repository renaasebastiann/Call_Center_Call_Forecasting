CREATE DATABASE call_center;
USE call_center;

CREATE TABLE call_data (
    call_id VARCHAR(100) NULL,
    agent VARCHAR(50) NULL,
    call_date DATE NULL,
    call_time TIME NULL,
    topic VARCHAR(100) NULL,
    answered ENUM('Y', 'N') NULL,
    resolved ENUM('Y', 'N') NULL,
    speed_of_answer_sec varchar(25) NULL,
    avg_talk_duration_sec TIME NULL,
    satisfaction_rating varchar(25) NULL
);
SHOW VARIABLES LIKE 'secure_file_priv';
SHOW GLOBAL VARIABLES LIKE 'local_infile';
SET GLOBAL local_infile = 1;

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.00\\CC-sample-data-1.xlsx - Sheet1.csv'
INTO TABLE call_data
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(call_id, agent, call_date, call_time, topic, answered, resolved, speed_of_answer_sec, avg_talk_duration_sec, satisfaction_rating);

SELECT * FROM call_data;

SELECT user, host FROM mysql.user;

SELECT call_date,
       COUNT(*) AS total_calls,
       AVG(speed_of_answer_sec) AS avg_speed_of_answer,
       AVG(avg_talk_duration_sec) AS avg_talk_duration,
       AVG(satisfaction_rating) AS avg_satisfaction
       
FROM call_data
GROUP BY call_date
ORDER BY call_date;
select count(distinct call_date) from call_data;

SELECT COUNT(*) AS total_calls FROM call_data;

SELECT agent, COUNT(*) AS calls_count
FROM call_data
GROUP BY agent
ORDER BY calls_count DESC;

SELECT call_date, AVG(speed_of_answer_sec) AS avg_speed_of_answer
FROM call_data
GROUP BY call_date
ORDER BY call_date;

SELECT call_date, AVG(avg_talk_duration_sec) AS avg_talk_duration
FROM call_data
GROUP BY call_date
ORDER BY call_date;

SELECT call_date, COUNT(*) AS total_calls, AVG(satisfaction_rating) AS avg_satisfaction
FROM call_data
GROUP BY call_date
ORDER BY call_date;

SELECT resolved, COUNT(*) AS count
FROM call_data
GROUP BY resolved;

