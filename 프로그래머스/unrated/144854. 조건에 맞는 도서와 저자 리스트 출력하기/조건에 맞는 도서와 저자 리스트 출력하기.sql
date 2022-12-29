/*
카테고리가 경제인
book ID,저자명, 출판일
출판일 기준으로 오름차순
*/
-- 코드를 입력하세요
SELECT 
    b.BOOK_ID,
    a.AUTHOR_NAME,
    date_format(b.PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
FROM BOOK AS b
LEFT JOIN AUTHOR AS a
ON b.AUTHOR_ID = a.AUTHOR_ID
WHERE b.CATEGORY = '경제'
ORDER BY b.PUBLISHED_DATE ASC;