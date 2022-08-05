-- 코드를 입력하세요
-- 보호 시작일(in)보다 입양일(out)이 더 빠른 동물의 아이디와 이름
-- 둘다 있어야 하니까 INNER JOIN 이겠네
-- 보호 시작일이 빠른 순으로 조회 (WHERE)
SELECT ai.ANIMAL_ID, ai.NAME
FROM ANIMAL_INS as ai
INNER JOIN ANIMAL_OUTS as ao
ON ai.ANIMAL_ID = ao.ANIMAL_ID
WHERE ai.DATETIME > ao.DATETIME
ORDER BY ai.DATETIME ASC
