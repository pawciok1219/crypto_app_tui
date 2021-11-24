import math
import time
import pandas as pd
import requests
import matplotlib.pyplot as plt
from datetime import datetime
import re

from asciimatics.effects import Cycle, Stars, Print
from asciimatics.event import KeyboardEvent
from asciimatics.renderers import FigletText, SpeechBubble, BarChart, ColourImageFile
from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, Widget, PopUpDialog
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
from asciimatics.renderers import ImageFile
import sys

from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()


class ListOfCharts(Frame):
    def __init__(self, screen):
        super(ListOfCharts, self).__init__(screen,
                                           screen.height // 5,
                                           screen.width // 5,
                                           hover_focus=True,
                                           can_scroll=False,
                                           title="Lista wykresów")

        options = [("Wykres Bitcoin'a", 1), ("Wykres Etherenum", 2), ("Wykres Binance Coin'a", 3),
                   ("Wykres Tether'a", 4), ("Wykres Solany", 5), ("Wykres Cardano", 6), ("Wykres XRP", 7),
                   ("Wykres Polkadot", 8), ("Wykres Dogecoin'a", 9), ("Wykres Shiba Inu", 10), ("Wykres Litecoin'a", 11)
                   ]

        self.listofcharts_view = ListBox(
            Widget.FILL_FRAME,
            options=options,
            name="menu_chart",
            add_scroll_bar=True,
            on_select=self._edit)

        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(self.listofcharts_view)
        layout.add_widget(Divider())

        layout2 = Layout([1, 1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Ok", self._ok), 0)
        layout2.add_widget(Button("Wróć", self._back), 3)

        self.fix()

    def _edit(self):
        self.save()
        selectOption = self.data['menu_chart']
        if selectOption == 1:
            wykres = generuj_wykres(waluta="bitcoin")
            wykres.plot(y='Cena_w_$USD', x='Okres_czasu', color='#4285F4')
            plt.title("Wykres Bitcoin'a(BTC)")
            plt.show()
        elif selectOption == 2:
            wykres = generuj_wykres(waluta="ethereum")
            wykres.plot(y='Cena_w_$USD', x='Okres_czasu', color='#4285F4')
            plt.title("Wykres Ethereum(ETH)")
            plt.show()
        elif selectOption == 3:
            wykres = generuj_wykres(waluta="binancecoin")
            wykres.plot(y='Cena_w_$USD', x='Okres_czasu', color='#4285F4')
            plt.title("Wykres Binance Coin'a(BNB)")
            plt.show()
        elif selectOption == 4:
            wykres = generuj_wykres(waluta="tether")
            wykres.plot(y='Cena_w_$USD', x='Okres_czasu', color='#4285F4')
            plt.title("Wykres Tether'a(USDT)")
            plt.show()
        elif selectOption == 5:
            wykres = generuj_wykres(waluta="solana")
            wykres.plot(y='Cena_w_$USD', x='Okres_czasu', color='#4285F4')
            plt.title("Wykres Solany(SOL)")
            plt.show()
        elif selectOption == 6:
            wykres = generuj_wykres(waluta="cardano")
            wykres.plot(y='Cena_w_$USD', x='Okres_czasu', color='#4285F4')
            plt.title("Wykres Cardano(ADA)")
            plt.show()
        elif selectOption == 7:
            wykres = generuj_wykres(waluta="ripple")
            wykres.plot(y='Cena_w_$USD', x='Okres_czasu', color='#4285F4')
            plt.title("Wykres XRP(XRP)")
            plt.show()
        elif selectOption == 8:
            wykres = generuj_wykres(waluta="polkadot")
            wykres.plot(y='Cena_w_$USD', x='Okres_czasu', color='#4285F4')
            plt.title("Wykres Polkadot(DOT)")
            plt.show()
        elif selectOption == 9:
            wykres = generuj_wykres(waluta="dogecoin")
            wykres.plot(y='Cena_w_$USD', x='Okres_czasu', color='#4285F4')
            plt.title("Wykres Dogecoin'a(DOGE)")
            plt.show()
        elif selectOption == 10:
            wykres = generuj_wykres(waluta="shiba-inu")
            wykres.plot(y='Cena_w_$USD', x='Okres_czasu', color='#4285F4')
            plt.title("Wykres ShibaInu(SHIB)")
            plt.show()
        elif selectOption == 11:
            wykres = generuj_wykres(waluta="litecoin")
            wykres.plot(y='Cena_w_$USD', x='Okres_czasu', color='#4285F4')
            plt.title("Wykres Litecoin'a(LTC)")
            plt.show()

    def _ok(self):
        self.save()
        selectOption = self.data['menu_chart']
        if selectOption == 1:
            wykres = generuj_wykres(waluta="bitcoin")
            wykres.plot(y='Cena_w_$USD', x='Okres_czasu', color='#4285F4')
            plt.title("Wykres Bitcoin'a(BTC)")
            plt.show()
        elif selectOption == 2:
            wykres = generuj_wykres(waluta="ethereum")
            wykres.plot(y='Cena_w_$USD', x='Okres_czasu', color='#4285F4')
            plt.title("Wykres Ethereum(ETH)")
            plt.show()
        elif selectOption == 3:
            wykres = generuj_wykres(waluta="binancecoin")
            wykres.plot(y='Cena_w_$USD', x='Okres_czasu', color='#4285F4')
            plt.title("Wykres Binance Coin'a(BNB)")
            plt.show()
        elif selectOption == 4:
            wykres = generuj_wykres(waluta="tether")
            wykres.plot(y='Cena_w_$USD', x='Okres_czasu', color='#4285F4')
            plt.title("Wykres Tether'a(USDT)")
            plt.show()
        elif selectOption == 5:
            wykres = generuj_wykres(waluta="solana")
            wykres.plot(y='Cena_w_$USD', x='Okres_czasu', color='#4285F4')
            plt.title("Wykres Solany(SOL)")
            plt.show()
        elif selectOption == 6:
            wykres = generuj_wykres(waluta="cardano")
            wykres.plot(y='Cena_w_$USD', x='Okres_czasu', color='#4285F4')
            plt.title("Wykres Cardano(ADA)")
            plt.show()
        elif selectOption == 7:
            wykres = generuj_wykres(waluta="ripple")
            wykres.plot(y='Cena_w_$USD', x='Okres_czasu', color='#4285F4')
            plt.title("Wykres XRP(XRP)")
            plt.show()
        elif selectOption == 8:
            wykres = generuj_wykres(waluta="polkadot")
            wykres.plot(y='Cena_w_$USD', x='Okres_czasu', color='#4285F4')
            plt.title("Wykres Polkadot(DOT)")
            plt.show()
        elif selectOption == 9:
            wykres = generuj_wykres(waluta="dogecoin")
            wykres.plot(y='Cena_w_$USD', x='Okres_czasu', color='#4285F4')
            plt.title("Wykres Dogecoin'a(DOGE)")
            plt.show()
        elif selectOption == 10:
            wykres = generuj_wykres(waluta="shiba-inu")
            wykres.plot(y='Cena_w_$USD', x='Okres_czasu', color='#4285F4')
            plt.title("Wykres ShibaInu(SHIB)")
            plt.show()
        elif selectOption == 11:
            wykres = generuj_wykres(waluta="litecoin")
            wykres.plot(y='Cena_w_$USD', x='Okres_czasu', color='#4285F4')
            plt.title("Wykres Litecoin'a(LTC)")
            plt.show()

    def _back(self):
        self.save()
        raise NextScene("Menu")


class AmountOfCurrency(Frame):
    def __init__(self, screen, walutaZ, walutaNa):
        super(AmountOfCurrency, self).__init__(screen,
                                               screen.height // 4,
                                               screen.width * 2 // 4,
                                               hover_focus=True,
                                               can_scroll=False,
                                               title="Wprowadź wartość")

        self.walutaZ = walutaZ
        self.walutaNa = walutaNa

        self.r = cg.get_coin_by_id(self.walutaZ)
        symbolZ = self.r["symbol"]
        self.kursnausd = self.r["market_data"]["current_price"]["usd"]

        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Text(label=f"Mam ({symbolZ}): ", name="value", validator="^\s*([0-9.]\d*\s*)+$"))
        # ^[0-9.]*$
        layout.add_widget(Divider())
        layout.add_widget(Text(label=f"Aktualny kurs: 1 {symbolZ} = {self.kursnausd} usd", readonly=True))
        layout.add_widget(Divider())

        layout2 = Layout([1, 1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Przelicz", self._go), 1)
        layout2.add_widget(Button("Wróć", self._back), 3)
        self.fix()

    def _go(self):
        global mesageValue
        self.save()
        valueTextBox = self.data['value']

        num_format = re.compile("^\s*([0-9.]\d*\s*)+$")
        isnumber = re.match(num_format, valueTextBox)

        # if valueTextBox == '' or (valueTextBox.isnumeric() == False or ('.' not in valueTextBox)):
        if not isnumber:
            self._scene.add_effect(
                PopUpDialog(self.screen,
                            "Wprowadź wartość liczbową!",
                            ["OK"],
                            has_shadow=True))
            return

        if self.walutaNa == "usd" or self.walutaNa == "eur" or self.walutaNa == "pln":
            kurs = self.r["market_data"]["current_price"][self.walutaNa]
            mesageValue = kurs * float(valueTextBox)
            message = "Otrzymasz: " + str(mesageValue) + f" ({self.walutaNa})"

            self._scene.add_effect(
                PopUpDialog(self.screen,
                            message,
                            ["OK"],
                            has_shadow=False,
                            theme="bright"))
        else:
            walutaNaUSD = self.kursnausd * float(valueTextBox)
            d = cg.get_coin_by_id(self.walutaNa)
            symbolNa = d["symbol"]
            kurs = d["market_data"]["current_price"]["usd"]
            mesageValue = float(walutaNaUSD) / float(kurs)
            message = "Otrzymasz: " + str(mesageValue) + f" ({symbolNa})"

            self._scene.add_effect(
                PopUpDialog(self.screen,
                            message,
                            ["OK"],
                            has_shadow=False,
                            theme="bright"))

    def _back(self):
        self.save()
        raise NextScene("Lista_convert")


class ListConvert(Frame):
    def __init__(self, screen):
        super(ListConvert, self).__init__(screen,
                                          screen.height // 4,
                                          screen.width // 4,
                                          hover_focus=True,
                                          can_scroll=False,
                                          title="Przelicznik")

        options = [("Bitcoin -> USD", 1), ("Etherenum -> USD", 2), ("Dogecoin -> USD", 3), ("Litecoin -> USD", 4),
                   ("Bitcoin -> EUR", 5), ("Etherenum -> EUR", 6), ("Dogecoin -> EUR", 7), ("Litecoin -> EUR", 8),
                   ("Bitcoin -> PLN", 9), ("Etherenum -> PLN", 10), ("Dogecoin -> PLN", 11), ("Litecoin -> PLN", 12),
                   ("Bitcoin -> Ethernum", 13), ("Etherenum -> Bitcoin", 14), ("Bitcoin -> Litecoin", 15),
                   ("Litecoin -> Bitcoin", 16),
                   ("Bitcoin -> Dogecoin", 17), ("Dogecoin -> Bitcoin", 18), ("Etherenum -> Litecoin", 19),
                   ("Litecoin -> Etherenum", 20),
                   ("Etherenum -> Dogecoin", 21), ("Dogecoin -> Etherenum", 22), ("Dogecoin -> Litecoin", 23),
                   ("Litecoin -> Dogecoin", 24)]

        self.listconvert_view = ListBox(
            Widget.FILL_FRAME,
            options=options,
            name="list_convert",
            add_scroll_bar=True,
            on_select=self._go)

        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Text("Wybierz opcje"))
        layout.add_widget(self.listconvert_view)
        layout.add_widget(Divider())

        layout2 = Layout([1, 1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Ok", self._ok, add_box=True), 0)
        layout2.add_widget(Button("Wróć", self._back), 3)

        self.fix()

    def _go(self):
        self.save()
        selectOption = self.data['list_convert']

        if selectOption == 1:
            raise NextScene("btctousd")
        elif selectOption == 2:
            raise NextScene("ethtousd")
        elif selectOption == 3:
            raise NextScene("dogetousd")
        elif selectOption == 4:
            raise NextScene("ltctousd")
        elif selectOption == 5:
            raise NextScene("btctoeur")
        elif selectOption == 6:
            raise NextScene("ethtoeur")
        elif selectOption == 7:
            raise NextScene("dogetoeur")
        elif selectOption == 8:
            raise NextScene("ltctoeur")
        elif selectOption == 9:
            raise NextScene("btctopln")
        elif selectOption == 10:
            raise NextScene("ethtopln")
        elif selectOption == 11:
            raise NextScene("dogetopln")
        elif selectOption == 12:
            raise NextScene("ltctopln")
        elif selectOption == 13:
            raise NextScene("btctoeth")
        elif selectOption == 14:
            raise NextScene("ethtobtc")
        elif selectOption == 15:
            raise NextScene("btctoltc")
        elif selectOption == 16:
            raise NextScene("ltctobtc")
        elif selectOption == 17:
            raise NextScene("btctodoge")
        elif selectOption == 18:
            raise NextScene("dogetobtc")
        elif selectOption == 19:
            raise NextScene("ethtoltc")
        elif selectOption == 20:
            raise NextScene("ltctoeth")
        elif selectOption == 21:
            raise NextScene("ethtodoge")
        elif selectOption == 22:
            raise NextScene("dogetoeth")
        elif selectOption == 23:
            raise NextScene("dogetoltc")
        elif selectOption == 24:
            raise NextScene("ltctodoge")

    def _ok(self):
        self.save()
        selectOption = self.data['list_convert']

        if selectOption == 1:
            raise NextScene("btctousd")
        elif selectOption == 2:
            raise NextScene("ethtousd")
        elif selectOption == 3:
            raise NextScene("dogetousd")
        elif selectOption == 4:
            raise NextScene("ltctousd")
        elif selectOption == 5:
            raise NextScene("btctoeur")
        elif selectOption == 6:
            raise NextScene("ethtoeur")
        elif selectOption == 7:
            raise NextScene("dogetoeur")
        elif selectOption == 8:
            raise NextScene("ltctoeur")
        elif selectOption == 9:
            raise NextScene("btctopln")
        elif selectOption == 10:
            raise NextScene("ethtopln")
        elif selectOption == 11:
            raise NextScene("dogetopln")
        elif selectOption == 12:
            raise NextScene("ltctopln")
        elif selectOption == 13:
            raise NextScene("btctoeth")
        elif selectOption == 14:
            raise NextScene("ethtobtc")
        elif selectOption == 15:
            raise NextScene("btctoltc")
        elif selectOption == 16:
            raise NextScene("ltctobtc")
        elif selectOption == 17:
            raise NextScene("btctodoge")
        elif selectOption == 18:
            raise NextScene("dogetobtc")
        elif selectOption == 19:
            raise NextScene("ethtoltc")
        elif selectOption == 20:
            raise NextScene("ltctoeth")
        elif selectOption == 21:
            raise NextScene("ethtodoge")
        elif selectOption == 22:
            raise NextScene("dogetoeth")
        elif selectOption == 23:
            raise NextScene("dogetoltc")
        elif selectOption == 24:
            raise NextScene("ltctodoge")

    def _back(self):
        self.save()
        raise NextScene("Menu")


class ListCrypto(Frame):
    def __init__(self, screen):
        super(ListCrypto, self).__init__(screen,
                                         screen.height // 4,
                                         screen.width // 4,
                                         hover_focus=True,
                                         can_scroll=False,
                                         title="Kryptowaluty")

        options = [("Bitcoin(BTC)", 1), ("Ethernum(ETH)", 2), ("Binance Coin(BNB)", 3), ("Solana(SOL)", 4),
                   ("Tether(USDT)", 5), ("Cardano(ADA)", 6),
                   ("XRP(XRP)", 7), ("Polkadot(DOT)", 8), ("Dogecoin(DOGE)", 9), ("ShibaInu(SHIB)", 10),
                   ("LiteCoin(LTC)", 11)]

        self.listcrypto_view = ListBox(
            Widget.FILL_FRAME,
            options=options,
            name="list_crypto",
            add_scroll_bar=True,
            on_select=self._go)

        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Text("Wybierz opcje"))
        layout.add_widget(self.listcrypto_view)
        layout.add_widget(Divider())

        layout2 = Layout([1, 1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Ok", self._ok, add_box=True), 0)
        layout2.add_widget(Button("Wróć", self._back), 3)

        self.fix()

    def _go(self):
        self.save()
        selectOption = self.data['list_crypto']
        if selectOption == 1:
            self.save()
            raise NextScene("BTC")
        elif selectOption == 2:
            self.save()
            raise NextScene("ETH")
        elif selectOption == 3:
            self.save()
            raise NextScene("BNB")
        elif selectOption == 4:
            self.save()
            raise NextScene("SOL")
        elif selectOption == 5:
            self.save()
            raise NextScene("USDT")
        elif selectOption == 6:
            self.save()
            raise NextScene("ADA")
        elif selectOption == 7:
            self.save()
            raise NextScene("XRP")
        elif selectOption == 8:
            self.save()
            raise NextScene("DOT")
        elif selectOption == 9:
            self.save()
            raise NextScene("DOGE")
        elif selectOption == 10:
            self.save()
            raise NextScene("SHIB")
        elif selectOption == 11:
            self.save()
            raise NextScene("LTC")

    def _ok(self):
        self.save()
        selectOption = self.data['list_crypto']
        if selectOption == 1:
            self.save()
            raise NextScene("BTC")
        elif selectOption == 2:
            self.save()
            raise NextScene("ETH")
        elif selectOption == 3:
            self.save()
            raise NextScene("BNB")
        elif selectOption == 4:
            self.save()
            raise NextScene("SOL")
        elif selectOption == 5:
            self.save()
            raise NextScene("USDT")
        elif selectOption == 6:
            self.save()
            raise NextScene("ADA")
        elif selectOption == 7:
            self.save()
            raise NextScene("XRP")
        elif selectOption == 8:
            self.save()
            raise NextScene("DOT")
        elif selectOption == 9:
            self.save()
            raise NextScene("DOGE")
        elif selectOption == 10:
            self.save()
            raise NextScene("SHIB")
        elif selectOption == 11:
            self.save()
            raise NextScene("LTC")

    def _back(self):
        self.save()
        raise NextScene("Menu")


class Menu(Frame):
    def __init__(self, screen):
        super(Menu, self).__init__(screen,
                                   screen.height * 2 // 5,
                                   screen.width * 2 // 5,
                                   hover_focus=True,
                                   can_scroll=False,
                                   title="Menu")

        options = [("Kursy kryptowalut", 1), ("Giełdy kryptowalut", 2),
                   ("Opisy kryptowalut", 3), ("Przelicznik kryptowalut", 4), ("Wykresy kryptowalut", 5)]

        self.menu_view = ListBox(
            Widget.FILL_FRAME,
            options=options,
            name="menu",
            add_scroll_bar=True,
            on_select=self._edit)

        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(self.menu_view)
        layout.add_widget(Divider())

        layout2 = Layout([1, 1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Ok", self._ok), 0)
        layout2.add_widget(Button("Wróć", self._back), 2)
        layout2.add_widget(Button("Zamknij", self._quit), 3)

        self.fix()

    def _edit(self):
        self.save()
        selectOption = self.data['menu']
        if selectOption == 1:
            raise NextScene("Kursy")
        elif selectOption == 2:
            raise NextScene("Giełdy")
        elif selectOption == 3:
            raise NextScene("Lista_krypto")
        elif selectOption == 4:
            raise NextScene("Lista_convert")
        elif selectOption == 5:
            raise NextScene("Lista_wykresow")

    def _ok(self):
        self.save()
        selectOption = self.data['menu']
        if selectOption == 1:
            raise NextScene("Kursy")
        elif selectOption == 2:
            raise NextScene("Giełdy")
        elif selectOption == 3:
            raise NextScene("Lista_krypto")
        elif selectOption == 4:
            raise NextScene("Lista_convert")
        elif selectOption == 5:
            raise NextScene("Lista_wykresow")

    def _back(self):
        self.save()
        raise NextScene("First")

    def _quit(self):
        self._scene.add_effect(
            PopUpDialog(self._screen,
                        "Czy jesteś pewien?",
                        ["Tak", "Nie"],
                        has_shadow=True,
                        on_close=self._quit_on_yes))

    @staticmethod
    def _quit_on_yes(selected):
        if selected == 0:
            raise StopApplication("User requested exit")


def dostepne_kryptowaluty():
    url = f'https://api.coingecko.com/api/v3/coins'
    response = requests.get(url)
    data = response.json()

    crypto_ids = []

    for asset in data:
        crypto_ids.append(asset['id'])

    return crypto_ids


def generuj_wykres(waluta, vs_currency='usd', days='max', interval='daily'):
    crypto_ids = dostepne_kryptowaluty()

    if waluta in crypto_ids:
        url = f"https://api.coingecko.com/api/v3/coins/{waluta}/market_chart"
        payload = {'vs_currency': vs_currency, 'days': days, 'interval': interval}
        response = requests.get(url, params=payload)
        data = response.json()

        timestamp_list, price_list = [], []

        for price in data['prices']:
            timestamp_list.append(datetime.fromtimestamp(price[0] / 1000))
            price_list.append(price[1])

        raw_data = {
            'Okres_czasu': timestamp_list,
            'Cena_w_$USD': price_list
        }

        df = pd.DataFrame(raw_data)
        return df
    else:
        print("Nie ma takiej kryptowaluty! ")


def global_shortcuts(event):
    if isinstance(event, KeyboardEvent):
        c = event.key_code
        #  Zatrzymaj aplikacje ctrl+q or ctrl+x
        if c in (17, 24):
            raise StopApplication("User terminated app")
        elif c == 13:
            raise NextScene("Menu")
        elif c == 16:
            globals().update(kolory="bright")


def pobierz_gieldy():
    r = requests.get("https://www.coingecko.com/pl/giełdy")
    df = pd.read_html(r.text)[0][:20]
    df = df[["Giełda", "Waluty", "Pary", "Liczba odwiedzin (SimilarWeb)"]]
    df["Giełda"] = df["Giełda"].apply(lambda x: x.split(" ")[0])
    df["Liczba odwiedzin (SimilarWeb)"] = df["Liczba odwiedzin (SimilarWeb)"].apply(lambda x: x.replace(",0", ""))
    return str(df.head(20))


def pobierzKursWaluty(zakres_poczatku, zakres_konca):
    r = requests.get("https://www.coingecko.com/pl")
    df = pd.read_html(r.text)[0][zakres_poczatku:zakres_konca]

    df = df[["Waluta", "Kurs", "1 h", "24 h", "7 dni"]]
    df["Waluta"] = df["Waluta"].apply(lambda x: x.split(" ")[0])
    return str(df)


def pobierz_kursy():
    r = requests.get("https://www.coingecko.com/pl")
    df = pd.read_html(r.text)[0]

    df = df[["Waluta", "Kurs", "1 h", "24 h", "7 dni", "Kapitalizacja rynkowa"]]
    df["Waluta"] = df["Waluta"].apply(lambda x: x.split(" ")[0])
    return str(df.head(20))


def wv(x):
    return lambda: 1 + math.sin(math.pi * (2 * time.time() + x) / 5)


def demo(screen, scene):
    effects = [
        Cycle(
            screen,
            FigletText("Centrum", font='big'),
            int(screen.height / 2 - 25)),
        Cycle(
            screen,
            FigletText("Kryptowalutowe", font='big'),
            int(screen.height / 2 - 15)),
        Cycle(
            screen,
            ImageFile("icon/bitcoin.jpg",height=23),
            int(screen.height / 2 - 5),
        ),
        Print(screen,
              SpeechBubble("Naciśnij Enter aby przejść do menu..."),
              screen.height - 5),
        Print(screen,
              SpeechBubble("Naciśnij ctrl+q lub ctrl+x aby zamknąć..."),
              screen.height - 3),
        Stars(screen, 300)
    ]

    effects_gielda = [
        Print(screen,
              FigletText("Giełdy  kryptowalut"),
              int(screen.height // 2 - 20),
              colour=Screen.COLOUR_CYAN,
              speed=1),
        Print(screen,
              SpeechBubble(pobierz_gieldy()),
              screen.height - 35, colour=Screen.COLOUR_CYAN),
    ]

    effects_kursy = [
        Print(screen,
              FigletText("Kursy  kryptowalut"),
              int(screen.height // 2 - 20),
              colour=Screen.COLOUR_YELLOW,
              speed=1),
        Print(screen,
              BarChart(
                  13, 60,
                  [wv(1), wv(2), wv(3), wv(4), wv(5), wv(7), wv(8), wv(9)],
                  colour=[c for c in range(1, 3)],
                  axes=BarChart.BOTH,
                  scale=2.0,
                  char="$"),
              x=75, y=12, transparent=False, speed=2),
        Print(screen,
              SpeechBubble(pobierz_kursy()),
              screen.height - 24,
              colour=Screen.COLOUR_YELLOW),
    ]

    effects_btc = [
        Print(screen,
              ColourImageFile(screen, "icon/bitcoin_1.jpg", height=20),
              int(screen.height / 12),
              attr=8),
        Print(screen, SpeechBubble("Aktualny Kurs"),
              screen.height - 24, colour=Screen.COLOUR_GREEN),
        Print(screen,
              SpeechBubble(pobierzKursWaluty(0, 1)),
              screen.height - 22),
        Print(screen, SpeechBubble("Portfele"),
              screen.height - 18, colour=Screen.COLOUR_GREEN),
        Print(screen, SpeechBubble("-- Cypto.com \n"
                                   "-- Ledgar \n"
                                   "-- Trezor \n"
                                   "-- Bitcan"),
              screen.height - 16),
        Print(screen, SpeechBubble("Opis Kryptowaluty"),
              screen.height - 10, colour=Screen.COLOUR_GREEN),
        Print(screen, SpeechBubble(
            "Kryptowaluta wprowadzona w 2009 roku przez osobę (bądź grupę osób) o pseudonimie Satoshi Nakamoto."
            "Wykopał on wtedy\n"
            "pierwszy blok bitcoinów o wartości 50 BTC. Pierwszy, realny kurs bitcoina ustalono na podstawie kosztów"
            " wydobycia.\n"
            "Było to 5 października 2009 r. i za jednego dolara można było wówczas kupić aż 1309 BTC. Dziś role się"
            " odwróciły i\n"
            "to bitcoin jest zdecydowanie droższy."),
              screen.height - 8),

    ]
    effects_eth = [
        Print(screen,
              ColourImageFile(screen, "icon/ethereum_1.jpg", height=20),
              int(screen.height / 12),
              attr=8),
        Print(screen, SpeechBubble("Aktualny Kurs"),
              screen.height - 24, colour=Screen.COLOUR_GREEN),
        Print(screen,
              SpeechBubble(pobierzKursWaluty(1, 2)),
              screen.height - 22),
        Print(screen, SpeechBubble("Portfele"),
              screen.height - 18, colour=Screen.COLOUR_GREEN),
        Print(screen, SpeechBubble("-- Cypto.com \n"
                                   "-- MyEtherWallet \n"
                                   "-- Metamask \n"
                                   "-- Ledgar \n"
                                   "-- Bitcan"),
              screen.height - 16),
        Print(screen, SpeechBubble("Opis Kryptowaluty"),
              screen.height - 9, colour=Screen.COLOUR_GREEN),
        Print(screen, SpeechBubble(
            "Projekt Ethereum ujrzał światło dzienne w styczniu 2014 r. Prace nad nim rozpoczął Vitalik Buterin -"
            " programista i badacz \n"
            "kryptowalut, który wcześniej pracował nad Bitcoinem.Ethereum, podobnie jak Bitcoin, jest systemem"
            " zdecentralizowanym.\n"
            "Oznacza to, że ETH nie podlega pod żaden podmiot zarządzający. Opiera się o technologię blockchain."),
              screen.height - 7),
    ]
    effects_bnb = [
        Print(screen,
              ColourImageFile(screen, "icon/binancecoin_1.jpg", height=20),
              int(screen.height / 12),
              attr=8),
        Print(screen, SpeechBubble("Aktualny Kurs"),
              screen.height - 24, colour=Screen.COLOUR_GREEN),
        Print(screen,
              SpeechBubble(pobierzKursWaluty(2, 3)),
              screen.height - 22),
        Print(screen, SpeechBubble("Portfele"),
              screen.height - 18, colour=Screen.COLOUR_GREEN),
        Print(screen, SpeechBubble("-- Ledgar"),
              screen.height - 16),
        Print(screen, SpeechBubble("Opis Kryptowaluty"),
              screen.height - 13, colour=Screen.COLOUR_GREEN),
        Print(screen, SpeechBubble(
            "Binance Coin to wypuszczony w 2017 roku przez jedną z największych na świecie giełd kryptowalut Binance."
            " Token bazuje na formacie ERC20,\n"
            "a jego całkowita podaż wynosi 200 milionów. Token BNB wykorzystywany jest na giełdzie Binance do"
            " regulowania opłat transakcyjnych,\n"
            "umożliwiając użytkownikom płacenie niższego fee."),
              screen.height - 11),
    ]

    effects_usdt = [
        Print(screen,
              ColourImageFile(screen, "icon/tether_1.jpg", height=20),
              int(screen.height / 12),
              attr=8),
        Print(screen, SpeechBubble("Aktualny Kurs"),
              screen.height - 24, colour=Screen.COLOUR_GREEN),
        Print(screen,
              SpeechBubble(pobierzKursWaluty(3, 4)),
              screen.height - 22),
        Print(screen, SpeechBubble("Portfele"),
              screen.height - 18, colour=Screen.COLOUR_GREEN),
        Print(screen, SpeechBubble("-- Ledgar\n"
                                   "-- Bitcan\n"
                                   "-- Crypto.com"),
              screen.height - 16),
        Print(screen, SpeechBubble("Opis Kryptowaluty"),
              screen.height - 11, colour=Screen.COLOUR_GREEN),
        Print(screen, SpeechBubble(
            "Tether to pierwsza stabilna kryptowaluta, która pojawiła się na giełdzie w 2014 roku w wyniku współpracy"
            " przedsiębiorcy Reeve’a Collinsa,\n"
            "inwestora Brocka Pierce’a i programisty Craiga Sellersa. Należy do grupy tak zwanych stablecoins"
            " powiązanych z konkretnym aktywem w stosunku 1:1.\n"
            "Wartość Tethera zawsze zmierza do wyrównania kursu dolara amerykańskiego (USD), ponieważ właśnie na tej"
            " walucie się opiera."),
              screen.height - 9),
    ]

    effects_sol = [
        Print(screen,
              ColourImageFile(screen, "icon/solana_1.jpg", height=25),
              int(screen.height / 12),
              attr=8),
        Print(screen, SpeechBubble("Aktualny Kurs"),
              screen.height - 24, colour=Screen.COLOUR_GREEN),
        Print(screen,
              SpeechBubble(pobierzKursWaluty(4, 5)),
              screen.height - 22),
        Print(screen, SpeechBubble("Portfele"),
              screen.height - 18, colour=Screen.COLOUR_GREEN),
        Print(screen, SpeechBubble("-- Ledgar"),
              screen.height - 16),
        Print(screen, SpeechBubble("Opis Kryptowaluty"),
              screen.height - 13, colour=Screen.COLOUR_GREEN),
        Print(screen, SpeechBubble(
            "Solana to sieć blockchain skupiająca się na szybkich transakcjach i wysokiej przepustowości. Korzysta z "
            "unikalnej metody szeregowania transakcji, która\n"
            "znacznie poprawia prędkość. Użytkownicy mogą płacić opłaty transakcyjne i wchodzić w interakcje ze smart "
            "kontraktami za pomocą SOL, natywnej kryptowaluty\n"
            "dla tej sieci. Założony w 2017 przez Anatola Yakovenko z Solana Labs, blockchain Solany stosuje nowe "
            "metody weryfikacji transakcji. Bitcoin, Ethereum i wiele\n"
            "innych projektów cierpi na problemy związane ze skalowalnością i prędkością transakcji."
        ),
              screen.height - 11),

    ]

    effects_ada = [
        Print(screen,
              ColourImageFile(screen, "icon/cardano_1.jpg", height=20),
              int(screen.height / 12),
              attr=8),
        Print(screen, SpeechBubble("Aktualny Kurs"),
              screen.height - 24, colour=Screen.COLOUR_GREEN),
        Print(screen,
              SpeechBubble(pobierzKursWaluty(5, 6)),
              screen.height - 22),
        Print(screen, SpeechBubble("Portfele"),
              screen.height - 18, colour=Screen.COLOUR_GREEN),
        Print(screen, SpeechBubble("-- Ledgar\n"
                                   "-- Trezor"),
              screen.height - 16),
        Print(screen, SpeechBubble("Opis Kryptowaluty"),
              screen.height - 12, colour=Screen.COLOUR_GREEN),
        Print(screen, SpeechBubble(
            "Cardano (ADA) to kompleksowa platforma oparta na technologii blockchain, posiadająca własną kryptowalutę "
            "ADA, która została wydana w 2017 roku. Cardano \n"
            "jest projektem zbudowanym od podstaw na własnym kodzie źródłowym. Twórcy mają w planie stworzenie "
            "najbardziej rozbudowanej platformy blockchain, od\n"
            "podstaw na własnym kodzie źródłowym. Twórcy mają w planie stworzenie najbardziej rozbudowanej platformy "
            "blockchain, lepszej niż m.in. Ethereum (ETH)."),
              screen.height - 10),
    ]

    effects_xrp = [
        Print(screen,
              ColourImageFile(screen, "icon/xrp_1.jpg", height=20),
              int(screen.height / 12),
              attr=8),
        Print(screen, SpeechBubble("Aktualny Kurs"),
              screen.height - 24, colour=Screen.COLOUR_GREEN),
        Print(screen,
              SpeechBubble(pobierzKursWaluty(6, 7)),
              screen.height - 22),
        Print(screen, SpeechBubble("Portfele"),
              screen.height - 18, colour=Screen.COLOUR_GREEN),
        Print(screen, SpeechBubble("-- Crypto.com\n"
                                   "-- Trezor\n"
                                   "-- Ledgar"),
              screen.height - 16),
        Print(screen, SpeechBubble("Opis Kryptowaluty"),
              screen.height - 11, colour=Screen.COLOUR_GREEN),
        Print(screen, SpeechBubble(
            "XRP to kryptowaluta używana przez rejestr XRP, która obsługuje międzynarodowe przekazy i wymianę walut. "
            "XRP może działać jako waluta pomostowa w transakcjach\n"
            "obejmujących różne waluty, takie jak dolary amerykańskie, jeny japońskie, euro, franki i inne używane w "
            "sieci XRP. XRP nie może być wydobywany. Powstała w roku 2012."),
              screen.height - 9),
    ]

    effects_dot = [
        Print(screen,
              ColourImageFile(screen, "icon/polkadot_1.jpg", height=20),
              int(screen.height / 12),
              attr=8),
        Print(screen, SpeechBubble("Aktualny Kurs"),
              screen.height - 24, colour=Screen.COLOUR_GREEN),
        Print(screen,
              SpeechBubble(pobierzKursWaluty(7, 8)),
              screen.height - 22),
        Print(screen, SpeechBubble("Portfele"),
              screen.height - 18, colour=Screen.COLOUR_GREEN),
        Print(screen, SpeechBubble("-- Ledger\n"
                                   "-- Fearless Wallet"),
              screen.height - 16),
        Print(screen, SpeechBubble("Opis Kryptowaluty"),
              screen.height - 12, colour=Screen.COLOUR_GREEN),
        Print(screen, SpeechBubble(
            "Polkadot (DOT) to innowacyjna i relatywnie młoda kryptowaluta, która umożlwiwia obsługę wielu "
            "blockchainów jednocześnie. Niewątpliwie zastosowanie i funkcjonalność \n"
            "tej technologii sprawia, że token DOT jest obecnie dostępny na kilkudziesięciu międzynarodowych giełdach "
            "kryptowalut, co w jednoznaczny sposób winduje wartość monety i\n"
            "umożliwia jej dotarcie do jeszcze szerszego grona inwestorów i użytkowników. Sieć Polkadot została "
            "stworzona w 2017 roku przez Gavina Wooda, współzałożyciela Ethereum."),
              screen.height - 10),
    ]

    effects_doge = [
        Print(screen,
              ColourImageFile(screen, "icon/dogecoin_1.jpg", height=20),
              int(screen.height / 12),
              attr=8),
        Print(screen, SpeechBubble("Aktualny Kurs"),
              screen.height - 24, colour=Screen.COLOUR_GREEN),
        Print(screen,
              SpeechBubble(pobierzKursWaluty(8, 9)),
              screen.height - 22),
        Print(screen, SpeechBubble("Portfele"),
              screen.height - 18, colour=Screen.COLOUR_GREEN),
        Print(screen, SpeechBubble("-- Ledger\n"
                                   "-- Trezor"),
              screen.height - 16),
        Print(screen, SpeechBubble("Opis Kryptowaluty"),
              screen.height - 12, colour=Screen.COLOUR_GREEN),
        Print(screen, SpeechBubble(
            "Dogecoin to kryptowaluta oparta na kodzie źródłowym Litecoina, która początkowo miała być internetowym "
            "żartem, opartym na graficznym memie Doge („Pieseł”).\n"
            "Szybko okazało się jednak, że DOGE został pozytywnie przyjęty, zwłaszcza przez użytkowników Reddita, "
            "głównie ze względu na szybkie transfery i bardzo niskie \n"
            "koszty transakcyjne. Sieć DOGE ruszyła dokładnie 6 grudnia 2013 r. Kurs DogeCoina często zależy od "
            "tweetów zamieszczanych przez Elona Muska."),
              screen.height - 10),
    ]

    effects_shib = [
        Print(screen,
              ColourImageFile(screen, "icon/shibainu_1.jpg", height=20),
              int(screen.height / 12),
              attr=8),
        Print(screen, SpeechBubble("Aktualny Kurs"),
              screen.height - 24, colour=Screen.COLOUR_GREEN),
        Print(screen,
              SpeechBubble(pobierzKursWaluty(10, 11)),
              screen.height - 22),
        Print(screen, SpeechBubble("Portfele"),
              screen.height - 18, colour=Screen.COLOUR_GREEN),
        Print(screen, SpeechBubble("-- AtomicWallet\n"
                                   "-- Exodus"),
              screen.height - 16),
        Print(screen, SpeechBubble("Opis Kryptowaluty"),
              screen.height - 12, colour=Screen.COLOUR_GREEN),
        Print(screen, SpeechBubble(
            "Shiba Inu to token, który aspiruje do bycia opartą na Ethereum alternatywą dla dogecoina, popularnego "
            "memecoina. W przeciwieństwie do bitcoina, który został\n"
            "zaprojektowany z myślą o ograniczonej podaży, SHIB celowo charakteryzuje się dużą podażą, wynoszącą "
            "jeden kwadrylion. Został on uruchomiony anonimowo, przez\n"
            "osobę o pseudonimie Ryoshi, w sierpniu 2020 roku."),
              screen.height - 10),
    ]

    effects_ltc = [
        Print(screen,
              ColourImageFile(screen, "icon/litecoin_1.jpg", height=20),
              int(screen.height / 12),
              attr=8),
        Print(screen, SpeechBubble("Aktualny Kurs"),
              screen.height - 24, colour=Screen.COLOUR_GREEN),
        Print(screen,
              SpeechBubble(pobierzKursWaluty(13, 14)),
              screen.height - 22),
        Print(screen, SpeechBubble("Portfele"),
              screen.height - 18, colour=Screen.COLOUR_GREEN),
        Print(screen, SpeechBubble("-- Crypto.com\n"
                                   "-- Trezor\n"
                                   "-- Ledgar\n"
                                   "-- ViaWallet"),
              screen.height - 16),
        Print(screen, SpeechBubble("Opis Kryptowaluty"),
              screen.height - 9, colour=Screen.COLOUR_GREEN),
        Print(screen, SpeechBubble(
            "Kryptowaluta, a także otwartoźródłowy projekt na licencji X11. Zainspirowany i niemal identyczny "
            "technicznie jak bitcoin, litecoin jest tworzony i przekazywany \n"
            "bez udziału centralnego emitenta. Kryptowaluta została stworzona przez programistę pochodzącego z "
            "Wybrzeża Kości Słoniowej, Charliego Lee w 2011 roku."),
              screen.height - 7),
    ]

    scenes = [
        Scene(effects, -1, name="First"),
        Scene(effects_kursy, -1, name="Kursy"),
        Scene(effects_gielda, -1, name="Giełdy"),
        Scene(effects_btc, -1, name="BTC"),
        Scene(effects_eth, -1, name="ETH"),
        Scene(effects_bnb, -1, name="BNB"),
        Scene(effects_usdt, -1, name="USDT"),
        Scene(effects_sol, -1, name="SOL"),
        Scene(effects_ada, -1, name="ADA"),
        Scene(effects_xrp, -1, name="XRP"),
        Scene(effects_dot, -1, name="DOT"),
        Scene(effects_doge, -1, name="DOGE"),
        Scene(effects_shib, -1, name="SHIB"),
        Scene(effects_ltc, -1, name="LTC"),
        Scene([ListConvert(screen)], -1, name="Lista_convert"),
        Scene([ListCrypto(screen)], -1, name="Lista_krypto"),
        Scene([Menu(screen)], -1, name="Menu"),
        Scene([AmountOfCurrency(screen, "bitcoin", "usd")], -1, name="btctousd"),
        Scene([AmountOfCurrency(screen, "bitcoin", "eur")], -1, name="btctoeur"),
        Scene([AmountOfCurrency(screen, "bitcoin", "pln")], -1, name="btctopln"),
        Scene([AmountOfCurrency(screen, "ethereum", "usd")], -1, name="ethtousd"),
        Scene([AmountOfCurrency(screen, "ethereum", "eur")], -1, name="ethtoeur"),
        Scene([AmountOfCurrency(screen, "ethereum", "pln")], -1, name="ethtopln"),
        Scene([AmountOfCurrency(screen, "dogecoin", "usd")], -1, name="dogetousd"),
        Scene([AmountOfCurrency(screen, "dogecoin", "eur")], -1, name="dogetoeur"),
        Scene([AmountOfCurrency(screen, "dogecoin", "pln")], -1, name="dogetopln"),
        Scene([AmountOfCurrency(screen, "litecoin", "usd")], -1, name="ltctousd"),
        Scene([AmountOfCurrency(screen, "litecoin", "eur")], -1, name="ltctoeur"),
        Scene([AmountOfCurrency(screen, "litecoin", "pln")], -1, name="ltctopln"),
        Scene([AmountOfCurrency(screen, "bitcoin", "ethereum")], -1, name="btctoeth"),
        Scene([AmountOfCurrency(screen, "ethereum", "bitcoin")], -1, name="ethtobtc"),
        Scene([AmountOfCurrency(screen, "bitcoin", "litecoin")], -1, name="btctoltc"),
        Scene([AmountOfCurrency(screen, "litecoin", "bitcoin")], -1, name="ltctobtc"),
        Scene([AmountOfCurrency(screen, "bitcoin", "dogecoin")], -1, name="btctodoge"),
        Scene([AmountOfCurrency(screen, "dogecoin", "bitcoin")], -1, name="dogetobtc"),
        Scene([AmountOfCurrency(screen, "ethereum", "litecoin")], -1, name="ethtoltc"),
        Scene([AmountOfCurrency(screen, "litecoin", "ethereum")], -1, name="ltctoeth"),
        Scene([AmountOfCurrency(screen, "ethereum", "dogecoin")], -1, name="ethtodoge"),
        Scene([AmountOfCurrency(screen, "dogecoin", "ethereum")], -1, name="dogetoeth"),
        Scene([AmountOfCurrency(screen, "dogecoin", "litecoin")], -1, name="dogetoltc"),
        Scene([AmountOfCurrency(screen, "litecoin", "dogecoin")], -1, name="ltctodoge"),
        Scene([ListOfCharts(screen)], -1, name="Lista_wykresow")
    ]

    screen.play(scenes, stop_on_resize=False, start_scene=scene, allow_int=True, unhandled_input=global_shortcuts)


last_scene = None
while True:
    try:
        Screen.wrapper(demo, catch_interrupt=True, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene
