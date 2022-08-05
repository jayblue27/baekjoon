-- 코드를 입력하세요
-- 고양이와, 개가 각각 몇마리인가
-- 고양이가 먼저 나와야 한다. 
SELECT a.ANIMAL_TYPE, COUNT(ANIMAL_TYPE)
FROM ANIMAL_INS as a
GROUP BY a.ANIMAL_TYPE
ORDER BY a.ANIMAL_TYPE