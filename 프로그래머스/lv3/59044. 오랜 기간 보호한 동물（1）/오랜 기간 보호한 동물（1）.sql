-- 코드를 입력하세요
-- 입양 못간 동물 -> 들어왔는데 못나간 (left join) 동물
-- 가장 오래 있었던 동물 3마리 (가장 먼저 들어온)의 이름, 보호 시작일(DATETIME)
SELECT ai.NAME, ai.DATETIME
FROM ANIMAL_INS as ai
LEFT JOIN ANIMAL_OUTS as ao
ON ai.ANIMAL_ID = ao.ANIMAL_ID
WHERE ao.ANIMAL_ID IS NULL
ORDER BY ai.DATETIME LIMIT 3