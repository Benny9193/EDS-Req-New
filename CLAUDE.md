# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Report Generation Defaults

- **Default date range**: Most recent completed budget year, which runs **December 1 – November 30**.
- **Infer the current date from context at the start of every session** to determine the correct budget years:
  - Budget year ends November 30. If today is on or after December 1, the most recently completed year started the prior December 1.
  - Example: today = 2026-03-11 → most recent completed = **Dec 1, 2024 – Nov 30, 2025** | current in-progress = **Dec 1, 2025 – Nov 30, 2026**
- Only use a different date range when the user explicitly requests it.

## Report Field Conventions

- **Always use `BidHeaderId`** (from the `Bids` table) — never `BidHeaderKey` — when querying or displaying bid header references in reports.

## Vendor ID Lookup

Active vendors with purchase orders (Dec 2022 – Nov 2025), ordered by total spend.
Format: `VendorId | Code | Name | PO Count | Total Spend`

| VendorId | Code | Name | POs | Total Spend |
|----------|------|------|-----|-------------|
| 9 | 0009 | School Specialty, LLC | 205,723 | $62,112,979.69 |
| 2198 | 2222 | Staples Inc dba Staples Contract & Commercial LLC | 55,509 | $21,982,662.44 |
| 3 | 0003 | Cascade School Supplies, Inc. | 94,345 | $19,058,086.73 |
| 135 | 0118 | Varsity Brands, Inc. dba BSN Sports LLC | 18,177 | $12,319,475.43 |
| 4 | 0004 | Blick Art Materials LLC | 14,501 | $11,392,729.01 |
| 9045 | 1538 | United Supply of NJ Corp | 62,325 | $9,988,290.34 |
| 552 | 0528 | School Health Corporation | 19,747 | $8,799,702.38 |
| 541 | 0518 | School Specialty LLC dba Nasco Education | 33,384 | $5,900,306.01 |
| 8341 | 8080 | W.B. Mason Co., Inc. | 8,989 | $5,570,653.70 |
| 916 | 0904 | Carolina Biological Supply Co | 11,119 | $4,726,186.17 |
| 8175 | 6664 | George L. Heider Inc. dba Sportsman's | 5,485 | $4,180,896.96 |
| 897 | 0885 | Lakeshore Learning Materials, LLC | 19,493 | $3,874,709.23 |
| 537 | 0513 | Henry Schein, Inc. | 8,854 | $3,618,331.80 |
| 5937 | 6906 | Midwest Technology Products | 3,457 | $2,889,124.47 |
| 944 | 0928 | Flinn Scientific, Inc. | 6,036 | $2,295,716.88 |
| 1002 | 0982 | VWR Funding, Inc dba Wards Science | 8,191 | $2,239,782.45 |
| 1738 | 1748 | Really Good Stuff, LLC | 17,349 | $1,983,106.41 |
| 3495 | 3513 | W.W. Grainger, Inc. dba Grainger | 1,398 | $1,758,871.75 |
| 3264 | 3287 | W.B. Mason Co., Inc. | 642 | $1,718,067.42 |
| 6679 | 7666 | Adorama Inc. | 1,835 | $1,706,025.32 |
| 770 | 0752 | Demco, Inc. | 4,867 | $1,666,704.63 |
| 2576 | 2612 | Eric Armin Inc. dba EAI Education | 10,346 | $1,484,648.55 |
| 6653 | 7640 | Laux Sports LLC dba Laux Sporting Goods | 2,002 | $1,442,382.44 |
| 3877 | 3916 | W.B. Mason Co., Inc. | 5,187 | $1,433,202.91 |
| 5175 | 6019 | Paxton Patterson LLC | 2,275 | $1,355,338.36 |
| 24 | 0014 | Stan's Sport Center Inc. | 1,283 | $1,339,160.80 |
| 3580 | 3604 | Imperial Bag & Paper Co., LLC | 254 | $1,283,001.77 |
| 2093 | 2112 | Triple Crown Sports, Inc. | 2,499 | $1,255,545.41 |
| 969 | 0950 | National Art & School Supplies, Inc. | 4,359 | $1,118,299.26 |
| 5641 | 6485 | S&S Worldwide, Inc. | 11,899 | $1,070,344.44 |
| 941 | 0925 | Fisher Scientific Company LLC | 5,103 | $1,065,376.80 |
| 2360 | 2393 | Sports Paradise | 550 | $1,011,199.27 |
| 2347 | 2380 | R&R Trophy & Sporting Goods dba Harrison S.G. | 2,250 | $950,529.30 |
| 6384 | 7351 | All American Sports Corp dba Riddell, Inc. | 385 | $935,209.48 |
| 583 | 0559 | Performance Health Holdings, Inc. dba Medco Supply | 6,607 | $884,115.72 |
| 984 | 0967 | VWR Funding, Inc dba Sargent Welch | 4,979 | $862,046.96 |
| 455 | 0432 | Kurtz Bros., Inc. | 13,684 | $811,727.87 |
| 611 | 0589 | S.A.N.E. | 1,568 | $791,855.79 |
| 3649 | 3674 | Puresan Holdings LLC | 127 | $734,609.19 |
| 5169 | 6013 | Metco Supply Inc. | 1,279 | $649,717.43 |
| 3369 | 3390 | Spruce Industries, Inc. | 106 | $642,445.31 |
| 4256 | 4312 | Sport's Time, Inc. | 175 | $634,454.99 |
| 5890 | 6835 | Pitsco Education, LLC | 1,966 | $623,165.64 |
| 863 | 0849 | Shar Products Company dba Shar Music | 1,990 | $621,583.68 |
| 979 | 0961 | Parco Scientific Company | 2,212 | $616,077.87 |
| 9325 | 5868 | Charles J Becker & Bro Inc/Beckers School Supplies | 5,811 | $573,170.55 |
| 1175 | 1156 | Uniforms For All Sports, Inc. | 679 | $558,226.68 |
| 880 | 0868 | Music In Motion Inc. | 2,490 | $547,048.71 |
| 3842 | 3877 | United Sales USA Corp. | 2,274 | $545,931.43 |
| 2941 | 2975 | Guitar Center Stores Inc dba Music and Arts | 3,450 | $536,887.83 |
| 7879 | 5428 | M&M Frankel Disposables Inc. | 62 | $496,009.19 |
| 2284 | 2316 | School Health Corporation dba Palos Sports | 1,543 | $492,146.43 |
| 6417 | 7384 | Kaplan Early Learning Company | 2,048 | $423,477.61 |
| 3072 | 3105 | Central Poly-Bag Corp. | 206 | $422,562.58 |
| 1623342 | 9535 | MD Buying Group LLC | 4,392 | $416,542.37 |
| 9237 | 0439 | Paper Clips Inc. | 1,624 | $416,061.92 |
| 3384 | 3405 | Tricull Industries Inc. dba Cleaning Systems Co. | 191 | $415,693.26 |
| 4065 | 4112 | American Eagle Co Inc. dba Teacher's Discovery | 3,104 | $404,394.75 |
| 8919 | 4824 | K&S Music Inc. | 1,437 | $398,876.39 |
| 1199 | 1182 | Cooper Electric Supply LLC dba Cooper Electric | 587 | $389,417.78 |
| 3104 | 3137 | Aramsco, Inc. | 697 | $374,242.75 |
| 3016 | 3051 | Atra Janitorial Supply Co. dba BradyPlus Co | 43 | $371,470.58 |
| 1932 | 1951 | O'Shea Lumber Company Inc. | 89 | $354,079.25 |
| 907 | 0895 | Catalano Musical Products | 1,252 | $349,588.70 |
| 5622 | 6465 | Ceramic Supply, Inc. | 724 | $331,207.45 |
| 14658 | 5345 | KTTA Enterprises, Inc dba South Jersey Sports | 578 | $326,658.07 |
| 1030 | 1008 | Camcor, Inc. | 741 | $323,203.74 |
| 3281 | 3303 | Simplify Chemical Solutions Inc. | 60 | $320,729.37 |
| 2193 | 2217 | Super Duper, Inc dba Super Duper Publications | 3,592 | $318,018.65 |
| 3660 | 3685 | Interboro Packaging Corporation | 266 | $314,178.36 |
| 5976 | 6944 | Varsity Spirit Fashions & Supplies LLC | 135 | $305,296.51 |
| 2130 | 2149 | Zams, Inc. | 527 | $303,921.20 |
| 9148 | 4963 | Winning Teams By Nissel, LLC | 431 | $300,479.13 |
| 795 | 0777 | The Library Store, Inc. | 1,832 | $288,289.25 |
| 913 | 0901 | ASI Associates, Inc. dba Arbor Scientific | 1,172 | $284,136.63 |
| 3235 | 3259 | W.B. Mason Co., Inc. | 416 | $277,301.47 |
| 1711600 | 9824 | Lakeshore Learning Materials, LLC | 2,086 | $266,797.91 |
| 3953 | 3995 | RSR Electronics Inc dba Electronix Express | 1,071 | $259,701.04 |
| 3954 | 3996 | Earlychildhood LLC dba Discount School Supply | 3,515 | $259,250.53 |
| 125 | 0109 | M-F Athletic Co Inc dba MFAC LLC | 317 | $249,362.50 |
| 12720 | 5971 | Aquatic Allstars LLC | 268 | $205,906.25 |
| 3215 | 3241 | John A. Earl, Inc. | 165 | $186,790.96 |
| 1623505 | 9743 | ASB Sports Acquisition Inc dba Game One | 666 | $186,098.97 |
| 2317 | 2350 | Metro Sport Inc dba Metro Swim Shop | 145 | $183,022.20 |
| 15621 | 6543 | Donna Jana Enterprizes LLC dba My Price Supply | 518 | $182,233.01 |
| 286 | 0267 | Bluum USA Inc. | 722 | $177,855.58 |
| 6092 | 7061 | Longstreth Sporting Goods, LLC | 341 | $160,031.70 |
| 8824 | 8468 | Absolute Fencing Gear Inc. | 68 | $150,970.66 |
| 4137 | 4186 | MSC Industrial Supply Co. | 12 | $148,713.89 |
| 411 | 0389 | Pyramid School Products dba Pyramid Paper Company | 645 | $148,701.83 |
| 3059 | 3094 | Camden Bag & Paper Co. dba Brady IFS NJ | 3 | $147,265.87 |
| 2997 | 3034 | American Paper Towel Co. dba BradyPlus Co. | 17 | $141,170.85 |
| 4961 | 5631 | Metro Team Outfitters dba Metro Team Sports | 150 | $139,827.70 |
| 7917 | 6884 | Pioneer Athletics dba Pioneer Manufacturing Co | 425 | $137,475.73 |
| 1721 | 1730 | HD Supply Facilities Maintenance dba HD Supply Inc | 7 | $133,584.00 |
| 8209 | 8981 | Advantage Music Limited | 574 | $131,931.29 |
| 8293 | 9563 | Washington Music Sales Center, Inc. | 560 | $119,986.10 |
| 13256 | 8158 | Plastic Express Inc. | 85 | $118,782.62 |
| 3605 | 3629 | Hillyard Inc. dba Hillyard / Mid-Atlantic | 42 | $109,972.30 |
| 5661 | 6505 | Eppy's Tool & Equipment Warehouse, Inc. | 57 | $107,240.46 |
| 1610724 | 8983 | A.O.M. Inc dba Creative Kids | 2,124 | $106,636.65 |
| 9371 | 5563 | Continental Hardware Inc. | 44 | $104,565.34 |
| 6739 | 7727 | West Music Company, Inc. | 956 | $102,840.50 |
| 3699 | 3726 | Z&Z Supply Merger Sub, LLC dba Johnstone Supply | 15 | $99,111.17 |
| 1364 | 1357 | Impex Micro LLC | 277 | $88,687.19 |
| 3456 | 3476 | Unipak Corp. | 10 | $87,130.40 |
| 117 | 0101 | Metuchen Center Inc | 27 | $84,885.96 |
| 1621069 | 9386 | Rmac Supplies Corp. | 31 | $75,576.95 |
| 3196 | 3224 | Indco, Inc. | 88 | $70,003.76 |
| 8784 | 8401 | PC University Distributors Inc. | 128 | $59,676.79 |
| 1623210 | 9489 | Johnson Lambe Company, Inc. | 111 | $59,529.78 |
| 8535 | 5338 | Washington Music Sales Center, Inc. | 117 | $57,722.35 |
| 1711130 | 9663 | PZ&SZ LLC dba Apex Supply USA | 80 | $56,818.78 |
| 13963 | 2130 | Sachs & Zitcer Supply Corp. | 8 | $53,874.04 |
| 3367 | 3389 | Scoles Floorshine Industries dba Scoles Systems | 27 | $52,239.26 |
| 9619 | 7579 | Farrar Filter Company, Inc. | 30 | $51,787.51 |
| 2787 | 2823 | Garden State Metals dba Metal Supermarkets | 6 | $48,007.37 |
| 8211 | 0609 | Hand2mind Inc | 314 | $45,859.93 |
| 6977 | 8203 | OTC Brands, Inc dba Oriental Trading Co. | 825 | $45,796.92 |
| 1623127 | 9422 | Propoint Imprints & Promotions, Ltd. | 29 | $44,473.70 |
| 374 | 0352 | Bluum USA, Inc. | 191 | $43,344.63 |
| 4946 | 5616 | HGNJ Marketing Group, LLC | 75 | $41,426.63 |
| 1588 | 1591 | Ocean Janitorial Supply, Inc. | 90 | $41,355.50 |
| 5688 | 6533 | Sweetwater Sound, LLC | 247 | $40,862.41 |
| 1623487 | 9589 | Sure Industries LLC | 36 | $39,815.63 |
| 716 | 0695 | Acco Brands Corporation dba Acco Brands USA LLC | 109 | $38,296.92 |
| 1850 | 1866 | Blue Gauntlet Fencing Gear, Inc. | 29 | $37,688.81 |
| 1117731 | 7838 | Metal Supply Center, LLC | 9 | $37,662.61 |
| 1686 | 1691 | AZ Plastics LLC | 8 | $37,314.25 |
| 3653 | 3678 | Capital Supply Company | 36 | $36,195.08 |
| 7031 | 8331 | Klingspor Corporation dba Klingspor's Woodworking | 310 | $33,694.35 |
| 2170 | 2189 | Brookaire Company, LLC | 24 | $29,394.29 |
| 2294 | 2326 | American Process Lettering Inc dba AMPRO | 33 | $27,843.88 |
| 14953 | 5470 | Fun and Function LLC | 364 | $27,379.60 |
| 2961 | 2995 | L&W Supply Corp. dba Feldman Lumber | 9 | $25,598.05 |
| 5803 | 6691 | Stadium System, Inc. | 14 | $22,123.85 |
| 1615090 | 9233 | Project Lead The Way, Inc. | 8 | $21,349.00 |
| 11602 | 1498 | Wallington Plumbing & Heating Supply Co. | 2 | $20,654.21 |
| 1989 | 2008 | Totowa Parts LLC dba JDL Corp./Prostock Auto Parts | 9 | $20,139.54 |
| 3891 | 3930 | Scott Electric Co. | 112 | $19,111.15 |
| 6072 | 7041 | Plaques & Such, LLC | 21 | $18,429.30 |
| 3464 | 3483 | Knight Marketing Enterprises LLC | 50 | $17,516.07 |
| 6212 | 7178 | Sports Imports, Inc. | 8 | $17,012.09 |
| 9519 | 2511 | PROJECT LEAD THE WAY | 5 | $16,288.60 |
| 1189 | 1171 | Adolph Kiefer & Associates LLC dba Kiefer Aquatics | 48 | $16,082.67 |
| 14668 | 5197 | Eastern Janitorial Supply, LLC | 1 | $15,323.99 |
| 127 | 0110 | Jostens, Inc dba Neff | 33 | $13,977.25 |
| 7764 | T079 | Savvas Learning Company, LLC | 10 | $12,974.22 |
| 515 | 0491 | Lindenmeyr Munroe Div. Central National Gottesman | 1 | $12,599.80 |
| 1615022 | 9193 | Centurion Partners Health & Fitness dba Fitnessmith | 2 | $12,171.00 |
| 2775 | 2811 | SupplyitAll dba South Jersey Paper Company | 16 | $11,707.58 |
| 6205 | 7171 | Resilite Sports Products, Inc. | 1 | $11,694.48 |
| 1552 | 1555 | VEX Robotics, Inc. | 7 | $10,805.60 |
| 2947 | 2981 | Best Plumbing Specialties, Inc. | 7 | $10,053.84 |
| 5576 | 6422 | Joseph Gartland Inc. dba Beautiful Rags | 16 | $9,964.20 |
| 7883 | 7890 | Penn Jersey Paper Co., LLC a BradyPlus Company | 5 | $9,902.21 |
| 5047 | 5721 | R&S Distributors JK LLC | 20 | $9,710.99 |
| 4809 | 5096 | Macie Publishing Company | 6 | $7,993.66 |
| 1990 | 2009 | Allegheny Educational Systems, Inc. | 1 | $7,991.83 |
| 7621 | 9666 | Sterling Sanitary Supply Corp. | 51 | $7,261.79 |
| 3505 | 3526 | Amity Vacuum, Inc. | 24 | $7,034.92 |
| 1610629 | 9878 | S&F Supplies | 1 | $6,434.61 |
| 9930 | F097 | SADLIER-OXFORD | 9 | $5,444.71 |
| 2767 | 2804 | Hubert Company | 6 | $5,301.31 |
| 5750 | 6609 | Rapid Steel Supply Corp. | 4 | $5,252.52 |
| 2768 | 2805 | J.B. PRINCE COMPANY | 5 | $4,991.24 |
| 1621002 | 9328 | Lotus Connect LLC | 171 | $4,596.34 |
| 4142 | 4191 | Johnson's Restaurant Equipment, Inc. | 2 | $4,390.94 |
| 1711107 | 9651 | Schai Education Solutions LLC dba Bintiva | 92 | $3,228.19 |
| 1711330 | 9721 | AMPT Studio, LLC | 1 | $3,039.50 |
| 13489 | 0659 | Tyrone & Brothers Wholesale & Retail, Inc. | 7 | $3,036.16 |
| 8414 | T202 | Vista Higher Learning | 1 | $2,735.18 |
| 15391 | 5930 | Subscription Services of America, Inc. | 12 | $2,569.11 |
| 3147 | 3178 | General Chemical & Supply, Inc. | 1 | $2,495.62 |
| 7713 | T021 | Houghton Mifflin Harcourt | 6 | $2,384.08 |
| 4824 | 5205 | Bio Company Inc dba Bio Corporation | 14 | $2,369.60 |
| 856 | 0842 | Russo Music Center, Inc. | 4 | $2,074.00 |
| 3192 | 3220 | I. Janvey & Sons, Inc. | 8 | $1,957.04 |
| 9905 | F072 | MCGRAW HILL EDUCATION | 2 | $1,939.20 |
| 8801 | 7968 | AJJ Equipment and Supplies/DC Equipment & Supplies | 4 | $1,934.88 |
| 9951 | F118 | Wayside Publishing | 1 | $1,925.46 |
| 681 | 0657 | Different Roads to Learning, Inc. | 62 | $1,763.90 |
| 842 | 0828 | Wenger Corporation | 1 | $1,717.00 |
| 5577 | 6423 | Peters Camera Shop | 3 | $1,704.88 |
| 3120 | 3151 | Edmer Sanitary Supply Co., Inc. | 5 | $1,415.90 |
| 1711547 | 9776 | Crafts and More dba Elegant Display Corp | 34 | $1,251.21 |
| 1711632 | 9840 | Congeriem Inc. | 1 | $1,214.52 |
| 5904 | 6849 | Sheffield Pottery, Inc. | 2 | $1,073.88 |
| 2822 | 2858 | PATTERSON DENTAL COMPANY | 1 | $952.05 |
| 1602 | 1604 | Peripole, Inc. | 2 | $898.34 |
| 1711161 | 9670 | iCount Method | 3 | $889.51 |
| 1620912 | 9262 | Proactive Parents LLC dba Educate With Toys | 6 | $845.89 |
| 1432097 | 8746 | Great Minds PBC | 3 | $815.12 |
| 7781 | T093 | Perfection Learning | 4 | $736.15 |
| 1711145 | 9668 | ReadBright | 3 | $698.56 |
| 7828 | 5133 | Mill Wiping Rags, Inc. | 1 | $680.00 |
| 7737 | T045 | Zaner-Bloser, Inc. | 5 | $677.22 |
| 1711137 | 9667 | Roth Publishers Inc. | 4 | $635.84 |
| 5786 | 6648 | Emerald Island Supply Company Inc. | 4 | $624.87 |
| 1679 | 1684 | United Electric Supply Company Inc. | 4 | $568.83 |
| 7808 | T120 | D&S Marketing Systems | 2 | $499.00 |
| 1711896 | 9940 | BookPal | 1 | $480.42 |
| 1711160 | 9669 | Leren Curriculum | 2 | $397.37 |
| 1711891 | 9938 | Lighthouse Resources LLC | 1 | $353.10 |
| 1711795 | 9909 | DEW Online Store, LLC | 1 | $327.55 |
| 3005 | 3041 | Appco Paper & Plastics Corp. | 2 | $292.24 |
| 8408 | T195 | LOYOLA PRESS | 2 | $281.13 |
| 789 | 0771 | Follett Content Solutions, LLC | 2 | $251.99 |
| 1711680 | 9841 | Chef's Corner Restaurant Equipment & Supplies | 2 | $220.22 |
| 1711117 | 9654 | Learning Without Tears | 1 | $207.90 |
| 8939 | 8454 | J & B Musical Instruments Inc. | 6 | $193.18 |
| 1610787 | 9891 | PureTek Group Inc | 2 | $186.07 |
| 1582 | 1585 | Johnstone Supply | 1 | $174.81 |
| 1711894 | 9943 | PAF Reading Program | 1 | $172.81 |
| 10496 | T504 | MOSDOS PRESS | 1 | $150.04 |
| 9853 | F020 | CARSON DELLOSA PUBLISHER | 2 | $129.79 |
| 1711889 | 9941 | Lishkas Hasofer | 1 | $107.43 |
| 15518 | 6099 | SIMPLE SOLUTIONS. | 1 | $100.00 |
| 1711104 | 9649 | EPS Operations LLC | 1 | $93.08 |
| 13261 | 8172 | Amplify Education, Inc. | 1 | $82.08 |
| 14464 | 5315 | ANDYMARK, INC. | 1 | $59.08 |
| 12957 | 9562 | SparkFun Electronics | 1 | $44.10 |
| 1711890 | 9939 | The Otzar Haseforim of Monsey Inc | 1 | $30.00 |
| 1711504 | 9759 | Schoolhouse Publishing | 1 | $25.00 |
| 1711897 | 9942 | Haksav Vehaloshon | 1 | $15.00 |
| 13959 | 2069 | SUPERIOR TEXT | 1 | $6.45 |

> **Note**: 226 active vendors with POs Dec 2022–Nov 2025. To refresh this table, a scheduled task (`annual-vendor-table-refresh`) runs each December 15 and will regenerate the vendor query and update these rows. You can also trigger it manually from the Scheduled section in the sidebar. Last refreshed: 2026-03-27.

### Vendors with Multiple VendorId Entries

These vendors appear under more than one VendorId/Code — all are intentional separate contracts, not data errors.

**School Specialty (combined ~$68.0M)**
| VendorId | Code | Name | POs | Total Spend |
|----------|------|------|-----|-------------|
| 9 | 0009 | School Specialty, LLC | 205,723 | $62,112,979.69 |
| 541 | 0518 | School Specialty LLC dba Nasco Education | 33,384 | $5,900,306.01 |

**W.B. Mason (combined ~$9.0M)**
| VendorId | Code | Name | POs | Total Spend |
|----------|------|------|-----|-------------|
| 8341 | 8080 | W.B. Mason Co., Inc. | 8,989 | $5,570,653.70 |
| 3264 | 3287 | W.B. Mason Co., Inc. | 642 | $1,718,067.42 |
| 3877 | 3916 | W.B. Mason Co., Inc. | 5,187 | $1,433,202.91 |
| 3235 | 3259 | W.B. Mason Co., Inc. | 416 | $277,301.47 |

**School Health Corporation (combined ~$9.3M)**
| VendorId | Code | Name | POs | Total Spend |
|----------|------|------|-----|-------------|
| 552 | 0528 | School Health Corporation | 19,747 | $8,799,702.38 |
| 2284 | 2316 | School Health Corporation dba Palos Sports | 1,543 | $492,146.43 |

**VWR Funding (combined ~$3.1M)**
| VendorId | Code | Name | POs | Total Spend |
|----------|------|------|-----|-------------|
| 1002 | 0982 | VWR Funding, Inc dba Wards Science | 8,191 | $2,239,782.45 |
| 984 | 0967 | VWR Funding, Inc dba Sargent Welch | 4,979 | $862,046.96 |

**Lakeshore Learning Materials (combined ~$4.1M)**
| VendorId | Code | Name | POs | Total Spend |
|----------|------|------|-----|-------------|
| 897 | 0885 | Lakeshore Learning Materials, LLC | 19,493 | $3,874,709.23 |
| 1711600 | 9824 | Lakeshore Learning Materials, LLC | 2,086 | $266,797.91 |

**Bluum USA (combined ~$221K)**
| VendorId | Code | Name | POs | Total Spend |
|----------|------|------|-----|-------------|
| 286 | 0267 | Bluum USA Inc. | 722 | $177,855.58 |
| 374 | 0352 | Bluum USA, Inc. | 191 | $43,344.63 |

**Washington Music Sales Center (combined ~$178K)**
| VendorId | Code | Name | POs | Total Spend |
|----------|------|------|-----|-------------|
| 8293 | 9563 | Washington Music Sales Center, Inc. | 560 | $119,986.10 |
| 8535 | 5338 | Washington Music Sales Center, Inc. | 117 | $57,722.35 |

**Project Lead The Way (combined ~$38K)**
| VendorId | Code | Name | POs | Total Spend |
|----------|------|------|-----|-------------|
| 1615090 | 9233 | Project Lead The Way, Inc. | 8 | $21,349.00 |
| 9519 | 2511 | PROJECT LEAD THE WAY | 5 | $16,288.60 |

## Project Overview

EDS (Educational Data Services) is a multi-component system consisting of:
1. **Universal Requisition System** - Product catalog and shopping cart for school supplies (FastAPI + Alpine.js)
2. **SQL Server Monitoring Tools** - Performance analysis, index management, blocking investigation
3. **DBA Agent** - AI-powered database assistant with natural language to SQL capabilities

## Common Commands

### API Development
```bash
# Install dependencies
pip install -e ".[api,dev]"

# Run API server (development)
uvicorn api.main:app --reload --port 8000

# Run API via module
python -m api.main
```

### Testing
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=api --cov=scripts --cov-report=html

# Run specific test file
pytest tests/api/test_products.py -v

# Skip integration tests (no DB required)
pytest -m "not integration"

# Skip E2E browser tests
pytest -m "not e2e"

# E2E tests only (requires: pip install -e ".[e2e]" && playwright install)
pytest -m e2e
```

### Monitoring Scripts
```bash
capture-baseline                    # Capture performance metrics
analyze-performance --days 30       # Analyze issues
extract-indexes --min-saving 80     # Find missing indexes
investigate-blocking --date 2025-01-09
generate-report                     # Comprehensive report
```

### DBA Agent
```bash
python -m agent chat                # Interactive chat
eds-agent ask "What tables exist?"  # Single question
eds-agent sql "Top 10 vendors"      # Generate SQL
```

## Architecture

### API Layer (`/api/`)
- **main.py** - FastAPI app with middleware stack, router registration, generic frontend page serving
- **middleware.py** - Security headers (CSP), rate limiting (sliding window), `get_current_user` auth dependency
- **database.py** - pyodbc connection pooling with context managers (`get_db_cursor()`, `execute_query()`)
- **models.py** - Pydantic models: Product, Category, Vendor, Cart, APIStatus, Requisition*, RequisitionStatus enum
- **cache.py** - In-memory TTL cache with async lock and decorators
- **routes/** - Endpoint modules: products, categories, vendors, auth, requisitions

Routes are registered with `/api` prefix. Health endpoints: `GET /api/health`, `GET /api/status`

**Middleware stack** (applied in order): CORS → SecurityHeaders → RateLimit

**Frontend page serving**: A single generic catch-all handler (`/{full_path:path}`) serves all HTML pages. Clean URLs (`/checkout`) and `.html` URLs (`/checkout.html`) resolve to the same file. Route aliases are defined in `_ROUTE_ALIASES` dict. Directory traversal is prevented via `Path.resolve()` + `is_relative_to()`.

### Frontend (`/frontend/`)
Alpine.js application with modular JS architecture:
- **index.html** - Main app entry point (requisition/catalog interface)
- **login.html** - Authentication page
- **checkout.html** - Cart checkout flow
- **product-detail.html** - Product detail view
- **js/** - Flat directory with 18 modules: `app.js` (Alpine init), `api-client.js` (fetch wrapper), `auth.js`, `cart.js`, `browse.js`, `checkout.js`, `orders.js`, `approvals.js`, `saved-lists.js`, `dashboard.js`, `reports.js`, `ui.js`, `autocomplete.js`, `product-helpers.js`, `product-detail.js`, `config.js`, `auth-guard.js`, `login.js`
- **css/** - Component styles using CSS custom properties

EDS brand colors defined via CSS custom properties: `eds-primary: #1c1a83`, `eds-secondary: #4a4890`, `eds-accent: #b70c0d`

### Monitoring Scripts (`/scripts/`)
Standalone Python scripts for database administration:
- **db_utils.py** - Shared database utilities (different from api/database.py)
- **config.py** - YAML config with environment variable overrides
- Entry points defined in pyproject.toml `[project.scripts]`

### DBA Agent (`/agent/`)
See `/agent/CLAUDE.md` for detailed agent documentation.

Key modules:
- **core/agent.py** - EDSAgent orchestrator
- **llm/** - Provider abstraction (Claude, OpenAI, Ollama)
- **tools/** - SQL executor, query generator, script runner
- **rag/** - Vector store with ChromaDB for documentation search

## Database Connections

The SQL Server hosts 22 databases (see [`DATABASE_INVENTORY.md`](/docs/DATABASE_INVENTORY.md)). The two used by this codebase:
- **EDS** - Production catalog (products, vendors, categories, users, sessions) — ~1.4 TB, 439 tables
- **dpa_EDSAdmin** - DPA monitoring data (performance metrics, blocking events)

Environment variables:
```
DB_SERVER=eds-sqlserver.eastus2.cloudapp.azure.com
DB_DATABASE_CATALOG=EDS        # For API
DB_DATABASE=dpa_EDSAdmin       # For monitoring scripts
DB_USERNAME=EDSAdmin
DB_PASSWORD=<secret>
```

## Environment Variables (Middleware & Security)

```
EDS_ENV=development          # "production" restricts CORS to explicit origins
EDS_CORS_ORIGINS=            # Comma-separated allowed origins (required in production)
EDS_RATE_LIMIT=120           # Requests per minute per IP (default: 120)
EDS_BEHIND_PROXY=false       # Trust X-Forwarded-For header for real client IP
EDS_DEBUG=false              # Enable /api/debug/connection endpoint
```

## Authentication Flow

Login uses `sp_FA_AttemptLogin` stored procedure:
1. Frontend POSTs to `/api/auth/login` with district_code, user_number, password
2. Stored proc validates credentials and creates session in SessionTable
3. Session data stored in localStorage, checked on app load
4. Session validated every 5 minutes via `/api/auth/session/{id}`
5. Logout clears localStorage and redirects to login.html

Session timeouts (defined in `api/middleware.py`):
- **Max session age**: 8 hours (`SESSION_TIMEOUT_HOURS`)
- **Inactivity timeout**: 2 hours (`SESSION_INACTIVITY_HOURS`)

## Test Structure

```
tests/
├── conftest.py              # Global fixtures
├── api/
│   ├── conftest.py          # TestClient fixture with mocked DB
│   ├── test_health.py       # Health/status endpoints, CORS headers
│   ├── test_products.py     # Product search, filter, pagination
│   ├── test_categories.py   # Category listing
│   ├── test_vendors.py      # Vendor listing
│   ├── test_middleware.py   # Security headers, rate limiting, auth dependency (22 tests)
│   ├── test_auth.py         # Login, session validation, logout, touch (14 tests)
│   └── test_requisitions.py # Submit, list, update, cancel, approve, reject (32 tests)
├── e2e/                     # Playwright browser tests
│   ├── conftest.py
│   └── test_*.py
```

**Mocking patterns**:
- API tests mock `api.database` functions at the usage site (e.g. `@patch("api.routes.auth.get_db_cursor")`)
- Auth dependency mocked via `@patch("api.routes.requisitions.get_user_from_session")`
- Rate limit tests use isolated minimal FastAPI apps to avoid interference
- Use `@pytest.mark.integration` for tests requiring real DB

## Docker Deployment

```bash
docker-compose up -d          # Start all services
docker-compose logs -f api    # View API logs
```

Services: frontend (nginx:alpine, port 80), api (python:3.11-slim, port 8000), elasticsearch (ES 8.17.0, port 9200 — **note**: production runs ES 7.15.2, see [`ELASTICSEARCH_INFRASTRUCTURE.md`](/docs/ELASTICSEARCH_INFRASTRUCTURE.md))

## Kubernetes Infrastructure

Two AKS clusters in East US 2 (Kubernetes 1.32.10), both with mixed Linux/Windows node pools:
- **eds-aks-prod** (eds-prod-rg) - 13 nodes (8 Linux, 5 Windows), production workloads
- **eds-aks-uat** (eds-uat-rg) - 12 nodes (7 Linux, 5 Windows), UAT/staging workloads

See `/docs/kubernetes-clusters.md` for full cluster documentation (node pools, VM sizes, deployments, services, resource utilization).

```bash
# Context switching
kubectx eds-aks-prod           # Switch to production
kubectx eds-aks-uat            # Switch to UAT
kubens eds-web-app             # Switch namespace
```

## Key Files

- `/pyproject.toml` - Dependencies, entry points, pytest config
- `/config.yaml` - Thresholds, analysis settings, output directories
- `/.env` - Database credentials and middleware config (copy from .env.example)
- `/docker-compose.yml` - Multi-service orchestration
- `/api/middleware.py` - Auth dependency, rate limiter, CSP/security headers

## Documentation

All documentation lives in `/docs/`. See [`/docs/README.md`](/docs/README.md) for the full index.

### Core System Docs
- [`ARCHITECTURE.md`](/docs/ARCHITECTURE.md) - Universal Requisition app architecture (client, API, database layers). See also [`wiki/architecture/system-overview.md`](/docs/wiki/architecture/system-overview.md) for full infrastructure view
- [`DEVELOPMENT.md`](/docs/DEVELOPMENT.md) - Local development environment setup (Python 3.12+, prerequisites)
- [`DEPLOYMENT.md`](/docs/DEPLOYMENT.md) - Docker & Kubernetes deployment instructions
- [`TESTING.md`](/docs/TESTING.md) - Testing guide (unit, API, E2E, integration with pytest)
- [`TESTING_REFERENCE.md`](/docs/TESTING_REFERENCE.md) - Detailed testing reference: fixtures, mocking patterns, every test file documented
- [`CI_CD.md`](/docs/CI_CD.md) - CI/CD pipeline documentation (GitHub Actions test.yml, deploy.yml, troubleshooting)
- [`CONFIGURATION.md`](/docs/CONFIGURATION.md) - Configuration reference (.env, config.yaml, priority order)
- [`FRONTEND_TROUBLESHOOTING.md`](/docs/FRONTEND_TROUBLESHOOTING.md) - Frontend/application troubleshooting (CORS, localStorage, API errors). For DB troubleshooting see [`wiki/troubleshooting/`](/docs/wiki/troubleshooting/)

### Application Docs
- [`FRONTEND_ARCHITECTURE.md`](/docs/FRONTEND_ARCHITECTURE.md) - Complete frontend architecture guide (Alpine.js, modules, state management, auth, CSS)
- [`API_ROUTES.md`](/docs/API_ROUTES.md) - Complete API routes reference (~65 endpoints across 14 route modules)
- [`UNIVERSAL_REQUISITION.md`](/docs/UNIVERSAL_REQUISITION.md) - Requisition interface user & developer guide
- [`API_REFERENCE.md`](/docs/API_REFERENCE.md) - Python monitoring tools API reference (db_utils, config, logging)
- [`MONITORING_SCRIPTS_REFERENCE.md`](/docs/MONITORING_SCRIPTS_REFERENCE.md) - Complete reference for all 58 monitoring scripts, CLI entry points, configuration, output files, and workflows
- [`AGENT_CLI.md`](/docs/AGENT_CLI.md) - DBA Agent CLI usage and commands
- [`AGENT_TECHNICAL_REFERENCE.md`](/docs/AGENT_TECHNICAL_REFERENCE.md) - DBA Agent technical deep dive (RAG pipeline, memory, tools, security, export, GUI)
- [`demo-script.md`](/docs/demo-script.md) - Demo walkthrough script
- [`frontend-comparison-walkthrough.md`](/docs/frontend-comparison-walkthrough.md) - Frontend version comparison guide

### Database Schema & Structure
- [`SCHEMA.md`](/docs/SCHEMA.md) - Schema guide with ERD diagrams and organizational hierarchy. Pairs with `EDS_DATA_DICTIONARY.md` (reference) below
- [`EDS_SUMMARY.md`](/docs/EDS_SUMMARY.md) - Executive summary of database objects
- [`DATABASE_INVENTORY.md`](/docs/DATABASE_INVENTORY.md) - Full inventory of all 22 databases on the SQL Server instance
- [`EDS_DATA_DICTIONARY.md`](/docs/EDS_DATA_DICTIONARY.md) - Complete generated table/column reference (439 tables, 4,638 columns)
- [`EDS_ERD.md`](/docs/EDS_ERD.md) - Entity relationship diagrams (Mermaid)
- [`EDS_INDEXES.md`](/docs/EDS_INDEXES.md) - Index documentation (1,115 indexes)
- [`EDS_STATUS_CODES.md`](/docs/EDS_STATUS_CODES.md) - Status codes and lookup tables (StatusTable, 53 rows)

### Stored Procedures & Views
- [`EDS_STORED_PROCEDURES.md`](/docs/EDS_STORED_PROCEDURES.md) - Technical reference: all 396 stored procedures with parameters and source
- [`EDS_PROCEDURES_GUIDE.md`](/docs/EDS_PROCEDURES_GUIDE.md) - Business context guide: key procedures with usage examples and workflow context
- [`EDS_VIEWS.md`](/docs/EDS_VIEWS.md) - Technical reference: all 475 views with SQL definitions and dependencies
- [`EDS_VIEWS_GUIDE.md`](/docs/EDS_VIEWS_GUIDE.md) - Business context guide: views with naming conventions and domain organization

### Dependencies & Analysis
- [`EDS_PROCEDURE_DEPENDENCIES.md`](/docs/EDS_PROCEDURE_DEPENDENCIES.md) - SP call chains, table access patterns, workflow orchestration
- [`EDS_ROOT_PROCEDURES.md`](/docs/EDS_ROOT_PROCEDURES.md) - 77 entry point procedures by category
- [`EDS_CIRCULAR_DEPS.md`](/docs/EDS_CIRCULAR_DEPS.md) - Circular dependency analysis (0 circular, 34 recursive)
- [`EDS_RECURSIVE_PROCEDURES.md`](/docs/EDS_RECURSIVE_PROCEDURES.md) - 34 self-calling procedures (tree traversal, org hierarchy)
- [`EDS_INFINITE_LOOP_ANALYSIS.md`](/docs/EDS_INFINITE_LOOP_ANALYSIS.md) - Infinite loop pattern analysis (1 HIGH, 78 LOW severity)
- [`EDS_TRIGGERS.md`](/docs/EDS_TRIGGERS.md) - 59 triggers documentation (includes view-based INSTEAD OF triggers)

### Data Management & Governance
- [`EDS_DATA_OWNERSHIP.md`](/docs/EDS_DATA_OWNERSHIP.md) - Data stewardship roles and RACI matrix
- [`EDS_ETL_INTEGRATIONS.md`](/docs/EDS_ETL_INTEGRATIONS.md) - External system integration points (SSO, financial, vendor systems)
- [`EDS_ACCESS_CONTROL.md`](/docs/EDS_ACCESS_CONTROL.md) - Multi-layered access control (auth, RBAC, row-level, column-level)
- [`EDS_ARCHIVE_STRATEGY.md`](/docs/EDS_ARCHIVE_STRATEGY.md) - Data retention/archival strategy (policy, compliance, design). Pairs with analysis below
- [`EDS_ARCHIVE_ANALYSIS.md`](/docs/EDS_ARCHIVE_ANALYSIS.md) - Archive vs active schema comparison (49 archived tables, current state)

### Business & Operations
- [`EDS_BUSINESS_DOMAINS.md`](/docs/EDS_BUSINESS_DOMAINS.md) - Overview of tables by functional area. See [`domains/`](/docs/domains/) for deep dives per domain
- [`EDS_BUSINESS_WORKFLOWS.md`](/docs/EDS_BUSINESS_WORKFLOWS.md) - Key business processes (bidding, orders, vendors, catalogs, budgets)
- [`AZURE_INFRASTRUCTURE.md`](/docs/AZURE_INFRASTRUCTURE.md) - Full Azure inventory: 31 resource groups, 14 VMs, networking, storage, Key Vaults, DR/ASR
- [`ELASTICSEARCH_INFRASTRUCTURE.md`](/docs/ELASTICSEARCH_INFRASTRUCTURE.md) - ES VM, 44 indices, version mismatch (7.15.2 prod vs 8.17.0 dev), security concerns
- [`kubernetes-clusters.md`](/docs/kubernetes-clusters.md) - AKS cluster documentation (prod/UAT, nodes, workloads, networking)
- [`guides/DAILY_MONITORING_GUIDE.md`](/docs/guides/DAILY_MONITORING_GUIDE.md) - SQL-based daily monitoring queries and dashboard. See also [`wiki/operations/daily-monitoring.md`](/docs/wiki/operations/daily-monitoring.md) for checklist workflow

### Domain-Specific Deep Dives
- [`tables/TIER1_TABLES.md`](/docs/tables/TIER1_TABLES.md) - 25 critical tables (CrossRefs 150.6M, Items 30.1M, Detail 30.8M rows)
- [`domains/BIDDING_DOMAIN.md`](/docs/domains/BIDDING_DOMAIN.md) - Bidding & procurement (51 tables, ~506M rows, lifecycle diagrams, ERD)
- [`domains/ORDERS_DOMAIN.md`](/docs/domains/ORDERS_DOMAIN.md) - Orders & purchasing (47 tables, ~395M rows, lifecycle diagrams)
- [`domains/VENDORS_USERS_DOMAIN.md`](/docs/domains/VENDORS_USERS_DOMAIN.md) - Vendors & users (51 tables, ~24M rows, hierarchy diagrams)
- [`domains/INVENTORY_FINANCE_DOMAIN.md`](/docs/domains/INVENTORY_FINANCE_DOMAIN.md) - Inventory & finance (~40 tables, ~260M rows)

### Wiki (Navigable Knowledge Base)
- [`wiki/index.md`](/docs/wiki/index.md) - Wiki home with full navigation
- **Getting Started**
  - [`wiki/getting-started/index.md`](/docs/wiki/getting-started/index.md) - Quick orientation to the EDS system
  - [`wiki/getting-started/quick-reference.md`](/docs/wiki/getting-started/quick-reference.md) - One-page system overview and key metrics
  - [`wiki/getting-started/glossary.md`](/docs/wiki/getting-started/glossary.md) - EDS procurement terminology definitions
- **Business Context**
  - [`wiki/business/what-is-eds.md`](/docs/wiki/business/what-is-eds.md) - EDS as a K-12 e-procurement platform
  - [`wiki/business/entities/`](/docs/wiki/business/entities/) - Districts, schools, users, vendors, requisitions, POs, bids, catalogs
  - [`wiki/business/workflows/`](/docs/wiki/business/workflows/) - Requisition-to-PO, vendor bidding, budget approval
- **Schema by Domain**
  - [`wiki/schema/by-domain/`](/docs/wiki/schema/by-domain/) - Bidding (76 tables), orders (45), vendors (32), inventory (28), users (24), finance (18), documents (15)
- **Architecture**
  - [`wiki/architecture/system-overview.md`](/docs/wiki/architecture/system-overview.md) - Full infrastructure view (K8s, IIS, Azure VMs)
  - [`wiki/architecture/application-stack.md`](/docs/wiki/architecture/application-stack.md) - EDSIQ, web services, Kubernetes deployment
  - [`wiki/architecture/database-architecture.md`](/docs/wiki/architecture/database-architecture.md) - SQL Server 2017 on Azure, performance monitoring
  - [`wiki/architecture/integrations.md`](/docs/wiki/architecture/integrations.md) - External systems (auth, finance, vendors, notifications)
- **Performance**
  - [`wiki/performance/known-issues/`](/docs/wiki/performance/known-issues/) - usp_GetIndexData (critical), vendor sync, trigger blocking, CrossRef blocking, SSO deadlocks
  - [`wiki/performance/incidents/`](/docs/wiki/performance/incidents/) - Incident log; includes 2026-01-06 blocking post-mortem
- **Troubleshooting** (database-focused)
  - [`wiki/troubleshooting/slow-queries.md`](/docs/wiki/troubleshooting/slow-queries.md) - Slow query diagnosis and resolution
  - [`wiki/troubleshooting/blocking.md`](/docs/wiki/troubleshooting/blocking.md) - Session locking and blocking procedures
  - [`wiki/troubleshooting/deadlocks.md`](/docs/wiki/troubleshooting/deadlocks.md) - Circular lock deadlock resolution
  - [`wiki/troubleshooting/runbooks/`](/docs/wiki/troubleshooting/runbooks/) - Emergency runbooks: blocking response, high CPU
- **Operations**
  - [`wiki/operations/daily-monitoring.md`](/docs/wiki/operations/daily-monitoring.md) - Morning health check and DBA on-call checklist
- **User Activity**
  - [`wiki/user-activity/application-users.md`](/docs/wiki/user-activity/application-users.md) - System accounts and database connectivity
  - [`wiki/user-activity/usage-patterns.md`](/docs/wiki/user-activity/usage-patterns.md) - Peak activity times and daily/weekly patterns

### Documentation Templates
- [`templates/`](/docs/templates/) - Templates for new documentation: table, procedure, view, domain

### DBA Agent
- [`/agent/CLAUDE.md`](/agent/CLAUDE.md) - Agent architecture, CLI commands, development guidelines
- [`/agent/agent/data/training/`](/agent/agent/data/training/) - 19 RAG training docs (business domains, workflows, procedures, queries, performance)
- [`/agent/data/schemas/dpa_EDSAdmin_schema.md`](/agent/data/schemas/dpa_EDSAdmin_schema.md) - DPA monitoring database schema

### PDF Exports
- [`/docs/pdf/`](/docs/pdf/) - 20 compiled PDF versions of documentation
