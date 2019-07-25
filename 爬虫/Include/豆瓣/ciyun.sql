/*
Navicat MySQL Data Transfer

Source Server         : 阿里云
Source Server Version : 50716
Source Host           : biggsai.com:3306
Source Database       : project

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2019-07-26 04:16:23
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for ciyun
-- ----------------------------
DROP TABLE IF EXISTS `ciyun`;
CREATE TABLE `ciyun` (
  `moviename` varchar(255) DEFAULT NULL,
  `id` int(11) DEFAULT NULL,
  `text` varchar(8000) CHARACTER SET utf8mb4 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
