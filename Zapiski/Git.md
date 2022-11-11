# **Git** 

Git je brezplačna in odprtokodna programska oprema za porazdeljen nadzor različic: sledenje spremembam v katerem koli nizu datotek, ki se običajno uporablja za usklajevanje dela med programerji, ki skupaj razvijajo izvorno kodo med razvojem programske opreme. Njegovi cilji vključujejo hitrost, celovitost podatkov in podporo za porazdeljene, nelinearne poteke dela (na tisoče vzporednih vej, ki delujejo na različnih sistemih).

<img src="Slike/Git_Diagram.png" width="600" alt="Delovanje Gita">

- ## **Zmogljivost**
    Značilnosti surove zmogljivosti Gita so zelo močne v primerjavi s številnimi alternativami. Commitanje, branching, merging in primerjava preteklih različic so optimizirani za učinkovitost. Algoritmi, implementirani znotraj Gita, izkoriščajo poglobljeno znanje o pogostih atributih dreves izvorne kode, kako se običajno spreminjajo skozi čas in kakšni so vzorci dostopa.

- ## **Varnost**
    Git je bil zasnovan tako, da je upravljane izvorne kode njegova najvišja prioriteta. Vsebina datotek kot tudi resnična razmerja med datotekami in imeniki, različicami, oznakami in odobritvami, vsi ti objekti v repozitoriju Git so zavarovani s kriptografsko varnim algoritmom zgoščevanja, imenovanim SHA1. To ščiti kodo in zgodovino sprememb pred naključnimi in zlonamernimi spremembami ter zagotavlja, da je zgodovina popolnoma sledljiva.

- ## **Fleksibilnost**
    Eden od Gitovih ključnih načrtovalskih ciljev je Fleksibilnost. Git je prilagodljiv v več pogledih: v podpori za različne vrste nelinearnih razvojnih delovnih tokov, v svoji učinkovitosti tako pri majhnih kot velikih projektih ter v združljivosti s številnimi obstoječimi sistemi in protokoli.

## **Git rebase**

To je postopek premikanja ali združevanja zaporedja commitov v novi base commit. Rebasing je najbolj uporabno in enostavno vizualiziran v kontekstu branchov. Proces si lahko tako:

<img src="Slike/Git_rebasing.png" width="600" alt="Kako deluje rebase">

Z vidika vsebine je rebasing spreminjanje baze brancha iz enega commita v drugega, zaradi česar je videti, kot da smo svoj branch ustvarili iz druge objave. Interno Git to doseže tako, da ustvari nove commite in jih uporabi za navedeno bazo. Zelo pomembno je razumeti, da čeprav veja izgleda enako, je sestavljena iz povsem novih potrditev.