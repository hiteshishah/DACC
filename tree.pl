ancestor_couple(A, B, Person) :- ancestor(A, Person), ancestor(B, Person), offspring(C, A), offspring(C, B), male(A), female(B).

remove_dups([], []).
remove_dups([First | Rest], NewRest) :- member(First, Rest), remove_dups(Rest, NewRest).
remove_dups([First | Rest], [First | NewRest]) :- not(member(First, Rest)), remove_dups(Rest, NewRest).

uncle_list(Uncles, Person) :- findall(Uncle, uncle(Uncle, Person), List), remove_dups(List, Uncles).

aunt_list(Aunts, Person) :- findall(Aunt, aunt(Aunt, Person), List), remove_dups(List, Aunts).

cousin(X, Y) :- sibling(Z, Y), cousin(X, Z).
cousin(X, Y) :- parent(A, X), parent(B, Y), sibling(A, B), X\==Y.

uncle(X, Y) :- sibling(Z, Y), uncle(X, Z).
uncle(X, Y) :- sibling(X, Z), parent(Z, Y), male(X).

aunt(X, Y) :- sibling(Z, Y), aunt(X, Z).
aunt(X, Y) :- sibling(X, Z), parent(Z, Y), female(X).

sibling(X, Y) :- parent(Z, X), parent(Z, Y), X\==Y.

ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
ancestor(X, Y) :- parent(X, Y).

grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

offspring(Y, X) :- parent(X, Y).

parent(richardFranklin,carolRomanowski).
parent(margaretMoore,carolRomanowski).
parent(oscarFranklin,ellenFranklin).
parent(blancheAdams,ellenFranklin).
parent(oscarFranklin,haroldFranklin).
parent(blancheAdams,haroldFranklin).
parent(oscarFranklin,dorisFranklin).
parent(blancheAdams,dorisFranklin).
parent(oscarFranklin,jeanFranklin).
parent(blancheAdams,jeanFranklin).
parent(oscarFranklin,llewellynoscarFranklin).
parent(blancheAdams,llewellynoscarFranklin).
parent(oscarFranklin,richardFranklin).
parent(blancheAdams,richardFranklin).
parent(llewellynFranklin,oscarFranklin).
parent(katherineTwining,oscarFranklin).
parent(miltonAdams,blancheAdams).
parent(miltonAdams,edithAdams).
parent(miltonAdams,ednaAdams).
parent(miltonAdams,ireneAdams).
parent(miltonAdams,dorothyAdams).
parent(miltonAdams,velmaAdams).
parent(miltonAdams,sadieAdams).
parent(ellenWhite,blancheAdams).
parent(ellenWhite,edithAdams).
parent(ellenWhite,ednaAdams).
parent(ellenWhite,ireneAdams).
parent(ellenWhite,dorothyAdams).
parent(ellenWhite,velmaAdams).
parent(ellenWhite,sadieAdams).
parent(oscaraFranklin,llewellynFranklin).
parent(maryDoak,llewellynFranklin).
parent(oscaraFranklin,williamFranklin).
parent(maryDoak,williamFranklin).
parent(oscaraFranklin,edwinFranklin).
parent(maryDoak,edwinFranklin).
parent(oscaraFranklin,delvinFranklin).
parent(maryDoak,delvinFranklin).
parent(oscaraFranklin,charlesFranklin).
parent(maryDoak,charlesFranklin).
parent(jesseTwining,katherineTwining).
parent(maryGoodwin,katherineTwining).
parent(averyWhite,ellenWhite).
parent(dencyPhillips,ellenWhite).
parent(eliWhite,averyWhite).
parent(lydiaJohnson,averyWhite).
parent(joshuaWhite,eliWhite).
parent(elizabethMorse,eliWhite).
parent(sarahMead,joshuaWhite).
parent(davidWhite,joshuaWhite).
parent(mercyHazen,sarahMead).
parent(abnerMead,sarahMead).
parent(calebHazen,mercyHazen).
parent(mercyBradstreet,mercyHazen).
parent(johnBradstreet,mercyBradstreet).
parent(anneDudley,johnBradstreet).
parent(gov_simonBradstreet,johnBradstreet).
parent(sir_thomasDudley,anneDudley).
parent(dorothyYorke,anneDudley).
parent(sir_rogerDudley,sir_thomasDudley).
parent(susannahThorne,sir_thomasDudley).
parent(sir_henryDudley,sir_rogerDudley).
parent(unknownWifeOfsir_henryDudley,sir_rogerDudley).
parent(sir_johnSutton,sir_henryDudley).
parent(cicelyGray,sir_henryDudley).
parent(sir_edwardSutton, sir_johnSutton).
parent(ceciliaWilloughby,sir_johnSutton).
parent(sir_williamWilloughby, ceciliaWilloughby).
parent(janeStrangeways,ceciliaWilloughby).
parent(thomasStrangeways, janeStrangeways).
parent(catherineNeville,janeStrangeways).
parent(richardPlantagenet, king_richardIII).
parent(cecilyNeville,king_richardIII).
parent(ralphdeNeville,catherineNeville).
parent(joanBeaufort,catherineNeville).
parent(ralphdeNeville, cecilyNeville).
parent(joanBeaufort,cecilyNeville).


female(carolRomanowski).
female(margaretMoore).
female(ellenFranklin).
female(dorisFranklin).
female(jeanFranklin).
female(blancheAdams).
female(edithAdams).
female(ednaAdams).
female(ireneAdams).
female(dorothyAdams).
female(velmaAdams).
female(sadieAdams).
female(ellenWhite).
female(lydiaJohnson).
female(elizabethMorse).
female(katherineTwining).
female(maryDoak).
female(maryGoodwin).
female(dencyPhillips).
female(sarahMead).
female(mercyHazen).
female(mercyBradstreet).
female(anneDudley).
female(dorothyYorke).
female(susannahThorne).
female(unknownWifeOfsir_henryDudley).
female(cicelyGray).
female(ceciliaWilloughby).
female(janeStrangeways).
female(catherineNeville).
female(cecilyNeville).
female(joanBeaufort).

male(richardFranklin).
male(haroldFranklin).
male(llewellynoscarFranklin).
male(oscarFranklin).
male(llewellynFranklin).
male(charlesFranklin).
male(delvinFranklin).
male(edwinFranklin).
male(williamFranklin).
male(oscaraFranklin).
male(miltonAdams).
male(jesseTwining).
male(averyWhite).
male(eliWhite).
male(calebHazen).
male(abnerMead).
male(joshuaWhite).
male(davidWhite).
male(johnBradstreet).
male(gov_simonBradstreet).
male(sir_thomasDudley).
male(sir_rogerDudley).
male(sir_henryDudley).
male(sir_johnSutton).
male(sir_williamWilloughby).
male(thomasStrangeways).
male(richardPlantagenet).
male(king_richardIII).
male(ralphdeNeville).


