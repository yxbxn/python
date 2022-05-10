# [IF THEN] customer 테이블에서 고객의 번호를 입력받아, 고객의 신용한도가 10000이하면 ‘SILVER’, 10000~50000이면 ‘GOLD’ 50000이 넘으면 ‘PLATINUM’으로 나타내는 함수를 작성하고, 447번, 141번 고객을 출력해서 확인

DELIMITER $$

CREATE PROCEDURE GetCustomerLevel(
    IN  pCustomerNumber INT, 
    OUT pCustomerLevel  VARCHAR(20))
BEGIN
    DECLARE credit DECIMAL DEFAULT 0;

    SELECT creditLimit 
    INTO credit
    FROM customers
    WHERE customerNumber = pCustomerNumber;

    IF credit > 50000 THEN
        SET pCustomerLevel = 'PLATINUM';
    ELSEIF credit <= 50000 AND credit > 10000 THEN
        SET pCustomerLevel = 'GOLD';
    ELSE
        SET pCustomerLevel = 'SILVER';
    END IF;
END $$

DELIMITER ;

# [CASE] orders 테이블에서 요청일자와 배송일자를 확인하여 다음 조건을 만족하는 배송상태를 평가하는 함수를 작성하고, 주문번호 10100을 출력해서 확인

DELIMITER $$

CREATE PROCEDURE GetDeliveryStatus(
	IN pOrderNumber INT,
    OUT pDeliveryStatus VARCHAR(100)
)
BEGIN
	DECLARE waitingDay INT DEFAULT 0;
    SELECT 
		DATEDIFF(requiredDate, shippedDate)
	INTO waitingDay
	FROM orders
    WHERE orderNumber = pOrderNumber;
    
    CASE 
		WHEN waitingDay = 0 THEN 
			SET pDeliveryStatus = 'On Time';
        WHEN waitingDay >= 1 AND waitingDay < 5 THEN
			SET pDeliveryStatus = 'Late';
		WHEN waitingDay >= 5 THEN
			SET pDeliveryStatus = 'Very Late';
		ELSE
			SET pDeliveryStatus = 'No Information';
	END CASE;	
END$$
DELIMITER ;
