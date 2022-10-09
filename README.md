# klipper-configuration <!-- omit in toc -->

- [Setup](#setup)
- [Printers](#printers)
  - [Voron 2.4](#voron-24)
    - [Dockable probe (temporary until merged with Klipper)](#dockable-probe-temporary-until-merged-with-klipper)
- [Slicer configuration](#slicer-configuration)
  - [Start gcode](#start-gcode)
  - [End gcode](#end-gcode)

## Setup

Clone this repository into `~/klipper_config_github`:
```shell
cd ~/klipper_config
git clone https://github.com/nielsvz/klipper-configuration.git github
```

After cloning the repository make sure to include the main config file into `printer.cfg`:
```shell
echo '[include ../klipper_config/github/voron-2/main.cfg]' > ~/klipper_config/printer.cfg
```

## Printers

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
PRINT_START EXTRUDER_TEMP=[first_layer_temperature] BED_TEMP=[first_layer_bed_temperature] NOZZLE_SIZE=[nozzle_diameter] FILAMENT_TYPE=[filament_type] BED_MESH=0
```

SuperSlicer:  
```
M190 S0
M109 S0
PRINT_START EXTRUDER_TEMP={first_layer_temperature[initial_extruder] + extruder_temperature_offset[initial_extruder]} BED_TEMP=[first_layer_bed_temperature] CHAMBER_TEMP=[chamber_temperature] NOZZLE_SIZE=[nozzle_diameter] FILAMENT_TYPE=[filament_type] BED_MESH=0
```

Cura 5.0:
```
PRINT_START EXTRUDER_TEMP={material_print_temperature_layer_0} BED_TEMP={material_bed_temperature_layer_0} NOZZLE_SIZE={machine_nozzle_size} FILAMENT_TYPE={material_type} CHAMBER={build_volume_temperature} BED_MESH=0
```

IdeaMaker
```
M104 S0
M140 S0
PRINT_START EXTRUDER_TEMP={temperature_extruder1} BED_TEMP={temperature_heatbed} NOZZLE_SIZE={machine_nozzle_diameter1} FILAMENT_TYPE={filament_name_abbreviation1} BED_MESH=0
```

### End gcode
Any slicer:
```
PRINT_END
```
