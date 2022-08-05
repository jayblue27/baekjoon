-- WHERE 변수 LIKE 'ab%'

-- el이 들어가는 이름
-- ID, 이름
-- 이름 순으로 조회 
-- '개'

-- 코드를 입력하세요
SELECT ai.ANIMAL_ID, ai.NAME
FROM ANIMAL_INS as ai
WHERE ai.ANIMAL_TYPE = 'Dog' and ai.NAME LIKE '%el%'
ORDER BY ai.NAME ASC