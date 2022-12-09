import os, time, datetime, maskpass, cursor
from colorama import Fore as F, init

def start():
    os.system("cls || clear")
    os.system("title @piegio_ HTML Item Auto-Writer")
    cursor.hide()
    try:
        open("items.txt", "a")
        open('./result/results.html', 'a')
    except: pass
    print(F.WHITE + " [ " + F.LIGHTCYAN_EX + datetime.datetime.fromtimestamp(time.time()).strftime("%H:%M:%S") + F.WHITE + " ] - [ " + F.LIGHTCYAN_EX + "DEBUG" + F.WHITE + " ] Insert Items in \"items.txt\" with format \"name= | url= | path= | nosale= | withsale= \"")
    maskpass.askpass(prompt = F.WHITE + " [ " + F.LIGHTCYAN_EX + datetime.datetime.fromtimestamp(time.time()).strftime("%H:%M:%S") + F.WHITE + " ] - [ " + F.LIGHTCYAN_EX + "INPUT" + F.WHITE + " ] Press Enter.", mask = "")
    for item in open("items.txt", "r").read().splitlines():
        it = item.split(" | ")
        name = it[0].replace("@name = ", "")
        tags = it[1].replace("@tags = ", "")
        url = it[2].replace("@url = ", "")
        path = it[3].replace("@path = ", "")
        nosale = it[4].replace("@nosale = ", "")
        withsale = it[5].replace("@withsale = ", "")
        sizes = it[7].replace("@size = ", "")
        img1 = it[6].replace("@imgs = ", "").split(" \ ")[0]
        img2 = it[6].replace("@imgs = ", "").split(" \ ")[1]
        img3 = it[6].replace("@imgs = ", "").split(" \ ")[2]
        img4 = it[6].replace("@imgs = ", "").split(" \ ")[3]
        itmFormat = f"""<div class = "item" style = "display: inline-block; padding: 0px; width: 190px; height: 250px; box-shadow: 0px 0 30px 10px rgba(255, 255, 255, 0);">
    <div class = "cls2" style = "height: auto;"><a href = "./products/{str(path)}"><img class = "im" src = "{str(url)}" style = "width: auto; height: 120px;"></a></div>
    <div class = "itemtitle" style = "height: auto;"><a href = "./products/{str(path)}" style = "color: black; font-size: 85%; text-decoration: none;"><br>{str(name)}</a></div>
    <div class = "cls1" style = "height: auto;"><a href = "./products/{str(path)}" style = "font-family: 'Roboto Mono', monospace; color: black; opacity: 80%; font-size: 85%; text-decoration: line-through !important;"><br>€{str(nosale)} </a></div>
    <div class = "cls1" style = "height: auto;"><a href = "./products/{str(path)}" style = "font-family: 'Roboto Mono', monospace; color: black; font-size: 105%; text-decoration: none">€{str(withsale)}</a></div>
    <div class = "tags" style = "height: auto; font-size: 0px; scale: 0%; color: white; opacity: 0%;"><a href = "./products/{str(path)}" style = "height: auto;">{str(tags)}</a></div>
</div>"""

        pathfile = f"""<!DOCTYPE html>
<html lang = "en">
    <head>
        <meta http-equiv="content-type" content="text/html;charset=utf-8" />
    </head>
    <script src = "https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <style>
    </style>
    <title>Sneakers Reserve - {str(name)}</title>
    <link rel = "icon" href = "../ico.png" type = "image/icon type">
    <link href = "../style.css" rel="stylesheet">
    <meta name = "viewport" content = "width=device-width,initial-scale=1.0">
    <center>
        <div class = "mainpage">
            <a href = "../home.html"><img class = "ico" src = "../ico.png" style="width: 150px; height: auto; padding: 10px;"></a><br>
            <div class = "mid" style = "padding-top:0.1%;margin-top: 1px; width: 40%; height: 1px; border-bottom: 1.5px solid #bbbbbb46; text-align: center; margin-bottom: 30px;"></div>
            <div class = "path" style = "text-decoration:none;height:auto;color:rgb(116, 116, 116);font-size: 70%;"><span class = "pathtext" style = "height: auto; opacity: 60%;">Sneakers Reserve</span> / <a style = "text-decoration:none; color:rgb(116, 116, 116);" href = "../home.html"><span class = "pathtext" style = "height: auto; opacity: 60%;">Catalogo</span></a> / <span class = "pathtext" style = "height: auto;">{str(name)}</span></div><br>
            <br><span class = "parentTitle" style = "color:rgb(83, 83, 83);font-size: 130%;">{str(name)}<br></span><br>
            <a href = ""><img class = "itemImage" src = "{str(img1)}" style = "height: auto;"></a>
            <a href = ""><img class = "itemImage" src = "{str(img2)}" style = "height: auto;"></a>
            <a href = ""><img class = "itemImage" src = "{str(img3)}" style = "height: auto;"></a>
            <a href = ""><img class = "itemImage" src = "{str(img4)}" style = "height: auto;"></a>
            <br><br><span class = "text-decoration-line-through"><br>€{str(nosale)}</span>
            <span style = "color:black;" class = "text"> €{str(withsale)}<br></span>
            <br>
            <button class = "sizebutton" style = "height: 45px;">{str(sizes)} <b>EU</b></button>
            <a href = "https://www.instagram.com/sneakerssreserve"><button class = "orderbutton" style = "height: 45px;">Ordina</button></a>
            <span style = "height: auto;"><br></span>
            <span class = "space"><br></span>
            <div class = "mid" style = "padding-top:0.1%;margin-top: 1px; width: 40%; height: 1px; border-bottom: 1.5px solid #bbbbbb46; text-align: center; margin-bottom: 30px;"></div>
            <span class = "parentTitle" style = "color:black;font-size: 130%;">Prodotti Correlati</span>
            <div style = "height: auto" class = "container">
                <div id = "itm" class = "item" style = "display: inline-block; padding: 0px; width: 190px; height: 250px; box-shadow: 0px 0 30px 10px rgba(255, 255, 255, 0);">
                    <div class = "cls2" style = "height: auto;"><a href = "./j4-lightning"><img class = "im" src = "https://images.stockx.com/360/Air-Jordan-4-Retro-Lightning-2021/Images/Air-Jordan-4-Retro-Lightning-2021/Lv2/img04.jpg?fm=webp&auto=compress&w=576&dpr=1&updated_at=1638476062&h=384&q=75" style = "width: auto; height: 120px;"></a></div>
                    <div class = "itemtitle" style = "height: auto;"><a href = "./j4-lightning" style = "color: black; font-size: 85%; text-decoration: none;"><br>J4 Lightning</a></div>
                    <div class = "cls1" style = "height: auto;"><a href = "./j4-lightning" style = "font-family: 'Roboto Mono', monospace; color: black; opacity: 80%; font-size: 85%; text-decoration: line-through !important;"><br>€220,99 </a></div>
                    <div class = "cls1" style = "height: auto;"><a href = "./j4-lightning" style = "font-family: 'Roboto Mono', monospace; color: black; font-size: 105%; text-decoration: none">€134,99</a></div>
                    <div class = "tags" style = "height: auto; font-size: 0px; scale: 0%; color: white; opacity: 0%;"><a href = "./j4-lightning" style = "height: auto;">scarpe jordan j4 light lightning gialle giallo yellow</a></div>
                </div>
                <div class = "item" style = "display: inline-block; padding: 0px; width: 190px; height: 250px; box-shadow: 0px 0 30px 10px rgba(255, 255, 255, 0);">
                    <div class = "cls2" style = "transform: scale(106%); height: auto;"><a href = "./j1-unc"><img class = "im" src = "https://cdn.discordapp.com/attachments/985798860561596446/1037054076627734638/j1unc.png" style = "width: auto; height: 120px;"></a></div>
                    <div class = "itemtitle" style = "height: auto;"><a href = "./j1-unc" style = "color: black; font-size: 85%; text-decoration: none;"><br>J1 UNC</a></div>
                    <div class = "cls1" style = "height: auto;"><a href = "./j1-unc" style = "font-family: 'Roboto Mono', monospace; color: black; opacity: 80%; font-size: 85%; text-decoration: line-through !important;"><br>€339,99 </a></div>
                    <div class = "cls1" style = "height: auto;"><a href = "./j1-unc" style = "font-family: 'Roboto Mono', monospace; color: black; font-size: 105%; text-decoration: none">€129,99</a></div>
                    <div class = "tags" style = "height: auto; font-size: 0px; scale: 0%; color: white; opacity: 0%;"><a href = "./j1-unc" style = "height: auto;">scarpe jordan 1 j1 unc university blue blu azzurre azzurro cyan camo</a></div>
                </div>
                <div id = "itm" class = "item" style = "display: inline-block; padding: 0px; width: 190px; height: 250px; box-shadow: 0px 0 30px 10px rgba(255, 255, 255, 0);">
                    <div class = "cls2" style = "height: auto;"><a href = "./af1-offUNC"><img class = "im" src = "https://images.stockx.com/360/Nike-Air-Force-1-Low-Off-White-MCA-University-Blue/Images/Nike-Air-Force-1-Low-Off-White-MCA-University-Blue/Lv2/img04.jpg?fm=webp&auto=compress&w=576&dpr=1&updated_at=1635175415&h=384&q=75" style = "width: auto; height: 120px;"></a></div>
                    <div class = "itemtitle" style = "height: auto;"><a href = "./af1-offUNC" style = "color: black; font-size: 85%; text-decoration: none;"><br>AF1 Off UNC</a></div>
                    <div class = "cls1" style = "height: auto;"><a href = "./af1-offUNC" style = "font-family: 'Roboto Mono', monospace; color: black; opacity: 80%; font-size: 85%; text-decoration: line-through !important;"><br>€349,99 </a></div>
                    <div class = "cls1" style = "height: auto;"><a href = "./af1-offUNC" style = "font-family: 'Roboto Mono', monospace; color: black; font-size: 105%; text-decoration: none">€129,99</a></div>
                    <div class = "tags" style = "height: auto; font-size: 0px; scale: 0%; color: white; opacity: 0%;"><a href = "./af1-offUNC" style = "height: auto;">scarpe af1 af air force off offwhite UNC cyan blue blu azzurre azzurro</a></div>
                </div>
                <div id = "itm" class = "item" style = "display: inline-block; padding: 0px; width: 190px; height: 250px; box-shadow: 0px 0 30px 10px rgba(255, 255, 255, 0);">
                    <div class = "cls2" style = "height: auto;"><a href = "./af1-white"><img class = "im" src = "https://images.stockx.com/360/Nike-Air-Force-1-Low-White-07/Images/Nike-Air-Force-1-Low-White-07/Lv2/img04.jpg?fm=webp&auto=compress&w=576&dpr=1&updated_at=1635275427&h=384&q=75" style = "width: auto; height: 120px;"></a></div>
                    <div class = "itemtitle" style = "height: auto;"><a href = "./af1-white" style = "color: black; font-size: 85%; text-decoration: none;"><br>AF1 White</a></div>
                    <div class = "cls1" style = "height: auto;"><a href = "./af1-white" style = "font-family: 'Roboto Mono', monospace; color: black; opacity: 80%; font-size: 85%; text-decoration: line-through !important;"><br>€149,99 </a></div>
                    <div class = "cls1" style = "height: auto;"><a href = "./af1-white" style = "font-family: 'Roboto Mono', monospace; color: black; font-size: 105%; text-decoration: none">€99,99</a></div>
                    <div class = "tags" style = "height: auto; font-size: 0px; scale: 0%; color: white; opacity: 0%;"><a href = "./af1-white" style = "height: auto;">scarpe af1 air force af bianche white bianco</a></div>
                </div>
                <div id = "itm" class = "item" style = "display: inline-block; padding: 0px; width: 190px; height: 250px; box-shadow: 0px 0 30px 10px rgba(255, 255, 255, 0);">
                    <div class = "cls2" style = "height: auto;"><a href = "./j4-blackcat"><img class = "im" src = "https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img04.jpg?fm=webp&auto=compress&w=576&dpr=1&updated_at=1635341304&h=384&q=75" style = "width: auto; height: 120px;"></a></div>
                    <div class = "itemtitle" style = "height: auto;"><a href = "./j4-blackcat" style = "color: black; font-size: 85%; text-decoration: none;"><br>J4 Black Cat</a></div>
                    <div class = "cls1" style = "height: auto;"><a href = "./j4-blackcat" style = "font-family: 'Roboto Mono', monospace; color: black; opacity: 80%; font-size: 85%; text-decoration: line-through !important;"><br>€220,99 </a></div>
                    <div class = "cls1" style = "height: auto;"><a href = "./j4-blackcat" style = "font-family: 'Roboto Mono', monospace; color: black; font-size: 105%; text-decoration: none">€134,99</a></div>
                    <div class = "tags" style = "height: auto; font-size: 0px; scale: 0%; color: white; opacity: 0%;"><a href = "./j4-blackcat" style = "height: auto;">scarpe jordan j4 black cat black nere nero blackcat</a></div>
                </div>
            </div>
            <span class = "space"><br></span>
            <div class = "mid" style = "padding-top:0.5%;margin-top: 1px; width: 70%; height: 1px; border-bottom: 1.5px solid #bbbbbb75; text-align: center; margin-bottom: 30px;"></div>
            <a style = "text-decoration: none;" class = "footer" href = "https://www.instagram.com/sneakerssreserve"><span style = "color: rgb(0, 0, 0); font-size: 125%;" >Sneakers Reserve ®️2022-2023. Tutti i diritti riservati</span></a><br>
            <a href = "./home.html"> <img src = "./ico.png" style="width: 110px; height: auto; padding: 10px;"></a><a href = "https://www.instagram.com/sneakerssreserve">
            </div>
        </div>
    </center>
</html>"""
        open(f"./products/{str(path)}.html", "a", encoding = "utf-8").write(str(pathfile))
        open("./results/items.html", "a")
        if open("./results/items.html", "r").read() == "":
            open("./results/items.html", "a").write(str(itmFormat))
        else:
            open("./results/items.html", "a").write(str("\n" + itmFormat))
        print(F.WHITE + " [ " + F.LIGHTCYAN_EX + datetime.datetime.fromtimestamp(time.time()).strftime("%H:%M:%S") + F.WHITE + " ] - [ " + F.LIGHTCYAN_EX + "DEBUG" + F.WHITE + " ] Item Inserted: " + F.WHITE + str(name))
    maskpass.askpass(prompt = F.WHITE + " [ " + F.LIGHTCYAN_EX + datetime.datetime.fromtimestamp(time.time()).strftime("%H:%M:%S") + F.WHITE + " ] - [ " + F.LIGHTCYAN_EX + "INPUT" + F.WHITE + " ] Press Enter.", mask = "")
    start()
start()