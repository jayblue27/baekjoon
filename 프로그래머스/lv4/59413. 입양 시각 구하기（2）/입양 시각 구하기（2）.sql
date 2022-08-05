-- 가장 활발한 입양시간 (0~23) (없는 데이터에 대한 값을 추가 시켜줘야 함)
-- SET 명령어 사용해야 함 -> 어떤 변수에 특정 값을 할당
-- https://jaaamj.tistory.com/155

-- 코드를 입력하세요
SET @HOUR = -1;  # HOUR 변수를 -1로 선언
SELECT (@HOUR := @HOUR +1) AS HOUR, # 0~23 생성, HOUR
       (SELECT COUNT(HOUR(DATETIME)) FROM ANIMAL_OUTS WHERE HOUR(DATETIME)=@HOUR) AS COUNT # 이해하기 어렵구만
FROM ANIMAL_OUTS
WHERE @HOUR < 23;