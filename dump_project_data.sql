-- MySQL dump 10.19  Distrib 10.3.29-MariaDB, for debian-linux-gnueabihf (armv7l)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	10.3.29-MariaDB-0+deb10u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `rooms`
--

DROP TABLE IF EXISTS `rooms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rooms` (
  `room_id` smallint(6) NOT NULL,
  `sensor_id` smallint(6) NOT NULL,
  PRIMARY KEY (`room_id`),
  KEY `sensor_id` (`sensor_id`),
  CONSTRAINT `rooms_ibfk_1` FOREIGN KEY (`sensor_id`) REFERENCES `sensors` (`sensor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rooms`
--

LOCK TABLES `rooms` WRITE;
/*!40000 ALTER TABLE `rooms` DISABLE KEYS */;
INSERT INTO `rooms` VALUES (23,1),(24,2),(25,3),(26,4);
/*!40000 ALTER TABLE `rooms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sensors`
--

DROP TABLE IF EXISTS `sensors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sensors` (
  `sensor_id` smallint(6) NOT NULL,
  `sensor_type` varchar(255) NOT NULL,
  `sensor_value` int(11) NOT NULL,
  `time_stamp` datetime DEFAULT current_timestamp(),
  `sensor_unit` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sensors`
--

LOCK TABLES `sensors` WRITE;
/*!40000 ALTER TABLE `sensors` DISABLE KEYS */;
INSERT INTO `sensors` VALUES (1,'temperature',21,'2021-10-16 22:14:40','C'),(1,'humidity',30,'2021-10-16 22:14:40','%'),(2,'temperature',19,'2021-10-16 22:14:40','C'),(2,'humidity',10,'2021-10-16 22:14:40','%'),(3,'temperature',24,'2021-10-16 22:14:40','C'),(3,'humidity',15,'2021-10-16 22:14:40','%'),(4,'temperature',20,'2021-10-16 22:14:40','C'),(4,'humidity',13,'2021-10-16 22:14:40','%'),(1,'temperature',20,'2021-10-17 11:41:28','C'),(1,'humidity',10,'2021-10-17 11:41:28','%'),(2,'temperature',23,'2021-10-17 11:41:28','C'),(2,'humidity',25,'2021-10-17 11:41:28','%'),(3,'temperature',20,'2021-10-17 11:41:28','C'),(3,'humidity',15,'2021-10-17 11:41:28','%'),(4,'temperature',17,'2021-10-17 11:41:28','C'),(4,'humidity',17,'2021-10-17 11:41:28','%');
/*!40000 ALTER TABLE `sensors` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-04 23:45:44