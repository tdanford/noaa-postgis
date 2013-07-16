import web
import json

DB = web.database(dbn='postgres', db='gis_template')

urls = (
    '/', 'index'
)

class index:
    def GET(self): 
        return json.dumps(find_overlaps('POLYGON((-100.0 30.0, -90.0 30.0, -90.0 20.0, -100.0 20.0, -100.0 30.0))'))

def find_overlaps(wkt_string):
    rows = [dict(x) for x in DB.select('all_geometries', dict(wkt=wkt_string), what='gid,tablename,ST_AsGeoJSON(the_geom)', where='ST_Overlaps(the_geom, ST_GeomFromText($wkt))')]
    for row in rows: 
        row['st_asgeojson'] = json.loads(row['st_asgeojson'])
    return rows

if __name__=='__main__':
	app = web.application(urls, globals())
	app.internalerror = web.debugerror
	app.run()


