-- 코드를 입력하세요
-- ROUND함수 -> 반올림 함수, 첫번째 자리에 반올림할 수 입력, 두번째 자리에 몇번째에서 반올림할지를 입력
SELECT ROUND(AVG(DAILY_FEE)) as AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE='SUV'
GROUP BY CAR_TYPE