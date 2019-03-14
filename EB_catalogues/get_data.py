# This script is reading in data from various papers to create one big table

import numpy as np
from astropy.coordinates import Angle
from astropy.table import Table
import astropy.units as u

# EBLM project single line EBs, Triaud et al 2017
# Periods and coordinates in T6, magnitudes and spectral type in T4
tableD = Table.read('https://www.aanda.org/articles/aa/full_html/2017/12/aa30993-17/T6.html',
                    format='html', data_start=4, header_start=1)

# Ugly hack to work around UTF – character
tableD['dec'] = Angle(["-{}".format(i.split('–')[1]) if len(i.split('–')) > 1
                       else "{}".format(i) for i in tableD['dec']], unit=u.deg)
tableD['RA'] = Angle(tableD['RA'], unit=u.hourangle)

# Filter out the Northern, long period ones
targets_triaud17 = tableD[np.logical_and(tableD['dec'] > -30, tableD['P'] > 5)]
