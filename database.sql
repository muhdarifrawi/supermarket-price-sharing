-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: supermarket_price_sharing
-- ------------------------------------------------------
-- Server version	5.7.27-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `brand`
--

DROP TABLE IF EXISTS `brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `brand` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brand`
--

LOCK TABLES `brand` WRITE;
/*!40000 ALTER TABLE `brand` DISABLE KEYS */;
INSERT INTO `brand` VALUES (1,'Aaa'),(2,'Alpen'),(3,'Amazin Grace'),(4,'Arnotts'),(5,'Ayam Brand'),(6,'Bahlsen'),(7,'Britannia'),(8,'Brookfarm'),(9,'Cadbury'),(10,'Calbee'),(11,'Camel'),(12,'Captain Oats'),(13,'Carman\'S'),(14,'Chupa Chups'),(15,'Cj'),(16,'Cowhead'),(17,'Crusty\'S'),(18,'Del Monte'),(19,'Ego'),(20,'Fairprice'),(21,'Farmland'),(22,'Fisherman'),(23,'Food For Friends'),(24,'Freedom Foods'),(25,'Frezfruta'),(26,'Gardenia'),(27,'Glico'),(28,'Golden Chef'),(29,'Golden Rice Box'),(30,'Gulong'),(31,'Haldiram\'S'),(32,'Haribo'),(33,'Harvest Fields'),(34,'Hershey\'S'),(35,'Highway'),(36,'Hosen'),(37,'Hunted + Gathered'),(38,'Jack \'N Jill'),(39,'John West'),(40,'Julie\'S'),(41,'Kangshifu'),(42,'Kellogg\'S'),(43,'Khong Guan'),(44,'Kinder Bueno'),(45,'Kirkland'),(46,'Kit,Kat'),(47,'Koka'),(48,'Kraft'),(49,'Lakerol'),(50,'Lay\'S'),(51,'Lindt'),(52,'Loacker'),(53,'Lotte'),(54,'Maggi'),(55,'Mayvers'),(56,'Meiji'),(57,'Mili'),(58,'Mission'),(59,'M&M\'S'),(60,'Munchy\'S'),(61,'Myojo'),(62,'Narcissus'),(63,'Nature\'S Wonders'),(64,'Nestle'),(65,'New Moon'),(66,'Nissin'),(67,'Nongshim'),(68,'Oreo'),(69,'Origins'),(70,'Ottogi'),(71,'Peter Pan'),(72,'Post'),(73,'Prima Taste'),(74,'Pringles'),(75,'Quaker'),(76,'Redondo'),(77,'Ricola'),(78,'Ritter Sport'),(79,'Samyang'),(80,'Sing Long'),(81,'Skippy'),(82,'Smuckers'),(83,'St.Dalfour'),(84,'Strepsils'),(85,'Sunshine'),(86,'S&W'),(87,'Tai Sun'),(88,'Tao Kae Noi'),(89,'Tesco'),(90,'Tesco Finest'),(91,'The Natural Confectionery Co.'),(92,'Tohato'),(93,'Tong Garden'),(94,'Town Bus'),(95,'Tulip'),(96,'Twisties'),(97,'Uha'),(98,'Vicks'),(99,'Yifon'),(100,'Yum Earth');
/*!40000 ALTER TABLE `brand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `brand_supermarket`
--

DROP TABLE IF EXISTS `brand_supermarket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `brand_supermarket` (
  `brand_id` int(11) NOT NULL,
  `supermarket_id` int(11) NOT NULL,
  PRIMARY KEY (`brand_id`,`supermarket_id`),
  KEY `idx_brand_supermarket` (`supermarket_id`),
  CONSTRAINT `fk_brand_supermarket__brand` FOREIGN KEY (`brand_id`) REFERENCES `brand` (`id`),
  CONSTRAINT `fk_brand_supermarket__supermarket` FOREIGN KEY (`supermarket_id`) REFERENCES `supermarket` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brand_supermarket`
--

LOCK TABLES `brand_supermarket` WRITE;
/*!40000 ALTER TABLE `brand_supermarket` DISABLE KEYS */;
INSERT INTO `brand_supermarket` VALUES (5,2),(5,3),(90,4),(88,5),(12,6);
/*!40000 ALTER TABLE `brand_supermarket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `brand_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_item__brand_name` (`brand_id`),
  CONSTRAINT `fk_item__brand_name` FOREIGN KEY (`brand_id`) REFERENCES `brand` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item`
--

LOCK TABLES `item` WRITE;
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` VALUES (1,5,'Sardines in Tomato'),(2,5,'Sardines in Tomato Sauce'),(3,90,'Maple Biscuits'),(4,88,'Tasty'),(5,12,'Instant Oatmeal');
/*!40000 ALTER TABLE `item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itemcost`
--

DROP TABLE IF EXISTS `itemcost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `itemcost` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime DEFAULT NULL,
  `cost` varchar(255) NOT NULL,
  `user_id` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  `supermarket_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_itemcost__item` (`item_id`),
  KEY `idx_itemcost__supermarket` (`supermarket_id`),
  KEY `idx_itemcost__user` (`user_id`),
  CONSTRAINT `fk_itemcost__item` FOREIGN KEY (`item_id`) REFERENCES `item` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_itemcost__supermarket` FOREIGN KEY (`supermarket_id`) REFERENCES `supermarket` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_itemcost__user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itemcost`
--

LOCK TABLES `itemcost` WRITE;
/*!40000 ALTER TABLE `itemcost` DISABLE KEYS */;
INSERT INTO `itemcost` VALUES (1,'2019-11-06 15:45:05','$4',2,1,2),(2,'2019-11-06 15:46:05','$2.50',3,1,3),(3,'2019-11-06 15:47:09','$12',4,3,4),(4,'2019-11-06 15:48:01','$5.50',5,4,5);
/*!40000 ALTER TABLE `itemcost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `location` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `address` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location`
--

LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` VALUES (1,'Na','Tampines Mall'),(2,'NA','Tampines Mall'),(3,'NA','Tampines Megamart'),(4,'NA','Bishan'),(5,'NA','Bedok Center'),(6,'NA','Simei Eastpoint');
/*!40000 ALTER TABLE `location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location_supermarket`
--

DROP TABLE IF EXISTS `location_supermarket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `location_supermarket` (
  `location_id` int(11) NOT NULL,
  `supermarket_id` int(11) NOT NULL,
  PRIMARY KEY (`location_id`,`supermarket_id`),
  KEY `idx_location_supermarket` (`supermarket_id`),
  CONSTRAINT `fk_location_supermarket__location` FOREIGN KEY (`location_id`) REFERENCES `location` (`id`),
  CONSTRAINT `fk_location_supermarket__supermarket` FOREIGN KEY (`supermarket_id`) REFERENCES `supermarket` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location_supermarket`
--

LOCK TABLES `location_supermarket` WRITE;
/*!40000 ALTER TABLE `location_supermarket` DISABLE KEYS */;
INSERT INTO `location_supermarket` VALUES (1,1),(1,2),(3,3),(4,4),(5,5),(6,6);
/*!40000 ALTER TABLE `location_supermarket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supermarket`
--

DROP TABLE IF EXISTS `supermarket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `supermarket` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supermarket`
--

LOCK TABLES `supermarket` WRITE;
/*!40000 ALTER TABLE `supermarket` DISABLE KEYS */;
INSERT INTO `supermarket` VALUES (1,'NTUC'),(2,'Giant'),(3,'Giant'),(4,'Cold Storage'),(5,'Sheng Siong'),(6,'NTUC');
/*!40000 ALTER TABLE `supermarket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Kira'),(2,'Kira'),(3,'Athrun'),(4,'Badang'),(5,'Badang'),(7,'asd200');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-08  7:48:41
