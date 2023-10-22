/*
1. 문제이해
- 2022년 1월의 카테고리별 책 판매량 합산
- 카테고리명(CATEGORY), 총 판매량(TOTAL_SALES)

2. 접근방법
- 
- BOOK <- BOOK SALES JOIN
- 2022년 1월 
- GROUP BY CATEGORY
- SUM()
- 카테고리명 기준 오름차순 정렬
*/

# 13분
SELECT 
    CATEGORY, 
    SUM(sales) AS TOTAL_SALES
FROM BOOK
LEFT JOIN BOOK_SALES
USING (BOOK_ID)
WHERE 
    sales_date >= "2022-01-01" AND 
    sales_date < "2022-02-01"
GROUP BY CATEGORY
ORDER BY CATEGORY;