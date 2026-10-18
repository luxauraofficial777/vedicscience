#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv, json, os, re

STUDY = r'C:\LuxAura\study'
OUT = os.path.join(STUDY, 'OpenCodeBP', 'outputs', 'claims_part3.csv')
C_LIGHT = 2.99792458e10
HC_EV_CM = 1.239841984e-4

rows = []
counts = {}

def add(cid, fname, line, text, band='', qn='', val='', unit='', fhz='', eev='', cls='', ved=''):
    text = text.replace('"', "'").replace('\r', '').replace('\n', ' ').strip()
    if len(text) > 200: text = text[:197] + '...'
    rows.append(dict(claim_id=cid, file=fname, line=line, text=text, band=band,
        quantity=qn, value=val, unit=unit, freq_Hz=fhz, energy_eV=eev,
        claimed_class=cls, vedic_link=ved))

def c2h(c): return f'{float(c)*C_LIGHT:.6g}'
def c2e(c): return f'{float(c)*HC_EV_CM:.6g}'

def read_lines(fname):
    return open(os.path.join(STUDY, fname), encoding='utf-8', errors='ignore').read().splitlines()

# ===================== IDEAS_RESEARCH_BRIEF.md =====================
F = 'IDEAS_RESEARCH_BRIEF.md'
L = read_lines(F); idx = 0
def idea(ln, qn, val, unit='', fhz='', eev='', cls='literature'):
    global idx; idx += 1
    add(f'IDEAS-{idx:03d}', F, ln, L[ln-1], '', qn, val, unit, fhz, eev, cls)

idea(28, 'fine_structure_constant', '1/137', cls='literature')
idea(28, 'fine_structure_constant', '1/128', cls='literature')
idea(30, 'spatial_variation_sigma', '4.2', 'sigma')
idea(30, 'alpha_variation_amplitude', '1.02', 'e-5')
idea(30, 'alpha_variation_uncertainty', '0.21', 'e-5')
idea(31, 'formation_pressure', '113', 'GPa')
idea(31, 'transparency_pressure', '200', 'GPa')
idea(36, 'equivalence_parameter', '-3', 'e-14')
idea(36, 'equivalence_uncertainty', '5', 'e-14')
idea(37, 'equivalence_parameter', '-1.5', 'e-15')
idea(37, 'equivalence_uncertainty', '2.3', 'e-15')
idea(37, 'equivalence_bound', '1e-15', '')
idea(48, 'temperature', '5000', 'K')
idea(49, 'vibrational_wavenumber', '860', 'cm^-1', c2h(860), c2e(860))
idea(49, 'rate_slowdown_factor', '5.5', 'x')
idea(62, 'sound_carried_mass', '0.1', 'mg')
idea(63, 'travel_speed', '3.5', 'km/s', '3500', '')
idea(64, 'distance_range', '500-3000', 'km')
idea(79, 'frequency', '0.8146566', 'mHz', '814.6566', '')
idea(80, 'frequency', '7.8', 'Hz', '7.8', '')
idea(81, 'period', '5.9', 'yr')
idea(95, 'electric_potential', '0.55', 'V')
idea(95, 'altitude', '322', 'miles')
idea(95, 'scale_height_increase', '271', '%')
idea(95, 'force_ratio', '10.6', 'x g')
idea(100, 'turbopause_altitude', '100', 'km')
idea(108, 'tidal_agreement', '0.3-1', '%')
idea(108, 'G_drift_rate', '7.1', 'e-14/yr')
idea(108, 'G_drift_uncertainty', '7.6', 'e-14/yr')
idea(135, 'coupling_bound', '1e-13-1e-15', '')
idea(142, 'earthquake_mass', '1e11', 'kg')
idea(159, 'test_cost', '2000', 'USD')
idea(160, 'frequency', '20-400', 'kHz', '20000-400000', '')
idea(160, 'detector_wavelength', '355', 'nm', '8.447e14', '')
counts[F] = idx

# ===================== ASTRA_COMPARATIVE_BRIEF.md =====================
F = 'ASTRA_COMPARATIVE_BRIEF.md'
L = read_lines(F); idx = 0
def astra(ln, qn, val, unit='', fhz='', eev='', cls='reference', ved=''):
    global idx; idx += 1
    add(f'ASTR-{idx:03d}', F, ln, L[ln-1], '', qn, val, unit, fhz, eev, cls, ved)

astra(22, 'shock_pressure', '100', 'MPa', cls='reference')
astra(32, 'strain', '1.5', 'e-4', cls='hypothesis', ved='Vajra')
astra(32, 'modulus_reduction', '77', '%', cls='hypothesis', ved='Vajra')
astra(32, 'shock_pressure', '100', 'MPa', cls='literature', ved='Vajra')
astra(32, 'focus_size', '4-8', 'mm', cls='literature', ved='Vajra')
astra(32, 'power_density', '4-7', 'MW/m^3', cls='derived', ved='Vajra')
astra(32, 'frequency', '100-250', 'Hz', '100-250', cls='derived', ved='Vajra')
astra(32, 'frequency', '20950', 'Hz', '20950', cls='hypothesis', ved='Vajra')
astra(32, 'frequency_glide', '25', '%', cls='derived', ved='Vajra')
astra(33, 'Mach_number', '5-8', cls='hypothesis', ved='Brahmastra')
astra(33, 'overpressure', '3.46', 'MPa', cls='derived', ved='Brahmastra')
astra(33, 'overpressure', '34', 'atm', cls='derived', ved='Brahmastra')
astra(33, 'overpressure_doc_value', '3.41', 'MPa', cls='reference', ved='Brahmastra')
astra(33, 'duration', '12', 'yr', cls='literature', ved='Brahmastra')
astra(35, 'damping_ratio', '0.035', cls='computed', ved='Narayanastra')
astra(35, 'Q_factor', '29', cls='computed', ved='Narayanastra')
astra(35, 'Q_squared', '800', cls='computed', ved='Narayanastra')
astra(35, 'stress_growth_exponent', '10^3-10^4', cls='hypothesis', ved='Narayanastra')
astra(35, 'target_speed', '2', 'm/s', cls='derived', ved='Narayanastra')
astra(35, 'carrier_frequency', '21', 'kHz', '21000', cls='derived', ved='Narayanastra')
astra(35, 'doppler_shift', '122', 'Hz', '122', cls='derived', ved='Narayanastra')
astra(35, 'resonance_half_width', '356', 'Hz', '356', cls='derived', ved='Narayanastra')
astra(37, 'sound_level', '145-165', 'dB', cls='hypothesis', ved='Sammohana')
astra(37, 'frequency', '6-12', 'Hz', '6-12', cls='hypothesis', ved='Sammohana')
astra(37, 'beat_frequency', '7', 'Hz', '7', cls='hypothesis', ved='Sammohana')
astra(37, 'carrier_frequency', '40000', 'Hz', '40000', cls='hypothesis', ved='Sammohana')
astra(37, 'carrier_frequency', '40007', 'Hz', '40007', cls='hypothesis', ved='Sammohana')
astra(37, 'power_loss', '86', 'dB', cls='derived', ved='Sammohana')
astra(37, 'source_range', '50', 'm', cls='literature', ved='Sammohana')
astra(38, 'angular_resolution', '1', 'deg', cls='literature', ved='Abdavedhi')
astra(55, 'energy_density', '1', 'MW/m^3', cls='reference')
astra(56, 'overpressure', '34', 'atm', cls='reference')
astra(79, 'overpressure', '3.46', 'MPa', cls='derived')
astra(81, 'Q_inverse', '1', cls='reference')
astra(96, 'syllable_count', '24', cls='literature')
astra(96, 'syllable_count', '44', cls='literature')
astra(105, 'frequency_glide', '25', '%', cls='hypothesis')
astra(105, 'semitone_glide', '5', 'semitones', cls='hypothesis')
astra(105, 'strain', '1.5', 'e-4', cls='hypothesis')
astra(119, 'test_cost', '500-1500', 'USD')
astra(123, 'falloff_rate', '12', 'dB/octave', cls='reference')
astra(129, 'energy_density', '35', 'MJ/m^3', cls='reference')
astra(129, 'energy_density', '16.8', 'MJ/m^3', cls='reference')
astra(134, 'target_speed_sweep', '0-10', 'm/s', cls='computed')
astra(134, 'stress_growth_exponent', '10^3-10^4', cls='hypothesis')
counts[F] = idx

# ===================== Standard_Dislocation_Tunneling_Reference.md =====================
F = 'Standard_Dislocation_Tunneling_Reference.md'
L = read_lines(F); idx = 0
def sdtr(ln, qn, val, unit='', fhz='', eev='', cls='house standard'):
    global idx; idx += 1
    add(f'SDTR-{idx:03d}', F, ln, L[ln-1], '', qn, val, unit, fhz, eev, cls)

sdtr(39, 'tau_0', '0.53', 'ps', '5.3e-13')
sdtr(39, 'frequency', '20-100', 'kHz', '20000-100000')
sdtr(41, 'adiabaticity_parameter', '1e-7', cls='house standard')
sdtr(43, 'acoustic_period', '10-50', 'us')
sdtr(43, 'traversal_time', '0.5-2', 'ps', '5e-13-2e-12')
sdtr(50, 'viscous_drag', '5e-4', 'Pa*s')
sdtr(50, 'temperature_threshold', '1-10', 'K')
sdtr(69, 'burgers_vector', '2.5', 'Angstrom')
sdtr(69, 'peierls_period', '2.5', 'Angstrom')
sdtr(70, 'shear_modulus', '30', 'GPa')
sdtr(70, 'density', '2850', 'kg/m^3')
sdtr(70, 'shear_wave_speed', '3244.4', 'm/s')
sdtr(71, 'peierls_stress', '50', 'MPa')
sdtr(71, 'attempt_frequency', '1e12', 'Hz', '1e12')
sdtr(72, 'S_0_over_hbar', '196.59')
sdtr(72, 'tau_0', '0.5324', 'ps', '5.324e-13')
sdtr(78, 'S_B_over_hbar', '82.656')
sdtr(78, 'log10_tunneling_rate', '-168.09')
sdtr(83, 'S_B_over_hbar', '11.057')
sdtr(83, 'log10_tunneling_rate', '-44.27')
sdtr(88, 'S_B_over_hbar', '0.262')
sdtr(88, 'log10_tunneling_rate', '-4.28')
sdtr(90, 'frequency', '25', 'kHz', '25000')
sdtr(90, 'Q_0', '2500')
sdtr(94, 'temperature', '4', 'K')
sdtr(94, 'Q_eff', '2422.5')
sdtr(94, 'ring_down_time', '15.422', 'ms')
sdtr(94, 'thermal_occupation', '3.334e6')
sdtr(96, 'temperature', '77', 'K')
sdtr(96, 'Q_eff', '1599.3')
sdtr(96, 'ring_down_time', '10.181', 'ms')
sdtr(96, 'thermal_occupation', '6.418e7')
sdtr(98, 'temperature', '300', 'K')
sdtr(98, 'Q_eff', '735.3')
sdtr(98, 'ring_down_time', '4.681', 'ms')
sdtr(98, 'thermal_occupation', '2.5e8')
counts[F] = idx

# ===================== Standard_Mineral_Spectroscopy_Acoustics_Reference.md =====================
F = 'Standard_Mineral_Spectroscopy_Acoustics_Reference.md'
L = read_lines(F); idx = 0
def smsr(ln, qn, val, unit='', fhz='', eev='', cls='house standard'):
    global idx; idx += 1
    add(f'SMSR-{idx:03d}', F, ln, L[ln-1], '', qn, val, unit, fhz, eev, cls)

bonds_md = [
    (19, 'Si-O', 10.193, 595.0, 995.4, 1000.0, 29.84),
    (20, 'Si-O-Si', 10.193, 128.0, 461.7, 464.0, 13.84),
    (21, 'Al-O', 10.044, 310.0, 723.8, 725.0, 21.70),
    (22, 'Mg-O', 9.648, 145.0, 505.1, 502.0, 15.14),
    (23, 'Fe-O', 12.436, 135.0, 429.2, 432.0, 12.87),
    (24, 'O-H', 0.948, 730.0, 3614.7, 3625.0, 108.37),
]
for ln, name, mu, k, calc, obs, thz in bonds_md:
    smsr(ln, 'k_force_constant', str(k), 'N/m')

# Raman minerals - dominant peaks only (bolded in source)
for ln, cm in [(31,464),(33,509),(35,666),(35,1010),(37,824),(37,856)]:
    smsr(ln, 'Raman_peak', str(cm), 'cm^-1', c2h(cm), c2e(cm))

smsr(43, 'piezoelectric_d11', '2.31', 'pC/N')
smsr(44, 'permittivity', '4.52')
smsr(45, 'piezoelectric_g11', '0.0577', 'V*m/N')
for ln, (s, q, v, e) in {
    49: (0.10, 0.231, 11.55, 0.667),
    52: (2.50, 5.775, 288.70, 416.742),
    56: (50.00, 115.500, 5773.96, 166696.849),
}.items():
    smsr(ln, 'piezoelectric_stress', str(s), 'MPa')
    smsr(ln, 'open_circuit_voltage', str(v), 'V')

smsr(61, 'bubble_radius', '5.0', 'um')
smsr(61, 'frequency', '20.0', 'kHz', '20000')
smsr(61, 'acoustic_pressure', '1.15', 'bar')
smsr(62, 'expansion_ratio', '4.2238')
smsr(63, 'compression_ratio', '0.4337')
smsr(64, 'collapse_speed', '39.75', 'm/s')
counts[F] = idx

# ===================== quantum_dislocation_tunneling_data.json =====================
F = 'quantum_dislocation_tunneling_data.json'
raw = read_lines(F); idx = 0
data = json.loads('\n'.join(raw))

def jfind(key, occ=0):
    n = -1
    for i, ln in enumerate(raw, 1):
        if f'"{key}"' in ln:
            n += 1
            if n == occ: return i
    return 0

def jq(ln, qn, val, unit='', fhz='', eev='', cls='computed'):
    global idx; idx += 1
    txt = raw[ln-1].strip() if 0 < ln <= len(raw) else ''
    add(f'JQD-{idx:03d}', F, ln, txt, '', qn, val, unit, fhz, eev, cls)

jq(jfind('S_0_over_hbar'), 'S_0_over_hbar', '196.59')
jq(jfind('tau_0_ps'), 'tau_0', '0.5324', 'ps', '5.324e-13')
jq(jfind('c_s_m_s'), 'shear_wave_speed', '3244.4', 'm/s')
for k, e in enumerate(data['petukhov_pokrovskii']['table']):
    ln = jfind('epsilon', k)
    idx += 1
    add(f'JQD-{idx:03d}', F, ln,
        f"epsilon={e['epsilon']}: S_B/hbar={e['S_B_over_hbar']}, tau_BL={e['tau_BL_ps']}ps, log10 assisted={e['log10_WKB_assisted']}",
        '', 'epsilon', e['epsilon'], '', '', '', 'computed')
for k, e in enumerate(data['glauber_decoherence']):
    ln = jfind('T_K', k)
    idx += 1
    add(f'JQD-{idx:03d}', F, ln,
        f"T={e['T_K']}K: Q_eff={e['Q_eff']}, tau_coh={e['tau_coh_ms']}ms, n_th={e['n_thermal_phonons']}",
        '', 'Q_eff', e['Q_eff'], '', '', '', 'computed')
counts[F] = idx

# ===================== standard_mineral_acoustics_data.json =====================
F = 'standard_mineral_acoustics_data.json'
raw = read_lines(F); idx = 0
data = json.loads('\n'.join(raw))

def jline_of(s):
    for i, ln in enumerate(raw, 1):
        if s in ln: return i
    return 0

def jma(ln, text, qn, val, unit='', fhz='', eev='', cls='reference'):
    global idx; idx += 1
    add(f'JMA-{idx:03d}', F, ln, text, '', qn, val, unit, fhz, eev, cls)

# bonds
for b in data['bonds']:
    short = b['bond'].split('(')[0].strip()[:4].rstrip(' \u2013-')
    ln = jline_of(short[:3])
    jma(ln, f"{b['bond']}: k={b['k_N_m']}N/m, mu={b['mu_amu']}amu, calc={b['calc_cm1']}cm-1, obs={b['obs_cm1']}cm-1, f={b['freq_THz']}THz",
        'k_force_constant', b['k_N_m'], 'N/m', str(b['freq_THz']*1e12), c2e(b['obs_cm1']))

# raman peaks - capture each mineral's primary peaks
# quartz
for cm in [464]:  # dominant
    ln = jline_of('Alpha-Quartz')
    jma(ln, f'Alpha-Quartz Raman_peak={cm}', 'Raman_peak', cm, 'cm^-1', c2h(cm), c2e(cm))
# plagioclase
ln = jline_of('Plagioclase')
jma(ln, f'Plagioclase Feldspar Raman_peak=509', 'Raman_peak', 509, 'cm^-1', c2h(509), c2e(509))
# clinopyroxene
ln = jline_of('Clinopyroxene')
jma(ln, f'Clinopyroxene Raman_peak=666', 'Raman_peak', 666, 'cm^-1', c2h(666), c2e(666))
# forsterite
ln = jline_of('Forsterite')
jma(ln, f'Forsterite Raman_peak=824', 'Raman_peak', 824, 'cm^-1', c2h(824), c2e(824))
ln = jline_of('Forsterite')
jma(ln, f'Forsterite Raman_peak=856', 'Raman_peak', 856, 'cm^-1', c2h(856), c2e(856))

# rayleigh_plesset summary
rp = data['rayleigh_plesset']
for key, qn, unit, fmul in [
    ('R0_um', 'bubble_radius', 'um', 0), ('f_kHz', 'frequency', 'kHz', 1e7),
    ('P_ac_bar', 'acoustic_pressure', 'bar', 0), ('max_R_over_R0', 'expansion_ratio', '', 0),
    ('min_R_over_R0', 'compression_ratio', '', 0), ('max_collapse_speed_m_s', 'collapse_speed', 'm/s', 0),
]:
    ln = jline_of(f'"{key}"')
    val = rp[key]
    jma(ln, f'rayleigh_plesset {key}: {val} {unit}', qn, val, unit,
        str(val*fmul) if fmul else '', '', 'computed')

# piezo constants
pz = data['piezo']
for key, qn, unit in [('d_11_pC_N','piezoelectric_d11','pC/N'),('g_11_Vm_N','piezoelectric_g11','V*m/N'),('eps_r','permittivity',''),('thickness_mm','plate_thickness','mm')]:
    ln = jline_of(f'"{key}"')
    jma(ln, f'piezo {key}: {pz[key]} {unit}', qn, pz[key], unit)

# piezo table - key values
occ = -1
for i, l in enumerate(raw, 1):
    if '"stress_MPa"' in l:
        occ += 1
        if occ not in [0,2,7]: continue  # 0.1, 2.5, 50.0 MPa
        t = pz['table'][occ]
        jma(i, f"stress={t['stress_MPa']}MPa: charge={t['charge_uC_m2']}uC/m2, V={t['open_circuit_V']}V, energy={t['elec_energy_mJ_m3']}mJ/m3",
            'piezoelectric_stress', t['stress_MPa'], 'MPa', '', '', 'computed')
counts[F] = idx

# ===================== verify_convergence_integral.py =====================
F = 'verify_convergence_integral.py'
L = read_lines(F); idx = 0
def vc(ln, qn, val, unit='', fhz='', eev='', cls='computed'):
    global idx; idx += 1
    add(f'VC-{idx:03d}', F, ln, L[ln-1], '', qn, val, unit, fhz, eev, cls)

vc(5, 'model_name', 'Delta_T_drift', cls='hypothesis')
vc(45, 'boundary_layer_thickness', '5.52e-4', 'm', cls='verified')
vc(45, 'frequency', '34.4', 'Hz', '34.4', cls='verified')
vc(46, 'critical_shear_threshold', '1500', 'Pa', cls='verified')
vc(47, 'crossover_gradient', '2.717e9', 'Pa/m', cls='computed')
vc(79, 'boundary_layer_thickness', '0.552', 'mm', cls='computed')
counts[F] = idx

# ===================== verify_metamaterial_and_hugoniot.py =====================
F = 'verify_metamaterial_and_hugoniot.py'
L = read_lines(F); idx = 0
def vm(ln, qn, val, unit='', fhz='', eev='', cls='computed'):
    global idx; idx += 1
    add(f'VM-{idx:03d}', F, ln, L[ln-1], '', qn, val, unit, fhz, eev, cls)

vm(8, 'stagnation_pressure', '7.48', 'GPa', cls='hypothesis')
vm(9, 'water_hammer_pressure', '3.25', 'GPa', cls='hypothesis')
vm(19, 'bulk_modulus', '50.0', 'GPa', cls='verified')
vm(20, 'density', '2850.0', 'kg/m^3', cls='verified')
vm(21, 'alpha_G', '2500.0', cls='verified')
vm(22, 'delta_G', '-4.0e6', 'Pa', cls='verified')
vm(23, 'eps_th', '1.0e-6', cls='verified')
vm(24, 'eps_ac', '1.5e-4', cls='verified')
vm(31, 'monopolar_resonance', '28000', 'Hz', '28000', cls='verified')
vm(33, 'coupling_strength', '0.35', cls='verified')
vm(34, 'damping_ratio', '0.035', cls='verified')
vm(36, 'dipolar_resonance', '27200', 'Hz', '27200', cls='verified')
vm(38, 'coupling_strength', '0.30', cls='verified')
vm(87, 'density', '998.0', 'kg/m^3', cls='verified')
vm(88, 'sound_speed', '1484.0', 'm/s', cls='verified')
vm(89, 'hugoniot_slope', '1.979', cls='verified')
vm(90, 'acoustic_impedance', '16.5e6', 'Rayl', cls='verified')
vm(98, 'concentration_factor', '25.085', cls='verified')
vm(96, 'jet_velocity', '2196', 'm/s', cls='computed')
vm(96, 'stagnation_pressure_matched', '7.48', 'GPa', cls='computed')
vm(96, 'stagnation_pressure_rigid', '12.78', 'GPa', cls='computed')
vm(96, 'water_hammer_linear', '3.25', 'GPa', cls='computed')
counts[F] = idx

# ===================== verify_quantum_resonance.py =====================
F = 'verify_quantum_resonance.py'
L = read_lines(F); idx = 0
def vq(ln, qn, val, unit='', fhz='', eev='', cls='computed'):
    global idx; idx += 1
    add(f'VQ-{idx:03d}', F, ln, L[ln-1], '', qn, val, unit, fhz, eev, cls)

vq(23, 'HBAR', '1.054571817e-34', 'J*s', cls='verified')
vq(24, 'KB', '1.380649e-23', 'J/K', cls='verified')
vq(40, 'burgers_vector', '2.50e-10', 'm', cls='verified')
vq(41, 'peierls_period', '2.50e-10', 'm', cls='verified')
vq(42, 'shear_modulus', '30.0', 'GPa', cls='verified')
vq(43, 'density', '2850.0', 'kg/m^3', cls='verified')
vq(44, 'shear_wave_speed', '3244.4', 'm/s', cls='computed')
vq(50, 'peierls_stress', '50', 'MPa', cls='verified')
vq(54, 'C_PP', '18.96', cls='verified')
vq(56, 'S_0_over_hbar', '196.59', cls='computed')
vq(59, 'tau_0', '0.5324', 'ps', '5.324e-13', cls='computed')
vq(63, 'eta_low', '1.0e-5', 'Pa*s', cls='verified')
vq(64, 'eta_high', '5.0e-4', 'Pa*s', cls='verified')
vq(66, 'acoustic_frequency', '1.0e10', 'Hz', '1e10', cls='verified')
vq(67, 'sigma_ac_ratio', '0.02', cls='verified')
vq(122, 'mode_frequency', '25000', 'Hz', '25000', cls='verified')
vq(125, 'Q_0', '2500.0', cls='verified')
vq(130, 'Q_eff_model', 'Q_0/(1+0.008*T)', cls='computed')
counts[F] = idx

# ===================== sim_cavity_acoustics.py =====================
F = 'sim_cavity_acoustics.py'
L = read_lines(F); idx = 0
def scp(ln, qn, val, unit='', fhz='', eev='', cls='computed'):
    global idx; idx += 1
    add(f'SC-{idx:03d}', F, ln, L[ln-1], '', qn, val, unit, fhz, eev, cls)

scp(8, 'fundamental_frequency', '34.4', 'Hz', '34.4', cls='verified')
scp(18, 'cavity_length', '5.0', 'm', cls='verified')
scp(18, 'cavity_width', '3.0', 'm', cls='verified')
scp(18, 'cavity_height', '2.5', 'm', cls='verified')
scp(19, 'air_density', '1.204', 'kg/m^3', cls='verified')
scp(19, 'sound_speed_air', '344.0', 'm/s', cls='verified')
scp(19, 'kinematic_viscosity', '1.516e-5', 'm^2/s', cls='verified')
scp(19, 'Prandtl_number', '0.713', cls='verified')
scp(19, 'adiabatic_index', '1.40', cls='verified')
scp(20, 'basalt_density', '2850.0', 'kg/m^3', cls='verified')
scp(20, 'shear_modulus', '30.0', 'GPa', cls='verified')
scp(20, 'bulk_modulus', '50.0', 'GPa', cls='verified')
scp(21, 'alpha_G', '2500.0', cls='verified')
scp(21, 'delta_G', '-4.0e6', 'Pa', cls='verified')
scp(21, 'eps_th', '1.0e-6', cls='verified')
scp(22, 'eps_ac', '1.5e-4', cls='verified')
scp(22, 'P_antinode', '2500.0', 'Pa', cls='verified')
scp(40, 'eigenmode', '(1,0,0)', fhz='34.4', cls='computed')
scp(41, 'eigenmode', '(2,0,0)', fhz='68.8', cls='computed')
scp(42, 'eigenmode', '(3,0,0)', fhz='103.2', cls='computed')
scp(43, 'eigenmode', '(1,1,0)', fhz='42.9', cls='computed')
scp(44, 'eigenmode', '(1,1,1)', fhz='46.2', cls='computed')
scp(90, 'G_eff', 'G_0*S_backbone', 'GPa', cls='computed')
scp(92, 'c_p_eff', 'sqrt(M_eff/rho_s)', 'm/s', cls='computed')
scp(93, 'Z_wall', 'rho_s*c_p_eff', 'MRayl', cls='computed')
counts[F] = idx

# ===================== sim_cavity_acoustics.cpp =====================
F = 'sim_cavity_acoustics.cpp'
L = read_lines(F)
# continue SC- numbering from py file
def scc(ln, qn, val, unit='', fhz='', eev='', cls='computed'):
    global idx; idx += 1
    add(f'SC-{idx:03d}', F, ln, L[ln-1], '', qn, val, unit, fhz, eev, cls)

scc(6, 'fundamental_frequency', '34.4', 'Hz', '34.4', cls='verified')
scc(24, 'cavity_length', '5.0', 'm', cls='verified')
scc(25, 'cavity_width', '3.0', 'm', cls='verified')
scc(26, 'cavity_height', '2.5', 'm', cls='verified')
scc(29, 'air_density', '1.204', 'kg/m^3', cls='verified')
scc(30, 'sound_speed_air', '344.0', 'm/s', '34.4', cls='verified')
scc(31, 'kinematic_viscosity', '1.516e-5', 'm^2/s', cls='verified')
scc(32, 'Prandtl_number', '0.713', cls='verified')
scc(33, 'adiabatic_index', '1.400', cls='verified')
scc(36, 'basalt_density', '2850.0', 'kg/m^3', cls='verified')
scc(37, 'shear_modulus', '30.0', 'GPa', cls='verified')
scc(38, 'bulk_modulus', '50.0', 'GPa', cls='verified')
scc(39, 'alpha_G', '2500.0', cls='verified')
scc(40, 'delta_G', '-4.0e6', 'Pa', cls='verified')
scc(41, 'eps_th', '1.0e-6', cls='verified')
scc(86, 'residual_softening_floor', '0.05', cls='verified')
scc(104, 'CFL_number', '0.5', cls='verified')
scc(185, 'drive_frequency', '34.4', 'Hz', '34.4', cls='computed')
scc(185, 'source_pressure', '2000.0', 'Pa', cls='computed')
scc(185, 'eps_ac', '1.5e-4', cls='verified')
_py_count = counts.get('sim_cavity_acoustics.py', 0)
counts[F] = idx - _py_count

# ===================== WRITE CSV =====================
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['claim_id','file','line','text','band','quantity','value','unit','freq_Hz','energy_eV','claimed_class','vedic_link'])
    w.writeheader()
    for r in rows: w.writerow(r)

order = ['IDEAS_RESEARCH_BRIEF.md','ASTRA_COMPARATIVE_BRIEF.md',
         'Standard_Dislocation_Tunneling_Reference.md','Standard_Mineral_Spectroscopy_Acoustics_Reference.md',
         'quantum_dislocation_tunneling_data.json','standard_mineral_acoustics_data.json',
         'verify_convergence_integral.py','verify_metamaterial_and_hugoniot.py',
         'verify_quantum_resonance.py','sim_cavity_acoustics.py','sim_cavity_acoustics.cpp']
total = 0
for k in order:
    v = counts.get(k, 0)
    print(f'{k}: {v}')
    total += v
print(f'TOTAL: {total} (csv data rows: {len(rows)})')
