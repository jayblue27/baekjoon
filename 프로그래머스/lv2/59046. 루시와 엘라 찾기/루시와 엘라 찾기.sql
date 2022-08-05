-- 들어온 동물 중 (ANIMAL_INS)
-- 이름이 = lucy, ella, pickle, rogan, sabrina, mitty
-- ID, NAME, 성별 및 중성화여부
-- ID순으로 정렬
-- in 함수

-- 코드를 입력하세요
SELECT ai.ANIMAL_ID, ai.NAME, ai.SEX_UPON_INTAKE
FROM ANIMAL_INS as ai
WHERE ai.NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ai.ANIMAL_ID