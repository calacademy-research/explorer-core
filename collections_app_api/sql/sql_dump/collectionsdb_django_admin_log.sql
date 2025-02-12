-- MySQL dump 10.13  Distrib 8.0.41, for Linux (x86_64)
--
-- Host: 0.0.0.0    Database: collectionsdb
-- ------------------------------------------------------
-- Server version	8.0.41

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
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-12-06 21:38:14.532248','543671633','urn:catalog:CAS:HERP:8141',2,'[{\"changed\": {\"fields\": [\"Description\"]}}]',268,2),(2,'2025-01-30 23:51:42.828352','543671633','urn:catalog:CAS:HERP:8141',2,'[{\"changed\": {\"fields\": [\"Description\"]}}]',268,2),(3,'2025-02-10 21:06:53.461240','543671633','urn:catalog:CAS:HERP:8141',2,'[{\"changed\": {\"fields\": [\"Description\"]}}]',268,2),(4,'2025-02-10 21:07:10.626938','583474648','urn:catalog:CAS:ORN:2920',2,'[{\"changed\": {\"fields\": [\"Description\"]}}]',268,2),(5,'2025-02-11 21:42:29.869846','543738784','OccurrenceGBIF - 543738784',3,'',276,2),(6,'2025-02-11 21:46:07.441707','543738784','OccurrenceGBIF - 543738784',3,'',276,2),(7,'2025-02-11 21:48:10.817432','543738784','OccurrenceGBIF - 543738784',3,'',276,2),(8,'2025-02-12 20:59:59.738326','543738784','OccurrenceGBIF - 543738784',3,'',276,2),(9,'2025-02-12 21:00:27.072025','543738784','urn:catalog:CAS:SUR:3888',3,'',268,2),(10,'2025-02-12 21:15:56.658737','543738784','OccurrenceGBIF - 543738784',3,'',276,2),(11,'2025-02-12 21:16:02.227239','543738784','urn:catalog:CAS:SUR:3888',3,'',268,2),(12,'2025-02-12 21:28:56.169440','543738784','OccurrenceGBIF - 543738784',3,'',276,2),(13,'2025-02-12 21:29:02.347843','543738784','urn:catalog:CAS:SUR:3888',3,'',268,2),(14,'2025-02-12 21:32:55.590098','543738784','OccurrenceGBIF - 543738784',3,'',276,2),(15,'2025-02-12 21:33:02.965151','543738784','urn:catalog:CAS:SUR:3888',3,'',268,2),(16,'2025-02-12 21:40:26.182477','543738784','OccurrenceGBIF - 543738784',3,'',276,2),(17,'2025-02-12 21:40:32.130993','543738784','urn:catalog:CAS:SUR:3888',3,'',268,2);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-12 14:02:42
