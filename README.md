# klipper-configuration <!-- omit in toc -->

- [Setup](#setup)
- [Printers](#printers)
  - [Voron 0.1](#voron-01)
  - [Voron 2.4](#voron-24)
    - [Dockable probe (temporary until merged with Klipper)](#dockable-probe-temporary-until-merged-with-klipper)
- [Slicer configuration](#slicer-configuration)
  - [Start gcode](#start-gcode)
  - [End gcode](#end-gcode)

## Setup

Clone this repository into `~/klipper_config_github`:
```shell
cd
git clone https://github.com/nielsvz/klipper-configuration.git klipper_config_github
```

After cloning the repository make sure to include the main config file into `printer.cfg`:
```shell
echo '[include ../klipper_config_github/voron-2/main.cfg]' > ~/klipper_config/printer.cfg
```

## Printers
### Voron 0.1
Klipper config for Voron 0.1
- SKR E3 Mini V2.0 (4x TMC2209)
- 2x 1.8 degree steppers for A/B (LDO - 40mm nema 14spec for Voron 0.1)
- 1x 1.8 degree stepper for Z (Prusa MK3S Z-motor with integrated leadscrew)
- 1x 1.8 degree stepper for extruder (LDO - 17mm nema 14)

### Voron 2.4
Klipper config for Voron 2.4 
- Spider v1.0
- 7x TMC2209
- 0.9 degree steppers for A/B (LDO)
- 1.8 degree steppers for Z (LDO)
- 1.8 degree stepper for extruder (LDO / Bondtech LGX)

#### Dockable probe (temporary until merged with Klipper)
```shell
cd klipper
# Only add this remote if you haven't done so already.
git remote add mental https://github.com/mental405/klipper.git

# Force update on Klipper and checkout only the dockable_probe module
git fetch --prune --all
git reset --hard origin/master
git checkout mental/work-annex-probe klippy/extras/dockable_probe.py
```

## Slicer configuration

### Start gcode
PrusaSlicer:  
```
M140 S0
M104 S0 ; uncomment to remove set&wait temp gcode added automatically after this start gcode
print_start EXTRUDER_TEMP=[first_layer_temperature] BED_TEMP=[first_layer_bed_temperature] NOZZLE_SIZE=[nozzle_diameter] FILAMENT_TYPE=[filament_type]
```

SuperSlicer:  
```
M190 S0
M109 S0 ; uncomment to remove set&wait temp gcode added automatically after this start gcode
print_start EXTRUDER_TEMP={first_layer_temperature[initial_extruder] + extruder_temperature_offset[initial_extruder]} BED_TEMP=[first_layer_bed_temperature] CHAMBER_TEMP=[chamber_temperature] NOZZLE_SIZE=[nozzle_diameter] FILAMENT_TYPE=[filament_type]
```

### End gcode
PrusaSlicer and SuperSlicer:
```
print_end
```
