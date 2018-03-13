# Extract_By_Mask-RasterConversion.py
#
# Author: Anthony M. Mwanthi, January 2017
# Purpose: 1. Extract raster dataset for a region specified by a shapefile
#          2. Convect raster datasets to points (shapefile)
# 
#Import arcpy module
import arcpy

# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")
arcpy.env.overwriteOutput = True
# Set Geoprocessing environments
arcpy.env.scratchWorkspace = "C:\\Anthony\\V2GRDGHA_PPT_MONTHLY\\Kenya\\ond"
arcpy.env.workspace = "C:\\Anthony\\V2GRDGHA_PPT_MONTHLY\\Kenya\\ond"

# Local variables:
kenya_adm1 = "C:\\Anthony\\V2GRDGHA_PPT_MONTHLY\\kenya_adm1.shp"
Extract_ken = "C:\\Anthony\\V2GRDGHA_PPT_MONTHLY\\Kenya\\"

list = arcpy.ListRasters("*.bil")
arcpy.env.overwriteOutput = True
print list
for img in list:
    "processing " + img
    arcpy.gp.ExtractByMask_sa(img, kenya_adm1, Extract_ken + img + ".tif")
"all files processed"

#..................convert raster to points ...................................
import arcpy
# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")
arcpy.env.overwriteOutput = True
ken_points = "C:\\Anthony\\V2GRDGHA_PPT_MONTHLY\\Kenya\\ond\\points"
arcpy.env.workspace = "C:\\Anthony\\V2GRDGHA_PPT_MONTHLY\\Kenya"
list = arcpy.ListRasters("*")
print list
for im in list:
    "processing " + im
    arcpy.RasterToPoint_conversion(im, ken_points + im, "VALUE")

#.....................end of the script
