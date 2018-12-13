s --> np(_), vp.

np(adj) --> adj, n(_).
np(det) --> det_sing, n(vowel).
np(det) --> det, n(_).

vp --> v_prep, pp.
vp --> v, np(adj).

pp --> p, np(det).

adj --> [large].
adj --> [elective].

n(cons) --> [crowds].
n(vowel) --> [orchestra].
n(cons) --> [man].
n(cons) --> [surgery].
n(vowel) --> [airplane].
n(cons) --> [city].

v_prep --> [listened].
v_prep --> [flew].

v --> [rejected].

p --> [to].
p --> [over].

det --> [the].
det_sing --> [an].

