-- PLACES -> 공간
-- 공간을 2개 이상 등록한 사람(헤비 유저)
-- 헤비 유저의 *
-- ID 순 정렬

-- 코드를 입력하세요
# 틀린 풀이 - 그룹바이 하면 하나밖에 안나오는데
# 헤비유저가 포함된 모든 정보를 불러 와야하므로
# SELECT *
# FROM PLACES as p
# GROUP BY p.HOST_ID
# HAVING p.HOST_ID >= 2
# ORDER BY p.ID

# WHERE IN 을 씀으로
SELECT * FROM PLACES
WHERE HOST_ID IN(
    SELECT HOST_ID FROM PLACES
    GROUP BY HOST_ID
    HAVING COUNT(ID) >= 2
)
ORDER BY ID ASC;