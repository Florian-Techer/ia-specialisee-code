from lifxlan import LifxLAN
# Init
num_lights = None

lifx = LifxLAN(num_lights)

lifx.get_power_all_lights()

# Allumer
# lifx.set_power_all_lights("on")


# Eteindre
lifx.set_power_all_lights("off")