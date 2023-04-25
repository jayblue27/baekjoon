# 게시글정보, 유저정보 테이블 2개 
# 게시글 3건이상 등록한 사용자 정보 조회
# writer_id 기준 3건 이상 인 사람 having

-- 코드를 입력하세요
WITH a AS (
SELECT WRITER_ID, COUNT(*) AS cnt
FROM USED_GOODS_BOARD
GROUP BY WRITER_ID
HAVING cnt >= 3)

SELECT 
    b.USER_ID, 
    b.NICKNAME, 
    CONCAT(CITY, ' ',STREET_ADDRESS1, ' ', STREET_ADDRESS2) AS '전체주소',
    CONCAT(SUBSTRING(TLNO,1,3),'-',SUBSTRING(TLNO,4,4),'-',SUBSTRING(TLNO,8,4)) AS '전화번호'
FROM a
LEFT JOIN USED_GOODS_USER as b
ON a.WRITER_ID = b.USER_ID
ORDER BY b.USER_ID DESC;
