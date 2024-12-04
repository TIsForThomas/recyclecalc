import math
def multiAllResources(a,b):
    return(a*b)
def addAllResources(a,b,c,d,e,f,g,h,i,j,k,l,m):
    return(a+b+c+d+e+f+g+h+i+j+k+l+m)
def addAllCloth(a,b,c):
    return(a+b+c)
class Component:
    def __init__(self, scrap, hqm, metal, cloth):
        self.scrap = scrap
        self.hqm = hqm
        self.metal = metal
        self.cloth = cloth
sheetMetal = Component(8,1,100,0)
roadSign = Component(5,1,0,0)
metalSpring = Component(10,1,0,0)
metalPipe = Component(5,1,0,0)
metalBlade = Component(2,0,15,0)
propaneTank = Component(1,0,50,0)
metalGear = Component(10,0,13,0)
semiBody = Component(15,2,75,0)
smgBody = Component(15,2,0,0)
rifleBody = Component(25,2,0,0)
techTrash = Component(20,1,0,0)
camEra = Component(40,4,0,0)
lapTop = Component(60,4,50,0)
sewingKit = Component(0,0,0,50)
rope = Component(0,0,0,15)
tarp = Component(0,0,0,50)

global safezoneIndicator

print("Thanks for using this handy dandy recycler calculator!")

safezoneIndicatorInput = input("Are you are recycling in a safe zone? Type: yes or no: ")

if safezoneIndicatorInput == "yes":
    print("You selected: Yes, I am in a safe zone")
    safezoneIndicator = True
elif safezoneIndicatorInput == "no":
    print("You selected: No, I am not in a safe zone")
    safezoneIndicator = False
else:
    print("invalid Input")

print("Please provide the ammount of components you brought to recycle in numerical form:")

while True:
    try:
        sheetMetalCount = int(input("How many sheet metals do you have?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break

sheetMetalScrapCount = multiAllResources(sheetMetal.scrap,sheetMetalCount)
sheetMetalHqmCount = multiAllResources(sheetMetal.hqm,sheetMetalCount)
sheetMetalMetalCount = multiAllResources(sheetMetal.metal,sheetMetalCount)

while True:
    try:
        roadSignCount = int(input("How many road signs do you have?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break

roadSignScrapCount = multiAllResources(roadSign.scrap,roadSignCount)
roadSignHqmCount = multiAllResources(roadSign.hqm,roadSignCount)
roadSignMetalCount = multiAllResources(roadSign.metal,roadSignCount)

while True:
    try:
        metalSpringCount = int(input("How many metal springs do you have?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break

metalSpringScrapCount = multiAllResources(metalSpring.scrap,metalSpringCount)
metalSpringHqmCount = multiAllResources(metalSpring.hqm,metalSpringCount)
metalSpringMetalCount = multiAllResources(metalSpring.metal,metalSpringCount)

while True:
    try:
        metalPipeCount = int(input("How many metal pipes do you have?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break

metalPipeScrapCount = multiAllResources(metalPipe.scrap,metalPipeCount)
metalPipeHqmCount = multiAllResources(metalPipe.hqm,metalPipeCount)
metalPipeMetalCount = multiAllResources(metalPipe.metal,metalPipeCount)

while True:
    try:
        metalBladeCount = int(input("How many metal blades do you have?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break

metalBladeScrapCount = multiAllResources(metalBlade.scrap,metalBladeCount)
metalBladeHqmCount = multiAllResources(metalBlade.hqm,metalBladeCount)
metalBladeMetalCount = multiAllResources(metalBlade.metal,metalBladeCount)

while True:
    try:
        propaneTankCount = int(input("How many propane tanks do you have?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break

propaneTankScrapCount = multiAllResources(propaneTank.scrap,propaneTankCount)
propaneTankHqmCount = multiAllResources(propaneTank.hqm,propaneTankCount)
propaneTankMetalCount = multiAllResources(propaneTank.metal,propaneTankCount)

while True:
    try:
        metalGearCount = int(input("How many gears do you have?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break

metalGearScrapCount = multiAllResources(metalGear.scrap,metalGearCount)
metalGearHqmCount = multiAllResources(metalGear.hqm,metalGearCount)
metalGearMetalCount = multiAllResources(metalGear.metal,metalGearCount)

while True:
    try:
        semiBodyCount = int(input("How many semi bodies do you have?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break

semiBodyScrapCount = multiAllResources(semiBody.scrap,semiBodyCount)
semiBodyHqmCount = multiAllResources(semiBody.hqm,semiBodyCount)
semiBodyMetalCount = multiAllResources(semiBody.metal,semiBodyCount)

while True:
    try:
        smgBodyCount = int(input("How many smg bodies do you have?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break

smgBodyScrapCount = multiAllResources(smgBody.scrap,smgBodyCount)
smgBodyHqmCount = multiAllResources(smgBody.hqm,smgBodyCount)
smgBodyMetalCount = multiAllResources(smgBody.metal,smgBodyCount)

while True:
    try:
        rifleBodyCount = int(input("How many rifle bodies do you have?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break

rifleBodyScrapCount = multiAllResources(rifleBody.scrap,rifleBodyCount)
rifleBodyHqmCount = multiAllResources(rifleBody.hqm,rifleBodyCount)
rifleBodyMetalCount = multiAllResources(rifleBody.metal,rifleBodyCount)

while True:
    try:
        techTrashCount = int(input("How much tech trash do you have?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break

techTrashScrapCount = multiAllResources(techTrash.scrap,techTrashCount)
techTrashHqmCount = multiAllResources(techTrash.hqm,techTrashCount)
techTrashMetalCount = multiAllResources(techTrash.metal,techTrashCount)

while True:
    try:
        camEraCount = int(input("How many cameras do you have?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break

camEraScrapCount = multiAllResources(camEra.scrap,camEraCount)
camEraHqmCount = multiAllResources(camEra.hqm,camEraCount)
camEraMetalCount = multiAllResources(camEra.metal,camEraCount)

while True:
    try:
        lapTopCount = int(input("How many laptops do you have?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break

lapTopScrapCount = multiAllResources(lapTop.scrap,lapTopCount)
lapTopHqmCount = multiAllResources(lapTop.hqm,lapTopCount)
lapTopMetalCount = multiAllResources(lapTop.metal,lapTopCount)

while True:
    try:
        sewingKitCount = int(input("How many sewing kits do you have?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break

sewingKitClothCount = multiAllResources(sewingKit.cloth,sewingKitCount)

while True:
    try:
        ropeCount = int(input("How much rope do you have?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break

ropeClothCount = multiAllResources(rope.cloth,ropeCount)

while True:
    try:
        tarpCount = int(input("How much tarp do you have?: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break


tarpClothCount = multiAllResources(tarp.cloth,tarpCount)

totalPreSafeZoneScrap = addAllResources(sheetMetalScrapCount, roadSignScrapCount, metalSpringScrapCount, metalPipeScrapCount, metalBladeScrapCount, propaneTankScrapCount, metalGearScrapCount, semiBodyScrapCount, smgBodyScrapCount, rifleBodyScrapCount, techTrashScrapCount, camEraScrapCount, lapTopScrapCount)

totalPreSafeZoneHqm = addAllResources(sheetMetalHqmCount, roadSignHqmCount, metalSpringHqmCount, metalPipeHqmCount, metalBladeHqmCount, propaneTankHqmCount, metalGearHqmCount, semiBodyHqmCount, smgBodyHqmCount, rifleBodyHqmCount, techTrashHqmCount, camEraHqmCount, lapTopHqmCount)

totalPreSafeZoneMetal = addAllResources(sheetMetalMetalCount, roadSignMetalCount, metalSpringMetalCount, metalPipeMetalCount, metalBladeMetalCount, propaneTankMetalCount, metalGearMetalCount, semiBodyMetalCount, smgBodyMetalCount, rifleBodyMetalCount, techTrashMetalCount, camEraMetalCount, lapTopMetalCount)

totalPreSafeZoneCloth = addAllCloth(sewingKitClothCount, ropeClothCount, ropeClothCount)

#print(totalPreSafeZoneScrap)

#print(totalPreSafeZoneHqm)

#print(totalPreSafeZoneMetal)

#print(totalPreSafeZoneCloth)

if safezoneIndicator == True: 
    totalSafeZoneScrap = round(multiAllResources(totalPreSafeZoneScrap, 0.8))
    totalSafeZoneHqm = round(multiAllResources(totalPreSafeZoneHqm, 0.8))
    totalSafeZoneMetal = round(multiAllResources(totalPreSafeZoneMetal, 0.8))
    totalSafeZoneCloth = round(multiAllResources(totalPreSafeZoneCloth, 0.8))
    
    print("Recycling inside of a Safe Zone, you will get", totalSafeZoneScrap, "Scrap", totalSafeZoneHqm, "HQM", totalSafeZoneMetal, "Metal Frags", totalSafeZoneCloth, "Cloth.")


elif safezoneIndicator == False: 
    totalNoSafeZoneScrap = round(multiAllResources(totalPreSafeZoneScrap, 1.2))
    totalNoSafeZoneHqm = round(multiAllResources(totalPreSafeZoneHqm, 1.2))
    totalNoSafeZoneMetal = round(multiAllResources(totalPreSafeZoneMetal, 1.2))
    totalNoSafeZoneCloth = round(multiAllResources(totalPreSafeZoneCloth, 1.2))

    print("Recycling outside of a Safe Zone, you will get", totalNoSafeZoneScrap, "Scrap", totalNoSafeZoneHqm, "HQM", totalNoSafeZoneMetal, "Metal Frags", totalNoSafeZoneCloth, "Cloth.")
else:
    print("Something went wrong")