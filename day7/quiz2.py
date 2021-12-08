from statistics import mean
import math

data = "16,1,2,0,4,2,7,1,2,14"
data = "1101,1,29,67,1102,0,1,65,1008,65,35,66,1005,66,28,1,67,65,20,4,0,1001,65,1,65,1106,0,8,99,35,67,101,99,105,32,110,39,101,115,116,32,112,97,115,32,117,110,101,32,105,110,116,99,111,100,101,32,112,114,111,103,114,97,109,10,1247,39,529,198,497,33,1618,2,28,653,764,312,163,62,263,4,243,1277,8,432,324,564,44,56,745,0,534,558,1026,313,482,410,411,63,461,261,561,62,428,42,1806,251,1186,553,241,795,127,1004,94,183,382,194,890,1025,1153,1064,155,278,203,666,1098,678,228,12,530,226,680,476,74,122,136,64,515,630,137,187,146,249,77,879,1174,257,9,353,1496,239,131,21,330,922,110,5,804,2,1195,756,195,399,1306,1495,1088,687,102,901,222,3,717,853,1242,573,406,645,1211,193,319,35,302,677,704,42,69,228,247,420,401,1006,124,662,355,746,483,211,1484,146,104,314,154,170,932,215,1600,1250,20,134,1038,724,728,157,261,1373,1113,449,339,415,1165,172,956,466,327,1342,27,1031,1233,547,636,100,440,510,154,28,949,222,867,11,297,218,814,169,358,1088,1071,630,1360,1106,249,13,312,7,56,1667,948,69,767,279,1032,82,139,636,592,684,294,952,83,252,158,450,1250,78,548,1052,1,1231,888,253,533,637,694,955,448,1351,1569,1060,65,269,450,102,962,408,259,61,20,437,14,1676,16,533,90,1727,623,286,48,395,169,271,140,652,139,1497,356,98,60,362,964,880,934,544,140,322,428,80,215,192,300,431,126,46,109,780,209,776,203,443,60,889,21,882,22,127,476,694,174,226,1041,364,282,541,429,755,770,931,967,1346,1240,647,150,199,137,181,1177,571,150,1104,56,517,286,1204,346,619,1269,307,425,228,254,328,570,956,1567,810,356,196,77,31,429,1178,6,502,310,443,1221,119,571,583,18,256,460,694,650,799,200,121,119,125,894,1263,610,892,635,93,320,252,371,1416,150,664,154,344,381,610,819,591,536,1312,1521,148,1232,70,50,328,226,752,1685,729,449,31,963,402,62,1365,928,619,538,950,202,19,271,292,59,55,345,189,302,29,217,486,1576,62,1364,122,1667,388,62,182,1278,13,459,729,821,293,78,5,111,135,868,94,196,14,342,185,271,1055,350,363,235,137,142,31,30,466,922,436,1174,81,114,244,770,54,288,579,4,1287,36,321,849,751,1081,342,359,829,1147,1092,125,269,1652,493,22,456,193,49,70,288,4,954,1718,84,154,24,171,220,1033,66,289,395,1732,1553,616,411,899,1398,402,219,621,343,293,422,494,80,732,1210,449,72,236,307,541,10,620,1361,605,351,1304,475,215,989,153,8,1229,113,216,3,170,998,308,964,1755,223,1694,1937,60,41,1120,491,1270,766,501,326,236,632,163,880,963,1213,1030,444,229,425,239,834,59,66,580,488,303,475,457,1182,150,1273,53,22,53,224,536,945,824,56,694,187,586,555,1464,188,538,286,120,260,38,70,13,678,916,542,235,1138,34,259,12,280,178,45,213,1,580,268,114,1076,536,185,825,374,282,186,3,356,393,385,597,53,187,288,10,194,447,949,521,84,124,16,221,153,800,969,241,40,76,565,7,238,252,13,276,461,30,1034,129,204,657,793,630,1068,97,537,226,155,363,531,458,123,442,1155,371,196,1764,1049,73,258,853,2,653,923,189,472,1119,582,974,948,447,161,1737,765,93,369,48,293,762,58,2,1282,242,67,1310,129,468,425,116,471,768,291,878,1138,569,427,725,515,67,526,766,213,1307,288,1589,1304,3,287,1050,14,7,428,1684,479,355,72,1233,21,1449,284,11,27,315,274,181,215,486,247,946,59,158,432,231,178,1722,13,189,439,13,72,211,239,841,175,893,234,328,154,134,13,653,31,40,303,110,172,113,515,69,1009,1413,450,172,168,92,385,1555,216,1487,72,173,339,496,779,1696,153,49,342,1225,141,873,402,777,269,767,361,108,536,1432,343,23,380,716,1609,958,1512,743,246,315,220,1634,16,405,61,1150,350,620,1,13,749,9,738,1391,334,148,1142,220,662,1612,878,65,164,235,95,499,929,399,1675,886,86,452,238,487,354,103,7,372,428,971,419,41,56,613,126,819,354,170,1025,1183,2,1201,813,339,272,400,13,221,1021,182,192,1239,52,508,266,42,504,1281,779,1629,46,65,541,1004,115,384,922,89,372,56,211,419,420,149,316,670,1271,253,845,260,25,624,402,54,270,1366,831,170,47,11,235,106,757,854,1343,548,32,29,283,200,11,443,12,372,239,165,440,1099,104,686,335,656,1182,994,1126,14,503,508,766,634,744,660,102,56,449,227,96,357,23,83,653,519,144,9,59,892,253,984,777,178,629,82"

data = [int(x) for x in data.split(",")]

m = mean(data)
mid = math.floor(m)
mid2 = math.ceil(m)

fuel = 0
fuel2 = 0

for x in data:
    n = abs(x - mid)
    fuel += (n * (n + 1) // 2)

    n = abs(x - mid2)
    fuel2 += (n * (n + 1) // 2)

print(min([fuel, fuel2]))
