-- GROUP BY ~ HAVING ~ 절
-- 그룹함수를 사용 후에 조건을 사용할 수 있다. 
-- 같은 상품을 2번 이상 구매한 사용자를 출력하는 것과 같이 그룹화한 그룹을 다시 조건에 맞게 그룹화할 수 있다.
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(SALES_DATE)>=2
ORDER BY USER_ID ASC, PRODUCT_ID DESC