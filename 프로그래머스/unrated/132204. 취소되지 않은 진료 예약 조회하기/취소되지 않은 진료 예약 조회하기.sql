# APPOINTMENT 기준으로 환자정보, 의사 정보 JOIN
# WHERE절에서 4월 13일, 취소되지 않은 예약, 진료과목 흉부외과(CS) 로 필터링
# 예약일시 기준 오름차순 정렬

-- 코드를 입력하세요
SELECT
    a.APNT_NO,
    p.PT_NAME,
    p.PT_NO,
    a.MCDP_CD,
    d.DR_NAME,
    a.APNT_YMD
FROM APPOINTMENT AS a
LEFT JOIN PATIENT AS p
USING(PT_NO)
LEFT JOIN DOCTOR AS d
ON a.MDDR_ID = d.DR_ID
WHERE
    DATE(a.APNT_YMD) = '2022-04-13' AND 
    a.MCDP_CD = 'CS' AND
    a.APNT_CNCL_YN = 'N'
ORDER BY a.APNT_YMD;