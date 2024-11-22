-- MySQL dump 10.13  Distrib 8.0.40, for Linux (x86_64)
--
-- Host: 0.0.0.0    Database: collectionsdb
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `collections_app_api_occurrence`
--

DROP TABLE IF EXISTS `collections_app_api_occurrence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `collections_app_api_occurrence` (
  `key` bigint NOT NULL,
  `occurrence_id` varchar(255) NOT NULL,
  `publishing_country` varchar(2) NOT NULL,
  `protocol` varchar(50) NOT NULL,
  `last_crawled` datetime(6) NOT NULL,
  `last_parsed` datetime(6) NOT NULL,
  `crawl_id` int NOT NULL,
  `basis_of_record` varchar(255) NOT NULL,
  `occurrence_status` varchar(255) NOT NULL,
  `sex` varchar(50) DEFAULT NULL,
  `life_stage` varchar(50) DEFAULT NULL,
  `scientific_name` varchar(255) NOT NULL,
  `decimal_latitude` double DEFAULT NULL,
  `decimal_longitude` double DEFAULT NULL,
  `elevation` double DEFAULT NULL,
  `continent` varchar(255) DEFAULT NULL,
  `state_province` varchar(255) DEFAULT NULL,
  `water_body` varchar(255) DEFAULT NULL,
  `higher_geography` longtext,
  `year` int DEFAULT NULL,
  `month` int DEFAULT NULL,
  `day` int DEFAULT NULL,
  `event_date` date DEFAULT NULL,
  `start_day_of_year` int DEFAULT NULL,
  `end_day_of_year` int DEFAULT NULL,
  `type_status` varchar(255) DEFAULT NULL,
  `issues` json NOT NULL,
  `modified` datetime(6) NOT NULL,
  `last_interpreted` datetime(6) NOT NULL,
  `license` varchar(200) NOT NULL,
  `is_sequenced` tinyint(1) NOT NULL,
  `identifiers` json NOT NULL,
  `media` json NOT NULL,
  `facts` json NOT NULL,
  `relations` json NOT NULL,
  `institution_key` varchar(235) NOT NULL,
  `collection_key` varchar(235) NOT NULL,
  `is_in_cluster` tinyint(1) NOT NULL,
  `recorded_by` varchar(255) DEFAULT NULL,
  `identified_by` varchar(255) DEFAULT NULL,
  `preparations` varchar(255) DEFAULT NULL,
  `geodetic_datum` varchar(255) NOT NULL,
  `record_number` varchar(255) DEFAULT NULL,
  `verbatim_event_date` varchar(255) DEFAULT NULL,
  `island_group` varchar(255) DEFAULT NULL,
  `island` varchar(255) DEFAULT NULL,
  `locality` longtext,
  `verbatim_locality` longtext,
  `collection_code` varchar(255) NOT NULL,
  `occurrence_remarks` longtext,
  `verbatim_elevation` varchar(255) DEFAULT NULL,
  `higher_classification` longtext,
  `georeference_sources` longtext,
  `publishing_org` varchar(235) NOT NULL,
  `recordsetName_id` varchar(235) NOT NULL,
  `taxon_id` int NOT NULL,
  `description` text,
  PRIMARY KEY (`key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collections_app_api_occurrence`
--

LOCK TABLES `collections_app_api_occurrence` WRITE;
/*!40000 ALTER TABLE `collections_app_api_occurrence` DISABLE KEYS */;
INSERT INTO `collections_app_api_occurrence` VALUES (543447984,'urn:catalog:CAS:HERP:10615','US','EML','2024-08-05 00:01:47.358000','2024-08-05 00:09:13.640000',399,'PRESERVED_SPECIMEN','PRESENT',NULL,NULL,'Amblyrhynchus cristatus jeffreysi Miralles & Macleod',-0.400444,-90.706028,NULL,'SOUTH_AMERICA','Galapagos Prov.','South Pacific Ocean','South Pacific Ocean; Ecuador; Galapagos Prov.; Galapagos Ids.; Rabida Id.',1905,12,21,'1905-12-21',355,355,NULL,'[\"COORDINATE_ROUNDED\", \"CONTINENT_DERIVED_FROM_COORDINATES\"]','2024-01-04 14:21:00.000000','2024-08-05 00:09:13.640000','http://creativecommons.org/publicdomain/zero/1.0/legalcode',0,'[{\"identifier\": \"urn:catalog:CAS:HERP:10615\"}]','[{\"type\": \"StillImage\", \"format\": \"image/jpeg\", \"license\": \"http://creativecommons.org/publicdomain/zero/1.0/\", \"identifier\": \"http://www.archive.org/stream/catalogueofdepar02unse#page/n313/mode/2up\", \"references\": \"http://researcharchive.calacademy.org/research/herpetology/catalog/index.asp?xAction=Search&RecStyle=Full&OrderBy=Museum%2C+CatNo&Sex=%5Bany%5D&Museum=CAS&Class=%5Bany%5D&Ordersub=%5Bany%5D&Stage=%5Bany%5D&PageStyle=Multiple&PageSize=20&Pres=%5Bany%5D&CatNo=10615&Page=1\", \"description\": \"catalog page\"}]','[]','[]','d2a2720687ab47eab5fcd2e57054b688','ba09c3233cf84e82900f23f2bdb46f17',0,'E.S. King','A. Miralles et al.','Alcohol','WGS84','2214','21 Dec 1905','Galapagos Ids.','Rabida Id.',NULL,'Jervis Island, Galapagos Archipelago.','HERP',NULL,NULL,'Animalia; Chordata; Reptilia; Sauria; Iguanidae','Google Earth, 2013.','66522820055c11d8b84eb8a03c50a862','cece4fc21fec4bb5a3357252548e3f0b',9483298,NULL),(543671633,'urn:catalog:CAS:HERP:8141','US','EML','2024-08-05 00:01:47.358000','2024-08-05 00:09:02.730000',399,'PRESERVED_SPECIMEN','PRESENT','FEMALE','Adult','Chelonoidis vandenburghi (Desola, 1930)',-0.456944,-91.050833,609.6,'SOUTH_AMERICA','Galapagos Prov.','South Pacific Ocean','South Pacific Ocean; Ecuador; Galapagos Prov.; Galapagos Ids.; Isabela Id.',1906,8,11,'1906-08-11',223,223,'HOLOTYPE','[\"COORDINATE_ROUNDED\", \"CONTINENT_DERIVED_FROM_COORDINATES\"]','2024-01-04 14:21:00.000000','2024-08-05 00:09:02.730000','http://creativecommons.org/publicdomain/zero/1.0/legalcode',0,'[{\"identifier\": \"urn:catalog:CAS:HERP:8141\"}]','[{\"type\": \"StillImage\", \"format\": \"image/jpeg\", \"license\": \"http://creativecommons.org/publicdomain/zero/1.0/\", \"identifier\": \"http://www.archive.org/stream/catalogueofdepar02unse#page/n149/mode/2up\", \"references\": \"http://researcharchive.calacademy.org/research/herpetology/catalog/index.asp?xAction=Search&RecStyle=Full&OrderBy=Museum%2C+CatNo&Sex=%5Bany%5D&Museum=CAS&Class=%5Bany%5D&Ordersub=%5Bany%5D&Stage=%5Bany%5D&PageStyle=Multiple&PageSize=20&Pres=%5Bany%5D&CatNo=8141&Page=1\", \"description\": \"catalog page\"}]','[]','[]','d2a2720687ab47eab5fcd2e57054b688','ba09c3233cf84e82900f23f2bdb46f17',0,'R.H. Beck','R. DeSola','Dry','WGS84','3861','11 Aug 1906','Galapagos Ids.','Isabela Id.','Cowley Mt','Cowley Mt. Albemarle Isl. Galapagos Archipelago','HERP','Holotype of Testudo vandenburghi DeSola, 1930.  Skull separate.  Slevin\'s notes give elevation as \'about 2000 ft.\'','ca 2000 ft','Animalia; Chordata; Reptilia; Testudines; Testudinidae','Google Earth, 2013.','66522820055c11d8b84eb8a03c50a862','cece4fc21fec4bb5a3357252548e3f0b',10857641,NULL),(583474648,'urn:catalog:CAS:ORN:2920','US','EML','2024-08-05 22:57:09.849000','2024-08-05 22:58:07.667000',671,'PRESERVED_SPECIMEN','PRESENT','MALE',NULL,'Asio flammeus galapagoensis (Gould, 1837)',NULL,NULL,NULL,'SOUTH_AMERICA','Galapagos Islands',NULL,'South America, Ecuador, Galapagos Islands, Isabela Island',1906,8,10,'1906-08-10',222,222,NULL,'[]','2024-03-27 11:55:18.000000','2024-08-05 22:58:07.667000','http://creativecommons.org/publicdomain/zero/1.0/legalcode',0,'[{\"identifier\": \"urn:catalog:CAS:ORN:2920\"}]','[]','[]','[]','d2a27206-87ab-47ea-b5fc-d2e57054b688','9525d06a-2187-4c50-b34e-2783b8bdff8c',0,'J. S. Hunter',NULL,'Feather; Skin Study; toepad','',NULL,'10 August 1906',NULL,NULL,'Isabela Island; Cowley Bay',NULL,'ORN',NULL,NULL,'Aves,Strigiformes,Strigidae',NULL,'66522820-055c-11d8-b84e-b8a03c50a862','4f29b6ab-20c0-4479-8795-4915bedcebd1',6176241,NULL);
/*!40000 ALTER TABLE `collections_app_api_occurrence` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-19 14:34:35
