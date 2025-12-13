-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 13, 2025 at 08:01 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `novelchem_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `history`
--

CREATE TABLE `history` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `pLC50` varchar(50) DEFAULT NULL,
  `atom_count` varchar(50) DEFAULT NULL,
  `smiles` varchar(255) DEFAULT NULL,
  `logP` varchar(50) DEFAULT NULL,
  `justification` varchar(255) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `history`
--

INSERT INTO `history` (`id`, `user_id`, `pLC50`, `atom_count`, `smiles`, `logP`, `justification`, `image`) VALUES
(100, 11, NULL, NULL, 'O=C(Nc1ccccc1)CCC(=O)NCCO', NULL, 'This molecule is a valid candidate as its predicted logP and atom count both fall within the specified target constraints. The presence of two amide functionalities and a terminal alcohol group contributes to a balanced lipophilicity and provides hydrogen', NULL),
(101, 11, NULL, NULL, 'CCCCNC(=O)Cc1ncccc1', NULL, 'This molecule satisfies the physicochemical constraints for lipophilicity and size, with its predicted logP and atom count falling within the target ranges. The butyl chain and pyridine ring contribute to its balanced lipophilicity, while its compact stru', NULL),
(102, 11, NULL, NULL, 'CNC(=O)c1sc(cc1)-c2ccc(OC)cc2', NULL, 'This molecule is a valid candidate because its predicted logP (2.94) and atom count (18) both fall within the specified target constraints, indicating suitable lipophilicity and small size for drug development. The two aromatic rings and methyl groups con', NULL),
(103, 11, NULL, NULL, 'Cc1cc(ncc1)CN(C)C(=O)C(C)O', NULL, 'The molecule\'s predicted logP and atom count satisfy the target constraints, indicating appropriate lipophilicity for membrane permeability and an ideal molecular size. Its pyridine core and aliphatic chain contribute to moderate lipophilicity, balanced b', NULL),
(104, 11, NULL, NULL, 'CC(=O)Oc1ccccc1CCNC(=O)C', NULL, 'The candidate\'s predicted logP and atom count fall within the specified target constraints, reflecting a balanced lipophilicity from its aromatic ring and aliphatic chains tempered by polar ester and amide groups, alongside a compact molecular size. While', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `password`) VALUES
(11, 'chemappfinal@gmail.com', 'chemappfinal@gmail.com', '$2b$12$e9vRUYYZ86DLF5v503GzOuXu8qolBRtU9YuYgqOUNcMpVP7AjN/0m');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `history`
--
ALTER TABLE `history`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `history`
--
ALTER TABLE `history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=105;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `history`
--
ALTER TABLE `history`
  ADD CONSTRAINT `history_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
