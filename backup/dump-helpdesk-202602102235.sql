-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: helpdesk
-- ------------------------------------------------------
-- Server version	9.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `asistencias`
--

DROP TABLE IF EXISTS `asistencias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `asistencias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `asistencia_empleado_codigo` int NOT NULL,
  `fecha` date NOT NULL,
  `estado` enum('P','A') NOT NULL,
  `asistencia_autorizado_email` varchar(40) DEFAULT NULL,
  `asistencia_fecha_cambio` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `asistencia_empleado_codigo` (`asistencia_empleado_codigo`,`fecha`),
  CONSTRAINT `asistencias_ibfk_1` FOREIGN KEY (`asistencia_empleado_codigo`) REFERENCES `empleados` (`empleado_codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asistencias`
--

LOCK TABLES `asistencias` WRITE;
/*!40000 ALTER TABLE `asistencias` DISABLE KEYS */;
INSERT INTO `asistencias` VALUES (1,1001,'2026-01-01','P','fredy_k8401@hotmail.com','2026-01-29 10:40:12'),(3,8401,'2026-01-02','P','fredy_k8401@hotmail.com','2026-01-28 10:36:11'),(4,1001,'2026-01-28','P','fredy_k8401@hotmail.com','2026-01-28 10:37:25'),(5,8401,'2026-01-28','P','fredy_k8401@hotmail.com','2026-01-28 10:37:27'),(6,1001,'2026-01-11','P','fredy_k8401@hotmail.com','2026-01-28 11:01:01'),(7,8401,'2026-01-11','P','fredy_k8401@hotmail.com','2026-01-28 11:01:03'),(8,8402,'2026-01-11','P','fredy_k8401@hotmail.com','2026-01-28 11:01:03'),(9,8402,'2026-01-10','P','fredy_k8401@hotmail.com','2026-01-28 11:01:08'),(10,8401,'2026-01-10','P','fredy_k8401@hotmail.com','2026-01-28 11:01:09'),(11,1001,'2026-01-10','P','fredy_k8401@hotmail.com','2026-01-28 11:01:10'),(13,8401,'2026-01-01','P','fredy_k8401@hotmail.com','2026-01-29 10:26:05'),(14,8402,'2026-01-01','P','fredy_k8401@hotmail.com','2026-01-29 10:26:06'),(15,8402,'2026-01-02','P','fredy_k8401@hotmail.com','2026-01-29 10:26:07'),(17,1001,'2026-01-02','P','fredy_k8401@hotmail.com','2026-01-29 10:40:14'),(18,1001,'2026-01-03','P','fredy_k8401@hotmail.com','2026-01-29 10:40:16'),(19,1001,'2026-01-04','P','fredy_k8401@hotmail.com','2026-01-29 10:40:18'),(20,1001,'2026-01-05','P','fredy_k8401@hotmail.com','2026-01-30 11:56:36'),(21,1001,'2026-01-06','P','fredy_k8401@hotmail.com','2026-01-30 11:56:38'),(22,1001,'2026-01-07','P','fredy_k8401@hotmail.com','2026-01-30 11:56:39'),(23,1001,'2026-01-08','P','fredy_k8401@hotmail.com','2026-01-30 11:56:40'),(24,1001,'2026-02-21','P','fredy_k8401@hotmail.com','2026-01-31 18:10:22'),(25,1001,'2026-02-22','P','fredy_k8401@hotmail.com','2026-01-31 18:10:24'),(26,1001,'2026-02-23','P','fredy_k8401@hotmail.com','2026-01-31 18:10:25'),(27,1001,'2026-02-02','P','fredy_k8401@hotmail.com','2026-02-05 22:50:56'),(28,1001,'2026-02-03','P','fredy_k8401@hotmail.com','2026-02-05 22:50:57'),(29,1001,'2026-02-04','P','fredy_k8401@hotmail.com','2026-02-05 22:50:59'),(30,1001,'2026-02-05','P','fredy_k8401@hotmail.com','2026-02-05 23:18:17'),(31,8401,'2026-02-02','P','fredy_k8401@hotmail.com','2026-02-07 20:07:52'),(32,8401,'2026-02-03','P','fredy_k8401@hotmail.com','2026-02-07 20:07:52'),(33,8401,'2026-02-04','P','fredy_k8401@hotmail.com','2026-02-07 20:07:54'),(34,8401,'2026-02-05','P','fredy_k8401@hotmail.com','2026-02-07 20:07:57'),(35,8402,'2026-02-02','P','fredy_k8401@hotmail.com','2026-02-07 20:08:02'),(36,8402,'2026-02-03','P','fredy_k8401@hotmail.com','2026-02-07 20:08:02'),(37,8402,'2026-02-04','P','fredy_k8401@hotmail.com','2026-02-07 20:08:05'),(38,8402,'2026-02-05','P','fredy_k8401@hotmail.com','2026-02-07 20:08:07'),(39,8403,'2026-02-01','P','fredy_k8401@hotmail.com','2026-02-09 22:33:45'),(40,8403,'2026-02-02','P','fredy_k8401@hotmail.com','2026-02-09 22:33:46'),(41,8403,'2026-02-03','P','fredy_k8401@hotmail.com','2026-02-09 22:33:47'),(42,8403,'2026-02-04','P','fredy_k8401@hotmail.com','2026-02-09 22:33:48'),(43,8403,'2026-02-05','P','fredy_k8401@hotmail.com','2026-02-09 22:33:49'),(44,8401,'2026-02-21','P','fredy_k8401@hotmail.com','2026-02-09 22:34:01'),(45,8402,'2026-02-21','P','fredy_k8401@hotmail.com','2026-02-09 22:34:02'),(46,8403,'2026-02-22','P','fredy_k8401@hotmail.com','2026-02-09 22:34:03'),(47,8402,'2026-02-22','P','fredy_k8401@hotmail.com','2026-02-09 22:34:04'),(48,8401,'2026-02-22','P','fredy_k8401@hotmail.com','2026-02-09 22:34:04'),(49,8401,'2026-02-23','P','fredy_k8401@hotmail.com','2026-02-09 22:34:05'),(50,8402,'2026-02-23','P','fredy_k8401@hotmail.com','2026-02-09 22:34:06'),(51,8403,'2026-02-23','P','fredy_k8401@hotmail.com','2026-02-09 22:34:08');
/*!40000 ALTER TABLE `asistencias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `autorizados`
--

DROP TABLE IF EXISTS `autorizados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `autorizados` (
  `autorizado_email` varchar(40) DEFAULT NULL,
  `autorizado_password` varchar(15) DEFAULT NULL,
  `autorizado_filler` varchar(20) DEFAULT NULL,
  `autorizado_id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`autorizado_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `autorizados`
--

LOCK TABLES `autorizados` WRITE;
/*!40000 ALTER TABLE `autorizados` DISABLE KEYS */;
INSERT INTO `autorizados` VALUES ('fredy_k8401@hotmail.com','Paco8401',NULL,1);
/*!40000 ALTER TABLE `autorizados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cierres`
--

DROP TABLE IF EXISTS `cierres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cierres` (
  `cierre_id` int NOT NULL AUTO_INCREMENT,
  `cierre_periodo` varchar(6) COLLATE utf8mb4_unicode_ci NOT NULL,
  `cierre_estado` char(1) COLLATE utf8mb4_unicode_ci NOT NULL,
  `cierre_autorizado_email` varchar(40) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `cierre_fecha_cambio` datetime DEFAULT NULL,
  PRIMARY KEY (`cierre_id`),
  UNIQUE KEY `uq_cierre_periodo` (`cierre_periodo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cierres`
--

LOCK TABLES `cierres` WRITE;
/*!40000 ALTER TABLE `cierres` DISABLE KEYS */;
INSERT INTO `cierres` VALUES (1,'202601','C','fredy_k8401@hotmail.com','2026-02-01 08:30:00'),(2,'202602','','fredy_k8401@hotmail.com','2026-02-09 22:33:17');
/*!40000 ALTER TABLE `cierres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `conceptos`
--

DROP TABLE IF EXISTS `conceptos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `conceptos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `concepto_codigo` varchar(40) DEFAULT NULL,
  `concepto_nombre` varchar(40) DEFAULT NULL,
  `concepto_tipo` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='conceptos';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conceptos`
--

LOCK TABLES `conceptos` WRITE;
/*!40000 ALTER TABLE `conceptos` DISABLE KEYS */;
INSERT INTO `conceptos` VALUES (1,'INGRESO_COMPRAS','INGRESO COMPRAS','ING'),(2,'INGRESO_OTROS','INGRESO OTROS','ING'),(3,'SALIDA_VENTAS','SALIDA VENTAS','SAL'),(4,'SALIDA_OTROS','SALIDA OTROS','SAL');
/*!40000 ALTER TABLE `conceptos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empleados`
--

DROP TABLE IF EXISTS `empleados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empleados` (
  `empleado_id` int NOT NULL AUTO_INCREMENT,
  `empleado_codigo` int NOT NULL,
  `empleado_nombres` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `empleado_filler` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `empleado_email` varchar(40) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `empleado_estado` char(1) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'A',
  `asistencia_autorizado_email` varchar(40) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `asistencia_fecha_cambio` datetime DEFAULT NULL,
  PRIMARY KEY (`empleado_id`),
  UNIQUE KEY `uq_empleado_codigo` (`empleado_codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleados`
--

LOCK TABLES `empleados` WRITE;
/*!40000 ALTER TABLE `empleados` DISABLE KEYS */;
INSERT INTO `empleados` VALUES (1,1001,'Jose Espinoza B','Gerencia','jose.espinoza@bramil.com','V',NULL,NULL),(3,8401,'Fredy Espinoza','Gerencia','fredy.espinoza@bramil.com','V',NULL,NULL),(4,8402,'Lucero Quispe',NULL,NULL,'V',NULL,NULL),(5,8403,'GUSTAVO ROJAS',NULL,NULL,'V',NULL,NULL);
/*!40000 ALTER TABLE `empleados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `farmacos`
--

DROP TABLE IF EXISTS `farmacos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `farmacos` (
  `farmaco_codigo` varchar(15) DEFAULT NULL,
  `farmaco_nombre` varchar(50) DEFAULT NULL,
  `farmaco_marca_id` varchar(15) DEFAULT NULL,
  `farmaco_cantidad` decimal(10,0) DEFAULT NULL,
  `farmaco_precio` decimal(10,0) DEFAULT NULL,
  `farmaco_fecha_creacion` date DEFAULT NULL,
  `farmaco_usuario_crea` varchar(40) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='farmacos';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farmacos`
--

LOCK TABLES `farmacos` WRITE;
/*!40000 ALTER TABLE `farmacos` DISABLE KEYS */;
INSERT INTO `farmacos` VALUES ('RK02018783','FARMACON','2',6,1,'2025-10-24','USER_NOT_LOGGED',1),('RK02018788','RK020187880','3',5,25,'2025-10-24','Fredy_k8401@hotmail.com',2),('ENALAPRIL','ENALAPRIL','5',10,1,'2025-10-25','Fredy_k8401@hotmail.com',3),('LISINOPRIL','LISINOPRIL','6',1,10,'2025-10-25','Fredy_k8401@hotmail.com',4),('BUSCAPYNA','BUSCAPINE','6',1,1,'2025-10-29','Fredy_k8401@hotmail.com',5),('DIPLOFENACO','DIPLOFENACO','6',10,10,'2025-10-31','Fredy_k8401@hotmail.com',6),('JANUVIA','JANUVIA','1',15,15,'2025-10-31','Fredy_k8401@hotmail.com',7),('ANTALAGINA','ANTALGINA DE 100MML','ROCHE 5',0,10,'2025-11-17','fredy_k8401@hotmail.com',8),('MEJORAL','MEJORAL 100ML','ROCHE 5',15,15,'2025-11-17','fredy_k8401@hotmail.com',9),('MENTHOLATUM','MENTOLATHUM','ROCHE 5',10,15,'2025-11-17','fredy_k8401@hotmail.com',10);
/*!40000 ALTER TABLE `farmacos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marcas`
--

DROP TABLE IF EXISTS `marcas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marcas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `marca_codigo` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `marca_nombre` varchar(50) DEFAULT NULL,
  `marca_vigencia` varchar(1) DEFAULT NULL,
  `marca_fecha_registro` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marcas`
--

LOCK TABLES `marcas` WRITE;
/*!40000 ALTER TABLE `marcas` DISABLE KEYS */;
INSERT INTO `marcas` VALUES (1,'ROCHE','ROCHE 1','V',NULL),(2,'ROCHE 1','ROCHE 11','V',NULL),(3,'ROCHE 2','ROCHE 20','V',NULL),(4,'ROCHE 3','ROCHE 3','V',NULL),(5,'Merck','Merck','V',NULL),(6,'AstraZeneca','AstraZeneca','V',NULL),(7,'Novartis','Novartis','V',NULL),(8,'Pfizer','Pfizer','V',NULL),(9,'ROCHE 5','ROCHE 55','V',NULL);
/*!40000 ALTER TABLE `marcas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movimientos`
--

DROP TABLE IF EXISTS `movimientos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movimientos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `movimiento_farmaco_codigo` varchar(15) DEFAULT NULL,
  `movimiento_marca_codigo` varchar(15) DEFAULT NULL,
  `movimiento_cantidad` int DEFAULT NULL,
  `movimiento_precio` decimal(10,0) DEFAULT NULL,
  `movimiento_fecha` date DEFAULT NULL,
  `movimiento_autorizado_email` varchar(40) DEFAULT NULL,
  `movimiento_concepto_tipo` varchar(3) DEFAULT NULL,
  `movimiento_periodo` varchar(6) DEFAULT NULL,
  `movimiento_concepto_codigo` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='movimientos';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movimientos`
--

LOCK TABLES `movimientos` WRITE;
/*!40000 ALTER TABLE `movimientos` DISABLE KEYS */;
INSERT INTO `movimientos` VALUES (1,'BUSCAPYNA','AstraZeneca',1,1,'2025-10-29','Fredy_k8401@hotmail.com','ING','202510','INGRESO_COMPRAS'),(2,'DIPLOFENACO','AstraZeneca',10,10,'2025-10-31','Fredy_k8401@hotmail.com','ING','202510','INGRESO_COMPRAS'),(3,'JANUVIA','ROCHE',15,15,'2025-10-31','Fredy_k8401@hotmail.com','ING','202510','INGRESO_OTROS'),(4,'MENTHOLATUM','ROCHE 5',10,15,'2025-11-17','fredy_k8401@hotmail.com','ING','202511','INGRESO_COMPRAS'),(5,'ANTALAGINA','ROCHE 5',10,10,'2025-11-17','fredy_k8401@hotmail.com','ING','202511','INGRESO_COMPRAS'),(6,'ANTALAGINA','ROCHE 5',25,10,'2025-11-17','fredy_k8401@hotmail.com','SAL','202511','SALIDA_VENTAS'),(7,'ANTALAGINA','ROCHE 5',5,10,'2025-11-18','fredy_k8401@hotmail.com','SAL','202511','SALIDA_VENTAS');
/*!40000 ALTER TABLE `movimientos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'helpdesk'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-02-10 22:35:14
