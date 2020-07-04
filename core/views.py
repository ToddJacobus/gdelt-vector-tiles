from django.db import connection
from django.http import Http404, HttpResponse


def mvt_tiles(request, zoom, x, y):
    """custom view to serve mapbox vector tiles for polygon model"""
    with connection.cursor() as cursor:
        cursor.execute(
            f"""
                SELECT ST_AsMVT(tile) 
                FROM (
                        SELECT 
                            id, 
                            ST_AsMVTGeom(
                                geometry, 
                                TileBBox({zoom},{x},{y},4326)
                            ) 
                        FROM 
                            core_point
                     ) AS tile
            """)
        tile = bytes(cursor.fetchone()[0])
        if not len(tile):
            raise Http404()
    return HttpResponse(tile, content_type="application/x-protobuf")