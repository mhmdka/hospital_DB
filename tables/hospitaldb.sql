-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 13, 2019 at 04:44 AM
-- Server version: 10.1.34-MariaDB
-- PHP Version: 7.2.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hospitaldb`
--

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

CREATE TABLE `appointment` (
  `Doctor_UserCode` int(5) NOT NULL,
  `Patient_UserCode` int(5) NOT NULL,
  `Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `assignbed`
--

CREATE TABLE `assignbed` (
  `RoomNumber` int(4) NOT NULL,
  `RoomFloor` int(2) NOT NULL,
  `BedNumber` int(2) NOT NULL,
  `Patient_UserCode` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `bed`
--

CREATE TABLE `bed` (
  `RoomNumber` int(4) NOT NULL,
  `RoomFloor` int(2) NOT NULL,
  `BedNumber` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `commit_message`
--

CREATE TABLE `commit_message` (
  `Doctor_UserCode` int(5) NOT NULL,
  `Patient_UserCode` int(5) NOT NULL,
  `MessageID` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `drug`
--

CREATE TABLE `drug` (
  `DrugName` varchar(20) NOT NULL,
  `Price` int(10) NOT NULL,
  `ExpirationDate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `examine`
--

CREATE TABLE `examine` (
  `Patient_UserCode` int(5) NOT NULL,
  `Nurse_UserCode` int(5) NOT NULL,
  `Detail` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `given`
--

CREATE TABLE `given` (
  `Doctor_UserCode` int(5) NOT NULL,
  `Patient_UserCode` int(5) NOT NULL,
  `PrescriptionID` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `has_drug`
--

CREATE TABLE `has_drug` (
  `PrescriptionID` int(5) NOT NULL,
  `DrugName` varchar(20) NOT NULL,
  `Quantity` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `managedrug`
--

CREATE TABLE `managedrug` (
  `PrescriptionID` int(5) NOT NULL,
  `DrugName` varchar(20) NOT NULL,
  `PaymentID` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `managelab`
--

CREATE TABLE `managelab` (
  `PrescriptionID` int(5) NOT NULL,
  `LabStaff_UserCode` int(5) NOT NULL,
  `ResultID` int(5) NOT NULL,
  `PaymentID` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `message`
--

CREATE TABLE `message` (
  `MessageID` int(5) NOT NULL,
  `Date` date NOT NULL,
  `Detail` varchar(1000) NOT NULL,
  `Title` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `PaymentID` int(11) NOT NULL,
  `Amount` int(9) NOT NULL,
  `Date` date NOT NULL,
  `Kind` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `prescription`
--

CREATE TABLE `prescription` (
  `PrescriptionID` int(5) NOT NULL,
  `isValid` tinyint(1) NOT NULL,
  `DrugFlag` tinyint(1) NOT NULL,
  `ExamineFlag` tinyint(1) NOT NULL,
  `Test_Type` int(1) NOT NULL,
  `Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `result`
--

CREATE TABLE `result` (
  `ResultID` int(5) NOT NULL,
  `Detail` varchar(1000) NOT NULL,
  `TakenDate` date NOT NULL,
  `GivenDate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `RoomNumber` int(4) NOT NULL,
  `Floor` int(2) NOT NULL,
  `BedCount` int(2) NOT NULL,
  `HallwayName` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `test`
--

CREATE TABLE `test` (
  `PrescriptionID` int(5) NOT NULL,
  `LabStaff_UserCode` int(5) NOT NULL,
  `ResultID` int(5) NOT NULL,
  `Price` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `User_Code` int(5) NOT NULL,
  `Username` varchar(20) NOT NULL,
  `Password` varchar(20) NOT NULL,
  `E-Mail` varchar(20) NOT NULL,
  `Phone_Number` varchar(11) NOT NULL,
  `YOB` smallint(4) NOT NULL,
  `Gender` enum('Male','Female') NOT NULL,
  `Height` smallint(3) NOT NULL,
  `Weight` smallint(3) NOT NULL,
  `Age` tinyint(2) NOT NULL,
  `Postal_Code` int(10) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Type` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appointment`
--
ALTER TABLE `appointment`
  ADD PRIMARY KEY (`Doctor_UserCode`,`Patient_UserCode`),
  ADD KEY `appointment_user_User_Code_fk_2` (`Patient_UserCode`);

--
-- Indexes for table `assignbed`
--
ALTER TABLE `assignbed`
  ADD PRIMARY KEY (`RoomNumber`,`RoomFloor`,`BedNumber`,`Patient_UserCode`),
  ADD KEY `assignbed_user_User_Code_fk` (`Patient_UserCode`);

--
-- Indexes for table `bed`
--
ALTER TABLE `bed`
  ADD PRIMARY KEY (`RoomNumber`,`RoomFloor`,`BedNumber`);

--
-- Indexes for table `commit_message`
--
ALTER TABLE `commit_message`
  ADD PRIMARY KEY (`Doctor_UserCode`,`Patient_UserCode`,`MessageID`),
  ADD KEY `commit_message_message_MessageID_fk` (`MessageID`),
  ADD KEY `commit_message_user_User_Code_fk_2` (`Patient_UserCode`);

--
-- Indexes for table `drug`
--
ALTER TABLE `drug`
  ADD PRIMARY KEY (`DrugName`);

--
-- Indexes for table `examine`
--
ALTER TABLE `examine`
  ADD PRIMARY KEY (`Patient_UserCode`,`Nurse_UserCode`),
  ADD KEY `examine_user_User_Code_fk_2` (`Nurse_UserCode`);

--
-- Indexes for table `given`
--
ALTER TABLE `given`
  ADD PRIMARY KEY (`Patient_UserCode`,`Doctor_UserCode`,`PrescriptionID`),
  ADD KEY `Doctor_UserCode` (`Doctor_UserCode`),
  ADD KEY `PrescriptionID` (`PrescriptionID`);

--
-- Indexes for table `has_drug`
--
ALTER TABLE `has_drug`
  ADD PRIMARY KEY (`PrescriptionID`,`DrugName`),
  ADD KEY `has_drug_drug_DrugName_fk` (`DrugName`);

--
-- Indexes for table `managedrug`
--
ALTER TABLE `managedrug`
  ADD PRIMARY KEY (`PrescriptionID`,`DrugName`,`PaymentID`),
  ADD KEY `PaymentID` (`PaymentID`);

--
-- Indexes for table `managelab`
--
ALTER TABLE `managelab`
  ADD PRIMARY KEY (`PrescriptionID`,`LabStaff_UserCode`,`ResultID`,`PaymentID`),
  ADD KEY `managelab_payment_PaymentID_fk` (`PaymentID`);

--
-- Indexes for table `message`
--
ALTER TABLE `message`
  ADD PRIMARY KEY (`MessageID`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`PaymentID`);

--
-- Indexes for table `prescription`
--
ALTER TABLE `prescription`
  ADD PRIMARY KEY (`PrescriptionID`);

--
-- Indexes for table `result`
--
ALTER TABLE `result`
  ADD PRIMARY KEY (`ResultID`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`RoomNumber`,`Floor`);

--
-- Indexes for table `test`
--
ALTER TABLE `test`
  ADD PRIMARY KEY (`PrescriptionID`,`LabStaff_UserCode`,`ResultID`),
  ADD KEY `test_result_ResultID_fk` (`ResultID`),
  ADD KEY `test_user_User_Code_fk_2` (`LabStaff_UserCode`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`User_Code`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `message`
--
ALTER TABLE `message`
  MODIFY `MessageID` int(5) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `PaymentID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `User_Code` int(5) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `appointment`
--
ALTER TABLE `appointment`
  ADD CONSTRAINT `appointment_user_User_Code_fk` FOREIGN KEY (`Doctor_UserCode`) REFERENCES `user` (`User_Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `appointment_user_User_Code_fk_2` FOREIGN KEY (`Patient_UserCode`) REFERENCES `user` (`User_Code`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `assignbed`
--
ALTER TABLE `assignbed`
  ADD CONSTRAINT `assignbed_ibfk_1` FOREIGN KEY (`RoomNumber`,`RoomFloor`,`BedNumber`) REFERENCES `bed` (`RoomNumber`, `RoomFloor`, `BedNumber`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `assignbed_user_User_Code_fk` FOREIGN KEY (`Patient_UserCode`) REFERENCES `user` (`User_Code`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `bed`
--
ALTER TABLE `bed`
  ADD CONSTRAINT `bed_ibfk_1` FOREIGN KEY (`RoomNumber`,`RoomFloor`) REFERENCES `room` (`RoomNumber`, `Floor`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `commit_message`
--
ALTER TABLE `commit_message`
  ADD CONSTRAINT `commit_message_message_MessageID_fk` FOREIGN KEY (`MessageID`) REFERENCES `message` (`MessageID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `commit_message_user_User_Code_fk` FOREIGN KEY (`Doctor_UserCode`) REFERENCES `user` (`User_Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `commit_message_user_User_Code_fk_2` FOREIGN KEY (`Patient_UserCode`) REFERENCES `user` (`User_Code`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `examine`
--
ALTER TABLE `examine`
  ADD CONSTRAINT `examine_user_User_Code_fk` FOREIGN KEY (`Patient_UserCode`) REFERENCES `user` (`User_Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `examine_user_User_Code_fk_2` FOREIGN KEY (`Nurse_UserCode`) REFERENCES `user` (`User_Code`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `given`
--
ALTER TABLE `given`
  ADD CONSTRAINT `given_ibfk_1` FOREIGN KEY (`Patient_UserCode`) REFERENCES `user` (`User_Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `given_ibfk_2` FOREIGN KEY (`Doctor_UserCode`) REFERENCES `user` (`User_Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `given_ibfk_3` FOREIGN KEY (`PrescriptionID`) REFERENCES `prescription` (`PrescriptionID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `has_drug`
--
ALTER TABLE `has_drug`
  ADD CONSTRAINT `has_drug_drug_DrugName_fk` FOREIGN KEY (`DrugName`) REFERENCES `drug` (`DrugName`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `has_drug_prescription_PrescriptionID_fk` FOREIGN KEY (`PrescriptionID`) REFERENCES `prescription` (`PrescriptionID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `managedrug`
--
ALTER TABLE `managedrug`
  ADD CONSTRAINT `managedrug_ibfk_1` FOREIGN KEY (`PrescriptionID`,`DrugName`) REFERENCES `has_drug` (`PrescriptionID`, `DrugName`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `managedrug_ibfk_2` FOREIGN KEY (`PaymentID`) REFERENCES `payment` (`PaymentID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `managelab`
--
ALTER TABLE `managelab`
  ADD CONSTRAINT `managelab_ibfk_1` FOREIGN KEY (`PrescriptionID`,`LabStaff_UserCode`,`ResultID`) REFERENCES `test` (`PrescriptionID`, `LabStaff_UserCode`, `ResultID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `managelab_payment_PaymentID_fk` FOREIGN KEY (`PaymentID`) REFERENCES `payment` (`PaymentID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `test`
--
ALTER TABLE `test`
  ADD CONSTRAINT `test_prescription_PrescriptionID_fk` FOREIGN KEY (`PrescriptionID`) REFERENCES `prescription` (`PrescriptionID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `test_result_ResultID_fk` FOREIGN KEY (`ResultID`) REFERENCES `result` (`ResultID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `test_user_User_Code_fk_2` FOREIGN KEY (`LabStaff_UserCode`) REFERENCES `user` (`User_Code`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
