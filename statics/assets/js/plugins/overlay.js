google.maps.__gjsload__('overlay', function(_){var XC=function(a){this.Eg=a},Dqa=function(){},YC=function(a){a.Ly=a.Ly||new Dqa;return a.Ly},Eqa=function(a){this.Ch=new _.En(()=>{const b=a.Ly;if(a.getPanes()){if(a.getProjection()){if(!b.ex&&a.onAdd)a.onAdd();b.ex=!0;a.draw()}}else{if(b.ex)if(a.onRemove)a.onRemove();else a.remove();b.ex=!1}},0)},Fqa=function(a,b){const c=YC(a);let d=c.lw;d||(d=c.lw=new Eqa(a));_.Ob(c.Ph||[],_.Fk);var e=c.ni=c.ni||new _.Bla;const f=b.__gm;e.bindTo("zoom",f);e.bindTo("offset",f);e.bindTo("center",f,"projectionCenterQ");
e.bindTo("projection",b);e.bindTo("projectionTopLeft",f);e=c.yC=c.yC||new XC(e);e.bindTo("zoom",f);e.bindTo("offset",f);e.bindTo("projection",b);e.bindTo("projectionTopLeft",f);a.bindTo("projection",e,"outProjection");a.bindTo("panes",f);e=()=>_.Fn(d.Ch);c.Ph=[_.Dk(a,"panes_changed",e),_.Dk(f,"zoom_changed",e),_.Dk(f,"offset_changed",e),_.Dk(b,"projection_changed",e),_.Dk(f,"projectioncenterq_changed",e)];_.Fn(d.Ch);b instanceof _.al?(_.Pl(b,"Ox"),_.Nl(b,148440)):b instanceof _.jm&&(_.Pl(b,"Oxs"),
_.Nl(b,181451))},Kqa=function(a){if(a){var b=a.getMap();if(Gqa(a)!==b&&b&&b instanceof _.al){const c=b.__gm;c.overlayLayer?a.__gmop=new Hqa(b,a,c.overlayLayer):c.Fg.then(({kh:d})=>{const e=new Iqa(b,d);d.Bi(e);c.overlayLayer=e;Jqa(a);Kqa(a)})}}},Jqa=function(a){if(a){var b=a.__gmop;b&&(a.__gmop=null,b.Eg.unbindAll(),b.Eg.set("panes",null),b.Eg.set("projection",null),b.Gg.tl(b),b.Fg&&(b.Fg=!1,b.Eg.onRemove?b.Eg.onRemove():b.Eg.remove()))}},Gqa=function(a){return(a=a.__gmop)?a.map:null},Lqa=function(a,
b){a.Eg.get("projection")!=b&&(a.Eg.bindTo("panes",a.map.__gm),a.Eg.set("projection",b))};_.Ha(XC,_.Vk);XC.prototype.changed=function(a){a!="outProjection"&&(a=!!(this.get("offset")&&this.get("projectionTopLeft")&&this.get("projection")&&_.qj(this.get("zoom"))),a==!this.get("outProjection")&&this.set("outProjection",a?this.Eg:null))};var ZC={};_.Ha(Eqa,_.Vk);ZC.Dl=function(a){if(a){var b=a.getMap();(YC(a).gC||null)!==b&&(b&&Fqa(a,b),YC(a).gC=b)}};ZC.tl=function(a){const b=YC(a);var c=b.ni;c&&c.unbindAll();(c=b.yC)&&c.unbindAll();a.unbindAll();a.set("panes",null);a.set("projection",null);b.Ph&&_.Ob(b.Ph,_.Fk);b.Ph=null;b.lw&&(b.lw.Ch.Cj(),b.lw=null);delete YC(a).gC};var $C={},Hqa=class{constructor(a,b,c){this.map=a;this.Eg=b;this.Gg=c;this.Fg=!1;_.Pl(this.map,"Ox");_.Nl(this.map,148440);c.Dl(this)}draw(){this.Fg||(this.Fg=!0,this.Eg.onAdd&&this.Eg.onAdd());this.Eg.draw&&this.Eg.draw()}},Iqa=class{constructor(a,b){this.Ig=a;this.Gg=b;this.Eg=null;this.Fg=[]}dispose(){}vi(a,b,c,d,e,f,g,h){const k=this.Eg=this.Eg||new _.sA(this.Ig,this.Gg,()=>{});k.vi(a,b,c,d,e,f,g,h);for(const m of this.Fg)Lqa(m,k),m.draw()}Dl(a){this.Fg.push(a);this.Eg&&Lqa(a,this.Eg);this.Gg.refresh()}tl(a){_.Wb(this.Fg,
a)}};$C.Dl=Kqa;$C.tl=Jqa;_.vk("overlay",{wA:function(a){if(a){(0,ZC.tl)(a);(0,$C.tl)(a);var b=a.getMap();b&&(b instanceof _.al?(0,$C.Dl)(a):(0,ZC.Dl)(a))}},preventMapHitsFrom:a=>{_.mw(a,{Tk:({event:b})=>{_.wu(b.Hh)},Zj:b=>_.Yv(b),Wp:b=>_.Zv(b),Uk:b=>_.Zv(b),rk:b=>_.$v(b)}).Fr(!0)},preventMapHitsAndGesturesFrom:a=>{a.addEventListener("click",_.Bk);a.addEventListener("contextmenu",_.Bk);a.addEventListener("dblclick",_.Bk);a.addEventListener("mousedown",_.Bk);a.addEventListener("mousemove",_.Bk);a.addEventListener("MSPointerDown",
_.Bk);a.addEventListener("pointerdown",_.Bk);a.addEventListener("touchstart",_.Bk);a.addEventListener("wheel",_.Bk)}});});