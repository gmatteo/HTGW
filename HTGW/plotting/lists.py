from __future__ import division
from __future__ import print_function,  division

__author__ = 'setten'
__version__ = "0.1"
__maintainer__ = "Michiel van Setten"
__email__ = "mjvansetten@gmail.com"
__date__ = "Sept 2014"

colors = ['r',  'g',  'b',  'y',  'm',  'c',  'k',  'k',  'k',  'k',  'k',  'k',  'k',  'k']

ptable = {
    'H': [1, None, 1.0079, 'Hydrogen', 'H', -259, -253, 0.09, 0.14, 1776, 1, '1s1', 13.5984],
    'He': [2, None, 4.0026, 'Helium', 'He', -272, -269, 0.18, None, 1895, 18, '1s2', 24.5874],
    'Li': [3, None, 6.941, 'Lithium', 'Li', 180, 1347, 0.53, None, 1817, 1, 'He 2s1', 5.3917],
    'Be': [4, None, 9.0122, 'Beryllium', 'Be', 1278, 2970, 1.85, None, 1797, 2, 'He 2s2', 9.3227],
    'B': [5, None, 10.811, 'Boron', 'B', 2300, 2550, 2.34, None, 1808, 13, 'He 2s2 2p1', 8.298],
    'C': [6, None, 12.0107, 'Carbon', 'C', 3500, 4827, 2.26, 0.094,  'ancient', 14, 'He 2s2 2p2', 11.2603],
    'N': [7, None, 14.0067, 'Nitrogen', 'N', -210, -196, 1.25, None, 1772, 15, 'He 2s2 2p3', 14.5341],
    'O': [8, None, 15.9994, 'Oxygen', 'O', -218, -183, 1.43, 46.71, 1774, 16, 'He 2s2 2p4', 13.6181],
    'F': [9, None, 18.9984, 'Fluorine', 'F', -220, -188, 1.7, 0.029, 1886, 17, 'He 2s2 2p5', 17.4228],
    'Ne': [10, None, 20.1797, 'Neon', 'Ne', -249, -246, 0.9, None, 1898, 18, 'He 2s2 2p6', 21.5645],
    'Na': [11, None, 22.9897, 'Sodium', 'Na', 98, 883, 0.97, 2.75, 1807, 1, 'Ne 3s1', 5.1391],
    'Mg': [12, None, 24.305, 'Magnesium', 'Mg', 639, 1090, 1.74, 2.08, 1755, 2, 'Ne 3s2', 7.6462],
    'Al': [13, None, 26.9815, 'Aluminum', 'Al', 660, 2467, 2.7, 8.07, 1825, 13, 'Ne 3s2 3p1', 5.9858],
    'Si': [14, None, 28.0855, 'Silicon', 'Si', 1410, 2355, 2.33, 27.69, 1824, 14, 'Ne 3s2 3p2', 8.1517],
    'P': [15, None, 30.9738, 'Phosphorus', 'P', 44, 280, 1.82, 0.13, 1669, 15, 'Ne 3s2 3p3', 10.4867],
    'S': [16, None, 32.065, 'Sulfur', 'S', 113, 445, 2.07, 0.052,  'ancient', '16, Ne 3s2 3p4', 10.36],
    'Cl': [17, None, 35.453, 'Chlorine', 'Cl', -101, -35, 3.21, 0.045, 1774, 17, 'Ne 3s2 3p5', 12.9676],
    'Ar': [18, None, 39.948, 'Argon', 'Ar', -189, -186, 1.78, None, 1894, 18, 'Ne 3s2 3p6', 15.7596],
    'K': [19, None, 39.0983, 'Potassium', 'K', 64, 774, 0.86, 2.58, 1807, 1, 'Ar 4s1', 4.3407],
    'Ca': [20, None, 40.078, 'Calcium', 'Ca', 839, 1484, 1.55, 3.65, 1808, 2, 'Ar 4s2', 6.1132],
    'Sc': [21, None, 44.9559, 'Scandium', 'Sc', 1539, 2832, 2.99, None, 1879, 3, 'Ar 3d1 4s2', 6.5615],
    'Ti': [22, None, 47.867, 'Titanium', 'Ti', 1660, 3287, 4.54, 0.62, 1791, 4, 'Ar 3d2 4s2', 6.8281],
    'V': [23, None, 50.9415, 'Vanadium', 'V', 1890, 3380, 6.11, None, 1830, 5, 'Ar 3d3 4s2', 6.7462],
    'Cr': [24, None, 51.9961, 'Chromium', 'Cr', 1857, 2672, 7.19, 0.035, 1797, 6, 'Ar 3d5 4s1', 6.7665],
    'Mn': [25, None, 54.938, 'Manganese', 'Mn', 1245, 1962, 7.43, 0.09, 1774, 7, 'Ar 3d5 4s2', 7.434],
    'Fe': [26, None, 55.845, 'Iron', 'Fe', 1535, 2750, 7.87, 5.05,  'ancient', 8, 'Ar 3d6 4s2', 7.9024],
    'Co': [27, None, 58.9332, 'Cobalt', 'Co', 1495, 2870, 8.9, None, 1735, 9, 'Ar 3d7 4s2', 7.881],
    'Ni': [28, None, 58.6934, 'Nickel', 'Ni', 1453, 2732, 8.9, 0.019, 1751, 10, 'Ar 3d8 4s2', 7.6398],
    'Cu': [29, None, 63.546, 'Copper', 'Cu', 1083, 2567, 8.96, None,  'ancient', 11, 'Ar 3d10 4s1', 7.7264],
    'Zn': [30, None, 65.39, 'Zinc', 'Zn', 420, 907, 7.13, None,  'ancient', 12, 'Ar 3d10 4s2', 9.3942],
    'Ga': [31, None, 69.723, 'Gallium', 'Ga', 30, 2403, 5.91, None, 1875, 13, 'Ar 3d10 4s2 4p1', 5.9993],
    'Ge': [32, None, 72.64, 'Germanium', 'Ge', 937, 2830, 5.32, None, 1886, 14, 'Ar 3d10 4s2 4p2', 7.8994],
    'As': [33, None, 74.9216, 'Arsenic', 'As', 81, 613, 5.72, None,  'ancient', 15, 'Ar 3d10 4s2 4p3', 9.7886],
    'Se': [34, None, 78.96, 'Selenium', 'Se', 217, 685, 4.79, None, 1817, 16, 'Ar 3d10 4s2 4p4', 9.7524],
    'Br': [35, None, 79.904, 'Bromine', 'Br', -7, 59, 3.12, None, 1826, 17, 'Ar 3d10 4s2 4p5', 11.8138],
    'Kr': [36, None, 83.8, 'Krypton', 'Kr', -157, -153, 3.75, None, 1898, 18, 'Ar 3d10 4s2 4p6', 13.9996],
    'Rb': [37, None, 85.4678, 'Rubidium', 'Rb', 39, 688, 1.63, None, 1861, 1, 'Kr 5s1', 4.1771],
    'Sr': [38, None, 87.62, 'Strontium', 'Sr', 769, 1384, 2.54, None, 1790, 2, 'Kr 5s2', 5.6949],
    'Y': [39, None, 88.9059, 'Yttrium', 'Y', 1523, 3337, 4.47, None, 1794, 3, 'Kr 4d1 5s2', 6.2173],
    'Zr': [40, None, 91.224, 'Zirconium', 'Zr', 1852, 4377, 6.51, 0.025, 1789, 4, 'Kr 4d2 5s2', 6.6339],
    'Nb': [41, None, 92.9064, 'Niobium', 'Nb', 2468, 4927, 8.57, None, 1801, 5, 'Kr 4d4 5s1', 6.7589],
    'Mo': [42, None, 95.94, 'Molybdenum', 'Mo', 2617, 4612, 10.22, None, 1781, 6, 'Kr 4d5 5s1', 7.0924],
    'Tc': [43, 1, 98, 'Technetium', 'Tc', 2200, 4877, 11.5, None, 1937, 7, 'Kr 4d5 5s2', 7.28],
    'Ru': [44, None, 101.07, 'Ruthenium', 'Ru', 2250, 3900, 12.37, None, 1844, 8, 'Kr 4d7 5s1', 7.3605],
    'Rh': [45, None, 102.9055, 'Rhodium', 'Rh', 1966, 3727, 12.41, None, 1803, 9, 'Kr 4d8 5s1', 7.4589],
    'Pd': [46, None, 106.42, 'Palladium', 'Pd', 1552, 2927, 12.02, None, 1803, 10, 'Kr 4d10', 8.3369],
    'Ag': [47, None, 107.8682, 'Silver', 'Ag', 962, 2212, 10.5, None,  'ancient', 11, 'Kr 4d10 5s1', 7.5762],
    'Cd': [48, None, 112.411, 'Cadmium', 'Cd', 321, 765, 8.65, None, 1817, 12, 'Kr 4d10 5s2', 8.9938],
    'In': [49, None, 114.818, 'Indium', 'In', 157, 2000, 7.31, None, 1863, 13, 'Kr 4d10 5s2 5p1', 5.7864],
    'Sn': [50, None, 118.71, 'Tin', 'Sn', 232, 2270, 7.31, None,  'ancient', 14, 'Kr 4d10 5s2 5p2', 7.3439],
    'Sb': [51, None, 121.76, 'Antimony', 'Sb', 630, 1750, 6.68, None,  'ancient', 15, 'Kr 4d10 5s2 5p3', 8.6084],
    'Te': [52, None, 127.6, 'Tellurium', 'Te', 449, 990, 6.24, None, 1783, 16, 'Kr 4d10 5s2 5p4', 9.0096],
    'I': [53, None, 126.9045, 'Iodine', 'I', 114, 184, 4.93, None, 1811, 17, 'Kr 4d10 5s2 5p5', 10.4513],
    'Xe': [54, None, 131.293, 'Xenon', 'Xe', -112, -108, 5.9, None, 1898, 18, 'Kr 4d10 5s2 5p6', 12.1298],
    'Cs': [55, None, 132.9055, 'Cesium', 'Cs', 29, 678, 1.87, None, 1860, 1, 'Xe 6s1', 3.8939],
    'Ba': [56, None, 137.327, 'Barium', 'Ba', 725, 1140, 3.59, 0.05, 1808, 2, 'Xe 6s2', 5.2117],
    'La': [57, None, 138.9055, 'Lanthanum', 'La', 920, 3469, 6.15, None, 1839, 3, 'Xe 5d1 6s2', 5.5769],
    'Ce': [58, None, 140.116, 'Cerium', 'Ce', 795, 3257, 6.77, None, 1803, 101, 'Xe 4f1 5d1 6s2', 5.5387],
    'Pr': [59, None, 140.9077, 'Praseodymium', 'Pr', 935, 3127, 6.77, None, 1885, 101, 'Xe 4f3 6s2', 5.473],
    'Nd': [60, None, 144.24, 'Neodymium', 'Nd', 1010, 3127, 7.01, None, 1885, 101, 'Xe 4f4 6s2', 5.525],
    'Pm': [61, 1, 145, 'Promethium', 'Pm', 1100, 3000, 7.3, None, 1945, 101, 'Xe 4f5 6s2', 5.582],
    'Sm': [62, None, 150.36, 'Samarium', 'Sm', 1072, 1900, 7.52, None, 1879, 101, 'Xe 4f6 6s2', 5.6437],
    'Eu': [63, None, 151.964, 'Europium', 'Eu', 822, 1597, 5.24, None, 1901, 101, 'Xe 4f7 6s2', 5.6704],
    'Gd': [64, None, 157.25, 'Gadolinium', 'Gd', 1311, 3233, 7.9, None, 1880, 101, 'Xe 4f7 5d1 6s2', 6.1501],
    'Tb': [65, None, 158.9253, 'Terbium', 'Tb', 1360, 3041, 8.23, None, 1843, 101, 'Xe 4f9 6s2', 5.8638],
    'Dy': [66, None, 162.5, 'Dysprosium', 'Dy', 1412, 2562, 8.55, None, 1886, 101, 'Xe 4f10 6s2', 5.9389],
    'Ho': [67, None, 164.9303, 'Holmium', 'Ho', 1470, 2720, 8.8, None, 1867, 101, 'Xe 4f11 6s2', 6.0215],
    'Er': [68, None, 167.259, 'Erbium', 'Er', 1522, 2510, 9.07, None, 1842, 101, 'Xe 4f12 6s2', 6.1077],
    'Tm': [69, None, 168.9342, 'Thulium', 'Tm', 1545, 1727, 9.32, None, 1879, 101, 'Xe 4f13 6s2', 6.1843],
    'Yb': [70, None, 173.04, 'Ytterbium', 'Yb', 824, 1466, 6.9, None, 1878, 101, 'Xe 4f14 6s2', 6.2542],
    'Lu': [71, None, 174.967, 'Lutetium', 'Lu', 1656, 3315, 9.84, None, 1907, 101, 'Xe 4f14 5d1 6s2', 5.4259],
    'Hf': [72, None, 178.49, 'Hafnium', 'Hf', 2150, 5400, 13.31, None, 1923, 4, 'Xe 4f14 5d2 6s2', 6.8251],
    'Ta': [73, None, 180.9479, 'Tantalum', 'Ta', 2996, 5425, 16.65, None, 1802, 5, 'Xe 4f14 5d3 6s2', 7.5496],
    'W': [74, None, 183.84, 'Tungsten', 'W', 3410, 5660, 19.35, None, 1783, 6, 'Xe 4f14 5d4 6s2', 7.864],
    'Re': [75, None, 186.207, 'Rhenium', 'Re', 3180, 5627, 21.04, None, 1925, 7, 'Xe 4f14 5d5 6s2', 7.8335],
    'Os': [76, None, 190.23, 'Osmium', 'Os', 3045, 5027, 22.6, None, 1803, 8, 'Xe 4f14 5d6 6s2', 8.4382],
    'Ir': [77, None, 192.217, 'Iridium', 'Ir', 2410, 4527, 22.4, None, 1803, 9, 'Xe 4f14 5d7 6s2', 8.967],
    'Pt': [78, None, 195.078, 'Platinum', 'Pt', 1772, 3827, 21.45, None, 1735, 10, 'Xe 4f14 5d9 6s1', 8.9587],
    'Au': [79, None, 196.9665, 'Gold', 'Au', 1064, 2807, 19.32, None,  'ancient', 11, 'Xe 4f14 5d10 6s1', 9.2255],
    'Hg': [80, None, 200.59, 'Mercury', 'Hg', -39, 357, 13.55, None,  'ancient', 12, 'Xe 4f14 5d10 6s2', 10.4375],
    'Tl': [81, None, 204.3833, 'Thallium', 'Tl', 303, 1457, 11.85, None, 1861, 13, 'Xe 4f14 5d10 6s2 6p1', 6.1082],
    'Pb': [82, None, 207.2, 'Lead', 'Pb', 327, 1740, 11.35, None,  'ancient', 14, 'Xe 4f14 5d10 6s2 6p2', 7.4167],
    'Bi': [83, None, 208.9804, 'Bismuth', 'Bi', 271, 1560, 9.75, None,  'ancient', 15, 'Xe 4f14 5d10 6s2 6p3', 7.2856],
    'Po': [84, 1, 209, 'Polonium', 'Po', 254, 962, 9.3, None, 1898, 16, 'Xe 4f14 5d10 6s2 6p4', 8.417],
    'At': [85, 1, 210, 'Astatine', 'At', 302, 337, None, None, 1940, 17, 'Xe 4f14 5d10 6s2 6p5', 9.3],
    'Rn': [86, 1, 222, 'Radon', 'Rn', -71, -62, 9.73, None, 1900, 18, 'Xe 4f14 5d10 6s2 6p6', 10.7485],
    'Fr': [87, 1, 223, 'Francium', 'Fr', 27, 677, None, None, 1939, 1, 'Rn 7s1', 4.0727],
    'Ra': [88, 1, 226, 'Radium', 'Ra', 700, 1737, 5.5, None, 1898, 2, 'Rn 7s2', 5.2784],
    'Ac': [89, 1, 227, 'Actinium', 'Ac', 1050, 3200, 10.07, None, 1899, 3, 'Rn 6d1 7s2', 5.17],
    'Th': [90, None, 232.0381, 'Thorium', 'Th', 1750, 4790, 11.72, None, 1829, 102, 'Rn 6d2 7s2', 6.3067],
    'Pa': [91, None, 231.0359, 'Protactinium', 'Pa', 1568, None, 15.4, None, 1913, 102, 'Rn 5f2 6d1 7s2', 5.89],
    'U': [92, None, 238.0289, 'Uranium', 'U', 1132, 3818, 18.95, None, 1789, 102, 'Rn 5f3 6d1 7s2', 6.1941],
    'Np': [93, 1, 237, 'Neptunium', 'Np', 640, 3902, 20.2, None, 1940, 102, 'Rn 5f4 6d1 7s2', 6.2657],
    'Pu': [94, 1, 244, 'Plutonium', 'Pu', 640, 3235, 19.84, None, 1940, 102, 'Rn 5f6 7s2', 6.0262],
    'Am': [95, 1, 243, 'Americium', 'Am', 994, 2607, 13.67, None, 1944, 102, 'Rn 5f7 7s2', 5.9738],
    'Cm': [96, 1, 247, 'Curium', 'Cm', 1340, None, 13.5, None, 1944, 102, None, 5.9915],
    'Bk': [97, 1, 247, 'Berkelium', 'Bk', 986, None, 14.78, None, 1949, 102, None, 6.1979],
    'Cf': [98, 1, 251, 'Californium', 'Cf', 900, None, 15.1, None, 1950, 102, None, 6.2817],
    'Es': [99, 1, 252, 'Einsteinium', 'Es', 860, None, None, None, 1952, 102, None, 6.42],
    'Fm': [100, 1, 257, 'Fermium', 'Fm', 1527, None, None, None, 1952, 102, None, 6.5],
    'Md': [101, 1, 258, 'Mendelevium', 'Md', None, None, None, None, 1955, 102, None, 6.58],
    'No': [102, 1, 259, 'Nobelium', 'No', 827, None, None, None, 1958, 102, None, 6.65],
    'Lr': [103, 1, 262, 'Lawrencium', 'Lr', 1627, None, None, None, 1961, 102, None, 4.9],
    'Rf': [104, 1, 261, 'Rutherfordium', 'Rf', None, None, None, None, 1964, 4, None, None],
    'Db': [105, 1, 262, 'Dubnium', 'Db', None, None, None, None, 1967, 5, None, None],
    'Sg': [106, 1, 266, 'Seaborgium', 'Sg', None, None, None, None, 1974, 6, None, None],
    'Bh': [107, 1, 264, 'Bohrium', 'Bh', None, None, None, None, 1981, 7, None, None],
    'Hs': [108, 1, 277, 'Hassium', 'Hs', None, None, None, None, 1984, 8, None, None],
    'Mt': [109, 1, 268, 'Meitnerium', 'Mt', None, None, None, None, 1982, 9, None, None]
}
