# Calculating Driver Current Settings
When using the 2208 / 2209 drivers, the voltage & current are set in software. In Klipper, the motor currents have two settings: run and hold. Klipper current settings are based on RMS and not on peak. Most motors are specified based on the peak current capacity.

## Calculating Currents
To calculate the maximum Klipper current settings for a given stepper, follow this process:

* Look up the specifications for the stepper motor and locate the peak current limits of the motor.
* Multiply the peak current by 0.707 to determine the maximum current in RMS. This is the maximum run current. (Typically round down to the nearest .1)
* Multiply the maximum run current by 0.6 to determine the hold current. (Typically round to the nearest (0.05)

## Example
The LDO 42STH130-1684 is specified with a maximum current of 1.68 Amps. Maximum run current is 1.68 * .707 = 1.1877, rounded down to a maximum RMS run current of 1.1 Amps. Maximum hold current is 1.1877 * 0.6 = 0.712, rounded to a maximum hold current of 0.7 Amps.

## Maximums
Whatever the maximum calculated current of the motor is, the maximum capacity of the 2209 driver is 1.2 Amps. Also, the calculation is for the maximum the motor can handle. It is recommended to start with smaller values and work from there.

## LDO motor kit for Voron 2.4
| Motor                     | Peak Current | Max Run/RMS Current | Run Current | Hold Current |
|---------------------------|--------------|---------------------|-------------|--------------|
| 42STH20-1004AS (Extruder) | 1.0A         | 0.707A              | 0.5A        | 0.4A         |
| 42STH40-2004MAH (A/B)     | 2.0A         | 1.414A              | 1.1A        | 0.8A         |
| 42STH48-2004AC (Z)        | 2.0A         | 1.414A              | 1.1A        | 0.8A         |
