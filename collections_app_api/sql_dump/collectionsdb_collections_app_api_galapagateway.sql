CREATE DATABASE  IF NOT EXISTS `collectionsdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `collectionsdb`;
-- MySQL dump 10.13  Distrib 8.0.39, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: collectionsdb
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
-- Table structure for table `collections_app_api_galapagateway`
--

DROP TABLE IF EXISTS `collections_app_api_galapagateway`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `collections_app_api_galapagateway` (
  `galapagatewayKey` bigint NOT NULL AUTO_INCREMENT,
  `recordset_id` varchar(45) DEFAULT NULL,
  `recordsetName_id` char(32) NOT NULL,
  `occurrence_id` varchar(45) NOT NULL,
  `scientific_name` varchar(235) DEFAULT NULL,
  `taxon_id` int DEFAULT NULL,
  PRIMARY KEY (`galapagatewayKey`),
  UNIQUE KEY `occurrence_id_UNIQUE` (`occurrence_id`),
  KEY `recordset_fk_idx` (`recordset_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collections_app_api_galapagateway`
--

LOCK TABLES `collections_app_api_galapagateway` WRITE;
/*!40000 ALTER TABLE `collections_app_api_galapagateway` DISABLE KEYS */;
INSERT INTO `collections_app_api_galapagateway` VALUES (1,'cece4fc2-1fec-4bb5-a335-7252548e3f0b','HERP','urn:catalog:CAS:HERP:10615','Amblyrhynchus cristatus jeffreysi Miralles & Macleod',9483298),(2,'cece4fc2-1fec-4bb5-a335-7252548e3f0b','HERP','urn:catalog:CAS:HERP:8141','Chelonoidis vandenburghi (Desola, 1930)',10857641),(3,'9525d06a-2187-4c50-b34e-2783b8bdff8c','ORN','urn:catalog:CAS:ORN:2920','Asio flammeus galapagoensis (Gould, 1837)',6176241);
/*!40000 ALTER TABLE `collections_app_api_galapagateway` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-27 18:26:06
