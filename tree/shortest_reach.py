state = 0
inputarray = [
"2",
"4 2",
"1 2",
"1 3",
"1",
"3 1",
"2 3",
"2",
]

inputarray2 = [ \

"1",
"70 1988",
"30 32",
"50 9",
"7 58",
"50 66",
"38 13",
"31 67",
"2 30",
"14 46",
"54 34",
"10 7",
"25 66",
"20 18",
"1 21",
"49 63",
"39 20",
"55 5",
"3 66",
"58 34",
"19 12",
"43 62",
"16 1",
"10 11",
"16 70",
"11 35",
"22 13",
"16 2",
"59 41",
"29 45",
"53 47",
"43 59",
"46 32",
"64 65",
"70 11",
"4 11",
"69 10",
"21 41",
"17 56",
"49 63",
"27 50",
"30 23",
"49 19",
"45 46",
"1 64",
"67 58",
"37 38",
"33 68",
"55 67",
"35 5",
"70 44",
"14 26",
"50 17",
"4 10",
"43 7",
"15 44",
"2 50",
"64 28",
"8 19",
"7 31",
"30 3",
"36 59",
"36 57",
"27 60",
"54 28",
"26 69",
"57 54",
"49 20",
"66 9",
"44 41",
"22 5",
"46 10",
"54 19",
"13 3",
"13 2",
"49 1",
"34 29",
"68 50",
"3 27",
"3 2",
"57 60",
"3 59",
"42 55",
"66 55",
"24 7",
"2 48",
"14 62",
"48 38",
"22 10",
"12 19",
"1 46",
"49 48",
"31 56",
"5 15",
"45 67",
"35 43",
"66 47",
"63 20",
"38 57",
"70 32",
"20 25",
"46 16",
"32 15",
"39 24",
"5 10",
"1 64",
"59 52",
"45 33",
"43 21",
"61 50",
"31 10",
"69 63",
"49 26",
"3 21",
"43 44",
"8 68",
"68 51",
"54 30",
"46 70",
"7 9",
"42 51",
"63 39",
"52 59",
"2 23",
"37 12",
"46 38",
"55 15",
"48 39",
"1 8",
"40 20",
"24 69",
"10 40",
"1 3",
"24 45",
"23 43",
"31 7",
"55 28",
"4 46",
"18 12",
"63 6",
"65 10",
"32 1",
"16 36",
"1 28",
"54 62",
"70 46",
"26 20",
"57 29",
"7 69",
"37 69",
"29 24",
"66 23",
"15 17",
"13 35",
"19 8",
"35 14",
"53 13",
"37 69",
"33 51",
"49 62",
"50 36",
"70 45",
"51 67",
"22 42",
"17 69",
"64 11",
"61 23",
"55 59",
"28 12",
"46 13",
"53 26",
"39 11",
"35 48",
"35 23",
"63 64",
"21 28",
"11 51",
"18 10",
"55 68",
"34 49",
"28 69",
"55 9",
"63 52",
"41 19",
"23 5",
"10 42",
"70 1",
"57 1",
"1 17",
"66 42",
"4 28",
"46 5",
"14 54",
"34 70",
"32 27",
"27 28",
"53 28",
"58 7",
"24 70",
"16 13",
"6 40",
"19 24",
"55 24",
"3 60",
"34 56",
"12 10",
"7 64",
"54 55",
"69 15",
"36 58",
"39 59",
"31 5",
"43 52",
"29 44",
"44 66",
"13 65",
"46 70",
"46 9",
"38 64",
"2 26",
"47 28",
"28 8",
"33 27",
"6 14",
"70 55",
"2 63",
"19 64",
"19 68",
"64 63",
"60 46",
"1 43",
"40 50",
"15 47",
"31 11",
"23 53",
"55 18",
"41 1",
"34 58",
"2 5",
"51 11",
"19 46",
"36 50",
"59 67",
"38 14",
"32 6",
"69 16",
"28 42",
"60 33",
"7 35",
"40 44",
"70 9",
"3 65",
"60 8",
"1 63",
"14 51",
"57 61",
"43 25",
"51 13",
"56 18",
"34 28",
"43 60",
"6 4",
"25 41",
"21 1",
"50 38",
"57 23",
"1 45",
"61 49",
"27 7",
"32 68",
"52 1",
"70 34",
"54 34",
"48 5",
"51 39",
"16 20",
"65 5",
"46 50",
"4 44",
"39 62",
"1 12",
"50 17",
"21 10",
"54 38",
"44 28",
"2 47",
"23 19",
"2 10",
"67 18",
"60 20",
"4 65",
"12 23",
"39 58",
"9 40",
"18 8",
"63 43",
"22 23",
"36 65",
"53 63",
"66 26",
"59 63",
"22 5",
"11 5",
"47 42",
"14 69",
"28 1",
"3 57",
"15 61",
"62 45",
"59 61",
"50 58",
"45 22",
"33 57",
"49 40",
"27 28",
"26 53",
"62 44",
"46 36",
"3 19",
"24 32",
"44 34",
"57 63",
"22 55",
"21 1",
"12 16",
"22 34",
"42 43",
"1 9",
"8 70",
"8 46",
"60 31",
"46 22",
"26 1",
"50 51",
"9 64",
"51 17",
"10 43",
"61 50",
"37 64",
"56 32",
"44 54",
"62 24",
"62 67",
"33 54",
"67 53",
"2 68",
"36 21",
"66 22",
"70 58",
"70 34",
"41 43",
"57 7",
"37 54",
"52 39",
"58 26",
"45 5",
"17 40",
"38 1",
"38 17",
"34 3",
"50 61",
"38 28",
"64 14",
"7 62",
"22 13",
"39 22",
"25 70",
"67 15",
"8 36",
"59 9",
"59 63",
"20 28",
"29 26",
"44 65",
"9 47",
"5 24",
"64 48",
"30 49",
"53 11",
"23 63",
"43 30",
"42 38",
"36 23",
"16 33",
"2 68",
"24 4",
"31 21",
"54 52",
"68 22",
"59 26",
"53 25",
"16 69",
"34 66",
"13 7",
"33 9",
"35 10",
"62 16",
"13 23",
"47 66",
"44 32",
"64 15",
"47 44",
"5 68",
"48 13",
"22 47",
"8 31",
"32 68",
"69 10",
"10 18",
"16 13",
"42 35",
"1 15",
"19 37",
"48 49",
"59 38",
"10 51",
"19 1",
"48 66",
"47 29",
"15 57",
"51 66",
"18 63",
"11 17",
"22 41",
"51 12",
"47 49",
"31 1",
"48 29",
"38 52",
"59 30",
"65 17",
"65 49",
"13 70",
"19 7",
"49 31",
"48 21",
"57 18",
"58 44",
"46 39",
"3 6",
"68 3",
"37 60",
"68 48",
"5 63",
"61 31",
"1 69",
"53 24",
"3 19",
"33 45",
"1 64",
"14 15",
"24 15",
"7 62",
"15 63",
"3 13",
"23 18",
"69 62",
"1 4",
"48 59",
"50 56",
"8 36",
"43 64",
"18 33",
"30 46",
"42 22",
"65 61",
"34 15",
"41 6",
"41 33",
"44 8",
"1 10",
"30 27",
"55 46",
"20 64",
"63 4",
"48 54",
"21 20",
"69 32",
"39 38",
"55 36",
"14 54",
"64 35",
"17 26",
"37 64",
"19 45",
"38 29",
"35 32",
"8 45",
"48 5",
"35 68",
"1 32",
"47 37",
"12 18",
"46 33",
"38 1",
"66 26",
"41 16",
"54 60",
"3 45",
"12 2",
"68 69",
"21 55",
"3 46",
"48 4",
"3 47",
"20 3",
"37 14",
"11 29",
"11 23",
"12 68",
"15 30",
"21 40",
"61 19",
"66 21",
"67 41",
"35 67",
"68 53",
"23 68",
"1 21",
"8 24",
"54 59",
"39 22",
"58 60",
"37 47",
"26 51",
"27 37",
"15 44",
"18 32",
"33 31",
"65 29",
"61 58",
"36 37",
"1 67",
"41 26",
"67 51",
"61 9",
"67 51",
"13 25",
"58 28",
"35 34",
"36 62",
"58 41",
"57 65",
"59 67",
"29 65",
"60 4",
"14 40",
"62 10",
"7 40",
"7 37",
"33 3",
"61 67",
"31 15",
"17 66",
"12 68",
"70 42",
"8 39",
"18 33",
"26 49",
"62 59",
"33 3",
"16 39",
"16 69",
"1 4",
"22 20",
"66 43",
"65 15",
"17 54",
"17 19",
"38 27",
"11 5",
"68 55",
"6 65",
"44 21",
"15 1",
"35 57",
"33 44",
"3 24",
"66 62",
"17 30",
"36 48",
"19 35",
"14 4",
"34 60",
"34 24",
"9 62",
"11 39",
"13 30",
"60 39",
"27 66",
"10 60",
"60 28",
"43 37",
"68 28",
"61 11",
"6 8",
"10 64",
"6 16",
"28 65",
"18 67",
"63 6",
"27 31",
"24 47",
"44 69",
"57 66",
"39 12",
"9 52",
"47 48",
"65 8",
"19 55",
"19 15",
"69 58",
"68 35",
"47 18",
"65 35",
"20 54",
"56 29",
"36 66",
"42 44",
"14 28",
"52 24",
"48 38",
"12 34",
"51 54",
"34 6",
"46 10",
"69 45",
"1 7",
"5 63",
"9 6",
"57 37",
"28 56",
"57 48",
"46 68",
"31 34",
"8 46",
"55 3",
"66 15",
"9 17",
"10 43",
"43 30",
"6 3",
"69 19",
"41 16",
"46 29",
"5 59",
"58 41",
"17 22",
"21 35",
"40 62",
"68 11",
"1 40",
"59 55",
"34 39",
"36 20",
"12 62",
"57 19",
"62 61",
"9 31",
"33 30",
"6 16",
"12 55",
"20 7",
"46 28",
"28 48",
"28 14",
"29 5",
"4 48",
"11 30",
"52 24",
"4 33",
"44 1",
"19 22",
"44 51",
"23 45",
"42 44",
"31 69",
"34 45",
"65 55",
"25 64",
"42 44",
"42 57",
"16 1",
"32 22",
"11 36",
"1 38",
"45 54",
"69 35",
"56 18",
"1 45",
"6 61",
"27 40",
"4 59",
"59 13",
"12 2",
"30 48",
"58 44",
"22 50",
"12 61",
"66 43",
"15 32",
"47 48",
"24 36",
"20 28",
"37 38",
"9 32",
"7 4",
"64 60",
"53 51",
"21 57",
"2 22",
"20 13",
"16 57",
"44 31",
"40 68",
"15 47",
"5 18",
"66 5",
"65 27",
"68 38",
"5 37",
"57 48",
"50 62",
"14 68",
"53 39",
"66 68",
"21 29",
"28 56",
"56 14",
"48 44",
"37 6",
"52 8",
"17 11",
"22 2",
"9 20",
"42 55",
"29 9",
"14 62",
"40 11",
"63 70",
"58 10",
"52 45",
"17 32",
"57 50",
"50 27",
"45 46",
"51 9",
"48 57",
"31 51",
"21 43",
"70 48",
"15 50",
"7 20",
"22 13",
"42 65",
"45 1",
"67 43",
"60 68",
"11 60",
"42 62",
"16 1",
"30 41",
"11 22",
"2 8",
"20 57",
"1 47",
"38 1",
"63 48",
"33 54",
"60 43",
"19 38",
"15 61",
"55 33",
"3 33",
"4 32",
"30 6",
"20 14",
"58 31",
"12 22",
"9 10",
"22 48",
"65 53",
"26 14",
"62 61",
"14 70",
"41 4",
"55 66",
"64 17",
"18 52",
"6 61",
"25 17",
"60 61",
"66 31",
"64 59",
"2 65",
"3 69",
"24 52",
"55 29",
"40 41",
"28 21",
"3 25",
"26 16",
"23 1",
"29 37",
"6 33",
"15 32",
"62 49",
"43 54",
"27 40",
"22 38",
"68 26",
"19 42",
"12 61",
"6 57",
"27 44",
"51 58",
"3 70",
"70 49",
"60 5",
"67 68",
"50 9",
"41 33",
"16 22",
"2 69",
"36 27",
"20 56",
"31 19",
"35 45",
"31 7",
"52 18",
"45 6",
"38 3",
"21 58",
"60 33",
"31 4",
"26 54",
"45 34",
"46 58",
"69 26",
"1 33",
"67 31",
"10 65",
"46 22",
"70 38",
"54 64",
"32 35",
"17 19",
"8 27",
"52 42",
"57 70",
"70 46",
"14 54",
"42 39",
"58 30",
"5 64",
"36 12",
"32 19",
"10 58",
"35 55",
"70 39",
"14 7",
"5 18",
"4 35",
"49 16",
"8 57",
"30 62",
"62 26",
"55 47",
"42 65",
"18 67",
"47 53",
"35 47",
"12 64",
"54 32",
"9 4",
"16 4",
"18 42",
"34 13",
"41 54",
"27 30",
"56 7",
"2 16",
"24 60",
"11 70",
"50 10",
"36 54",
"65 54",
"1 34",
"48 53",
"13 21",
"19 65",
"34 51",
"35 1",
"41 32",
"34 1",
"52 2",
"24 30",
"57 15",
"51 57",
"26 3",
"49 24",
"15 2",
"1 12",
"67 68",
"27 14",
"36 65",
"19 28",
"2 33",
"50 51",
"19 28",
"27 46",
"24 51",
"33 68",
"22 30",
"60 41",
"45 7",
"63 55",
"27 64",
"64 44",
"30 6",
"4 22",
"43 40",
"13 70",
"52 44",
"18 63",
"54 60",
"59 30",
"53 64",
"12 31",
"25 63",
"1 56",
"21 68",
"39 15",
"19 16",
"43 62",
"31 59",
"28 21",
"4 27",
"46 27",
"7 57",
"9 63",
"36 45",
"52 31",
"6 2",
"36 31",
"30 57",
"62 12",
"36 39",
"11 34",
"31 58",
"59 20",
"40 70",
"20 49",
"68 8",
"11 37",
"1 2",
"69 18",
"51 30",
"65 3",
"32 12",
"54 36",
"61 55",
"38 3",
"43 26",
"32 68",
"21 66",
"54 22",
"40 69",
"54 29",
"69 40",
"59 61",
"40 25",
"30 61",
"60 32",
"17 50",
"53 23",
"67 1",
"50 25",
"43 54",
"26 55",
"57 13",
"24 5",
"1 48",
"7 12",
"60 31",
"15 16",
"37 62",
"58 44",
"62 5",
"13 9",
"63 48",
"49 4",
"49 50",
"5 18",
"1 19",
"10 7",
"12 11",
"47 25",
"39 40",
"45 65",
"27 34",
"45 30",
"12 47",
"69 21",
"49 27",
"52 21",
"5 70",
"8 16",
"59 58",
"11 31",
"18 44",
"17 14",
"29 67",
"55 49",
"69 27",
"37 61",
"52 16",
"26 18",
"69 31",
"15 69",
"49 43",
"29 69",
"61 26",
"30 1",
"30 59",
"33 2",
"27 5",
"1 10",
"53 8",
"66 53",
"1 70",
"49 12",
"51 53",
"32 52",
"5 59",
"10 57",
"4 5",
"31 59",
"20 53",
"1 48",
"30 27",
"25 5",
"60 47",
"18 22",
"18 45",
"56 13",
"58 21",
"25 5",
"4 37",
"1 44",
"33 48",
"67 64",
"35 14",
"31 3",
"21 22",
"24 18",
"60 46",
"67 62",
"15 19",
"49 27",
"52 33",
"44 25",
"34 59",
"9 18",
"70 13",
"2 36",
"41 16",
"60 6",
"38 62",
"51 16",
"25 47",
"25 31",
"33 69",
"48 22",
"15 16",
"25 40",
"48 14",
"33 25",
"24 16",
"38 57",
"41 67",
"17 58",
"54 1",
"52 9",
"50 4",
"26 23",
"33 31",
"11 4",
"8 5",
"21 25",
"53 23",
"4 61",
"1 41",
"48 22",
"21 34",
"48 64",
"68 1",
"66 45",
"61 55",
"10 30",
"68 21",
"49 20",
"41 4",
"59 24",
"70 64",
"61 16",
"10 29",
"26 22",
"69 52",
"16 1",
"31 62",
"21 19",
"56 13",
"66 3",
"36 49",
"8 17",
"1 21",
"28 56",
"42 63",
"46 51",
"8 65",
"19 70",
"46 67",
"68 35",
"59 2",
"66 6",
"50 8",
"8 41",
"1 16",
"65 58",
"9 22",
"8 63",
"51 12",
"35 32",
"47 45",
"49 18",
"3 45",
"69 19",
"6 37",
"39 69",
"61 9",
"60 2",
"38 11",
"63 29",
"10 53",
"67 52",
"50 19",
"8 70",
"5 13",
"60 32",
"13 38",
"44 56",
"11 3",
"35 38",
"70 64",
"47 13",
"11 13",
"67 62",
"10 5",
"62 68",
"41 1",
"50 16",
"28 58",
"52 44",
"24 11",
"6 4",
"47 61",
"15 68",
"63 26",
"42 14",
"48 33",
"35 13",
"34 30",
"64 65",
"60 51",
"59 17",
"69 19",
"67 22",
"5 15",
"2 11",
"29 69",
"1 22",
"55 35",
"26 25",
"36 27",
"62 35",
"3 50",
"7 64",
"48 34",
"55 59",
"38 46",
"2 28",
"20 34",
"69 30",
"45 11",
"50 65",
"21 66",
"60 59",
"59 23",
"7 19",
"19 44",
"2 29",
"26 34",
"59 16",
"61 34",
"23 37",
"7 24",
"60 1",
"31 20",
"1 13",
"65 51",
"36 13",
"65 58",
"2 23",
"23 59",
"66 58",
"18 42",
"47 48",
"58 5",
"16 43",
"10 42",
"21 19",
"55 9",
"12 44",
"9 45",
"48 27",
"50 24",
"49 69",
"7 27",
"68 7",
"27 37",
"62 70",
"15 44",
"44 67",
"2 62",
"61 38",
"21 28",
"5 44",
"47 63",
"38 39",
"23 34",
"52 45",
"8 32",
"11 1",
"36 1",
"42 39",
"32 37",
"27 29",
"3 47",
"48 33",
"69 56",
"47 15",
"61 54",
"62 34",
"68 55",
"32 7",
"11 40",
"57 10",
"25 8",
"17 67",
"55 15",
"57 40",
"1 70",
"6 64",
"55 53",
"59 60",
"29 53",
"64 44",
"41 4",
"60 69",
"35 14",
"38 9",
"67 32",
"63 7",
"14 45",
"33 13",
"54 56",
"12 2",
"19 37",
"37 42",
"19 28",
"23 56",
"47 21",
"15 44",
"2 45",
"43 51",
"25 60",
"65 36",
"11 26",
"38 28",
"15 39",
"23 69",
"32 1",
"51 41",
"13 17",
"67 62",
"48 26",
"55 18",
"60 7",
"34 63",
"44 30",
"65 24",
"8 65",
"54 55",
"50 55",
"26 59",
"42 56",
"52 27",
"20 19",
"41 48",
"44 8",
"41 44",
"58 51",
"3 4",
"50 25",
"35 63",
"47 42",
"34 10",
"20 47",
"30 26",
"67 25",
"17 9",
"7 36",
"24 25",
"70 36",
"28 50",
"64 62",
"49 53",
"14 59",
"21 33",
"17 24",
"38 56",
"21 37",
"15 31",
"61 64",
"49 32",
"10 5",
"56 35",
"20 14",
"43 32",
"30 54",
"37 40",
"66 10",
"31 52",
"65 27",
"44 59",
"67 44",
"6 57",
"24 6",
"69 4",
"7 36",
"28 13",
"38 22",
"24 10",
"62 53",
"62 14",
"53 38",
"39 23",
"60 21",
"11 23",
"64 32",
"14 30",
"17 31",
"69 54",
"31 26",
"33 1",
"68 67",
"39 29",
"58 61",
"42 10",
"22 27",
"16 70",
"7 35",
"4 51",
"25 53",
"6 33",
"27 20",
"19 1",
"41 63",
"21 32",
"43 49",
"60 54",
"41 50",
"65 48",
"47 41",
"63 22",
"9 35",
"61 55",
"4 56",
"18 10",
"13 17",
"19 22",
"55 37",
"34 23",
"42 47",
"3 16",
"54 56",
"26 53",
"47 52",
"9 35",
"41 56",
"1 27",
"58 54",
"39 40",
"30 46",
"52 1",
"33 63",
"18 55",
"42 20",
"11 1",
"49 40",
"17 46",
"52 57",
"30 32",
"6 34",
"2 15",
"3 4",
"38 47",
"35 26",
"8 16",
"47 66",
"17 36",
"69 4",
"50 46",
"43 35",
"18 25",
"61 1",
"68 52",
"62 65",
"63 49",
"25 18",
"62 63",
"21 31",
"56 33",
"54 45",
"40 6",
"66 34",
"59 38",
"8 40",
"45 18",
"53 10",
"46 38",
"23 33",
"27 32",
"36 67",
"44 26",
"44 9",
"47 38",
"7 69",
"30 62",
"34 28",
"24 48",
"3 49",
"24 1",
"11 30",
"45 7",
"43 51",
"59 42",
"24 58",
"47 40",
"51 49",
"51 17",
"31 4",
"36 54",
"14 26",
"66 61",
"32 36",
"65 7",
"3 14",
"42 25",
"18 66",
"62 16",
"1 49",
"5 21",
"18 22",
"10 52",
"3 38",
"70 64",
"38 62",
"12 5",
"55 32",
"8 1",
"24 36",
"58 33",
"67 62",
"14 9",
"40 53",
"2 35",
"62 36",
"1 12",
"20 15",
"4 21",
"37 1",
"48 31",
"48 11",
"17 66",
"22 25",
"34 62",
"21 56",
"48 32",
"48 1",
"5 29",
"52 62",
"63 64",
"28 1",
"12 48",
"53 39",
"21 29",
"41 70",
"9 7",
"66 11",
"7 32",
"8 37",
"37 59",
"19 38",
"45 43",
"1 7",
"58 21",
"64 48",
"15 50",
"28 11",
"57 14",
"48 27",
"61 19",
"38 57",
"43 59",
"56 11",
"7 48",
"1 52",
"59 67",
"21 62",
"51 39",
"24 11",
"58 51",
"15 43",
"29 42",
"66 44",
"63 43",
"63 3",
"13 39",
"55 67",
"21 27",
"5 10",
"7 15",
"31 18",
"37 20",
"15 31",
"54 31",
"24 16",
"54 9",
"49 46",
"28 36",
"68 8",
"22 55",
"11 23",
"58 63",
"31 19",
"39 23",
"11 68",
"5 66",
"2 22",
"46 29",
"67 10",
"2 31",
"50 59",
"8 14",
"54 70",
"14 38",
"35 46",
"47 35",
"13 21",
"14 62",
"2 56",
"34 64",
"20 9",
"2 1",
"40 56",
"51 12",
"48 7",
"64 12",
"64 58",
"13 3",
"51 18",
"20 51",
"55 46",
"27 11",
"12 26",
"24 57",
"51 7",
"69 29",
"13 20",
"2 61",
"3 46",
"1 52",
"44 68",
"46 39",
"42 19",
"9 1",
"46 14",
"59 27",
"50 59",
"53 9",
"67 10",
"21 42",
"54 67",
"49 69",
"32 34",
"17 24",
"47 16",
"53 21",
"65 38",
"13 59",
"9 48",
"57 48",
"63 70",
"33 4",
"29 11",
"20 27",
"9 40",
"61 14",
"48 32",
"54 15",
"45 69",
"24 32",
"55 19",
"53 10",
"47 64",
"23 46",
"32 55",
"70 66",
"2 11",
"65 7",
"70 1",
"63 69",
"26 8",
"61 32",
"48 70",
"49 57",
"4 21",
"25 58",
"50 48",
"32 56",
"42 35",
"49 59",
"46 36",
"49 26",
"21 35",
"52 34",
"65 66",
"39 40",
"12 19",
"45 57",
"29 17",
"16 14",
"16 49",
"46 60",
"43 54",
"22 1",
"54 14",
"56 28",
"61 28",
"17 18",
"34 70",
"13 9",
"46 69",
"18 52",
"5 62",
"34 31",
"69 22",
"19 48",
"48 6",
"29 64",
"44 15",
"55 24",
"51 1",
"50 12",
"37 6",
"8 55",
"1 15",
"64 54",
"39 24",
"21 57",
"17 22",
"57 53",
"26 36",
"2 25",
"24 25",
"1 4",
"29 60",
"32 2",
"62 32",
"2 43",
"25 39",
"45 57",
"1 55",
"28 53",
"30 51",
"15 1",
"7 11",
"70 37",
"41 27",
"40 65",
"12 6",
"24 18",
"33 69",
"56 66",
"14 68",
"33 4",
"21 10",
"26 15",
"56 46",
"65 41",
"37 58",
"21 25",
"12 7",
"65 46",
"30 8",
"50 12",
"65 45",
"11 16",
"13 69",
"1 12",
"54 55",
"16 57",
"14 26",
"29 40",
"28 24",
"69 26",
"33 63",
"6 39",
"54 36",
"47 48",
"22 52",
"4 47",
"25 35",
"68 25",
"34 69",
"42 26",
"63 18",
"7 55",
"57 16",
"29 24",
"29 27",
"31 5",
"28 42",
"63 18",
"15 55",
"19 67",
"40 5",
"65 43",
"46 30",
"15 16",
"13 65",
"64 4",
"38 61",
"32 55",
"44 3",
"44 48",
"20 64",
"70 21",
"58 39",
"6 61",
"51 52",
"25 49",
"67 61",
"3 9",
"33 45",
"30 65",
"7 27",
"62 37",
"65 52",
"11 40",
"31 15",
"22 43",
"46 69",
"62 55",
"16 3",
"5 44",
"69 31",
"68 4",
"36 27",
"58 21",
"56 32",
"53 24",
"23 7",
"63 70",
"57 7",
"3 19",
"52 60",
"58 66",
"55 30",
"50 51",
"67 30",
"27 44",
"64 28",
"12 48",
"48 9",
"44 52",
"12 52",
"17 28",
"51 15",
"68 24",
"54 33",
"10 28",
"51 62",
"40 38",
"2 3",
"36 39",
"52 38",
"35 49",
"66 18",
"57 28",
"61 67",
"32 4",
"51 38",
"15 41",
"62 7",
"12 21",
"70 50",
"70 60",
"38 67",
"20 41",
"24 66",
"25 10",
"57 31",
"35 29",
"52 9",
"8 36",
"26 10",
"22 45",
"34 12",
"62 26",
"33 49",
"65 41",
"28 16",
"16 46",
"9 61",
"6 37",
"35 57",
"41 17",
"47 30",
"6 27",
"60 27",
"10 31",
"2 66",
"69 45",
"27 28",
"39 67",
"31 56",
"59 40",
"1 19",
"39 26",
"37 41",
"18 31",
"55 41",
"30 45",
"67 24",
"53 68",
"37 47",
"5 10",
"69 11",
"4 5",
"20 12",
"10 28",
"63 55",
"17 21",
"43 61",
"38 31",
"67 57",
"32 20",
"23 9",
"27 54",
"8 1",
"8 5",
"3 4",
"24 44",
"60 1",
"52 58",
"1 64",
"42 36",
"3 31",
"22 70",
"46 10",
"62 24",
"60 8",
"40 50",
"55 18",
"54 55",
"61 67",
"14 58",
"28 50",
"25 35",
"47 61",
"44 27",
"42 12",
"47 2",
"8 51",
"32 18",
"4 32",
"16 1",
"57 39",
"13 14",
"44 28",
"38 52",
"38 55",
"62 52",
"9 24",
"7 30",
"68 30",
"41 17",
"54 57",
"37 29",
"43 61",
"43 65",
"44 51",
"70 36",
"60 40",
"26 10",
"27 1",
"23 46",
"56 20",
"61 41",
"36 49",
"54 39",
"45 46",
"12 51",
"65 12",
"34 63",
"66 36",
"52 26",
"16 58",
"47 34",
"21 50",
"1 47",
"64 15",
"51 13",
"56 68",
"51 43",
"14 25",
"62 10",
"63 69",
"34 57",
"46 65",
"56 47",
"28 39",
"55 56",
"67 27",
"8 37",
"70 17",
"62 59",
"42 66",
"57 58",
"1 8",
"40 70",
"53 43",
"49 14",
"36 70",
"16 28",
"46 51",
"37 45",
"54 14",
"65 32",
"39 70",
"55 6",
"64 12",
"17 28",
"46 6",
"45 60",
"1 53",
"46 47",
"50 29",
"59 28",
"36 49",
"69 6",
"33 66",
"51 25",
"55 9",
"36 4",
"22 45",
"9 19",
"16 21",
"18 66",
"26 4",
"27 28",
"46 13",
"12 37",
"41 65",
"7 28",
"40 27",
"9 45",
"16"
]

def input():
    global state
    result = inputarray2[state]
    state += 1
    return result

import collections as col
class Node:
    def __init__(self, ID):
        self.ID = ID
        self.children = []

        self.distance = 0

    def __hash__(self):
        return hash(self.ID)

    def __eq__(self, other):
        return self.ID == other.ID

    def __str__(self):
        return str("{}".format(self.ID))

    def add_child(self,child):

        self.children.append(child)
        child.children.append(self)


class Tree:
    def __init__(self):
        self.idnodes = {}


    def add(self, ID1, ID2):
        if ID1 not in self.idnodes:
            self.idnodes[ID1] = Node(ID1)
        if ID2 not in self.idnodes:
            self.idnodes[ID2] = Node(ID2)
        self.idnodes[ID1].add_child(self.idnodes[ID2])

    def distance(self,ID):
        if ID in self.idnodes:
            return self.idnodes[ID].distance
        else:
            return - 1

    def rewalk(self,  ID):
        self.idnodes[ID].distance = 0
        S = set()
        Q = col.deque()
        S.add(self.idnodes[ID])
        Q.appendleft(self.idnodes[ID])

        while len(Q) > 0:
            current = Q.pop()
            for p in current.children:
                if p not in S:
                    p.distance = current.distance + 6
                    S.add(p)
                    Q.appendleft(p)


n = int(input())
for i in range(n):
    vn,en = map(int,input().split())
    t = Tree()
    for j in range(en):
        v1,v2  = map(int,input().split())
        t.add(v1,v2)
    sn =  int(input())
    t.rewalk (sn)
    vtw = list(range(1,vn+1))
    vtw.remove(sn)
    print(*(map(t.distance, vtw)))


