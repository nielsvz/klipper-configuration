# klipper-configuration <!-- omit in toc -->

- [Setup](#setup)
- [Printers](#printers)
  - [Voron 0.1](#voron-01)
  - [Voron 2.4](#voron-24)
    - [Dockable probe (temporary until merged with Klipper)](#dockable-probe-temporary-until-merged-with-klipper)
- [Slicer configuration](#slicer-configuration)
  - [Start gcode](#start-gcode)
  - [End gcode](#end-gcode)
  - [Between extrusion role change G-code](#between-extrusion-role-change-g-code)

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

### Between extrusion role change G-code
SuperSlicer only

Custom variables (Notes tab):
```
square_corner_velocity=8
acc_first_layer=1500
acc_externalperimeter=1000
acc_perimeter=2000
acc_infill_internal=7000
acc_infill_solid=4000
acc_infill_solid_top=2000
acc_infill_bridge=5000
acc_gapfill=2000
acc_skirt=4000
acc_supports=7000
acc_thinwall=2000
acc_default=4040
```

Between extrusion role change G-code (Custom G-code tab):
```
{if layer_num <= 1};Layer [layer_num] FIRST
{if extrusion_role=~/ExternalPerimeter/};[extrusion_role]0
SET_VELOCITY_LIMIT ACCEL=[acc_first_layer] ACCEL_TO_DECEL=[acc_first_layer] SQUARE_CORNER_VELOCITY=[square_corner_velocity]

{elsif extrusion_role=~/Perimeter/};[extrusion_role]
SET_VELOCITY_LIMIT ACCEL=[acc_first_layer] ACCEL_TO_DECEL=[acc_first_layer] SQUARE_CORNER_VELOCITY=[square_corner_velocity]

{else};[extrusion_role]
SET_VELOCITY_LIMIT ACCEL=[acc_first_layer] ACCEL_TO_DECEL=[acc_first_layer] SQUARE_CORNER_VELOCITY=[square_corner_velocity]
{endif}

{else}
{if extrusion_role=~/ExternalPerimeter/};[extrusion_role]0
SET_VELOCITY_LIMIT ACCEL=[acc_externalperimeter] ACCEL_TO_DECEL=[acc_externalperimeter] SQUARE_CORNER_VELOCITY=[square_corner_velocity]

{elsif extrusion_role=~/Perimeter/};[extrusion_role]
SET_VELOCITY_LIMIT ACCEL=[acc_perimeter] ACCEL_TO_DECEL=[acc_perimeter] SQUARE_CORNER_VELOCITY=[square_corner_velocity]

{elsif extrusion_role=~/OverhangPerimeter/};[extrusion_role]
SET_VELOCITY_LIMIT ACCEL=[acc_perimeter] ACCEL_TO_DECEL=[acc_perimeter] SQUARE_CORNER_VELOCITY=[square_corner_velocity]

{elsif extrusion_role=~/InternalInfill/};[extrusion_role]
SET_VELOCITY_LIMIT ACCEL=[acc_infill_internal] ACCEL_TO_DECEL=[acc_infill_internal] SQUARE_CORNER_VELOCITY=[square_corner_velocity]
PAUSE_INFILL EXECUTE=1 EXTRUSION_ROLE=[extrusion_role]

{elsif extrusion_role=~/TopSolidInfill/};[extrusion_role]
SET_VELOCITY_LIMIT ACCEL=[acc_infill_solid_top] ACCEL_TO_DECEL=[acc_infill_solid_top] SQUARE_CORNER_VELOCITY=[square_corner_velocity]

{elsif extrusion_role=~/SolidInfill/};[extrusion_role]
SET_VELOCITY_LIMIT ACCEL=[acc_infill_solid] ACCEL_TO_DECEL=[acc_infill_solid] SQUARE_CORNER_VELOCITY=[square_corner_velocity]

{elsif extrusion_role=~/BridgeInfill/};[extrusion_role]
SET_VELOCITY_LIMIT ACCEL=[acc_infill_bridge] ACCEL_TO_DECEL=[acc_infill_bridge] SQUARE_CORNER_VELOCITY=[square_corner_velocity]

{elsif extrusion_role=~/GapFill/};[extrusion_role]
SET_VELOCITY_LIMIT ACCEL=[acc_gapfill] ACCEL_TO_DECEL=[acc_gapfill] SQUARE_CORNER_VELOCITY=[square_corner_velocity]

{elsif extrusion_role=~/Skirt/};[extrusion_role]
SET_VELOCITY_LIMIT ACCEL=[acc_skirt] ACCEL_TO_DECEL=[acc_skirt] SQUARE_CORNER_VELOCITY=[square_corner_velocity]

{elsif extrusion_role=~/SupportMaterial/};[extrusion_role]
SET_VELOCITY_LIMIT ACCEL=[acc_supports] ACCEL_TO_DECEL=[acc_supports] SQUARE_CORNER_VELOCITY=[square_corner_velocity]

{elsif extrusion_role=~/SupportMaterialInterface/};[extrusion_role]
SET_VELOCITY_LIMIT ACCEL=[acc_supports] ACCEL_TO_DECEL=[acc_supports] SQUARE_CORNER_VELOCITY=[square_corner_velocity]

{elsif extrusion_role=~/ThinWall/};[extrusion_role]
SET_VELOCITY_LIMIT ACCEL=[acc_thinwall] ACCEL_TO_DECEL=[acc_thinwall] SQUARE_CORNER_VELOCITY=[square_corner_velocity]

{else};[extrusion_role]
SET_VELOCITY_LIMIT ACCEL=[acc_default] ACCEL_TO_DECEL=[acc_default] SQUARE_CORNER_VELOCITY=[square_corner_velocity]
{endif}
{endif}
```
