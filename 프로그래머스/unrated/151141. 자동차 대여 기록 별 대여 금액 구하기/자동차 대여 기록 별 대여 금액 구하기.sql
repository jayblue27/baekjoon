# 테이블 
# - car, rental history, discount plan
# 문제
# - 자동차 종류가 트럭
# - 대여 기록별 대여 금액
# - 대여 기록 ID, 대여 금액 리스트
# 정렬 
# - 대여금액 DESC, 기록 ID ASC

-- 코드를 입력하세요
# 대여기록(history)을 베이스로 차량정보(car)를 JOIN ON CAR_ID
# DURATION을 구하고, DURATION을 기준으로 DURATION TYPE 판단

# 다음 쿼리에서 차량과 DURATION_TYPE 기준으로 JOIN
# history별로 계산해본다. 
# 트럭만 필요하다. 


# 듀레이션 생성
WITH cte AS (
    SELECT 
        HISTORY_ID,
        CAR_TYPE,
        DAILY_FEE,
        date(end_date), date(start_date),
        DATEDIFF(date(end_date), date(start_date))+1 AS DURATION,
        CASE WHEN DATEDIFF(date(end_date), date(start_date))+1 >= 90 THEN '90일 이상'
        WHEN DATEDIFF(date(end_date), date(start_date))+1 >= 30 THEN '30일 이상'
        WHEN DATEDIFF(date(end_date), date(start_date))+1 >= 7 THEN '7일 이상'
        ELSE '해당 없음' END AS DURATION_TYPE
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS r 
    LEFT JOIN CAR_RENTAL_COMPANY_CAR AS c
    USING (CAR_ID)
    WHERE CAR_TYPE ='트럭'
)

SELECT
    HISTORY_ID,
-- 1일금액 * 할인율 * 기간
    FLOOR(DAILY_FEE * (100-IFNULL(DISCOUNT_RATE,0)) / 100 * DURATION) AS FEE
FROM cte
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS p
USING (CAR_TYPE, DURATION_TYPE)
ORDER BY 2 DESC, 1 DESC
    
# SELECT 
#     HISTORY_ID,
#     CAST(DAILY_FEE * ((100 - IFNULL(DISCOUNT_RATE, 0)) / 100) AS UNSIGNED) * DURATION AS FEE
# FROM cte AS c
# LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS d
# USING(CAR_TYPE, DURATION_TYPE)
# WHERE CAR_TYPE = '트럭'  
# ORDER BY 2 DESC, 1 ASC