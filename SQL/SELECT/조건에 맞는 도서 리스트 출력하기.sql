-- 코드를 입력하세요
-- DATE_FORMAT함수 -> 첫번째인수에 바꿔줄 날짜, 두번째 인수에 그 포멧을 입력한다.
-- 포멧에 %D는 24th로 표현되고 %M는 Octobal로 표현된다. %d는 24 %m은 10으로 표현된다.
-- LIKE알기! 스트링내에 부분적으로 표현하고 있는지 확인할 수 있는 좋은 함수
SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK
WHERE CATEGORY='인문' AND PUBLISHED_DATE LIKE '2021%'
ORDER BY PUBLISHED_DATE ASC