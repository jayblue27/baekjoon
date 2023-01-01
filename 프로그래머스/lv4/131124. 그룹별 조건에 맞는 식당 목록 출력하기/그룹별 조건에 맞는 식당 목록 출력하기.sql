-- 코드를 입력하세요
-- 리뷰를 가장 많이 작성한 회원의 리뷰 조회
-- 회원이름, 리뷰텍스트, 리뷰작성일
-- 작성일, 리뷰텍스트 오름차순 정렬

-- 리뷰를 가장 많이 작성한 회원의 id
# SELECT
#     MEMBER_NAME,
#     REVIEW_TEXT,
#     DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d')
# FROM REST_REVIEW
# LEFT JOIN MEMBER_PROFILE
# USING(MEMBER_ID)
# WHERE MEMBER_ID IN (SELECT MEMBER_ID
#                     FROM REST_REVIEW
#                     GROUP BY MEMBER_ID
#                     HAVING COUNT(*) = (SELECT MAX(CNT)
#                                        FROM (SELECT COUNT(*) AS CNT 
#                                              FROM REST_REVIEW 
#                                              GROUP BY MEMBER_ID) AS sub) )
# ORDER BY REVIEW_DATE, REVIEW_TEXT

SELECT
    mp.MEMBER_NAME,
    rr.REVIEW_TEXT,
    DATE_FORMAT(rr.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM REST_REVIEW AS rr
LEFT JOIN MEMBER_PROFILE AS mp
USING(MEMBER_ID)
-- MEMBER ID가 IN 내부에 해당하는 경우 FILTER
WHERE MEMBER_ID IN (
    -- COUNT값이 HAVING절에 해당하는 경우
    SELECT MEMBER_ID
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
    HAVING COUNT(*) = (
        -- HAVING : MEMBER ID별 가장 많은 리뷰 수
        SELECT COUNT(*) AS CNT 
        FROM REST_REVIEW 
        GROUP BY MEMBER_ID
        ORDER BY CNT DESC
        LIMIT 1))
ORDER BY REVIEW_DATE, REVIEW_TEXT