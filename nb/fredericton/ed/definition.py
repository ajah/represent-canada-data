from datetime import date

import boundaries

boundaries.register('Fredericton wards',
    domain='Fredericton, NB',
    last_updated=date(2012, 8, 21),
    name_func=boundaries.attr('WARD'),
    id_func=boundaries.attr('WARD_NUM'),
    authority='City of Fredericton',
    source_url='http://www.fredericton.ca/en/citygovernment/DataMain.asp',
    licence_url='http://www.fredericton.ca/en/citygovernment/TermsOfUse.asp',
    data_url='http://files.fredericton.ca/data/GISData/wards.zip',
    notes='We use NAD83(CSRS) / New Brunswick Stereographic (EPSG:2953) from http://spatialreference.org/ref/epsg/2953/prj/',
    encoding='iso-8859-1',
)
