/*
- 테이블
CAR_PRODUCTS

- 조건
Milk와 Yogurt르르 동시에 구입한 장바구니(CART_ID)

- 정렬
CART_ID 

GROUP_CONCAT(필드) + GROUP BY 활용 WHERE AND 적용
*/

# 코드를 입력하세요

-- milk 구매한 테이블 
WITH milk AS (
    SELECT *
    FROM CART_PRODUCTS
    WHERE NAME = 'milk'
),

-- yogurt 구매한 테이블
yogurt AS (
    SELECT *
    FROM CART_PRODUCTS
    WHERE NAME = 'yogurt')

-- 쿼리
SELECT CART_ID
FROM milk
INNER JOIN yogurt
USING(CART_ID)
ORDER BY CART_ID;