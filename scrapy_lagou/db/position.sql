/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50709
 Source Host           : localhost
 Source Database       : test

 Target Server Type    : MySQL
 Target Server Version : 50709
 File Encoding         : utf-8

 Date: 03/12/2017 22:17:03 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `position`
-- ----------------------------
DROP TABLE IF EXISTS `position`;
CREATE TABLE `position` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `j_id` int(11) DEFAULT NULL,
  `url` varchar(100) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `category` varchar(50) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `c_id` int(11) DEFAULT NULL,
  `c_url` varchar(100) DEFAULT NULL,
  `c_name` varchar(50) DEFAULT NULL,
  `industry` varchar(50) DEFAULT NULL,
  `financing_stage` varchar(50) DEFAULT NULL,
  `money` varchar(50) DEFAULT NULL,
  `experience` varchar(50) DEFAULT NULL,
  `education` varchar(255) DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2368 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
