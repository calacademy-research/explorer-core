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
-- Table structure for table `occurrence_gbif`
--

DROP TABLE IF EXISTS `occurrence_gbif`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `occurrence_gbif` (
  `raw_json` json DEFAULT NULL,
  `key` bigint NOT NULL,
  `datasetKey` varchar(36) DEFAULT NULL,
  `publishingOrgKey` varchar(36) DEFAULT NULL,
  `networkKeys` json DEFAULT NULL,
  `installationKey` varchar(36) DEFAULT NULL,
  `hostingOrganizationKey` varchar(36) DEFAULT NULL,
  `publishingCountry` char(2) DEFAULT NULL,
  `protocol` varchar(10) DEFAULT NULL,
  `lastCrawled` datetime DEFAULT NULL,
  `lastParsed` datetime DEFAULT NULL,
  `crawlId` int DEFAULT NULL,
  `extensions` json DEFAULT NULL,
  `basisOfRecord` varchar(50) DEFAULT NULL,
  `occurrenceStatus` varchar(20) DEFAULT NULL,
  `taxonKey` int DEFAULT NULL,
  `kingdomKey` int DEFAULT NULL,
  `phylumKey` int DEFAULT NULL,
  `classKey` int DEFAULT NULL,
  `familyKey` int DEFAULT NULL,
  `genusKey` int DEFAULT NULL,
  `speciesKey` int DEFAULT NULL,
  `acceptedTaxonKey` int DEFAULT NULL,
  `scientificName` varchar(255) DEFAULT NULL,
  `acceptedScientificName` varchar(255) DEFAULT NULL,
  `kingdom` varchar(255) DEFAULT NULL,
  `phylum` varchar(255) DEFAULT NULL,
  `family` varchar(255) DEFAULT NULL,
  `genus` varchar(255) DEFAULT NULL,
  `species` varchar(255) DEFAULT NULL,
  `genericName` varchar(255) DEFAULT NULL,
  `specificEpithet` varchar(255) DEFAULT NULL,
  `taxonRank` varchar(50) DEFAULT NULL,
  `taxonomicStatus` varchar(50) DEFAULT NULL,
  `iucnRedListCategory` varchar(50) DEFAULT NULL,
  `decimalLatitude` float DEFAULT NULL,
  `decimalLongitude` float DEFAULT NULL,
  `continent` varchar(50) DEFAULT NULL,
  `stateProvince` varchar(255) DEFAULT NULL,
  `gadm` json DEFAULT NULL,
  `waterBody` varchar(255) DEFAULT NULL,
  `higherGeography` varchar(255) DEFAULT NULL,
  `year` int DEFAULT NULL,
  `month` int DEFAULT NULL,
  `day` int DEFAULT NULL,
  `eventDate` date DEFAULT NULL,
  `startDayOfYear` int DEFAULT NULL,
  `endDayOfYear` int DEFAULT NULL,
  `issues` json DEFAULT NULL,
  `modified` datetime DEFAULT NULL,
  `lastInterpreted` datetime DEFAULT NULL,
  `license` varchar(255) DEFAULT NULL,
  `isSequenced` tinyint(1) DEFAULT '0',
  `identifiers` json DEFAULT NULL,
  `media` json DEFAULT NULL,
  `facts` json DEFAULT NULL,
  `relations` json DEFAULT NULL,
  `institutionKey` varchar(255) DEFAULT NULL,
  `collectionKey` varchar(255) DEFAULT NULL,
  `isInCluster` tinyint(1) DEFAULT '0',
  `recordedBy` varchar(255) DEFAULT NULL,
  `preparations` varchar(255) DEFAULT NULL,
  `geodeticDatum` varchar(50) DEFAULT NULL,
  `classField` varchar(255) DEFAULT NULL,
  `countryCode` char(2) DEFAULT NULL,
  `recordedByIDs` json DEFAULT NULL,
  `identifiedByIDs` json DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `gbifRegion` varchar(255) DEFAULT NULL,
  `publishedByGbifRegion` varchar(255) DEFAULT NULL,
  `identifier` varchar(255) DEFAULT NULL,
  `institutionID` varchar(255) DEFAULT NULL,
  `verbatimEventDate` varchar(255) DEFAULT NULL,
  `island` varchar(255) DEFAULT NULL,
  `islandGroup` varchar(255) DEFAULT NULL,
  `verbatimLocality` varchar(255) DEFAULT NULL,
  `collectionCode` varchar(255) DEFAULT NULL,
  `gbifID` varchar(255) DEFAULT NULL,
  `occurrenceID` varchar(255) DEFAULT NULL,
  `catalogNumber` varchar(255) DEFAULT NULL,
  `institutionCode` varchar(255) DEFAULT NULL,
  `collectionID` varchar(255) DEFAULT NULL,
  `higherClassification` varchar(255) DEFAULT NULL,
  `georeferenceSources` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `sex` varchar(50) DEFAULT NULL,
  `lifeStage` varchar(50) DEFAULT NULL,
  `elevation` float DEFAULT NULL,
  `typeStatus` varchar(255) DEFAULT NULL,
  `identifiedBy` varchar(255) DEFAULT NULL,
  `recordNumber` varchar(255) DEFAULT NULL,
  `locality` text,
  `occurrenceRemarks` text,
  `verbatimElevation` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `occurrence_gbif`
--

LOCK TABLES `occurrence_gbif` WRITE;
/*!40000 ALTER TABLE `occurrence_gbif` DISABLE KEYS */;
INSERT INTO `occurrence_gbif` VALUES ('\"{\\\"key\\\":543738784,\\\"datasetKey\\\":\\\"cece4fc2-1fec-4bb5-a335-7252548e3f0b\\\",\\\"publishingOrgKey\\\":\\\"66522820-055c-11d8-b84e-b8a03c50a862\\\",\\\"networkKeys\\\":[\\\"99d66b6c-9087-452f-a9d4-f15f2c2d0e7e\\\"],\\\"installationKey\\\":\\\"a43950ae-eb88-4ef4-bfff-43bcf12885ad\\\",\\\"hostingOrganizationKey\\\":\\\"66522820-055c-11d8-b84e-b8a03c50a862\\\",\\\"publishingCountry\\\":\\\"US\\\",\\\"protocol\\\":\\\"EML\\\",\\\"lastCrawled\\\":\\\"2025-01-27T00:01:44.678+00:00\\\",\\\"lastParsed\\\":\\\"2025-01-27T00:10:04.575+00:00\\\",\\\"crawlId\\\":424,\\\"extensions\\\":{\\\"http://rs.gbif.org/terms/1.0/Multimedia\\\":[{\\\"http://purl.org/dc/terms/identifier\\\":\\\"http://www.archive.org/stream/catalogueofspeci01unse#page/250/mode/2up\\\",\\\"http://purl.org/dc/terms/references\\\":\\\"http://researcharchive.calacademy.org/research/herpetology/catalog/index.asp?xAction=Search&RecStyle=Full&OrderBy=Museum%2C+CatNo&Sex=%5Bany%5D&Museum=CAS-SUR&Class=%5Bany%5D&Ordersub=%5Bany%5D&Stage=%5Bany%5D&PageStyle=Multiple&PageSize=20&Pres=%5Bany%5D&CatNo=3888&Page=1\\\",\\\"http://purl.org/dc/terms/description\\\":\\\"catalog page\\\",\\\"http://purl.org/dc/terms/type\\\":\\\"StillImage\\\",\\\"http://purl.org/dc/terms/license\\\":\\\"https://creativecommons.org/share-your-work/public-domain/cc0/\\\",\\\"http://purl.org/dc/terms/format\\\":\\\"image/jpeg\\\"}]},\\\"basisOfRecord\\\":\\\"PRESERVED_SPECIMEN\\\",\\\"occurrenceStatus\\\":\\\"PRESENT\\\",\\\"taxonKey\\\":8433459,\\\"kingdomKey\\\":1,\\\"phylumKey\\\":44,\\\"classKey\\\":11592253,\\\"familyKey\\\":9116,\\\"genusKey\\\":2460666,\\\"speciesKey\\\":5224953,\\\"acceptedTaxonKey\\\":5224953,\\\"scientificName\\\":\\\"Tropidurus delanonis Baur, 1890\\\",\\\"acceptedScientificName\\\":\\\"Microlophus delanonis (Baur, 1890)\\\",\\\"kingdom\\\":\\\"Animalia\\\",\\\"phylum\\\":\\\"Chordata\\\",\\\"family\\\":\\\"Tropiduridae\\\",\\\"genus\\\":\\\"Microlophus\\\",\\\"species\\\":\\\"Microlophus delanonis\\\",\\\"genericName\\\":\\\"Tropidurus\\\",\\\"specificEpithet\\\":\\\"delanonis\\\",\\\"taxonRank\\\":\\\"SPECIES\\\",\\\"taxonomicStatus\\\":\\\"SYNONYM\\\",\\\"iucnRedListCategory\\\":\\\"LC\\\",\\\"decimalLatitude\\\":-1.354167,\\\"decimalLongitude\\\":-89.659861,\\\"continent\\\":\\\"SOUTH_AMERICA\\\",\\\"stateProvince\\\":\\\"Galapagos Prov.\\\",\\\"gadm\\\":{\\\"level0\\\":{\\\"gid\\\":\\\"ECU\\\",\\\"name\\\":\\\"Ecuador\\\"},\\\"level1\\\":{\\\"gid\\\":\\\"ECU.9_1\\\",\\\"name\\\":\\\"Galápagos\\\"},\\\"level2\\\":{\\\"gid\\\":\\\"ECU.9.2_1\\\",\\\"name\\\":\\\"San Cristóbal\\\"},\\\"level3\\\":{\\\"gid\\\":\\\"ECU.9.2.2_1\\\",\\\"name\\\":\\\"Isla Santa Mara (Floreana) (Cab.\\\"}},\\\"waterBody\\\":\\\"South Pacific Ocean\\\",\\\"higherGeography\\\":\\\"South Pacific Ocean; Ecuador; Galapagos Prov.; Galapagos Ids.; Espanola Id.\\\",\\\"year\\\":1899,\\\"month\\\":5,\\\"day\\\":14,\\\"eventDate\\\":\\\"1899-05-14\\\",\\\"startDayOfYear\\\":134,\\\"endDayOfYear\\\":134,\\\"issues\\\":[\\\"COORDINATE_ROUNDED\\\",\\\"CONTINENT_DERIVED_FROM_COORDINATES\\\"],\\\"modified\\\":\\\"2024-01-04T14:21:00.000+00:00\\\",\\\"lastInterpreted\\\":\\\"2025-01-27T00:10:04.575+00:00\\\",\\\"license\\\":\\\"http://creativecommons.org/publicdomain/zero/1.0/legalcode\\\",\\\"isSequenced\\\":false,\\\"identifiers\\\":[{\\\"identifier\\\":\\\"urn:catalog:CAS:SUR:3888\\\"}],\\\"media\\\":[{\\\"type\\\":\\\"StillImage\\\",\\\"format\\\":\\\"image/jpeg\\\",\\\"references\\\":\\\"http://researcharchive.calacademy.org/research/herpetology/catalog/index.asp?xAction=Search&RecStyle=Full&OrderBy=Museum%2C+CatNo&Sex=%5Bany%5D&Museum=CAS-SUR&Class=%5Bany%5D&Ordersub=%5Bany%5D&Stage=%5Bany%5D&PageStyle=Multiple&PageSize=20&Pres=%5Bany%5D&CatNo=3888&Page=1\\\",\\\"description\\\":\\\"catalog page\\\",\\\"license\\\":\\\"http://creativecommons.org/publicdomain/zero/1.0/\\\",\\\"identifier\\\":\\\"http://www.archive.org/stream/catalogueofspeci01unse#page/250/mode/2up\\\"}],\\\"facts\\\":[],\\\"relations\\\":[],\\\"institutionKey\\\":\\\"d2a27206-87ab-47ea-b5fc-d2e57054b688\\\",\\\"collectionKey\\\":\\\"ba09c323-3cf8-4e82-900f-23f2bdb46f17\\\",\\\"isInCluster\\\":false,\\\"recordedBy\\\":\\\"E. Heller and R.E. Snodgrass\\\",\\\"preparations\\\":\\\"Alcohol\\\",\\\"geodeticDatum\\\":\\\"WGS84\\\",\\\"class\\\":\\\"Squamata\\\",\\\"countryCode\\\":\\\"EC\\\",\\\"recordedByIDs\\\":[],\\\"identifiedByIDs\\\":[],\\\"country\\\":\\\"Ecuador\\\",\\\"gbifRegion\\\":\\\"LATIN_AMERICA\\\",\\\"publishedByGbifRegion\\\":\\\"NORTH_AMERICA\\\",\\\"identifier\\\":\\\"urn:catalog:CAS:SUR:3888\\\",\\\"institutionID\\\":\\\"http://grbio.org/institution/california-academy-sciences\\\",\\\"verbatimEventDate\\\":\\\"14-20 May 1899\\\",\\\"island\\\":\\\"Espanola Id.\\\",\\\"islandGroup\\\":\\\"Galapagos Ids.\\\",\\\"verbatimLocality\\\":\\\"Hood Is., Galapagos\\\",\\\"collectionCode\\\":\\\"SUR\\\",\\\"gbifID\\\":\\\"543738784\\\",\\\"occurrenceID\\\":\\\"urn:catalog:CAS:SUR:3888\\\",\\\"catalogNumber\\\":\\\"3888\\\",\\\"institutionCode\\\":\\\"CAS\\\",\\\"collectionID\\\":\\\"http://grscicoll.org/institutional-collection/herpetology-0\\\",\\\"higherClassification\\\":\\\"Animalia; Chordata; Reptilia; Sauria; Tropiduridae\\\",\\\"georeferenceSources\\\":\\\"Google Earth, 2013.\\\"}\"',543738784,'cece4fc2-1fec-4bb5-a335-7252548e3f0b','66522820-055c-11d8-b84e-b8a03c50a862','[\"99d66b6c-9087-452f-a9d4-f15f2c2d0e7e\"]','a43950ae-eb88-4ef4-bfff-43bcf12885ad','66522820-055c-11d8-b84e-b8a03c50a862','US','EML','2025-01-27 00:01:45','2025-01-27 00:10:05',424,'{\"http://rs.gbif.org/terms/1.0/Multimedia\": [{\"http://purl.org/dc/terms/type\": \"StillImage\", \"http://purl.org/dc/terms/format\": \"image/jpeg\", \"http://purl.org/dc/terms/license\": \"https://creativecommons.org/share-your-work/public-domain/cc0/\", \"http://purl.org/dc/terms/identifier\": \"http://www.archive.org/stream/catalogueofspeci01unse#page/250/mode/2up\", \"http://purl.org/dc/terms/references\": \"http://researcharchive.calacademy.org/research/herpetology/catalog/index.asp?xAction=Search&RecStyle=Full&OrderBy=Museum%2C+CatNo&Sex=%5Bany%5D&Museum=CAS-SUR&Class=%5Bany%5D&Ordersub=%5Bany%5D&Stage=%5Bany%5D&PageStyle=Multiple&PageSize=20&Pres=%5Bany%5D&CatNo=3888&Page=1\", \"http://purl.org/dc/terms/description\": \"catalog page\"}]}','PRESERVED_SPECIMEN','PRESENT',8433459,1,44,11592253,9116,2460666,5224953,5224953,'Tropidurus delanonis Baur, 1890','Microlophus delanonis (Baur, 1890)','Animalia','Chordata','Tropiduridae','Microlophus','Microlophus delanonis','Tropidurus','delanonis','SPECIES','SYNONYM','LC',-1.35417,-89.6599,'SOUTH_AMERICA','Galapagos Prov.','{\"level0\": {\"gid\": \"ECU\", \"name\": \"Ecuador\"}, \"level1\": {\"gid\": \"ECU.9_1\", \"name\": \"Galápagos\"}, \"level2\": {\"gid\": \"ECU.9.2_1\", \"name\": \"San Cristóbal\"}, \"level3\": {\"gid\": \"ECU.9.2.2_1\", \"name\": \"Isla Santa Mara (Floreana) (Cab.\"}}','South Pacific Ocean','South Pacific Ocean; Ecuador; Galapagos Prov.; Galapagos Ids.; Espanola Id.',1899,5,14,'1899-05-14',134,134,'[\"COORDINATE_ROUNDED\", \"CONTINENT_DERIVED_FROM_COORDINATES\"]','2024-01-04 14:21:00','2025-01-27 00:10:05','http://creativecommons.org/publicdomain/zero/1.0/legalcode',0,'[{\"identifier\": \"urn:catalog:CAS:SUR:3888\"}]','[{\"type\": \"StillImage\", \"format\": \"image/jpeg\", \"license\": \"http://creativecommons.org/publicdomain/zero/1.0/\", \"identifier\": \"http://www.archive.org/stream/catalogueofspeci01unse#page/250/mode/2up\", \"references\": \"http://researcharchive.calacademy.org/research/herpetology/catalog/index.asp?xAction=Search&RecStyle=Full&OrderBy=Museum%2C+CatNo&Sex=%5Bany%5D&Museum=CAS-SUR&Class=%5Bany%5D&Ordersub=%5Bany%5D&Stage=%5Bany%5D&PageStyle=Multiple&PageSize=20&Pres=%5Bany%5D&CatNo=3888&Page=1\", \"description\": \"catalog page\"}]','[]','[]','d2a27206-87ab-47ea-b5fc-d2e57054b688','ba09c323-3cf8-4e82-900f-23f2bdb46f17',0,'E. Heller and R.E. Snodgrass','Alcohol','WGS84','Squamata','EC','[]','[]','Ecuador','LATIN_AMERICA','NORTH_AMERICA','urn:catalog:CAS:SUR:3888','http://grbio.org/institution/california-academy-sciences','14-20 May 1899','Espanola Id.','Galapagos Ids.','Hood Is., Galapagos','SUR','543738784','urn:catalog:CAS:SUR:3888','3888','CAS','http://grscicoll.org/institutional-collection/herpetology-0','Animalia; Chordata; Reptilia; Sauria; Tropiduridae','Google Earth, 2013.','2025-02-12 21:43:36',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `occurrence_gbif` ENABLE KEYS */;
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
