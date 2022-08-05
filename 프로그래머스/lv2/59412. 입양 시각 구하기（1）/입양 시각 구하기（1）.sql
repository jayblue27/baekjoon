-- https://extbrain.tistory.com/60
-- YEAR / MONTH / DAY / HOUR / MINUTE / SECOND
-- *TIME_FORMAT 쓰니까 시간 앞에 0이 붙더라 ex) 09
-- HOUR 쓰니까 9로 된다. 

-- 코드를 입력하세요
SELECT HOUR(ao.DATETIME) as HOUR, COUNT(*) as COUNT
FROM ANIMAL_OUTS as ao
GROUP BY HOUR(ao.DATETIME) 
HAVING HOUR >= 9 AND HOUR < 20
ORDER BY HOUR ASC