/*
*********************************************************************
customers 테이블의 모든 정보를 공통 컬럼(customerNumber)을 기준으로 payments 테이블과 연결해  조회해보기 (단, customer 테이블이 중심이 되도록!)
*********************************************************************
*/

select * from customers
left join payments
on customers.customerNumber = payments.customerNumber;

/*
*********************************************************************
customers 테이블의 모든 정보를 공통 컬럼(customerNumber)을 기준으로 payments 테이블과 연결해  조회해보기 (단, payments 테이블이 중심이 되도록!)
*********************************************************************
*/

select * from customers
inner join payments
on customers.customerNumber = payments.customerNumber
where customers.country = "USA";

/*
*********************************************************************
customers 테이블의 모든 정보를 공통 컬럼(customerNumber)을 기준으로 payments 테이블과 연결해  소비자의 국가(country)가 미국인 경우의 정보만 조회하기
*********************************************************************
*/
select * from customers
inner join payments
on customers.customerNumber = payments.customerNumber
where country = "USA";

/*
*********************************************************************
customers 테이블의 모든 정보를 공통 컬럼(customerNumber)을 기준으로 payments 테이블과 연결해  소비자의 국가(country)별 소비금액(amount)의 총합을 조회하기
*********************************************************************
*/

select country, sum(amount) from customers
inner join payments
on customers.customerNumber = payments.customerNumber
group by country;

/*
*********************************************************************
customers 테이블의 모든 정보를 공통 컬럼(customerNumber)을 기준으로 payments 테이블과 연결해  소비자의 국가(country)별 소비금액(amount)의 평균보다 높은 소비금액을 가진 사용자 정보를 조회하기
*********************************************************************
*/

select * from customers
inner join payments
on customers.customerNumber = payments.customerNumber
where amount >
(select avg(amount) from customers);