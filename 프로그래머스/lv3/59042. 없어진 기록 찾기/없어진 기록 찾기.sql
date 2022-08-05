-- 코드를 입력하세요
-- 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물
-- -> outs에만 기록이 있는 (right join) 동물의 ID, 이름 -> ID 순 
SELECT ao.ANIMAL_ID, ao.NAME
FROM ANIMAL_INS as ai
RIGHT JOIN ANIMAL_OUTS as ao
ON ai.ANIMAL_ID = ao.ANIMAL_ID
WHERE ai.ANIMAL_ID IS NULL