# **Secure Shell Protocol (SSH)**

SSH ali Secure Shell je omrežni komunikacijski protokol, ki omogoča komunikacijo med dvema računalnikoma in skupno rabo podatkov. Lastnost SSH-ja je, da je komunikacija med obema računalnikoma šifrirana, kar pomeni, da je primerna za uporabo v nezaščitenih omrežjih.

SSH omogoča storitev za najširši nabor operacijskih sistemov (Windows XP-10, Max OS X in Linux). SSH je zanesljiv in varen in se zaradi tega pogosto uporablja v skupnosti visokozmogljivega računalništva.

## **SSH Tunneling/SSH port forwarding**

SSH tunneling ali SSH port forwarding je metoda prenosa podatkov prek šifrirane povezave SSH. Tuneli SSH omogočajo, da se povezave do lokalnih vrat posredujejo oddaljenemu računalniku prek varnega kanala.

Torej je tuneliranje SSH le način za prenos podatkov z namenskim podatkovnim tokom (tunelom) znotraj obstoječe seje SSH. To je mogoče doseči z lokalnim port forwardingom, oddaljenim port forwardingom, dinamičnim port forwardingom ali z ustvarjanjem tunela TUN/TAP.

- **Local port forwarding** - Ko se uporablja lokalni port forwarding, se ustvari ločen tunel znotraj povezave SSH, ki posreduje omrežni promet od lokalnih vrat do vrat oddaljenega serverja

- **Remote port forwarding (reverse tunneling)** - Pogosto imenovano tudi reverse tunneling, oddaljeni port forwarding preusmeri vrata oddaljenega serverja na vrata lokalnega gostitelja. Ko se uporablja oddaljeno posredovanje vrat, se odjemalec najprej poveže s serverjom s SSH. Nato SSH ustvari ločen tunel znotraj obstoječe SSH povezave, ki preusmeri dohodni promet v oddaljenih vratih na lokalnega gostitelja (kjer je bila ustvarjena povezava SSH).

- **Dynamic port forwarding** - Tako lokalni kot oddaljeni forwarding zahteva definiranje lokalnih in oddaljenih vrat. Kaj pa, če so vrata vnaprej neznana ali če želite preusmeriti promet na poljubno destinacijo? Znano tudi kot dinamično tuneliranje ali proxy SSH SOCKS5, dinamični port forwarding vam omogoča, da določite povezovalna vrata, ki bodo dinamično posredovala ves  promet na oddaljeni strežnik.

- **SSH TUN/TAP tunneling** - SSH podpira device forwarding v tunelu (znano tudi kot TUN/TAP). TUN/TAP so navidezni omrežni vmesniki, ki jih je mogoče uporabiti za ustvarjanje tunela med dvema strežnikoma. Ta nastavitev je zanana tudi kot VPN za reveže.

## **SSH agent**

- ### **Kaj je SSH agent?**

    SSH agent je upravitelj ključev za SSH. Ključe in potrdila hrani v pomnilniku, nešifrirane in pripravljene da jih uporabi SSH. Prihrani vam vnašanje gesla vsakič, ko se povežete s serverjom. V  sistemu deluje v ozadju, ločeno od SSH, in se običajno zažene, ko prvič zaženete SSH po ponovnem zagonu.

    SSH agent varuje zasebne ključe zaradi stvari, ki jih ne počne:

    - Na disk ne zapiše nobenega ključnega materiala.
    - Ne dovoljuje izvoza  zasebnih ključev.

    Zasebne ključe, shranjene v agentu, je mogoče uporabiti samo za en namen: podpisovanje sporočil.

- ### **Če agent lahko samo podpisuje sporočila, kako SSH šifrira in dešifrira promet?**

    Par ključev SSH se uporablja samo za preverjanje pristnosti med začetnim rokovanjem.

    Primer, kako se uporabniški ključ preveri med rokovanjem SSH z vidika strežnika:

    1. Odjemalec posreduje serverju javni ključ.
    2. Server ustvari in pošlje kratko, naključno sporočilo, v katerem odjemalca prosi, naj ga podpiše z zasebnim ključem.
    3. Odjemalec prosi agenta SSH, da podpiše sporočilo in posreduje rezultat nazaj na server.
    4. Server preveri podpis z odjemalčevim javnim ključem.
    5. Server ima zdaj dokaz, da ima odjemalec svoj zasebni ključ.

- ### **Agent forwarding**

    Omogoča lokalnemu agentu SSH, da gre prek obstoječe SSH povezave in preveri pristnost na oddaljenem serverju. 
    
    ***Primer***:
    Recimo, da imate SSH v instanci EC2 in želite od tam klonirati zasebni repozitorij iz GitHub-a. Brez agent forwardinga bi morali kopijo svojega GitHub zasebnega ključa shraniti na gostitelja EC2. S posredovanjem posrednika lahko odjemalec skozi E2C uporabi ključe na lokalnem računalniku za preverjanje pristnosti na GitHub-u.
    
    #### ***Slabosti***

    Kdorkoli s root dostopom na oddaljenem gostitelju lahko
    dostopa do vašega lokalnega agenta SSH prek vtičnice. Uporabijo lahko vaše ključe, da se izdajo za vas na drugih napravah v omrežju.
