DELIMITER $$
CREATE TRIGGER update_model_url
BEFORE INSERT ON collections_app_api_occurrence
FOR EACH ROW
BEGIN
    DECLARE prefix VARCHAR(4);
    DECLARE id_number VARCHAR(5);
    DECLARE regex_match VARCHAR(20);

    -- extract the string after 'urn:catalog:CAS:'
    SET regex_match = SUBSTRING_INDEX(SUBSTRING_INDEX(NEW.occurrence_id, 'CAS:', -1), ':', -1); -- Get HERP:10615 or ORN:1234
    -- extract collection_code and occurrence_id number
    SET prefix = LEFT(regex_match, LOCATE(':', regex_match) - 1); -- Extract the collection_code (e.g., HERP, ORN, etc)
    SET id_number = SUBSTRING_INDEX(regex_match, ':', -1); -- Extract the occurrence_id number (e.g., 10615 or 1234)
    SET NEW.model_url = CONCAT('0.0.0.0/static/', prefix, id_number);

END$$
DELIMITER ;
