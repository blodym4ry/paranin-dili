const CAPS=__CAPS__, SC=__SCENES__, AV=__AV__;
const tl=gsap.timeline({paused:true});
const CV=(n,d)=>(getComputedStyle(document.documentElement).getPropertyValue(n).trim()||d);
const $=s=>document.querySelector(s);
const st=id=>SC.find(s=>s[0]===id)[1];
const fmt=v=>Math.round(v).toLocaleString('tr-TR');
function inn(sel,t,o={}){tl.fromTo(sel,{opacity:0,y:o.y??40,scale:o.s??1},{opacity:1,y:0,scale:1,duration:o.d??.45,ease:o.e??'expo.out'},t);}
function out(sel,t,d=.25){tl.to(sel,{opacity:0,y:-20,duration:d,ease:'power2.in'},t);}
function count(sel,a,b,t,d,f=fmt,pre='',suf=''){const o={v:a};tl.fromTo(o,{v:a},{v:b,duration:d,ease:'power2.inOut',onUpdate:()=>{$(sel).textContent=pre+f(o.v)+suf;}},t);}
function slam(sel,t){tl.fromTo(sel,{opacity:0,scale:1.4,transformOrigin:'0% 50%'},{opacity:1,scale:1,duration:.28,ease:'power4.in'},t);}
// ---- avatar window moves
const BW=740,BH=1040,BCX=540,BCY=770;
function win(v){const [x,y,w,h,r]=v;const s=Math.max(w/BW,h/BH);const cw=w/s,ch=h/s;const ix=(BW-cw)/2;const iy=(BH-ch)*(h<500?0.18:0.5);
 return {tf:{x:x+w/2-BCX,y:y+h/2-BCY,scale:s},cp:`inset(${iy.toFixed(1)}px ${ix.toFixed(1)}px ${(BH-ch-iy).toFixed(1)}px ${ix.toFixed(1)}px round ${(r/s).toFixed(1)}px)`, dy:(BH/2-(iy+ch/2))*s};}
const w0=win(AV.s1);tl.fromTo('#avw',{x:w0.tf.x,y:w0.tf.y+w0.dy,scale:w0.tf.scale*.94,opacity:0},{x:w0.tf.x,y:w0.tf.y+w0.dy,scale:w0.tf.scale,opacity:1,duration:.5,ease:'expo.out'},0);
tl.fromTo('#avc',{clipPath:w0.cp},{clipPath:w0.cp,duration:.01},0);
SC.slice(1).forEach(([id,a],k)=>{const v=AV[id],pv=AV[SC[k][0]];
 // AV[id]===null -> avatar hidden for this scene (graphics only)
 if(!v){if(pv)tl.to('#avbox',{opacity:0,duration:.3,ease:'power2.in'},a-.35);return;}
 const w=win(v);
 if(!pv){tl.set('#avw',{x:w.tf.x,y:w.tf.y+w.dy,scale:w.tf.scale},a-.4);tl.set('#avc',{clipPath:w.cp},a-.4);
  tl.fromTo('#avw',{scale:w.tf.scale*.94},{scale:w.tf.scale,duration:.5,ease:'expo.out',immediateRender:false},a-.05);tl.fromTo('#avbox',{opacity:0},{opacity:1,duration:.35,ease:'power2.out',immediateRender:false},a-.05);return;}
 tl.to('#avw',{x:w.tf.x,y:w.tf.y+w.dy,scale:w.tf.scale,duration:.7,ease:'expo.inOut'},a-.35);tl.to('#avc',{clipPath:w.cp,duration:.7,ease:'expo.inOut'},a-.35);});
tl.fromTo('#glow',{x:0,y:0},{x:520,y:900,duration:__DUR__,ease:'sine.inOut'},0);
// ---- captions
const host=$('#caps');
CAPS.forEach((c,i)=>{const d=document.createElement('div');d.className='cl';d.id='c'+i;
  d.innerHTML=c.w.map((w,j)=>`<span class="cw" id="c${i}w${j}">${w[0]}</span>`).join('');host.appendChild(d);
  const nx=CAPS[i+1]?CAPS[i+1].a:1e9; const end=Math.min(c.b,nx);
  tl.fromTo(d,{opacity:0,y:24},{opacity:1,y:0,duration:.16,ease:'power3.out'},c.a);
  c.w.forEach((w,j)=>{const el=`#c${i}w${j}`;
    if(w[2]===1) tl.set(el,{color:CV('--cap-em-fg','#0d0c0a'),backgroundColor:CV('--cap-em-bg','#e8b931'),borderRadius:'8px',paddingLeft:'.12em',paddingRight:'.12em'},w[1]);
    else if(w[2]===2) tl.set(el,{color:CV('--cap-red','#ff4a3d')},w[1]);
    else tl.set(el,{color:CV('--cap-on','#f3efe6')},w[1]);});
  tl.to(d,{opacity:0,duration:.08},end-.1);});
