-- 코드를 입력하세요
-- 리뷰를 가장 많이 작성한 회원의 리뷰 조회
-- 회원이름, 리뷰텍스트, 리뷰작성일
-- 작성일, 리뷰텍스트 오름차순 정렬

-- 리뷰를 가장 많이 작성한 회원의 id
# SELECT *
#     MEMBER_NAME,
#     REVIEW_TEXT,
#     DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d')
# FROM REST_REVIEW
# LEFT JOIN MEMBER_PROFILE
# USING(MEMBER_ID)
# WHERE MEMBER_ID IN (
#     SELECT MEMBER_ID
#     FROM REST_REVIEW
#     GROUP BY MEMBER_ID
#     HAVING COUNT(*) = (
#         SELECT MAX(cnt) AS MAX_CNT
#         FROM (
#             SELECT COUNT(*) AS CNT 
#             FROM REST_REVIEW 
#             GROUP BY MEMBER_ID) AS sub) )
# ORDER BY REVIEW_DATE, REVIEW_TEXT


SELECT 
    mp.MEMBER_NAME, 
    rr.REVIEW_TEXT, 
    substr(rr.REVIEW_DATE,1,10) as REVIEW_DATE
from MEMBER_PROFILE mp
left join REST_REVIEW rr
on mp.MEMBER_ID = rr.MEMBER_ID 
where rr.MEMBER_ID = (
    select MEMBER_ID
    from REST_REVIEW
    group by MEMBER_ID
    order by count(*) desc
    limit 1
)
order by rr.REVIEW_DATE, rr.REVIEW_TEXT