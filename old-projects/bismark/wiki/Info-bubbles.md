
---
title: Info-bubbles
date: 2011-07-15T12:12:27
lastmod: 2011-07-15T12:17:56
type: wiki
---
Information Filter Bubbles
==========================

Overview
--------

This is a project for understanding and quantifying [information filter
bubbles](http://www.thefilterbubble.com), using a distributed
measurement infrastructure like Bismark.

Intro
-----

Filter bubbles focus on the impact of web personalization based on\
regional and personal characteristics. A user is exposed to things\
that he will probably like and be interested to. This creates a\
virtual environment which looks very familiar and friendly, removing\
"irrelevant" and/or "unpopular" content, where relevance and\
popularity is based on a rich vector of personal, regional, technical\
characteristics, and limits the breadth of user's experience.

The argument so far is on a relatively high-level. A more systematic\
and detailed study could help us understand and quantify how these\
reflects to the experience users perceive.

Using a distributed measurement platform like Bismark we can generate\
identical search requests from different regions to study such
behaviors.

Design Ideas
------------

-   Home Gateways act as clients. They issue search requests in
    multiple\
    search engines (Bing, Google, Yahoo, - anything we could do with\
    Facebook?), and report the results back to a central server.

<!-- -->

-   Requests should not be hardcoded in the image. We don't expect a\
    query to have time variance, even if it has we can't predict it.
    The\
    clients can fetch a queriy from the server every day and then issue
    the\
    requests to the search engines (aka the "tip of the day")

Other Notes
-----------

-   What sort of requests would reveal differences? Should it be
    up-to-date information like news, or static content?
-   Get personalized behavior seems more difficult. It requires fake
    profiles, but how do you build history on this?
-   What other things can we detect? Censorship, ...?
-   Another way to do this would be using Tor and selecting the
    exit node.

