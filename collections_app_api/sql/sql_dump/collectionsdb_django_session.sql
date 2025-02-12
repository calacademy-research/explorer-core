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
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('38qjr0gyaisdabqx4vp5jqnrgnkgqgui','.eJxVjDsOwjAQBe_iGlnrv01JzxmsXX9wADlSnFSIu0OkFNC-mXkvFnFbW9xGWeKU2ZlJdvrdCNOj9B3kO_bbzNPc12Uiviv8oINf51yel8P9O2g42reuudRSUzJauAySjLVBOwEhWS-1UaaSBIcewHmqgpQwQKi1csp7FTJ7fwDjYDcV:1tIcsf:iUERNbMrjffOAHCHQFWSr_Y8rK5V5x4lm4fEKjjfgF8','2024-12-18 00:04:37.529699'),('4sfohz8okvcoxywt0rb85jztdq5alytv','.eJxVjDsOwjAQBe_iGlnrv01JzxmsXX9wADlSnFSIu0OkFNC-mXkvFnFbW9xGWeKU2ZlJdvrdCNOj9B3kO_bbzNPc12Uiviv8oINf51yel8P9O2g42reuudRSUzJauAySjLVBOwEhWS-1UaaSBIcewHmqgpQwQKi1csp7FTJ7fwDjYDcV:1tDWi5:nb0NRgIFW1oAlweBneZxnoMzP9o4g3hhRlN8rMzGiwY','2024-12-03 22:28:37.911984'),('g4qerju8kxniudrjyefhivnph2orpv2q','.eJxVjDEOwjAMRe-SGUVgp0nMyM4ZIsdOSQG1UtNOiLtDpQ6w_vfef5nE61LT2sqcBjVnA-bwu2WWRxk3oHceb5OVaVzmIdtNsTtt9jppeV529--gcqvfmiijxy7kk_bE2B8VSahzIuSicCCOGAAouxg5eMgIUMiDeodeBc37A9M-NzQ:1sgWZj:oYQAA24Wvl1PDOIgWizurTH_SZaHEKl6ntwsxH5U2qM','2024-09-03 21:39:35.397292'),('kdcksrkxkr1147z93cmh77280kfw9jt8','.eJxVjDsOwjAQBe_iGlnrv01JzxmsXX9wADlSnFSIu0OkFNC-mXkvFnFbW9xGWeKU2ZlJdvrdCNOj9B3kO_bbzNPc12Uiviv8oINf51yel8P9O2g42reuudRSUzJauAySjLVBOwEhWS-1UaaSBIcewHmqgpQwQKi1csp7FTJ7fwDjYDcV:1tEHOz:fGBdCJNZ9AGWrtTVKS5hWUadTQh28D8FZ62_wHwdQQw','2024-12-06 00:20:01.848424'),('lfpjndiqv39rjgis5bi42k0secaqze50','.eJxVjDsOwjAQBe_iGlnrv01JzxmsXX9wADlSnFSIu0OkFNC-mXkvFnFbW9xGWeKU2ZlJdvrdCNOj9B3kO_bbzNPc12Uiviv8oINf51yel8P9O2g42reuudRSUzJauAySjLVBOwEhWS-1UaaSBIcewHmqgpQwQKi1csp7FTJ7fwDjYDcV:1tEGlJ:xWFgasBLbUYU9EH-s-acB3WispNcXUe2QAFldje0DFY','2024-12-05 23:39:01.261825'),('pcj4gjmk7la99yweg231po0lk062yuad','.eJxVjDsOwjAQBe_iGlnrv01JzxmsXX9wADlSnFSIu0OkFNC-mXkvFnFbW9xGWeKU2ZlJdvrdCNOj9B3kO_bbzNPc12Uiviv8oINf51yel8P9O2g42reuudRSUzJauAySjLVBOwEhWS-1UaaSBIcewHmqgpQwQKi1csp7FTJ7fwDjYDcV:1tIc3X:ogX6l4W3odbqHK-kNoeT4DDiQvMv4P_v0kiLKvNp7PM','2024-12-17 23:11:47.399396'),('pcuketx7iibnazpmchtlxlkj59jnzff7','.eJxVjDsOwjAQBe_iGlnrv01JzxmsXX9wADlSnFSIu0OkFNC-mXkvFnFbW9xGWeKU2ZlJdvrdCNOj9B3kO_bbzNPc12Uiviv8oINf51yel8P9O2g42reuudRSUzJauAySjLVBOwEhWS-1UaaSBIcewHmqgpQwQKi1csp7FTJ7fwDjYDcV:1tddkY:f-LFRmTanGErRF7jf2Ispd1jrCWflu-6KYRjfCosP2s','2025-02-13 23:15:06.191749'),('sd98ogwfrrc9hfcz0qyga7grplm3uyz0','.eJxVjDsOwjAQBe_iGlnrv01JzxmsXX9wADlSnFSIu0OkFNC-mXkvFnFbW9xGWeKU2ZlJdvrdCNOj9B3kO_bbzNPc12Uiviv8oINf51yel8P9O2g42reuudRSUzJauAySjLVBOwEhWS-1UaaSBIcewHmqgpQwQKi1csp7FTJ7fwDjYDcV:1tJg1T:7x57HlYGfRjEr7-_PSQ99h2fsCoff2zCcaghAUh6BOk','2024-12-20 21:38:03.973972'),('vi32gu5lhetmbz5mhwqtu7651mswmvnp','.eJxVjDsOwjAQBe_iGlnrv01JzxmsXX9wADlSnFSIu0OkFNC-mXkvFnFbW9xGWeKU2ZlJdvrdCNOj9B3kO_bbzNPc12Uiviv8oINf51yel8P9O2g42reuudRSUzJauAySjLVBOwEhWS-1UaaSBIcewHmqgpQwQKi1csp7FTJ7fwDjYDcV:1tIcxX:V3qywUUEoaGgtnig9pu1EkN1_a6MWdDr9QHvPM8XF5Y','2024-12-18 00:09:39.808675');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
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
