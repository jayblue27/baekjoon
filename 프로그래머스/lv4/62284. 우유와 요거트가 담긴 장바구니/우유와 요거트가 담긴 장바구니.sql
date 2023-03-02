/*
- 테이블
CAR_PRODUCTS

- 조건
Milk와 Yogurt르르 동시에 구입한 장바구니(CART_ID)

- 정렬
CART_ID 

*/

# -- 코드를 입력하세요
WITH milk AS (
    SELECT *
    FROM CART_PRODUCTS
    WHERE NAME = 'milk'
),

yogurt AS (
    SELECT *
    FROM CART_PRODUCTS
    WHERE NAME = 'yogurt')

SELECT CART_ID
FROM milk
INNER JOIN yogurt
USING(CART_ID)
ORDER BY CART_ID;