
import time
import ambil
import random

nj = ambil.uagent()
datagent = {"uagent": nj, "bckagent": []}


def getuagent():
    while True:
        if len(datagent["uagent"]) != 0:
            cariagen = random.choice(datagent["uagent"])
            idxagen = datagent["uagent"].index(cariagen)
            if cariagen not in datagent["bckagent"]:
                datagent["bckagent"].append(cariagen)
                datagent["uagent"].pop(idxagen)
                break
            else:
                cariagen = False
                # for tt in datagent["uagent"]:
                #     print(tt)
            print(
                f"idx:{idxagen} lenagen:{len(datagent['uagent'])} lenback:{len(datagent['bckagent'])}")
        else:
            for t in datagent["bckagent"]:
                datagent["uagent"].append(t)
            datagent["bckagent"].clear()
            # print("stop")
    return cariagen


for itr in range(300):
    print()
    xxx = getuagent()
    print(xxx)
    time.sleep(0.09)
