import json, re, sys
R='/home/claude/paranin-dili/videos/'
def sec(slug):
    t=open(R+slug+'/paylasim.txt').read()
    def g(k):
        m=re.search(rf'^{k}:\s*(.*?)(?=^(?:UZUN|ILK_YORUM|YT_BASLIK|TT_BASLIK|KISA):|\Z)', t, re.S|re.M); return m.group(1).strip().strip('-').strip() if m else ''
    return {k:g(k) for k in ['UZUN','ILK_YORUM','YT_BASLIK','TT_BASLIK','KISA']}
def tags(text): return [h[1:] for h in re.findall(r'#\w+', text.split('\n')[-1])]
def main_posts(date, slug, media, cover):
    s=sec(slug); pd={"dateTime":f"{date}T19:45:00","timezone":"Europe/Istanbul"}
    base=dict(publicationDate=pd, text=s['UZUN'], firstCommentText=s['ILK_YORUM'], media=[media], autoPublish=True, draft=False, shortener=False, mediaAltText=[], smartLinkData={"ids":[]}, descendants=[], hasNotReadNotes=False, videoThumbnailUrl=cover)
    ig=dict(base, providers=[{"network":"instagram"}], instagramData={"autoPublish":True,"type":"REEL","isAiGenerated":False})
    yt=s['YT_BASLIK']; ytt=yt.replace(' #shorts','')
    oth=dict(base, providers=[{"network":"facebook"},{"network":"tiktok"},{"network":"youtube"}],
      facebookData={"type":"REEL","title":ytt},
      youtubeData={"title":yt,"type":"short","privacy":"public","tags":tags(s['UZUN']),"category":"EDUCATION","madeForKids":False,"isAiGeneratedContent":False},
      tiktokData={"privacyOption":"PUBLIC_TO_EVERYONE","title":s['TT_BASLIK'],"isAigc":False,"disableComment":False,"disableDuet":False,"disableStitch":False,"commercialContentThirdParty":False,"commercialContentOwnBrand":False,"autoAddMusic":False})
    return ig, oth
def trial(date, time, slug, media, cover):
    s=sec(slug)
    return dict(publicationDate={"dateTime":f"{date}T{time}:00","timezone":"Europe/Istanbul"}, text=s['KISA'], firstCommentText=s['ILK_YORUM'], providers=[{"network":"instagram"}], media=[media], autoPublish=True, draft=False, shortener=False, mediaAltText=[], smartLinkData={"ids":[]}, descendants=[], hasNotReadNotes=False, videoThumbnailUrl=cover, instagramData={"autoPublish":True,"type":"TRIAL_REEL","isAiGenerated":False,"shareTrialAutomatically":False})
if __name__=='__main__':
    kind,date,slug,media,cover=sys.argv[1:6]
    if kind=='main':
        for x in main_posts(date,slug,media,cover): print(json.dumps(x,ensure_ascii=False))
    else: print(json.dumps(trial(date,kind,slug,media,cover),ensure_ascii=False))

def all4(date, slug, commit, cover_commit, v2text):
    b=f'https://raw.githubusercontent.com/blodym4ry/paranin-dili/{commit}/public/aralik/{date}'
    cov=f'https://raw.githubusercontent.com/blodym4ry/paranin-dili/{cover_commit}/public/covers/{slug}.jpg'
    ig,oth=main_posts(date,slug,b+'.mp4',cov)
    v2=trial(date,'21:45',slug,b+'_v2.mp4',cov); p=v2['text'].split('\n\n'); p[0]=v2text; v2['text']='\n\n'.join(p)
    hz=trial(date,'22:45',slug,b+'_hz.mp4',cov)
    return [ig,oth,v2,hz]
