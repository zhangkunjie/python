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

 Date: 08/04/2017 08:25:51 AM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `fund_rank`
-- ----------------------------
DROP TABLE IF EXISTS `fund_rank`;
CREATE TABLE `fund_rank` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fund_id` varchar(20) DEFAULT NULL,
  `fund_name` varchar(50) DEFAULT NULL,
  `fund_name_abbr` varchar(20) DEFAULT NULL,
  `cal_date` date DEFAULT NULL,
  `net_asset_value` decimal(10,4) DEFAULT NULL,
  `accumulative` decimal(10,4) DEFAULT NULL,
  `oneday` varchar(255) DEFAULT NULL,
  `oneweek` varchar(255) DEFAULT NULL,
  `onemonth` varchar(255) DEFAULT NULL,
  `threemonth` varchar(255) DEFAULT NULL,
  `sixmonth` varchar(255) DEFAULT NULL,
  `oneyear` varchar(255) DEFAULT NULL,
  `twoyear` varchar(255) DEFAULT NULL,
  `threeyear` varchar(255) DEFAULT NULL,
  `thisyear` varchar(255) DEFAULT NULL,
  `setup` varchar(255) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10106 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
