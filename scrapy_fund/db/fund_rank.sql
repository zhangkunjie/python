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

 Date: 09/13/2017 08:46:01 AM
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
  `fund_name` varchar(100) DEFAULT NULL,
  `fund_name_abbr` varchar(50) DEFAULT NULL,
  `cal_date` varchar(50) DEFAULT NULL,
  `net_asset_value` float(10,4) DEFAULT NULL,
  `accumulative` float(10,4) DEFAULT NULL,
  `oneday` float(20,4) DEFAULT NULL,
  `oneweek` float(20,4) DEFAULT NULL,
  `onemonth` float(20,4) DEFAULT NULL,
  `threemonth` float(20,4) DEFAULT NULL,
  `sixmonth` float(20,4) DEFAULT NULL,
  `oneyear` float(20,4) DEFAULT NULL,
  `twoyear` float(20,4) DEFAULT NULL,
  `threeyear` float(20,4) DEFAULT NULL,
  `thisyear` float(20,4) DEFAULT NULL,
  `setup` float(20,4) DEFAULT NULL,
  `category` varchar(20) DEFAULT NULL,
  `score` float(20,4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6160 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
