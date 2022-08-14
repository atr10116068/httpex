import requests
import json
import websocket
import sys
import time
import pytz
import random,ambil
import threading
import seting
import datetime as dt
import colorama
from colorama import Fore, Style, init
init()
host="https://wjxwd01mwyo.dt01showxx02.com"

dat = {
    "idroom": [],
    "smsg": False,
    "tkn": "",
    "versi": seting.versi(),
    "typegame": "",
    "gamename": ""
}
cnt = {
    "roulete": -999,
    "dragontiger": -999,
    "threedice": -999,
    "color": -999,
    "baccarat": -999,
    "mark6": -999,
    "sicbo": -999,
}
sym = "⚠️"


# def sendmsg(tex):
#     roomgame()
#     uri = host+"/App/Live/SendMsg"
#     for idr in dat["idroom"]:
#         headers = {
#             "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
#             "bundleidentifier": "user",
#             "x-token": dat["tkn"],
#             "x-version": dat["versi"],
#             "accept-encoding": "identity",
#             "connection": "keep-alive"
#         }
#         para = {"live_id": idr, "content": tex}
#         req = requests.get(uri, params=para, headers=headers)
#         # print(json.loads(req.text))


# def roomgame():
#     dat['idroom'] = []
#     drm = {
#         "result": [],
#         "rapihkanjson": [],
#         "terfilter": []
#     }

#     def doreq1():
#         uriweb = host+"/App/Live/Index?category_id=3&page=1"
#         headers = {
#             "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
#             "bundleidentifier": "user",
#             "accept-encoding": "identity",
#             "host": "dt001piwfw.d9sph.cn",
#             "connection": "keep-alive",
#         }
#         res = requests.get(uriweb, headers=headers)
#         res = json.loads(res.text)
#         drm["result"].append(res["result"])

#     def doreq2():
#         uriweb = host+"/App/Live/Index?category_id=3&page=2"
#         headers = {
#             "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
#             "bundleidentifier": "user",
#             "accept-encoding": "identity",
#             "host": "dt001piwfw.d9sph.cn",
#             "connection": "keep-alive",
#         }
#         res = requests.get(uriweb, headers=headers)
#         res = json.loads(res.text)
#         drm["result"].append(res["result"])

#     def doreq3():
#         uriweb = host+"/App/Live/Index?category_id=3&page=3"
#         headers = {
#             "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
#             "bundleidentifier": "user",
#             "accept-encoding": "identity",
#             "host": "dt001piwfw.d9sph.cn",
#             "connection": "keep-alive",
#         }
#         res = requests.get(uriweb, headers=headers)
#         res = json.loads(res.text)
#         drm["result"].append(res["result"])

#     def doreq4():
#         uriweb = host+"/App/Live/Index?category_id=3&page=4"
#         headers = {
#             "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
#             "bundleidentifier": "user",
#             "accept-encoding": "identity",
#             "host": "dt001piwfw.d9sph.cn",
#             "connection": "keep-alive",
#         }
#         res = requests.get(uriweb, headers=headers)
#         res = json.loads(res.text)
#         drm["result"].append(res["result"])

#     def doreq5():
#         uriweb = host+"/App/Live/Index?category_id=3&page=5"
#         headers = {
#             "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
#             "bundleidentifier": "user",
#             "accept-encoding": "identity",
#             "host": "dt001piwfw.d9sph.cn",
#             "connection": "keep-alive",
#         }
#         res = requests.get(uriweb, headers=headers)
#         res = json.loads(res.text)
#         drm["result"].append(res["result"])

#     threads = []

#     t1 = threading.Thread(target=doreq1)
#     t1.daemon = True
#     t2 = threading.Thread(target=doreq2)
#     t2.daemon = True
#     t3 = threading.Thread(target=doreq3)
#     t3.daemon = True
#     t4 = threading.Thread(target=doreq4)
#     t4.daemon = True
#     t5 = threading.Thread(target=doreq5)
#     t5.daemon = True
#     threads.append(t1)
#     threads.append(t2)
#     threads.append(t3)
#     threads.append(t4)
#     threads.append(t5)

#     for i in range(5):
#         threads[i].start()

#     for i in range(5):
#         threads[i].join()

#     for i in drm["result"]:
#         for x in i:
#             drm["rapihkanjson"].append(x)

#     bck = []
#     for x in drm["rapihkanjson"]:
#         if x["nickname"] not in bck:
#             bck.append(x["nickname"])
#             drm["terfilter"].append(x)

#     itr = 1
#     for x in drm["terfilter"]:
#         print(f'{itr}. {x["nickname"]}')
#         itr += 1

#     for t in drm["terfilter"]:
#         dat["idroom"].append(t["live_id"])


# if input("connect room?") == "y":
#     dat["smsg"] = True
#     roomgame()


# def dec():
#     ressp = ""
#     f = open("tkn.txt", "r")
#     tknj = f.read()
#     tknarr = tknj.split("ATARO")
#     for pantek in tknarr:
#         try:
#             ressp += str(chr(int(pantek)))
#         except:
#             pass
#     return(ressp)


# xcode = dec()
# if len(xcode) < 3:
#     print("token tidak dikenali, ambil token di ataro")
#     exit()

ex = [
    {'type': 'broadcast', 'action': 'game_do_award', 'data': {'msg_body': {'game': 'sedie_1', 'game_number': '202202210215', 'cards': [2], 'cards_dic': {'default': ['2']}, 'win_key': [
        'zonghe_xiao', 'zonghe_dan', 'dianshu_2'], 'cards_status': 1, 'tip': ['Small', 'Odd'], 'next_round_game_number': '202202210216', 'next_round_draw_at': 1645385760, 'next_round_countdown': 58}}},
    {'type': 'broadcast', 'action': 'game_do_award', 'data': {'msg_body': {'game': 'pingpang_1', 'game_number': '202202210215', 'cards': [1, 3, 2, 4, 6, 7, 6], 'cards_dic': {'default': ['1', '3', '2', '4', '6', '7', '6']}, 'win_key': [
        'tou3wei_da', 'tou3wei_dan', 'hou1_6'], 'cards_status': 1, 'tip': ['Big', 'Odd'], 'next_round_game_number': '202202210216', 'next_round_draw_at': 1645385760, 'next_round_countdown': 58}}},
    {'type': 'broadcast', 'action': 'game_do_award', 'data': {'msg_body': {'game': 'tai_1', 'game_number': '202202210215', 'cards': {'default': ['1', '1', '7', '1', '9', '6'], 'q3': [['5', '4', '3'], ['2', '2', '4']], 'h3': [['4', '4', '2'], ['2', '5', '7']], 'w2': ['7', '4']}, 'cards_dic': {'default': ['1', '1', '7', '1', '9', '6'], 'q3': [['5', '4', '3'], ['2', '2', '4']], 'h3': [['4', '4', '2'], [
        '2', '5', '7']], 'w2': ['7', '4']}, 'win_key': ['yidengjiang_xiao', 'yidengjiang_dan', 'yidengjiangshouwei_1', 'yidengjiangweishu_6', 'q3a_xiao', 'q3a_shuang', 'q3b_xiao', 'q3b_shuang', 'h3a_xiao', 'h3a_shuang', 'h3b_da', 'h3b_shuang'], 'cards_status': 1, 'tip': ['Small', 'Odd'], 'next_round_game_number': '202202210216', 'next_round_draw_at': 1645385760, 'next_round_countdown': 58}}},
    {'type': 'broadcast', 'action': 'game_do_award', 'data': {'msg_body': {'game': 'shiyixuanwu_1', 'game_number': '202202210215', 'cards': [9, 4, 1, 11, 8], 'cards_dic': {'default': ['9', '4', '1', '11', '8']}, 'win_key': [
        'zonghe_zongda', 'zonghe_zongdan', 'diyiqiuliangmian_da', 'diyiqiuliangmian_dan', 'quanwuzhongyi_1', 'quanwuzhongyi_4', 'quanwuzhongyi_8', 'quanwuzhongyi_9', 'quanwuzhongyi_11'], 'cards_status': 1, 'tip': ['Big', 'Odd', 'Big', 'Odd'], 'next_round_game_number': '202202210216', 'next_round_draw_at': 1645385760, 'next_round_countdown': 58}}},
    {'type': 'broadcast', 'action': 'game_do_award', 'data': {'msg_body': {'game': 'saiche_1', 'game_number': '202202210215', 'cards': [8, 6, 2, 5, 10, 3, 4, 9, 1, 7], 'cards_dic': {'default': ['8', '6', '2', '5', '10', '3', '4', '9', '1', '7']}, 'win_key': [
        'guanjundanma_8', 'guanyahe_heda', 'guanyahe_heshuang', 'guanjunliangmian_da', 'guanjunliangmian_shuang'], 'cards_status': 1, 'tip': ['Big', 'Even', 'Big', 'Even'], 'next_round_game_number': '202202210216', 'next_round_draw_at': 1645385760, 'next_round_countdown': 58}}},
    {'type': 'broadcast', 'action': 'game_do_award', 'data': {'msg_body': {'indo': 'roulette', 'game': 'lunpan_1', 'game_number': '202202210215', 'cards': [15], 'cards_dic': {'default': ['15']}, 'win_key': [
        'lunpandaxiao_xiao', 'lunpanse_lunpansehei', 'lunpandanshuang_dan'], 'cards_status': 1, 'tip': ['Small', 'Odd'], 'next_round_game_number': '202202210216', 'next_round_draw_at': 1645385760, 'next_round_countdown': 58}}},
    {'type': 'broadcast', 'action': 'game_do_award', 'data': {'msg_body': {'game': 'shishicai_1', 'game_number': '202202210215', 'cards': [3, 2, 4, 7, 2], 'cards_dic': {'default': ['3', '2', '4', '7', '2']}, 'win_key': [
        'diyiqiuliangmian_xiao', 'diyiqiuliangmian_dan', 'diyiqiuliangmian_zhi', 'diyiqiuvsdiwuqiu_long', 'quanwuzhongyi_2', 'quanwuzhongyi_3', 'quanwuzhongyi_4', 'quanwuzhongyi_7'], 'cards_status': 1, 'tip': ['Small', 'Odd', 'Dr'], 'next_round_game_number': '202202210216', 'next_round_draw_at': 1645385760, 'next_round_countdown': 58}}},
    {'type': 'broadcast', 'action': 'game_do_award', 'data': {'msg_body': {'game': 'yuxiaxie_1', 'game_number': '202202210215', 'cards': [2, 5, 2], 'cards_dic': {'default': ['2', '5', '2']}, 'win_key': [
        'sanjun_2', 'sanjun_5', 'duanpai_22'], 'cards_status': 1, 'tip': [], 'next_round_game_number': '202202210216', 'next_round_draw_at': 1645385760, 'next_round_countdown': 58}}},
    {'type': 'broadcast', 'action': 'game_do_award', 'data': {'msg_body': {'indo': 'dragontiger', 'game': 'longhu_1', 'game_number': '202202210215', 'cards': {'default': ['11', '1'], 'long': 'H11', 'hu': 'S1'}, 'cards_dic': {'default': [
        '11', '1'], 'long': 'H11', 'hu': 'S1'}, 'win_key': ['longhuhe_long', 'longhuse_longhong', 'longhuse_huhei'], 'cards_status': 1, 'tip': [], 'next_round_game_number': '202202210216', 'next_round_draw_at': 1645385760, 'next_round_countdown': 57}}},
    {'type': 'broadcast', 'action': 'game_do_award', 'data': {'msg_body': {'game': 'henei_1', 'game_number': '202202210215', 'cards': ['3', '3', '7', '0', '2', '6', '1', '4', '4', '1', '6', '0', '7', '6', '3', '4', '6', '5', '0', '1', '3', '1', '6', '9', '4', '0', '6', '1', '7', '3', '7', '5', '1', '1',
                                                                                                                                       '2', '6', '0', '5', '2', '9', '2', '5', '4', '6', '9', '7', '7', '9', '1', '3', '8', '1', '2', '6', '1', '8', '8', '9', '4', '3', '6', '3', '4', '3', '7', '2', '2', '0', '6', '3', '6', '0', '5', '0', '0', '5', '9', '0', '6', '8', '2', '3', '0', '4', '9', '1', '3', '8', '0', '0', '7', '4', '4', '5', '1', '3', '6', '5', '2', '5', '9', '1', '9', '0', '5', '6', '5'], 'cards_dic': {'DB': [['3', '3', '7', '0', '2']], 'G1': [['6', '1', '4', '4', '1']], 'G2': [['6', '0', '7', '6', '3'], ['4', '6', '5', '0', '1']], 'G3': [['3', '1', '6', '9', '4'], ['0', '6', '1', '7', '3'], ['7', '5', '1', '1', '2'], ['6', '0', '5', '2', '9'], ['2', '5', '4', '6', '9'], ['7', '7', '9', '1', '3']], 'G4': [['8', '1', '2', '6'], ['1', '8', '8', '9'], ['4', '3', '6', '3'], ['4', '3', '7', '2']], 'G5': [['2', '0', '6', '3'], ['6', '0', '5', '0'], ['0', '5', '9', '0'], ['6', '8', '2', '3'], ['0', '4', '9', '1'], ['3', '8', '0', '0']], 'G6': [['7', '4', '4'], ['5', '1', '3'], ['6', '5', '2']], 'G7': [['5', '9'], ['1', '9'], ['0', '5'], ['6', '5']]}, 'win_key': ['weishudb2liangmian_xiao', 'weishudb2liangmian_shuang'], 'cards_status': 1, 'tip': [], 'next_round_game_number': '202202210216', 'next_round_draw_at': 1645385760, 'next_round_countdown': 57}}},
    {'type': 'broadcast', 'action': 'game_do_award', 'data': {'msg_body': {'game': 'ydhonglvparity_1', 'game_number': '202202210215', 'cards': [3, 2, 4, 0, 3], 'cards_dic': {'default': [
        '3', '2', '4', '0', '3']}, 'win_key': ['danma_3'], 'cards_status': 1, 'tip': [], 'next_round_game_number': '202202210216', 'next_round_draw_at': 1645385760, 'next_round_countdown': 57}}},
    {'type': 'broadcast', 'action': 'game_do_award', 'data': {'msg_body': {'game': 'ydhonglvsapre_1', 'game_number': '202202210215', 'cards': [3, 3, 4, 5, 3], 'cards_dic': {'default': [
        '3', '3', '4', '5', '3']}, 'win_key': ['danma_3'], 'cards_status': 1, 'tip': [], 'next_round_game_number': '202202210216', 'next_round_draw_at': 1645385760, 'next_round_countdown': 57}}},
    {'type': 'broadcast', 'action': 'game_do_award', 'data': {'msg_body': {'indo': 'threedice', 'game': 'kuaisan_1', 'game_number': '202202210215', 'cards': [4, 1, 3], 'cards_dic': {'default': ['4', '1', '3']}, 'win_key': [
        'sanjun_1', 'sanjun_3', 'sanjun_4', 'zonghe_xiao', 'zonghe_shuang'], 'cards_status': 1, 'tip': [8, 'Small', 'Even'], 'next_round_game_number': '202202210216', 'next_round_draw_at': 1645385760, 'next_round_countdown': 57}}},
    {'type': 'broadcast', 'action': 'game_do_award', 'data': {'msg_body': {'game': 'ydhonglvemerd_1', 'game_number': '202202210215', 'cards': [3, 5, 1, 7, 5], 'cards_dic': {'default': [
        '3', '5', '1', '7', '5']}, 'win_key': ['danma_5'], 'cards_status': 1, 'tip': [], 'next_round_game_number': '202202210216', 'next_round_draw_at': 1645385760, 'next_round_countdown': 57}}},
    {'type': 'broadcast', 'action': 'game_do_award', 'data': {'msg_body': {'indo': 'color', 'game': 'honglv_1', 'game_number': '202202210215', 'cards': [9], 'cards_dic': {'default': [
        '9']}, 'win_key': ['danma_9'], 'cards_status': 1, 'tip': [], 'next_round_game_number': '202202210216', 'next_round_draw_at': 1645385760, 'next_round_countdown': 57}}},
    {'type': 'broadcast', 'action': 'game_do_award', 'data': {'msg_body': {'indo': 'baccarat', 'game': 'baijiale_1', 'game_number': '202202210215', 'cards': {'default': [8, 2], 'player': ['D2', 'S3', 'H3'], 'banker': ['H13', 'D1', 'S1']}, 'cards_dic': {'default': [
        8, 2], 'player': ['D2', 'S3', 'H3'], 'banker': ['H13', 'D1', 'S1']}, 'win_key': ['daxiao_da', 'zhuangxian_xian'], 'cards_status': 1, 'tip': [], 'next_round_game_number': '202202210216', 'next_round_draw_at': 1645385760, 'next_round_countdown': 57}}},
    {'type': 'broadcast', 'action': 'game_do_award', 'data': {'msg_body': {'game': 'w24_1', 'game_number': '202202210215', 'cards': [12], 'cards_dic': {'default': ['12']}, 'win_key': [
        'liangmian_xiao', 'liangmian_shuang', 'weizhi_zhongjian', 'weizhi_diyihang', 'haoduan_0712', 'sebo_hong'], 'cards_status': 1, 'tip': ['Small', 'Even', 'Middle', 'Line 1'], 'next_round_game_number': '202202210216', 'next_round_draw_at': 1645385760, 'next_round_countdown': 58}}},
    {'type': 'broadcast', 'action': 'game_do_award', 'data': {'msg_body': {'game': 'm12_1', 'game_number': '202202210215', 'cards': [1], 'cards_dic': {'default': ['1']}, 'win_key': [
        'liangmian_xiao', 'liangmian_dan', 'weizhi_bianyuan', 'weizhi_disanhang', 'haoduan_0103', 'sebo_hong'], 'cards_status': 1, 'tip': ['Small', 'Odd', 'Edge', 'Line 3'], 'next_round_game_number': '202202210216', 'next_round_draw_at': 1645385760, 'next_round_countdown': 58}}},
    {'type': 'broadcast', 'action': 'game_do_award', 'data': {'msg_body': {'game': 'live48_1', 'game_number': '202202210215', 'cards': [27], 'cards_dic': {'default': ['27']}, 'win_key': [
        'liangmian_da', 'liangmian_dan', 'weizhi_zhongjian', 'weizhi_dierhang', 'haoduan_2536', 'sebo_hei'], 'cards_status': 1, 'tip': ['Big', 'Odd', 'Middle', 'Line 2'], 'next_round_game_number': '202202210216', 'next_round_draw_at': 1645385760, 'next_round_countdown': 58}}},
    {'type': 'broadcast', 'action': 'game_do_award', 'data': {'msg_body': {'indo': 'mark-6', 'game': 'liuhecai_1', 'game_number': '202202210215', 'cards': [10, 27, 37, 39, 21, 4, 17], 'cards_dic': {'default': ['10', '27', '37', '39', '21', '4', '17']}, 'win_key': [
        'temaliangmian_xiao', 'temaliangmian_dan', 'temashengxiao_gou', 'temasebo_lv'], 'cards_status': 1, 'tip': ['Small', 'Odd', 'Dog'], 'next_round_game_number': '202202210216', 'next_round_draw_at': 1645385760, 'next_round_countdown': 58}}},
    {'type': 'broadcast', 'action': 'game_do_award', 'data': {'msg_body': {'game': 'toto36_1', 'game_number': '202202210215', 'cards': [25], 'cards_dic': {'default': ['25']}, 'win_key': [
        'liangmian_da', 'liangmian_dan', 'weizhi_zhongjian', 'weizhi_disanhang', 'haoduan_1927', 'sebo_hong'], 'cards_status': 1, 'tip': ['Big', 'Odd', 'Middle', 'Line 3'], 'next_round_game_number': '202202210216', 'next_round_draw_at': 1645385760, 'next_round_countdown': 57}}},
    {'type': 'broadcast', 'action': 'game_do_award', 'data': {'msg_body': {'game': 'sanqiu_1', 'game_number': '202202210215', 'cards': [1, 6, 5], 'cards_dic': {'default': ['1', '6', '5']}, 'win_key': [
        'sanjun_1', 'sanjun_5', 'sanjun_6', 'zonghe_da', 'zonghe_shuang'], 'cards_status': 1, 'tip': [12, 'Big', 'Even'], 'next_round_game_number': '202202210216', 'next_round_draw_at': 1645385760, 'next_round_countdown': 57}}},
    {'type': 'broadcast', 'action': 'game_do_award', 'data': {'msg_body': {'game': 'ydhonglvbcone_1', 'game_number': '202202210215', 'cards': [3, 3, 6, 8, 9], 'cards_dic': {'default': [
        '3', '3', '6', '8', '9']}, 'win_key': ['danma_9'], 'cards_status': 1, 'tip': [], 'next_round_game_number': '202202210216', 'next_round_draw_at': 1645385760, 'next_round_countdown': 57}}},
    {'type': 'broadcast', 'action': 'game_do_award', 'data': {'msg_body': {'indo': 'sicbo', 'game': 'toubao_1', 'game_number': '202202210215', 'cards': [1, 2, 1], 'cards_dic': {'default': ['1', '2', '1']}, 'win_key': [
        'zonghe_xiao', 'zonghe_shuang'], 'cards_status': 1, 'tip': [4, 'Small', 'Even'], 'next_round_game_number': '202202210216', 'next_round_draw_at': 1645385760, 'next_round_countdown': 57}}},
    {'type': 'broadcast', 'action': 'game_do_award', 'data': {
        'msg_body': {'indo': 'allgame', 'game': 'allgame'}}}
]


dispmenu = ""
arjudul = []
for tipe in range(len(ex)):
    try:
        judul = ex[tipe]["data"]["msg_body"]["indo"]
        arjudul.append(judul)
        dispmenu += (
            f'{tipe+1}.{judul} <-- {ex[tipe]["data"]["msg_body"]["game"]}\n')
    except:
        arjudul.append("-")
        dispmenu += (
            f'{tipe+1}.{" - "} <-- {ex[tipe]["data"]["msg_body"]["game"]}\n')
print(dispmenu)
tipein = input("game number:")
tipe = ex[int(tipein)-1]["data"]["msg_body"]["game"]
dat["typegame"] = tipe
dat["gamename"] = arjudul[int(tipein)-1]


print(tipe)
print(dat["gamename"])


def c(colr, tex, dim):
    try:
        w = {
            "RED": Fore.RED,
            "GREEN": Fore.GREEN,
            "YELLOW": Fore.YELLOW,
            "BLUE": Fore.BLUE,
            "MAGENTA": Fore.MAGENTA,
            "CYAN": Fore.CYAN,

            "BLACK": Fore.BLACK,
            "WHITE": Fore.WHITE,
            "RESET": Fore.RESET,
        }
        if dim == 1:
            return f"{Style.DIM}{w[colr.upper()]}{tex}{Style.RESET_ALL}"
        else:
            return f"{w[colr.upper()]}{tex}{Style.RESET_ALL}"
    except:
        return tex


def Ioad():
    t = [98, 121, 58, 65, 84, 8710, 82, 79]
    lop = ""
    for y in range(len(t)):
        lop += chr(t[y])
        sys.stdout.write("> \t\t\t"+c("red", f"{lop}    \t\r", 0))
        sys.stdout.flush()
        time.sleep(0.1)
    for y in range(len(lop)):
        lop = lop[0:len(lop)-1]
        sys.stdout.write("> \t\t\t"+c("red", f"{lop}    \t\r", 0))
        sys.stdout.flush()
        time.sleep(0.1)


def roulette(dataobj):
    idi = dataobj["game_number"]
    aidi = idi[8:]
    hari = int(idi[6:8])
    bulan = int(idi[4:6])
    tahun = int(idi[:4])
    wday = dt.date(tahun, bulan, hari)
    wday = wday.strftime("%d %b %Y")
    minut = int(idi[8:])*60
    server_time = str(dt.timedelta(seconds=minut))[0:5]
    if server_time[4:5] == ":":
        server_time = server_time[0:4]

    # print(json.dumps(dataobj, indent=2))

    keyw = {
        "lunpandaxiao_da": "Big  ",
        "lunpandaxiao_xiao": "Small",
        "lunpanse_lunpansehong": "red",
        "lunpanse_lunpansehei": "black",
        "lunpandanshuang_dan": "Odd",
        "lunpandanshuang_shuang": "Even",
    }
    card = dataobj["cards_dic"]["default"][0]
    wink = dataobj["win_key"]

    # warnain text
    if card == "0":
        draw = c("green", "0", 0)
        disp = f'\t{wday}[{server_time}] {card}\t{draw}  '
    else:
        card = c(keyw[wink[1]], card, 0)

    wday = c("magenta", wday, 0)
    server_time = c("white", server_time, 0)
    disp = f'\t{wday}[{server_time}]    {card}   \t{keyw[wink[0]]} {keyw[wink[2]]}'

    if dat["gamename"] != "allgame":
        print(disp)
    else:
        if card == "0":
            print(f'Roulete\t{disp}')
            # if dat["smsg"] == True:
            #     if cnt["roulete"] >= 0:
            #         sendmsg(f'{sym} 0 di Roulete {cnt["roulete"]} putaran')
            #     else:
            #         sendmsg(f'{sym} 0 di Roulete')
            cnt["roulete"] = 0
        else:
            cnt["roulete"] += 1
            print(f'[{cnt["roulete"]}]Roulete')


def dragontiger(dataobj):
    idi = dataobj["game_number"]
    aidi = idi[8:]
    hari = int(idi[6:8])
    bulan = int(idi[4:6])
    tahun = int(idi[:4])
    wday = dt.date(tahun, bulan, hari)
    wday = wday.strftime("%d %b %Y")
    minut = int(idi[8:])*60
    server_time = str(dt.timedelta(seconds=minut))[0:5]
    if server_time[4:5] == ":":
        server_time = server_time[0:4]

    # print(json.dumps(dataobj, indent=2))

    keyw = {
        "longhuhe_he": "Draw",
        "longhuhe_hu": "Tiger",
        "longhuhe_long": "Dragon",
        "longhuse_longhei": "B-Dra",
        "longhuse_longhong": "R-Dra",
        "longhuse_huhei": "B-Tig",
        "longhuse_huhong": "R-Tig",
    }
    dr = dataobj["cards"]["default"][0]
    tg = dataobj["cards"]["default"][1]
    wink = dataobj["win_key"]

    # warnain text
    if keyw[wink[0]] == "Draw":
        draw = c("green", "  DRAW", 0)
        dr = c("green", dr, 0)
        tg = c("green", dr, 0)

        wday = c("magenta", wday, 0)
        server_time = c("white", server_time, 0)
        disp = f'\t{wday}[{server_time}] {dr} {tg}\t{draw}  '
    elif keyw[wink[0]] == "Dragon":
        dr = c("blue", dr, 0)
    else:
        tg = c("red", tg, 0)

    kd, kt = "█", "█"
    if keyw[wink[1]] == "B-Dra":
        kd = c("black", kd, 0)
    else:
        kd = c("red", kd, 0)
    if keyw[wink[2]] == "B-Tig":
        kt = c("black", kt, 0)
    else:
        kt = c("red", kt, 0)

    wday = c("magenta", wday, 0)
    server_time = c("white", server_time, 0)
    disp = f'\t{wday}[{server_time}]       {dr} {tg} \t{kd}{kt} {keyw[wink[0]]}'

    if dat["gamename"] != "allgame":
        print(disp)
    else:
        if keyw[wink[0]] == "Draw":
            print(f'DragonTiger\t{disp}')
            # if dat["smsg"] == True:
            #     if cnt["dragontiger"] >= 0:
            #         sendmsg(
            #             f'{sym} Draw {dataobj["cards"]["default"][0]} di DragonTiger {cnt["dragontiger"]} putaran')
            #     else:
            #         sendmsg(
            #             f'{sym} Draw {dataobj["cards"]["default"][0]} di DragonTiger')
            # cnt["dragontiger"] = 0
        else:
            cnt["dragontiger"] += 1
            print(f'[{cnt["dragontiger"]}]DragonTiger')


def sicbo(dataobj, st,betting):
    idi = dataobj["game_number"]
    aidi = idi[8:]
    hari = int(idi[6:8])
    bulan = int(idi[4:6])
    tahun = int(idi[:4])
    wday = dt.date(tahun, bulan, hari)
    wday = wday.strftime("%d %b %Y")
    minut = int(idi[8:])*60
    server_time = str(dt.timedelta(seconds=minut))[0:5]
    if server_time[4:5] == ":":
        server_time = server_time[0:4]

    card = f'  {dataobj["cards"][0]} {dataobj["cards"][1]} {dataobj["cards"][2]}'
    bs = dataobj["tip"][1]
    oe = dataobj["tip"][2]

    # warnain text
    if bs == "Big":
        bs = c("red", bs+"  ", 0)
    else:
        bs = c("cyan", bs, 0)
    if oe == "Odd":
        oe = c("blue", oe+" ", 0)
    else:
        oe = c("yellow", oe, 0)
    wday = c("magenta", wday, 0)
    server_time = c("white", server_time, 0)
    if dataobj["cards"][0] == dataobj["cards"][1] and dataobj["cards"][1] == dataobj["cards"][2]:
        # if dat["smsg"] == True:
        #     sendmsg(
        #         f'Cukup Aniiiii.... {dataobj["cards"][0]}{dataobj["cards"][0]}{dataobj["cards"][0]}')
        any = c("green", "ANY TRIPLE", 0)
        disp = f'\t{wday}[{server_time}] {card}\t{any}  {betting}'
    else:
        disp = f'\t{wday}[{server_time}] {card}\t{bs} {oe}  {betting}'

    if dat["gamename"] != "allgame":
        print(disp)
    else:
        if dataobj["cards"][0] == dataobj["cards"][1] and dataobj["cards"][1] == dataobj["cards"][2]:
            print(f'Sicbo\t{disp}')
            # if dat["smsg"] == True:
            #     if cnt[st] >= 0:
            #         sendmsg(
            #             f'{sym} {dataobj["cards"][0]}{dataobj["cards"][0]}{dataobj["cards"][0]} di {st} {cnt[st]} putaran')
            #     else:
            #         sendmsg(
            #             f'{sym} {dataobj["cards"][0]}{dataobj["cards"][0]}{dataobj["cards"][0]} di {st}')
            cnt[st] = 0
        else:
            cnt[st] += 1
            print(f'[{cnt[st]}]{st}')
    

    
    listObj={
        "results":{"bet":[]}
    }
    with open("betting.json", 'w') as json_file:
        json.dump(listObj, json_file, indent=2,  separators=(',',': '))


def baccarat(dataobj):
    idi = dataobj["game_number"]
    aidi = idi[8:]
    hari = int(idi[6:8])
    bulan = int(idi[4:6])
    tahun = int(idi[:4])
    wday = dt.date(tahun, bulan, hari)
    wday = wday.strftime("%d %b %Y")
    minut = int(idi[8:])*60
    server_time = str(dt.timedelta(seconds=minut))[0:5]
    if server_time[4:5] == ":":
        server_time = server_time[0:4]

    pb = "~"
    hsl = dataobj["cards"]["default"]
    if hsl[0] > hsl[1]:
        pb = "p"
    else:
        pb = "b"
    if hsl[0] == hsl[1]:
        pb = "t"

    cp = dataobj["cards"]["player"]
    cb = dataobj["cards"]["banker"]

    # cari big or small
    if cp[2] == "0":
        cp.pop(2)
    if cb[2] == "0":
        cb.pop(2)
    bs = "small"
    if len(cp) != 2:
        bs = "big"
    if len(cb) != 2:
        bs = "big"

    ispair = "|   ~"
    wdh = []
    for pir in cb:
        if pir[1:] not in wdh:
            wdh.append(pir[1:])
        else:
            ispair = c("red", "| bpair", 1)
    wdh.clear()
    for pir in cp:
        if pir[1:] not in wdh:
            wdh.append(pir[1:])
        else:
            ispair = c("blue", "| ppair", 1)

         # warnain text
    tainya = 0
    if pb == "p":
        pb = c("blue", "|    player", 0)
    elif pb == "b":
        pb = c("red", "|    banker", 0)
    else:
        tainya = 1
        pb = c("magenta", "|     tie   ", 0)
    if bs == "big":
        bs = c("red", "| "+bs, 0)
    else:
        bs = c("blue", "| "+bs, 0)
    wday = c("magenta", wday, 0)
    server_time = c("white", server_time, 0)

    disp = f'    {wday} [{server_time}]{pb}\t{ispair}\t{bs}  '

    if dat["gamename"] != "allgame":
        print(disp)
    else:
        if tainya == 1:
            print(f'Baccarat\t{disp}')
            # if dat["smsg"] == True:
            #     if cnt["baccarat"] >= 0:
            #         sendmsg(
            #             f'{sym} Tie di Baccarat {cnt["baccarat"]} putaran')
            #     else:
            #         sendmsg(f'{sym} Tie di Baccarat')
            cnt["baccarat"] = 0
        else:
            cnt["baccarat"] += 1
            print(f'[{cnt["baccarat"]}]Baccarat')


def clor(dataobj):
    idi = dataobj["game_number"]
    aidi = idi[8:]
    hari = int(idi[6:8])
    bulan = int(idi[4:6])
    tahun = int(idi[:4])
    wday = dt.date(tahun, bulan, hari)
    wday = wday.strftime("%d %b %Y")
    minut = int(idi[8:])*60
    server_time = str(dt.timedelta(seconds=minut))[0:5]
    if server_time[4:5] == ":":
        server_time = server_time[0:4]

    p = {
        'game': 'honglv_1',
        'game_number': '202203271169',
        'cards': [8],
        'cards_dic': {'default': ['8']},
        'win_key': ['danma_8'],
        'cards_status': 1,
        'tip': [],
        'next_round_game_number': '202203271170',
        'next_round_draw_at': 1648380600,
        'next_round_countdown': 58
    }
    wrna = {
        "0": "red",
        "1": "green",
        "2": "red",
        "3": "green",
        "4": "red",
        "5": "green",
        "6": "red",
        "7": "green",
        "8": "red",
        "9": "green",
    }
    janda = ["0", "5"]
    wink = str(dataobj["cards"][0])

    disp = f'    {wday} [{server_time}]\t{c(wrna[wink],wink,0)}  '
    if dat["gamename"] != "allgame":
        print(disp)
    else:
        if wink in janda:
            # print(f'Color\t{disp}')
            # if dat["smsg"] == True:
            #     if cnt["color"] >= 0:
            #         sendmsg(f'{sym} Janda di Color {cnt["color"]} putaran')
            #     else:
            #         sendmsg(f'{sym} Janda di Color')
            cnt["color"] = 0
        else:
            cnt["color"] += 1
            print(f'[{cnt["color"]}]Color')


def cek(dataobj):
    p = {
        'type': 'broadcast',
        'action': 'game_do_award',
        'data': {
            'msg_body': {
                'game': 'honglv_1',
                'game_number': '202203271159',
                'cards': [5],
                'cards_dic': {
                    'default': ['5']},
                'win_key': ['danma_5'],
                'cards_status': 1,
                'tip': [],
                'next_round_game_number': '202203271160',
                'next_round_draw_at': 1648380000,
                'next_round_countdown': 58}}}
    try:
        gn = dat["gamename"]
        datagame = dataobj["data"]["msg_body"]["game"]
        dataobj = dataobj["data"]["msg_body"]
        
        with open("betting.json") as json_file:
            ngebet = json.load(json_file)["results"]["bet"]
        if dat["gamename"] == "allgame":
            if datagame == "toubao_1":
                sicbo(dataobj, "sicbo",ngebet)
            elif datagame == "kuaisan_1":
                sicbo(dataobj, "threedice",ngebet)
            elif datagame == "baijiale_1":
                baccarat(dataobj)
            # elif datagame == "lunpan_1":
            #     roulette(dataobj)
            elif datagame == "longhu_1":
                dragontiger(dataobj)
            elif datagame == "honglv_1":
                clor(dataobj)
                print(c("cyan", "------------------------------------", 0))
        else:
            if dataobj["game"] == dat["typegame"] and "cards" in dataobj:
                if gn == "sicbo":
                    sicbo(dataobj, "sicbo",ngebet)
                elif gn == "threedice":
                    sicbo(dataobj, "threedice",ngebet)
                elif gn == "baccarat":
                    baccarat(dataobj)
                # elif gn == "roulette":
                #     roulette(dataobj)
                elif gn == "dragontiger":
                    dragontiger(dataobj)
                elif gn == "color":
                    clor(dataobj)
    except Exception as e:
        print(f"error di {datagame} : {e}")




print("> "+c("green", "Start the program", 0))


def running():
    # with open("user_token.json") as json_file:
    #     tokk = json.load(json_file)
    token = ambil.token()[69]
    dat["tkn"] = token
    # sendmsg("🧧")
    send1 = b"ping"
    
    uriweb = "wss://dt001wsgew.qrdnk.cn/?token="+token

    import _thread as thread

    def on_message(ws, message):
        datadadu = json.loads(message)
        for rer in datadadu:
            if rer["action"] == "game_do_award":
                cek(rer)

    def on_error(ws, error):
        pass

    def on_close(ws, x, y):
        for t in range(1):
            Ioad()
            time.sleep(1)
        running()

    def on_open(ws):
        def run(*args):
            ws.send(send1)
            # ws.close()
        thread.start_new_thread(run, ())

    if __name__ == "__main__":
        # websocket.enableTrace(True)
        ws = websocket.WebSocketApp(uriweb,
                                    on_open=on_open,
                                    on_message=on_message,
                                    on_error=on_error,
                                    on_close=on_close)

        ws.run_forever()


for x in range(random.randint(1, 2)):
    Ioad()
    time.sleep(1)
while True:
    running()
