# Script reads input shaper csv file and computes damping ratio as (f2 - f1) / (2 * f0) where f0 is the peak psd_xyz amplitude frequency and f1 and f2 are the frequencies at which the amplitude is 1/sqrt(2) of the peak amplitude.
# CSV columns:
# freq, psd_x, psd_y, psd_z, psd_xyz

import sys
import numpy as np
import pandas as pd
import scipy.interpolate as interpolate


# Read input file
if len(sys.argv) < 2:
    print("Usage: %s <input file>" % sys.argv[0])
    sys.exit(1)

input_file = sys.argv[1]
df = pd.read_csv(input_file, sep=',', header=0, names=['freq', 'psd_x', 'psd_y', 'psd_z', 'psd_xyz'])

peak_amplitude = df['psd_xyz'].max()
peak_freq = df['freq'][df['psd_xyz'].idxmax()]
f_ampl = peak_amplitude / np.sqrt(2)

# Interpolate psd_xyz to find frequency at which psd_xyz is 1/sqrt(2) of peak amplitude on both sides of peak frequency
f1 = interpolate.interp1d(df['psd_xyz'][df['freq'] < peak_freq], df['freq'][df['freq'] < peak_freq])(f_ampl)
f2 = interpolate.interp1d(df['psd_xyz'][df['freq'] > peak_freq], df['freq'][df['freq'] > peak_freq])(f_ampl)

# Compute damping ratio
damping_ratio = (f2 - f1) / (2 * peak_freq)

print("Peak frequency: %f" % peak_freq)
print("Damping ratio: %f" % damping_ratio)
