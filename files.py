from subutai_bazaar import cdn

f = cdn.CDN('bazaar.subutai.io')
print(f.Info('p2p'))

res = f.Upload('setup.py')
if res == None:
    print("Upload failed")
print(res)
