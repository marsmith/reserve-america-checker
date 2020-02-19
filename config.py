#use getWaterSites.py to generate list of water sites from campadk.com

campgrounds = [
    {
    "name": "SCAROON MANOR",
    "campadk_url": "https://www.campadk.com/campsitephotos/campgrounds/Scaroon+Manor/site/",
    "ra_url": "https://newyorkstateparks.reserveamerica.com/camping/scaroon-manor/r/campgroundDetails.do?contractCode=NY&parkId=3386",
    "preferred_sites": ['31', '32', '33', '34', '35']
    },
    {
    "name": "BROWN TRACT POND",
    "campadk_url": "https://www.campadk.com/campsitephotos/campgrounds/Brown+Tract+Pond/site/",
    "ra_url": "https://newyorkstateparks.reserveamerica.com/camping/brown-tract-pond-campground/r/campgroundDetails.do?contractCode=NY&parkId=625",
    "preferred_sites": ['7', '8', '10', '12', '14', '17', '18', '19', '22', '23', '26', '27', '28', '29', '33', '34', '35', '36', '37', '39', '40', '42', '43', '44', '45', '47', '69', '70', '73', '84', '85', '86', '87', '88', '89', '90']
    },
    {
    "name": "MOFFIT BEACH",
    "campadk_url": "https://www.campadk.com/campsitephotos/campgrounds/Moffit+Beach/site/",
    "ra_url": "https://newyorkstateparks.reserveamerica.com/camping/moffitt-beach-campground/r/campgroundDetails.do?contractCode=NY&parkId=673",
    "preferred_sites": ['106', '107', '109', '112', '114', '117', '118', '182', '183', '185', '187', '191', '192', '193', '196', '197', '198', '200', '202', '203', '205', '207', '210', '212', '214', '215', '216', '218', '220', '221', '223', '224', '226', '229', '231', '232', '233', '234', '235', '236', '237', '238', '239', '240', '241', '242', '244', '245', '247', '248', '250', '251', '252', '253']
    },
    {
    "name": "NORTHAMPTON BEACH",
    "campadk_url": "https://www.campadk.com/campsitephotos/campgrounds/Northampton+Beach/site/",
    "ra_url": "https://newyorkstateparks.reserveamerica.com/camping/northampton-beach-campground/r/campgroundDetails.do?contractCode=NY&parkId=681",
    "preferred_sites": ['3', '5', '6', '8', '10', '12', '13', '14', '32', '34', '36', '38', '39', '40', '41', '42', '43', '59', '62', '64', '66', '66A', '68', '69', '72', '73', '74A', '74', '83', '83A', '84', '86', '88', '89', '90', '92', '94', '95', '96', '98', '103', '104', '105', '106', '108', '110', '112', '204', '205', '206', '207', '208', '209', '211', '212', '213', '214', '215', '216', '216A', '220']
    },
    {
    "name": "LAKE HARRIS",
    "campadk_url": "https://www.campadk.com/campsitephotos/campgrounds/Lake+Harris/site/",
    "ra_url": "https://newyorkstateparks.reserveamerica.com/camping/lake-harris-campground/r/campgroundDetails.do?contractCode=NY&parkId=593",
    "preferred_sites": ['2', '3', '5', '6', '7', '8', '9', '10', '11', '12', '14', '16', '20', '25', '26', '27', '29', '30', '31', '33', '35', '36', '37', '38', '39', '41', '43', '45', '46', '47', '48', '50', '59', '60', '68', '69', '71', '73', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86']
    },
    {
    "name": "LAKE EATON",
    "campadk_url": "https://www.campadk.com/campsitephotos/campgrounds/Lake+Eaton/site/",
    "ra_url": "https://newyorkstateparks.reserveamerica.com/camping/lake-eaton-campground/r/campgroundDetails.do?contractCode=NY&parkId=594",
    "preferred_sites": ['31', '32', '33', '34', '35', '36', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '63', '65', '67', '69', '71', '73', '75', '77', '80', '81', '82', '83', '84', '85', '88', '91', '93', '96', '98', '100', '101', '102', '103']
    },
    {
    "name": "LIMEKILN LAKE",
    "campadk_url": "https://www.campadk.com/campsitephotos/campgrounds/Limekiln+Lake/site/",
    "ra_url": "https://newyorkstateparks.reserveamerica.com/camping/limekiln-lake/r/campgroundDetails.do?contractCode=NY&parkId=661",
    "preferred_sites": ['1', '2', '3', '4', '5', '10', '12', '14', '15', '16', '17', '19', '20', '21', '23', '25', '26', '28', '29', '34', '93', '94', '98', '99', '100', '101', '102', '103', '104', '106', '107', '109', '111', '113', '115', '116', '126', '128', '129', '160', '162', '163', '164', '275']
    },
    {
    "name": "CRANBERRY LAKE",
    "campadk_url": "https://www.campadk.com/campsitephotos/campgrounds/Cranberry+Lake/site/",
    "ra_url": "https://newyorkstateparks.reserveamerica.com/camping/cranberry-lake-campground/r/campgroundDetails.do?contractCode=NY&parkId=706",
    "preferred_sites": ['14A', '14', '24', '41', '42', '43', '44', '45', '46', '47', '48', '61', '62', '63', '64', '65', '67', '68', '69', '89', '91', '92', '93', '95', '97', '98', '110', '111', '113', '115', '117', '118', '120', '121', '122', '124', '130', '132']
    },
    {
    "name": "MEACHAM LAKE",
    "campadk_url": "https://www.campadk.com/campsitephotos/campgrounds/Meacham+Lake/site/",
    "ra_url": "https://newyorkstateparks.reserveamerica.com/camping/meacham-lake-campground/r/campgroundDetails.do?contractCode=NY&parkId=608",
    "preferred_sites": ['92', '93', '94', '95', '97', '149', '151', '153', '154', '156', '157', '159', '161', '162', '163', '164', '165', '166', '168', '170', '171', '172', '173', '175', '176', '177', '178', '182', '183', '184', '185', '186', '187', '188']
    },
    {
    "name": "GOLDEN BEACH",
    "campadk_url": "https://www.campadk.com/campsitephotos/campgrounds/Golden+Beach/site/",
    "ra_url": "https://newyorkstateparks.reserveamerica.com/camping/golden-beach-campground/r/campgroundDetails.do?contractCode=NY&parkId=642",
    "preferred_sites": ['100', '101', '103', '106', '157A']
    },
    {
    "name": "NICKS LAKE",
    "campadk_url": "https://www.campadk.com/campsitephotos/campgrounds/Nicks+Lake/site/",
    "ra_url": "https://newyorkstateparks.reserveamerica.com/camping/nicks-lake-campground/r/campgroundDetails.do?contractCode=NY&parkId=699",
    "preferred_sites": ['61', '62', '65', '68', '70', '71', '94', '96', '97', '99', '102', '103', '105', '107', '108', '111', '112']
    },
    {
    "name": "EIGHTH LAKE",
    "campadk_url": "https://www.campadk.com/campsitephotos/campgrounds/Eighth+Lake/site/",
    "ra_url": "https://newyorkstateparks.reserveamerica.com/camping/eighth-lake-campground/r/campgroundDetails.do?contractCode=NY&parkId=636",
    "preferred_sites": ['21', '23', '24', '25', '27', '28', '30', '31', '33', '35', '37', '39', '41', '42', '45', '112', '113', '114', '114A', '116', '118']
    },
    {
    "name": "LAKE DURANT",
    "campadk_url": "https://www.campadk.com/campsitephotos/campgrounds/Lake+Durant/site/",
    "ra_url": "https://newyorkstateparks.reserveamerica.com/camping/lake-durant/r/campgroundDetails.do?contractCode=NY&parkId=653",
    "preferred_sites": ['1A', '2', '6', '8', '10', '12', '14', '16', '17', '20', '22', '26', '28', '30', '32', '33', '34', '35', '40', '41', '42', '44', '45', '46', '49', '50', '51', '52']
    },
    {
    "name": "LEWEY LAKE",
    "campadk_url": "https://www.campadk.com/campsitephotos/campgrounds/Lewey+Lake/site/",
    "ra_url": "https://newyorkstateparks.reserveamerica.com/camping/lewey-lake/r/campgroundDetails.do?contractCode=NY&parkId=657",
    "preferred_sites": ['1', '2', '3', '4', '6', '12', '13', '14', '18', '19', '20', '21', '23', '24', '30', '33', '43', '44', '74', '75', '76', '80', '82', '84', '86', '87', '88', '92', '93', '95', '97', '99', '101', '103', '105', '107', '109', '111', '113', '115', '117', '119', '121', '124', '126', '128', '130', '132', '134', '138', '140', '142', '144', '146', '148', '150', '155', '157', '159', '161', '188', '193', '195', '197', '200', '202', '203', '205', '206']
    },
    {
    "name": "ROLLINS POND",
    "campadk_url": "https://www.campadk.com/campsitephotos/campgrounds/Rollins+Pond/site/",
    "ra_url": "https://newyorkstateparks.reserveamerica.com/camping/rollins-pond-campground/r/campgroundDetails.do?contractCode=NY&parkId=547",
    "preferred_sites": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '25', '27', '28', '30', '32', '34', '35', '36', '37', '40', '41', '42', '43', '45', '47', '48', '50', '53', '54', '56', '58', '59', '60', '61', '62', '63', '64', '68', '70', '72', '74', '76', '78', '81', '82', '83', '85', '88', '89', '91', '92', '105', '106', '107', '108', '109', '110', '113', '114', '116', '117', '118', '120', '121', '123', '125', '126', '127', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '140', '141', '143', '145', '146', '147', '148', '150', '151', '153', '154', '156', '158', '159', '160', '161', '163', '165', '167', '169', '172', '173', '174', '177', '182', '183', '184', '185', '186', '187', '188', '189', '190', '191', '192', '194', '195', '196', '197', '198', '199', '200', '201', '202', '203', '204', '205', '206', '208', '209', '211', '212', '213', '214', '215', '216', '218', '219', '220', '221', '222', '223', '224', '225', '226', '227', '228', '229', '230', '231', '232', '233', '234', '235', '237', '238', '239', '240', '241', '242', '243', '246', '247', '248', '249', '250', '251', '252', '253', '254', '255', '256', '257', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A14', 'A15', 'A16', 'A17', 'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27', 'A28', 'A29', 'A30', 'A31']
    },
    {
    "name": "FISH CREEK POND",
    "campadk_url": "https://www.campadk.com/campsitephotos/campgrounds/Fish+Creek/site/",
    "ra_url": "https://newyorkstateparks.reserveamerica.com/camping/fish-creek-pond-campground/r/campgroundDetails.do?contractCode=NY&parkId=574",
    "preferred_sites": ['1', '1W', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '174', '175', '176', '177', '178', '179', '180', '181', '182', '183', '184', '185', '186', '187', '188', '189', '190', '191', '192', '193', '194', '195', '196', '197', '198', '199', '200', '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '211', '212', '213', '214', '215', '216', '217', '218', '219', '220', '221', '222', '223', '224', '225', '226', '227', '228', '229', '230', '231', '232', '233', '234', '235', '236', '237', '238', '239', '240', '241', '242', '243', '244', '245', '246', '247', '248', '249', '250', '251', '252', '253', '254', '255', '256', '257', '258', '259', '260', '261', '262', '263', '264', '265', '266', '267', '268', '269', '270', '271', '272', '273', '274', '275', '276', '277', '278', '279', '280', '281', '282', '283', '284', '285', '286', '287', '288', '289', '290', '291', '292', '293', '294', '295', '296', '297', '298', '299', '300', '301', '302', '303', '304', '305', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'R1', 'R2']
    }   
]