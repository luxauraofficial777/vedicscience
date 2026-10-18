import os
import re
import csv
import sys

files_to_read = [
    "Task_01_Acoustic_Softening_NME_Report.md",
    "Task_02_Energy_Scaling_Matrix_Report.md",
    "Task_03_Numerical_Simulation_Spec_Report.md",
    "Task_04_Astra_Data_Hardening_Protocol_Report.md",
    "Task_05_Unified_Convergence_Integral_Report.md",
    "Consolidated_Master_Report_AS_NME.md",
]

study_dir = r"C:\LuxAura\study"
out_dir = r"C:\LuxAura\study\OpenCodeBP\outputs"
out_path = os.path.join(out_dir, "claims_part1.csv")

prefix_map = {
    "Task_01_Acoustic_Softening_NME_Report.md": "T01",
    "Task_02_Energy_Scaling_Matrix_Report.md": "T02",
    "Task_03_Numerical_Simulation_Spec_Report.md": "T03",
    "Task_04_Astra_Data_Hardening_Protocol_Report.md": "T04",
    "Task_05_Unified_Convergence_Integral_Report.md": "T05",
    "Consolidated_Master_Report_AS_NME.md": "MHR",
}

# Numeric patterns with units
num_unit_re = re.compile(
    r'([-+]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)\s*'
    r'(km|m|cm|mm|μm|um|nm|pm|Å|angstrom|s|ms|μs|us|ns|ps|'
    r'Hz|kHz|MHz|GHz|THz|J|kJ|MJ|eV|keV|MeV|GeV|W|kW|MW|GW|'
    r'Pa|MPa|GPa|TPa|bar|kbar|N|kN|K|°C|°F|V|mV|A|mA|F|pF|nF|'
    r'Ω|kΩ|MΩ|dB|mol|M|g|kg|mg|m²|m^2|cm²|cm^2|W/cm²|W/m²|W/m\^2|mW/cm²|'
    r'GPa·m¹/²|MPa·m½|J/m²|bits|TB|GB|PB|year|years|yr|month|months|day|days|'
    r'ppm|ppb|H|μH)\b',
    re.IGNORECASE
)

freq_unit_re = re.compile(r'([-+]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)\s*(Hz|kHz|MHz|GHz|THz)\b', re.IGNORECASE)
energy_unit_re = re.compile(r'([-+]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)\s*(eV|keV|MeV|GeV)\b', re.IGNORECASE)

# For symbol-style quantities
sym_re = re.compile(r'G_eff|sigma_t|Q[_-]?factor|power_density|workforce|frequency|strain_rate|'
                    r'shear_modulus|bulk_modulus|Young\'s_modulus|Poisson|density|viscosity|'
                    r'dislocation_density|tunneling_rate|relaxation_time|coherence_time|'
                    r'coupling|gain|threshold|bandgap|phonon_energy|lattice_parameter', re.IGNORECASE)

# Vedic/astra links
vedic_re = re.compile(r'(astra[-_]?0?\d+|barabar|sone\s*bhandar|sitatapatra|vajra|trishula|'
                      r'kavacha|varuna|agni|rudra|soma|vayu|brahma|indrajala)', re.IGNORECASE)

# Claimed class keywords
class_re = re.compile(r'(verified|validated|benchmark|computed|calculated|measured|'
                      r'hypothesis|theoretical|experimental|literature|model|command layer|'
                      r'command-layer|validated data|calibrated|derived)', re.IGNORECASE)

band_keywords = {
    'Q': ['quantum', 'tunneling', 'coherence', 'entanglement', 'superconduct', 'boson', 'fermion', 'hbar', 'wavefunction', 'eigenvalue'],
    'CE': ['chemical', 'electrical', 'ionic', 'electro', 'current', 'voltage', 'circuit', 'battery', 'electrode', 'dielectric', 'conductivity'],
    'V': ['vibrational', 'sound', 'acoustic', 'phonon', 'ultrasound', 'sonic', 'resonance', 'oscillation', 'vibration'],
    'X': ['cross-band', 'hybrid', 'coupled', 'multimodal', 'interband']
}

def infer_band(text):
    t = text.lower()
    scores = {'Q':0,'CE':0,'V':0,'X':0}
    for k,words in band_keywords.items():
        for w in words:
            if w in t: scores[k]+=1
    if scores['X']>0 or (scores['Q']>0 and scores['V']>0) or (scores['CE']>0 and (scores['Q']>0 or scores['V']>0)):
        return 'X'
    best = max(scores, key=scores.get)
    if scores[best]==0: return ''
    return best

def get_vedic(text):
    m = vedic_re.search(text)
    if m: return m.group(1)
    return ''

def get_class(text):
    m = class_re.search(text)
    if m: return m.group(1).lower()
    return ''

def extract_quantity(text):
    t = text
    # Common quantity names
    if re.search(r'G_eff|effective\s*shear', t, re.I): return 'G_eff'
    if re.search(r'sigma_t|tunneling\s*cross', t, re.I): return 'sigma_t'
    if re.search(r'\bQ\b|quality\s*factor', t, re.I): return 'Q'
    if re.search(r'power_density', t, re.I): return 'power_density'
    if re.search(r'workforce', t, re.I): return 'workforce'
    if re.search(r'frequency|f\s*=', t, re.I): return 'frequency'
    if re.search(r'strain_rate', t, re.I): return 'strain_rate'
    if re.search(r'dislocation_density', t, re.I): return 'dislocation_density'
    if re.search(r'phonon', t, re.I): return 'phonon_energy'
    if re.search(r'energy\s*density', t, re.I): return 'energy_density'
    if re.search(r'pressure|stress', t, re.I): return 'pressure'
    if re.search(r'temperature', t, re.I): return 'temperature'
    if re.search(r'amplitude', t, re.I): return 'amplitude'
    if re.search(r'gain', t, re.I): return 'gain'
    if re.search(r'bandgap|band\s*gap', t, re.I): return 'bandgap'
    m = sym_re.search(t)
    if m: return m.group(0).lower()
    return ''

def to_hz(val, unit):
    u = unit.lower()
    v = float(val)
    if u == 'khz': return str(int(v*1e3)) if v*1e3==int(v*1e3) else str(v*1e3)
    if u == 'mhz': return str(int(v*1e6)) if v*1e6==int(v*1e6) else str(v*1e6)
    if u == 'ghz': return str(int(v*1e9)) if v*1e9==int(v*1e9) else str(v*1e9)
    if u == 'thz': return str(int(v*1e12)) if v*1e12==int(v*1e12) else str(v*1e12)
    if u == 'hz': return val
    return ''

def to_eV(val, unit):
    u = unit.lower()
    v = float(val)
    if u == 'ev': return val
    if u == 'kev': return str(int(v*1e3)) if v*1e3==int(v*1e3) else str(v*1e3)
    if u == 'mev': return str(int(v*1e6)) if v*1e6==int(v*1e6) else str(v*1e6)
    if u == 'gev': return str(int(v*1e9)) if v*1e9==int(v*1e9) else str(v*1e9)
    return ''

def make_claim_id(prefix, idx):
    return f"{prefix}-{idx:03d}"

fieldnames = ["claim_id","file","line","text","band","quantity","value","unit","freq_Hz","energy_eV","claimed_class","vedic_link"]

def quote_field(s):
    # RFC 4180 style
    if s is None: s = ''
    s = str(s)
    if '"' in s or ',' in s or '\n' in s or '\r' in s:
        s = '"' + s.replace('"', '""') + '"'
    return s

rows = []
for fname in files_to_read:
    fpath = os.path.join(study_dir, fname)
    if not os.path.exists(fpath):
        print(f"MISSING: {fpath}", file=sys.stderr)
        continue
    prefix = prefix_map.get(fname, "UNK")
    with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
        for i, line in enumerate(f, start=1):
            # Skip very long data dumps that aren't natural text claims? but still look for numbers
            # Look for numeric+unit patterns
            for m in num_unit_re.finditer(line):
                val = m.group(1)
                unit = m.group(2)
                # Get short context - up to 200 chars around match
                start = max(0, m.start()-40)
                end = min(len(line), m.end()+120)
                text = line[start:end].strip()
                # Clean up
                text = re.sub(r'\s+', ' ', text)
                if len(text) > 200:
                    text = text[:197] + '...'
                # Extract fields
                band = infer_band(line)
                qty = extract_quantity(line)
                freq_hz = to_hz(val, unit) if freq_unit_re.match(m.group(0)) else ''
                energy_ev = to_eV(val, unit) if energy_unit_re.match(m.group(0)) else ''
                claimed_class = get_class(line)
                vedic = get_vedic(line)
                # Only create if it's a meaningful numeric assertion - has unit as we matched
                rows.append({
                    'file': fname,
                    'line': i,
                    'text': text,
                    'band': band,
                    'quantity': qty,
                    'value': val,
                    'unit': unit,
                    'freq_Hz': freq_hz,
                    'energy_eV': energy_ev,
                    'claimed_class': claimed_class,
                    'vedic_link': vedic
                })
    # Assign IDs sequentially per file
    # But we need to do this after collecting all - easier to group
    print(f"Scanned {fname}: found {sum(1 for r in rows if r['file']==fname)} so far...")

# Reassign claim_ids properly grouped by file in order
os.makedirs(out_dir, exist_ok=True)
# Regroup
grouped = {fname: [] for fname in files_to_read}
for r in rows:
    if r['file'] in grouped:
        grouped[r['file']].append(r)

# Write
with open(out_path, 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(fieldnames)
    total = 0
    per_file_counts = {}
    for fname in files_to_read:
        prefix = prefix_map[fname]
        items = grouped[fname]
        per_file_counts[fname] = len(items)
        total += len(items)
        for idx, item in enumerate(items, start=1):
            cid = make_claim_id(prefix, idx)
            w.writerow([
                cid,
                item['file'],
                item['line'],
                item['text'],
                item['band'],
                item['quantity'],
                item['value'],
                item['unit'],
                item['freq_Hz'],
                item['energy_eV'],
                item['claimed_class'],
                item['vedic_link']
            ])

print(f"TOTAL: {total}")
for k,v in per_file_counts.items():
    print(f"{k}: {v}")
