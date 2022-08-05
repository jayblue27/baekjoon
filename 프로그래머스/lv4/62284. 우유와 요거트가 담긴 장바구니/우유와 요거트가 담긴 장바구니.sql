-- https://blue-boy.tistory.com/194
-- milk와 yogurt를 동시에  구입한 장바구니
-- ID 조회
-- ID 순으로 정렬

# -- 코드를 입력하세요
# SELECT CART_ID
# FROM CART_PRODUCTS
# WHERE NAME IN ('Milk','Yogurt')
# GROUP BY CART_ID HAVING COUNT(ID) >= 2


# 서브쿼리
SELECT DISTINCT CART_ID
FROM CART_PRODUCTS
WHERE NAME = 'Milk' 
    AND CART_ID IN (SELECT DISTINCT CART_ID
                    FROM CART_PRODUCTS
                    WHERE NAME = 'Yogurt')
                                