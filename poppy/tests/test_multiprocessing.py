#Test functions for poppy multiprocessing

from .. import poppy_core
from .. import optics
from .. import conf

import numpy as np
import astropy.io.fits as fits
import sys

import pytest



@pytest.mark.skipif(
    (sys.version_info < (3, 4)),
    reason="Python 3.4 required for reliable forkserver start method"
)
def test_basic_multiprocessing():
    osys = poppy_core.OpticalSystem("test")
    pupil = optics.CircularAperture(radius=1)
    osys.addPupil(pupil)
    osys.addDetector(pixelscale=0.1, fov_arcsec=5.0) # use a large FOV so we grab essentially all the light and conserve flux

    source={'wavelengths': [1.0e-6, 1.1e-6, 1.2e-6, 1.3e-6], 'weights': [0.25, 0.25, 0.25, 0.25]}
    conf.use_fftw = False

    conf.use_multiprocessing = False
    psf_single = osys.calcPSF(source=source)

    conf.use_multiprocessing = True
    psf_multi = osys.calcPSF(source=source)

    assert np.allclose(psf_single[0].data, psf_multi[0].data), \
        "PSF from multiprocessing does not match PSF from single process"

    return psf_single, psf_multi

