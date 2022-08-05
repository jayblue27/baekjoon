-- 입양을 간 동물 중 (INNER)
-- 보호 기간이 가장 길었던 동물 두마리
-- 아이디, 이름
-- 보호 기간이 긴 순

-- 코드를 입력하세요
SELECT ai.ANIMAL_ID, ai.NAME
FROM ANIMAL_INS as ai
INNER JOIN ANIMAL_OUTS as ao
ON ai.ANIMAL_ID = ao.ANIMAL_ID
ORDER BY (ao.DATETIME - ai.DATETIME) DESC LIMIT 2;
