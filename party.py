#!/usr/bin/env python3
import time

party0 =  "      u'-_         /&\   __u__                /&\        \___/                 "
party1 =  "/'0')/   \(*o*)/ u(-_-)>  |#|     u('-')7   <(0w0)>     /(.c.)\                "

volleyball0 = "                          |       @*-._                                    "
volleyball1 = "\('o')/                   |              \(0u0\                            "

party = input("Do you like parties? ")
if "yes" in party:
	print(party0)
	print(party1)
if "no" in party:
	print("Well, that's a shame *('-')7")
volleyball = input("Do you like volleyball? ")
if "yes" in volleyball:
	print(volleyball0)
	print(volleyball1)
if "no" in volleyball:
	print(".", end="", flush=True)
	time.sleep(1)
	print(".", end="", flush=True)
	time.sleep(1)
	print(".", end="", flush=True)
	time.sleep(1.5)
	print("\n""*goktug left the server.*")
