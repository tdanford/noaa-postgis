#!/bin/bash

## this requires the existence of a tables.txt file in the same directory, which contains
## (listed out on different lines) the names of all the geometry tables in the db.

psql -d gis_template -c "CREATE TABLE all_geometries ( gid integer, tablename varchar(100), the_geom geometry );"

for table in `cat tables.txt`; do 
	psql -d gis_template -c "insert into all_geometries select gid, '${table}' as tablename, the_geom from ${table} ;" ; 
done 

psql -d gis_template -c "SELECT Populate_Geometry_Columns();"

