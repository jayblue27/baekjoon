-- ANIMAL_ID, NAME, DATETIME (시간을 제거하고 날짜만)
-- ANIMAL_ID 순으로 정렬
-- DATE_FORMAT(변수, 형태)

-- 코드를 입력하세요
SELECT ai.ANIMAL_ID, ai.NAME, DATE_FORMAT(ai.DATETIME, '%Y-%m-%d') as '날짜'
FROM ANIMAL_INS as ai
ORDER BY ai.ANIMAL_ID