---
title: Tree Ref {{id}}
layout: single
sidebar:
  nav: "trees"
gallery_t: 
{{gallery}}
gallery_c:
  - url: ./images/{{id}}/{{canopy_img}}_w.jpg
    image_path: ./images/{{id}}/{{canopy_img}}_th.jpg
    alt: "Canopy Density"
    title: "Canopy Density"
gallery_ll:
  - url: ./images/{{id}}/{{leaf_litter_img}}_w.jpg
    image_path: ./images/{{id}}/{{leaf_litter_img}}_th.jpg
    alt: "Leaf Litter"
    title: "Leaf Litter"
---

|*Lat/Long*|{{latlong}}|
|*OS Grid Location*|{{osgl}}|
|*(Original 2012 OSGL)*|{{2012osgl}}|
|*Sex*|{{sex}}|
|*Canopy Density*|{{canopy}}|
|*Leaf Litter*|{{leaf_litter}}|
|*Girth (ft)*|{{girth_ft}}|
|*Girth (m)*|{{girth_m}}|
|*Height measured*|{{height}}|
|*Comments*|{{comments}}|

{% include gallery id="gallery_t" layout="half" caption="Tree Ref {{id}}" %}

{% include gallery id="gallery_c" layout="half" caption="Canopy Density" %}

{% include gallery id="gallery_ll" layout="half" caption="Leaf Litter" %}

