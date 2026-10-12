import os, sys, shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
import profiles

print('list:', profiles.list_profiles())
print('active:', profiles.active_id())
for ref in ('profile_001', 'Profile 1', '001', '1', ''):
    info = profiles.resolve(ref)
    print('resolve(%r) ->' % ref, info['id'], info['display_name'],
          os.path.basename(info['style']), os.path.basename(info['labeled']))
try:
    profiles.resolve('profile_999')
except KeyError as e:
    print('missing ->', e)

p = profiles.create_profile('Scratch', copy_from='profile_001')
print('created:', p['id'], p['display_name'],
      'style:', os.path.exists(p['style']),
      'labeled:', os.path.isdir(p['labeled']),
      'glyphs:', os.path.isdir(p['glyphs']),
      'clusters:', os.path.isdir(p['clusters']))
# labeled manifest carried over?
import json
man = json.load(open(os.path.join(p['labeled'], 'manifest.json')))
print('copied library:', man['n_glyphs'], 'glyphs,', len(man['chars']), 'letters')

info = profiles.rename_profile(p['id'], 'Scratch Renamed')
print('renamed ->', info['display_name'])
info2 = profiles.set_active(p['id'])
print('active now:', profiles.active_id())
profiles.set_active('profile_001')
print('active restored:', profiles.active_id())

shutil.rmtree(p['labeled'], ignore_errors=True)
shutil.rmtree(p['glyphs'], ignore_errors=True)
shutil.rmtree(p['clusters'], ignore_errors=True)
os.remove(p['style'])
data = profiles._load()
data['profiles'].pop(p['id'], None)
if data['active'] == p['id']:
    data['active'] = 'profile_001'
profiles._save(data)
print('cleaned; list now:', [x[0] for x in profiles.list_profiles()])
print('ALL OK')
