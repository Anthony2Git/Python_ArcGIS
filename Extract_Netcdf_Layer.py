#-------------------------------------------#
# Author: Anthony M, Mwanthi, March 2018
# Purpose: Extract variable from netcdf files 
#          and create raster files
# ------------------------------------------#
#
#Import system modules  
import arcpy  
from arcpy import env  
from arcpy.sa import *  
  
# Input data source
path = "C:\\Work\\DrMutemi\\Evaluation_Runs"
out = "\\raster"	
arcpy.env.workspace = path
arcpy.env.overwriteOutput = True  
      
# Set output folder  
OutputFolder = path + out
            
# Loop through a list of files in the workspace  
# for now I only need a single file
NCfiles = arcpy.ListFiles("gpcp_ond_1997.nc*")  
      
for filename in NCfiles:  
     print("Processing: " + filename)  
     inNCfiles = path + "\\" + filename  
     fileroot = filename[0:(len(filename)-3)]  
     inVariable = "pr"  
     outRaster = OutputFolder + "\\" + fileroot  
    
	# Process: Make NetCDF Raster Layer  
     arcpy.MakeNetCDFRasterLayer_md(inNCfiles, inVariable, "lon", "lat", inVariable, "", "", "BY_VALUE")  
     
    # Process: Copy Raster  
     arcpy.CopyRaster_management(inVariable, outRaster + ".tif", "", "", "", "NONE", "NONE", "")  
         
print arcpy.GetMessages()  