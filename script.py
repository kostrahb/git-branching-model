#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pepa píše program

# Pepa je inteligentní, proto vyvíjí v dev

# Pepa si mezitím, co Franta vyvíjí novou featuru, všiml, že program je špatně napsaný a potenciálně se v něm nachází případ, který by mohl vést na nezamýšlené chování.
# Přepsal část kódu tak, aby k tomuto případu nemohlo dojít.

# Na tento velký projekt přibyl Franta, který dostal za úkol implementovat novou featuru (Dělá to, že nedělá nic)
# (Tyto dva řádky napsal Franta)

# Na projekt přibyla projektová manažerka Jana a nová juniorní vývojářka Amálka. Klient požaduje vytvoření nové velké featury. Jana proto vzala specifikace a protože se daná featura skládá z několika dílčích úkolů, rozdělila ji na tyto úkoly. První a nejlehčí část dostala na starost Amálka. Pro ní byla založena větev issue/big-feature-1 a má za úkol naprogramovat funkci, která nedělá nic.

# Franta dostal specifikace od Jany a Amálky a mohl tak začít programovat na své části projektu
# Jeho úkolem bylo naprogramovat
#  - funkci, která volá Amálčinu funkci, pak dělá nějaké výpočty a nakonec nevrátí nic
#  - funkci, která volá v cyklu Amálčinu funkci

from importantFunction import importantFunction

def functionThatDoesNothing1():
	importantFunction()
	a = 1
	b = 2
	c = a + b
	return

def functionThatDoesNothing1():
	for i in range(10):
		importantFunction()

# Pepa, protože je nejlepší programátor z týmu a vyzná se v pythoních balíčcích, dostal na starost napsání instalačního skriptu.
# Specifikováno od Jany dostal, že zákazník bude používat dvě funkce functionThatDoesNothing1 a functionThatDoesNothing2

