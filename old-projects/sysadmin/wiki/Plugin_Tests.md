
---
title: Plugin Tests
date: 2011-01-24T08:44:36
lastmod: 2011-01-24T08:44:36
type: wiki
---
Plugin Tests
============

{{graphviz(\
digraph finite\_state\_machine {\
rankdir=LR;\
size="8,5"\
node \[shape = doublecircle\]; LR\_0 LR\_3 LR\_4 LR\_8;\
node \[shape = circle\];\
LR\_0 -&gt; LR\_2 \[ label = "SS (B)" \];\
LR\_0 -&gt; LR\_1 \[ label = "SS (S)" \];\
LR\_1 -&gt; LR\_3 \[ label = "S (\$end)" \];\
LR\_2 -&gt; LR\_6 \[ label = "SS (b)" \];\
LR\_2 -&gt; LR\_5 \[ label = "SS (a)" \];\
LR\_2 -&gt; LR\_4 \[ label = "S (A)" \];\
LR\_5 -&gt; LR\_7 \[ label = "S (b)" \];\
LR\_5 -&gt; LR\_5 \[ label = "S (a)" \];\
LR\_6 -&gt; LR\_6 \[ label = "S (b)" \];\
LR\_6 -&gt; LR\_5 \[ label = "S (a)" \];\
LR\_7 -&gt; LR\_8 \[ label = "S (b)" \];\
LR\_7 -&gt; LR\_5 \[ label = "S (a)" \];\
LR\_8 -&gt; LR\_6 \[ label = "S (b)" \];\
LR\_8 -&gt; LR\_5 \[ label = "S (a)" \];\
}\
)}}
