
# Description: This is a script to calculate the physical space in a CPU taken up by the information in this file.

# First step is to find the number of characters in this file
with open(__file__, 'r') as f:
    num_chars_in_file = len(f.read())

# Next, we need to find the number of bytes in this file
import os
num_bytes_in_file = os.path.getsize(__file__)

# We need some physical dimensions of the CPU to calculate the volume, as well as the number of transistors in the CPU
# For the sake of this example, we will use the Intel Core i9-9900K CPU
# https://en.wikichip.org/wiki/intel/core_i9/i9-9900k
# Physical dimensions: 37.5 mm x 37.5 mm
# from these specs: https://www.techpowerup.com/cpu-specs/core-i9-9900k.c2098
# I see that the actual chip takes up only a fraction of this space

# dimensions of my hand-drawn diagram of the chip:
# chip_width = 4.5  # cm
# chip_height = 6.5  # cm
# total_height = 11 # cm

# diagram_total_area = total_height * total_height
# chip_area = chip_width * chip_height
# chip_area_ratio = chip_area / diagram_total_area
# print(f'Chip area ratio: {chip_area_ratio:.2f}')
# print(f'based on a {total_height} cm x {total_height} cm diagram with chip dimensions {chip_width} x {chip_height} cm')


# approximate the area of the chip on the total packaging as 25% of the total area
chip_area_ratio = 0.25

total_chip_area = 37.5 * 37.5  # mm^2
chip_area = total_chip_area * chip_area_ratio
print(f'Chip area ratio: {chip_area_ratio:.2f}')
print(f'Total chip area: {total_chip_area:.2f} mm^2')
print(f'Chip area: {chip_area:.2f} mm^2')

# approximate the depth of the die
die_depth = 0.8  # mm

# approximate the number of transistors in the CPU
number_of_transistors = 1.e10  # 10 billion transistors
transistor_volume = chip_area * die_depth / number_of_transistors
print(f'Number of transistors: {number_of_transistors:.2e}')

# convert mm^3 to um^3
transistor_volume_um3 = transistor_volume * (1.e3)**3
print(f'Transistor area: {transistor_volume_um3:.2f} um^3')


# damn this is a lot harder than I thought
# because we don't know the actual size of the transistors
# and the layout of the chip architecture to know how many transistors represent X bytes of information


# 2MB cache (L3) per core
# let's assume approximately 25% of each core is cache
core_cache_area_ratio = 0.25
core_chip_area_ratio = (4.7*3) / (24*11)
print(f'Core cache area ratio: {core_cache_area_ratio:.2f}')
print(f'Core chip area ratio: {core_chip_area_ratio:.4f}')

cache_area = core_cache_area_ratio * core_chip_area_ratio * chip_area
print(f'Cache area: {cache_area:.2f} mm^2')
print(f'Therefore {cache_area:.2f} mm^2 of the chip is taken up by 2MB of cache')

mb_per_cache = 2e6  # bytes
mm_area_per_mb = cache_area / mb_per_cache
print(f'{mm_area_per_mb:.9f} mm^2 per byte of cache')
um_area_per_mb = mm_area_per_mb * (1e3)**2
print(f'{um_area_per_mb:.2f} um^2 per byte of cache')

# therefore this file takes up
um_area_taken = um_area_per_mb * num_bytes_in_file
print(f'This file takes up {um_area_taken:.2f} um^2 of cache')
print(f'or it takes up {um_area_taken / 1e6:.7f} mm^2 of cache')
print(f'or it takes up {um_area_taken * 1e6:.2f} nm^2 of cache')

si_to_si_bond_length = .000236 # um

# we can estimate the number of "columns of silicon atoms" taken up per byte and by this file 
# (since we are estimating the area of this chip, not the volume)

# assume cubic silicon atoms
# the area covered by one unit cell is approximately

unit_cell_area = (si_to_si_bond_length) ** 2
print(f'Unit cell area: {unit_cell_area:.2e} um^2')

silicon_unit_cells_per_byte = um_area_per_mb / unit_cell_area
print(f'Number of silicon unit cells per byte: {silicon_unit_cells_per_byte:.2e}')
print(f'{((((um_area_taken * 1e6) ** 0.5) / si_to_si_bond_length / 1000) ** 2):2e}')

