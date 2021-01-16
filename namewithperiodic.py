periodic_table = {
    "H":"Hydrogen",
    "He":"Helium",
    "Li":"Lithium",
    "Be":"Beryllium",
    "B":"Boron",
    "C":"Carbon",
    "N":"Nitrogen",
    "O":"Oxygen",
    "F":"Fluorine",
    "Ne":"Neon",
    "Na":"Sodium",
    "Mg":"Magnesium",
    "Al":"Aluminum",
    "Si":"Silicon",
    "P":"Phosphorus",
    "S":"Sulfur",
    "Cl":"Chlorine",
    "Ar":"Argon",
    "K":"Potassium",
    "Ca":"Calcium",
    "Sc":"Scandium",
    "Ti":"Titanium",
    "V":"Vandium",
    "Cr":"Chromium",
    "Mn":"Manganese",
    "Fe":"Iron",
    "Co":"Cobalt",
    "Ni":"Nickel",
    "Cu":"Copper",
    "Zn":"Zinc",
    "Ga":"Gallium",
    "Ge":"Germanium",
    "As":"Arsenic",
    "Se":"Selenium",
    "Br":"Bromine",
    "Kr":"Krypton",
    "Rb":"Rubidium",
    "Sr":"Strontium",
    "Y":"Yttrium",
    "Zr":"Zirconium",
    "Nb":"Niobium",
    "Mo":"Molybdenum",
    "Tc":"Technetium",
    "Ru":"Ruthenium",
    "Rh":"Rhodium",
    "Pd":"Palladium",
    "Ag":"Silver",
    "Cd":"Cadmium",
    "In":"Indium",
    "Sn":"Tin",
    "Sb":"Antimony",
    "Te":"Tellerium",
    "I":"Iodine",
    "Xe":"Xenon",
    "Cs":"Cesium",
    "Ba":"Barium",
    "La":"Lanthanum",
    "Ce":"Cerium",
    "Pr":"Prasedymium",
    "Nd":"Neodymium",
    "Pm":"Promethium",
    "Sm":"Samarium",
    "Eu":"Europium",
    "Gd":"Gadolinium",
    "Tb":"Terbium",
    "Dy":"Dysprosium",
    "Ho":"Holmiun",
    "Er":"Erbium",
    "Tm":"Thulium",
    "Yb":"Ytterbium",
    "Lu":"Lutentium",
    "Hf":"Hafnium",
    "Ta":"Tantalum",
    "W":"Tungsten",
    "Re":"Rhenium",
    "Os":"Osmium",
    "Ir":"Iridium",
    "Pt":"Paltinum",
    "Au":"Gold",
    "Hg":"Mercury",
    "Tl":"Thallium",
    "Pb":"Lead",
    "Bi":"Bisumuth",
    "Po":"Polonium",
    "At":"Astatine",
    "Rn":"Radon",
    "Fr":"Francium",
    "Ra":"Radium",
    "Ac":"Actinium",
    "Th":"Thorium",
    "Pa":"Protactinium",
    "U":"Uranium",
    "Np":"Neptunium",
    "Pu":"Plutonium",
    "Am":"Americium",
    "Cm":"Curium",
    "Bk":"Berkelium",
    "Cf":"Californium",
    "Es":"Einstenium",
    "Fm":"Fermium",
    "Md":"Mendelevium",
    "No":"Nobelium",
    "Lr":"Lawrencium",
    "Rf":"Rutherfordium",
    "Db":"Dubnium",
    "Sg":"Seaborgium",
    "Bh":"Bohrium",
    "Hs":"Hassium",
    "Mt":"Meitnerium",
    "Ds":"Darmstadtium",
    "Rg":"Roentgenium",
    "Cn":"Copernicium",
    "Nh":"Nihounium",
    "Fl":"Flerovium",
    "Mc":"Moscovium",
    "Lv":"Livermorium",
    "Ts":"Tennessine",
    "Og":"Oganesson"
    }
keys = list(periodic_table.keys())

print(keys)
print('')

x = str(input("name please: "))
#complete name
name1 = []
for i in x:
    name1.append(i)
#odd index value name
newlst1 = []
for i,e in enumerate(x):
    if i%2 !=0:
        newlst1.append(e)
#even index value name
newlst2 = []
for i,e in enumerate(x):
    if i%2 ==0:
        newlst2.append(e.upper())
#combined index valued name that are paired
newlst3 = list(zip(newlst2,newlst1))
#print(newlst3)   


name2 = []
for i in newlst3:
    name2.append(''.join(i))

#print(name2)
    
name3 = []
for i in name2:
    if i in keys:
        name3.append(i)
    elif i not in keys:
        for e in i:
            if e.upper() in keys:
                name3.append(e.upper())
        


print(name3) 










