/*
조건
대여시작일 기준 2022년 8월 ~ 2022년 10월 
AND 위 기간의 총 대여횟수가 5회 이상인 자동차(CAR ID)

위 기간동안의
월별, 자동차ID별 총 대여횟수 -> 그룹by

정렬
MONTH - 오름차순
CAR_ID - 내림차순

특정 월의 총 대여 횟수가 0인 경우? 
*/

-- 코드를 입력하세요
-- 조건에 맞는 CAR_ID 추출
-- 2,7,8,10,11,12,13,15,18,20,21,23,25,27

# SELECT CAR_ID
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# WHERE 
#     START_DATE >= '2022-08-01' AND END_DATE < '2022-11-01'
# GROUP BY CAR_ID
# HAVING count(*) >= 5
# ORDER BY CAR_ID 

SELECT 
    MONTH(START_DATE) AS MONTH,
    CAR_ID,
    count(*) as RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE 
    START_DATE >= '2022-08-01' AND 
    START_DATE < '2022-11-01' AND
    CAR_ID IN (SELECT CAR_ID
               FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
               WHERE 
                    START_DATE >= '2022-08-01' AND 
                    START_DATE < '2022-11-01'
               GROUP BY CAR_ID
               HAVING count(*) >= 5)
GROUP BY MONTH, CAR_ID
ORDER BY MONTH ASC, CAR_ID DESC;
