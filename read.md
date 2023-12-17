*** Projekt 4 ***

Systemy kolejkowe

    1. Liczenie analityczne
    2. Symulacja

1. Samochody
2. Dystrybutory
3. Ile samochód spędza w kolejce?
4. Nowy samochód średnio co 120 sekund
5. Przyjazdy niezależne
    a. Czas obsługi dokładnie 60 s
    b. Czas obsługi ma rozkład normalny 60 sekund
    c. 
    d. Rozkład jednostajny 0 - 120

System M|G|1

Wymagania:

Program powinien zwrócić Tb średni czas przebywania zgłoszenia w buforze.

- Zgłoszenia przychodzą niezależnie średnio co 120s.
- Czas obsługi zgłoszenia wynosi:
  a) dokładnie 60s,
  b) jest zmienną losową o rozkładzie U(0,120), rozkład jednostajny
  c) jest zmienną losową o rozkładzie E(60), rozkład wykładniczy
  d) jest zmienną losową o rozkładzie N(60,20). rozkład normalny

uwagi:
 - za oddanie w terminie
 - własne generatory
 - badania porównawcze generatora własnego z wbudowanym, 4 x 0,5 pkt
 - za dokładność 0.1% w stosunku do wartości obliczonych, 4 x 0,5 pkt
 - za sprawozdanie z badaniami