#coding: utf-8
from datetime import date

import boundaries

boundaries.register(u'Québec boroughs',
    domain=u'Québec, QC',
    last_updated=date(2012, 2, 16),
    name_func=boundaries.clean_attr('NOM'),
    id_func=boundaries.attr('CODE'),
    authority=u'Ville de Québec',
    source_url='http://donnees.ville.quebec.qc.ca/donne_details.aspx?jdid=2',
    licence_url='http://donnees.ville.quebec.qc.ca/licence.aspx',
    notes='Convert the features to 2D with: ogr2ogr -f "ESRI Shapefile" -overwrite . ARROND.shp -nlt POLYGON. We use WGS 84 (EPSG:4326) from http://spatialreference.org/ref/epsg/4326/prj/',
    encoding='iso-8859-1',
)
