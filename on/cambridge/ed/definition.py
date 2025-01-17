from datetime import date

import boundaries

boundaries.register('Cambridge wards',
    domain='Cambridge, ON',
    last_updated=date(2012, 5, 29),
    name_func=lambda f: 'Ward %s' % f.get('WARD_ID'),
    id_func=boundaries.attr('WARD_ID'),
    authority='City of Cambridge',
    notes='We use a shapefile received via email.',
    encoding='iso-8859-1',
)
