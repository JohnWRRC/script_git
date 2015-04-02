import arcpy
from arcpy import env
env.workspace=r'E:\data_2015\Andre_regolin\___john\Sidnei_parte2\saidas_grass_eucdist'
rt=arcpy.ListRasters()

list_c1=[]
list_c4=[]

for i in rt:
    if 'C1' in i :
        list_c1.append(i)
    else:
        list_c4.append(i)


# C1 eucdist
arcpy.env.extent = "623856,87087767 6819548,27655256 830373,27045994 7018924,80061179"
for i in list_c1:
    
    print i
    out=i.replace('.tif','_asc.asc')
    arcpy.conversion.RasterToASCII(i,out)

#c4 euc
arcpy.env.extent = "448417,25364989 6608184,14265736 720291,486295508 6854829,83843274"
for i in list_c4   :
    out=i.replace('.tif','_asc.asc')
    arcpy.conversion.RasterToASCII(i,out)    
    



#c4 var ambientais
list_c4_varamb=[]
env.workspace=r'F:\data\john_pc2\sidnei\Grass\variaveis_amb_saida_grass'
rt=arcpy.ListRasters()
env.workspace=r'E:\data_2015\Andre_regolin\___john\Sidnei_parte2\variaveis_amb_saida_grass_asc_arcgis'
arcpy.env.extent = "448417,25364989 6608184,14265736 720291,486295508 6854829,83843274"
for i in rt:
    if "C4" in i :
        out=i.replace('.tif','_asc.asc')
        arcpy.conversion.RasterToASCII(i,out)        
