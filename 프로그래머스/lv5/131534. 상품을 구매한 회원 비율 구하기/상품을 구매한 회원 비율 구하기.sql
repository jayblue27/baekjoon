-- 코드를 입력하세요
-- 2021 가입회원
-- 상품 구매 회원수 - CASE AS PURCHASED
-- 구매 회원의 비율 (구매회원/전체회원) -> 년/월 별로, 소수점 1자리 2021년 기준
-- 년, 월기준 오름차순
SELECT 
    os.YEAR, 
    os.MONTH,
    COUNT(*) AS PURCHASED_USERS,
    ROUND(COUNT(*) / (
        -- 2021년 가입한 전체 회원수
        SELECT COUNT(*)
        FROM USER_INFO
        WHERE YEAR(JOINED) = 2021), 1) AS PURCHASED_RATIO
-- 구매한 2021년 가입회원수
FROM (
    SELECT 
        USER_ID, 
        YEAR(SALES_DATE) AS YEAR,
        MONTH(SALES_DATE) AS MONTH
    FROM ONLINE_SALE
    GROUP BY USER_ID, YEAR(SALES_DATE), MONTH(SALES_DATE)) AS os
LEFT JOIN USER_INFO AS ui
USING(USER_ID)
-- 2021 가입회원 
WHERE YEAR(ui.JOINED) = 2021
GROUP BY os.YEAR, os.MONTH
ORDER BY os.YEAR, os.MONTH;

# SELECT USER_ID, SALES_DATE
# FROM ONLINE_SALE
# GROUP BY USER_ID, SALES_DATE