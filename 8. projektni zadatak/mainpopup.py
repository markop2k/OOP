from PyQt5 import QtWidgets, QtGui, QtCore
import sys

from enumeratori import TipKorisnika, TipArtikla
from korisnik import PoslovniKorisnik, PrivatniKorisnik
from artikl import Automobil, Stan
from prodaja import Prodaja
from utilities import provjera_korisnickog_unosa_privatni, provjera_korisnickog_unosa_poslovni, provjera_unosa_artikla \
    , provjera_unosa_prodaje

korisnici = []
artikli = []
prodaje = []


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('8. Projektni zadatak')
        self.setMinimumSize(QtCore.QSize(1120, 620))
        self.initUI()

    def initUI(self):
        # parent widget
        self.centralwidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.setCentralWidget(self.centralwidget)

        # korisnik
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 1058, 281))
        self.hLayKorisnikArtikl = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.hLayKorisnikArtikl.setContentsMargins(0, 0, 0, 0)

        self.korisnikGroupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.korisnikGroupBox.setMinimumSize(QtCore.QSize(525, 279))
        self.korisnikGroupBox.setMaximumSize(QtCore.QSize(525, 279))
        self.korisnikGroupBox.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.korisnikGroupBox.setTitle("Korisnik")
        self.hLayKorisnikArtikl.addWidget(self.korisnikGroupBox)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.korisnikGroupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(63, 28, 131, 227))

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.korisnikGroupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(14, 28, 49, 227))

        self.gridLayoutWidget = QtWidgets.QWidget(self.korisnikGroupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(214, 28, 297, 191))

        self.vLayKorisnikInput = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vLayKorisnikInput.setContentsMargins(0, 0, 0, 0)

        self.comboBoxTipKorisnika = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBoxTipKorisnika.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBoxTipKorisnika.setMaximumSize(QtCore.QSize(16777215, 25))
        self.vLayKorisnikInput.addWidget(self.comboBoxTipKorisnika)

        for korisnik in TipKorisnika:
            self.comboBoxTipKorisnika.addItem(str(korisnik.value))

        self.comboBoxTipKorisnika.currentTextChanged.connect(self.combobox_changed)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.korisnikGroupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(14, 28, 49, 227))

        self.vLayKorisnikLabels = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.vLayKorisnikLabels.setContentsMargins(0, 0, 0, 0)

        self.prazanLabelKorisnik = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.prazanLabelKorisnik.setMinimumSize(QtCore.QSize(0, 25))
        self.prazanLabelKorisnik.setMaximumSize(QtCore.QSize(16777215, 25))
        self.prazanLabelKorisnik.setText("")
        self.vLayKorisnikLabels.addWidget(self.prazanLabelKorisnik)

        self.labelEmail = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelEmail.setMinimumSize(QtCore.QSize(0, 25))
        self.labelEmail.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEmail.setFont(font)
        self.labelEmail.setText("Email")
        self.vLayKorisnikLabels.addWidget(self.labelEmail)

        self.text_email = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.text_email.setMinimumSize(QtCore.QSize(0, 25))
        self.text_email.setMaximumSize(QtCore.QSize(16777215, 25))
        self.vLayKorisnikInput.addWidget(self.text_email)

        self.labelTelefon = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelTelefon.setMinimumSize(QtCore.QSize(0, 25))
        self.labelTelefon.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTelefon.setFont(font)
        self.labelTelefon.setText("Telefon")
        self.vLayKorisnikLabels.addWidget(self.labelTelefon)

        self.text_telefon = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.text_telefon.setMinimumSize(QtCore.QSize(0, 25))
        self.text_telefon.setMaximumSize(QtCore.QSize(16777215, 25))
        self.vLayKorisnikInput.addWidget(self.text_telefon)

        self.labelIme = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelIme.setMinimumSize(QtCore.QSize(0, 25))
        self.labelIme.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelIme.setFont(font)
        self.labelIme.setText("Ime")
        self.vLayKorisnikLabels.addWidget(self.labelIme)

        self.text_ime = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.text_ime.setMinimumSize(QtCore.QSize(0, 25))
        self.text_ime.setMaximumSize(QtCore.QSize(16777215, 25))
        self.vLayKorisnikInput.addWidget(self.text_ime)

        self.labelNaziv = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelNaziv.setMinimumSize(QtCore.QSize(0, 25))
        self.labelNaziv.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelNaziv.setFont(font)
        self.labelNaziv.setText("Naziv")
        self.labelNaziv.hide()
        self.vLayKorisnikLabels.addWidget(self.labelNaziv)

        self.text_naziv = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.text_naziv.setMinimumSize(QtCore.QSize(0, 25))
        self.text_naziv.setMaximumSize(QtCore.QSize(16777215, 25))
        self.vLayKorisnikInput.addWidget(self.text_naziv)
        self.text_naziv.hide()

        self.labelPrezime = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelPrezime.setMinimumSize(QtCore.QSize(0, 25))
        self.labelPrezime.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelPrezime.setFont(font)
        self.labelPrezime.setText("Prezime")
        self.vLayKorisnikLabels.addWidget(self.labelPrezime)

        self.text_prezime = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.text_prezime.setMinimumSize(QtCore.QSize(0, 25))
        self.text_prezime.setMaximumSize(QtCore.QSize(16777215, 25))
        self.vLayKorisnikInput.addWidget(self.text_prezime)

        self.labelWeb = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelWeb.setMinimumSize(QtCore.QSize(0, 25))
        self.labelWeb.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelWeb.setFont(font)
        self.labelWeb.setText("Web")
        self.labelWeb.hide()
        self.vLayKorisnikLabels.addWidget(self.labelWeb)

        self.text_web = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.text_web.setMinimumSize(QtCore.QSize(0, 25))
        self.text_web.setMaximumSize(QtCore.QSize(16777215, 25))
        self.vLayKorisnikInput.addWidget(self.text_web)
        self.text_web.hide()

        self.gridLayoutWidget = QtWidgets.QWidget(self.korisnikGroupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(214, 28, 297, 191))

        self.gLayPopisKorisnika = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gLayPopisKorisnika.setContentsMargins(0, 0, 0, 0)
        self.labelPopisKorisnika = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelPopisKorisnika.setText("Popis korisnika")
        self.gLayPopisKorisnika.addWidget(self.labelPopisKorisnika, 0, 1, 1, 1)

        self.listPopisKorisnika = QtWidgets.QListWidget(self)
        self.gLayPopisKorisnika.addWidget(self.listPopisKorisnika, 1, 1, 1, 2)

        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setMinimumSize(QtCore.QSize(295, 122))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setLayout(QtWidgets.QVBoxLayout())
        self.scrollArea.setWidget(self.listPopisKorisnika)
        self.gLayPopisKorisnika.addWidget(self.scrollArea, 1, 1, 1, 2)

        self.pushButtonDodajKorisnika = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtonDodajKorisnika.setText("Dodaj korisnika")
        self.pushButtonDodajKorisnika.clicked.connect(self.unos_korisnika)
        self.gLayPopisKorisnika.addWidget(self.pushButtonDodajKorisnika, 2, 1, 1, 1)

        self.pushButtonObrisiKorisnika = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtonObrisiKorisnika.setText("Obriši korisnika")
        self.pushButtonObrisiKorisnika.clicked.connect(self.obrisi_korisnika)
        self.gLayPopisKorisnika.addWidget(self.pushButtonObrisiKorisnika, 2, 2, 1, 1)

        self.label_error = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(50)
        self.label_error.setFont(font)
        self.label_error.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_error.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.gLayPopisKorisnika.addWidget(self.label_error, 3, 1, 1, 2)

        # artikl
        self.artiklGroupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.artiklGroupBox.setMinimumSize(QtCore.QSize(525, 279))
        self.artiklGroupBox.setMaximumSize(QtCore.QSize(525, 279))
        self.artiklGroupBox.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.artiklGroupBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(214, 28, 297, 191))

        self.gLayPopisArtikala = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gLayPopisArtikala.setContentsMargins(0, 0, 0, 0)

        self.labelPopisArtikala = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelPopisArtikala.setText("Popis artikala")
        self.gLayPopisArtikala.addWidget(self.labelPopisArtikala, 0, 1, 1, 1)

        self.pushButtonDodajArtikl = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButtonDodajArtikl.setText("Dodaj artikl")
        self.pushButtonDodajArtikl.clicked.connect(self.unos_artikla)
        self.gLayPopisArtikala.addWidget(self.pushButtonDodajArtikl, 2, 1, 1, 1)

        self.pushButtonObrisiArtikl = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButtonObrisiArtikl.setText("Obriši artikl")
        self.pushButtonObrisiArtikl.clicked.connect(self.obrisi_artikl)
        self.gLayPopisArtikala.addWidget(self.pushButtonObrisiArtikl, 2, 2, 1, 1)

        self.listPopisArtikala = QtWidgets.QListWidget(self.gridLayoutWidget_2)
        self.gLayPopisArtikala.addWidget(self.listPopisArtikala, 1, 1, 1, 2)

        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setMinimumSize(QtCore.QSize(295, 122))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setLayout(QtWidgets.QVBoxLayout())
        self.scrollArea.setWidget(self.listPopisArtikala)
        self.gLayPopisArtikala.addWidget(self.scrollArea, 1, 1, 1, 2)

        self.label_errorArtikl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_errorArtikl.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_errorArtikl.setAlignment(QtCore.Qt.AlignCenter)
        self.gLayPopisArtikala.addWidget(self.label_errorArtikl, 3, 1, 1, 2)

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.artiklGroupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(13, 28, 49, 227))

        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.artiklGroupBox)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(62, 28, 131, 227))
        self.vLayArtiklInput = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.vLayArtiklInput.setContentsMargins(0, 0, 0, 0)

        self.vLayArtiklLabels = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.vLayArtiklLabels.setContentsMargins(0, 0, 0, 0)

        self.comboBoxArtikl = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.comboBoxArtikl.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBoxArtikl.setMaximumSize(QtCore.QSize(16777215, 25))
        self.vLayArtiklInput.addWidget(self.comboBoxArtikl)

        for artikl in TipArtikla:
            self.comboBoxArtikl.addItem(str(artikl.value))

        self.comboBoxArtikl.currentTextChanged.connect(self.combobox_changed_artikl)

        self.prazanLabelArtikl = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.prazanLabelArtikl.setMinimumSize(QtCore.QSize(0, 25))
        self.prazanLabelArtikl.setMaximumSize(QtCore.QSize(16777215, 25))
        self.prazanLabelArtikl.setText("")
        self.vLayArtiklLabels.addWidget(self.prazanLabelArtikl)

        self.labelNaslov = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.labelNaslov.setMinimumSize(QtCore.QSize(0, 25))
        self.labelNaslov.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelNaslov.setFont(font)
        self.labelNaslov.setText("Naslov")
        self.vLayArtiklLabels.addWidget(self.labelNaslov)

        self.text_naslov = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.text_naslov.setMinimumSize(QtCore.QSize(0, 25))
        self.text_naslov.setMaximumSize(QtCore.QSize(16777215, 25))
        self.vLayArtiklInput.addWidget(self.text_naslov)

        self.labelOpis = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.labelOpis.setMinimumSize(QtCore.QSize(0, 25))
        self.labelOpis.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelOpis.setFont(font)
        self.labelOpis.setText("Opis")
        self.vLayArtiklLabels.addWidget(self.labelOpis)

        self.text_opis = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.text_opis.setMinimumSize(QtCore.QSize(0, 25))
        self.text_opis.setMaximumSize(QtCore.QSize(16777215, 25))
        self.vLayArtiklInput.addWidget(self.text_opis)

        self.labelCijena = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.labelCijena.setMinimumSize(QtCore.QSize(0, 25))
        self.labelCijena.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCijena.setFont(font)
        self.labelCijena.setText("Cijena")
        self.vLayArtiklLabels.addWidget(self.labelCijena)

        self.text_cijena = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.text_cijena.setMinimumSize(QtCore.QSize(0, 25))
        self.text_cijena.setMaximumSize(QtCore.QSize(16777215, 25))
        self.vLayArtiklInput.addWidget(self.text_cijena)

        self.labelSnaga = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.labelSnaga.setMinimumSize(QtCore.QSize(0, 25))
        self.labelSnaga.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelSnaga.setFont(font)
        self.labelSnaga.setText("Snaga")
        self.vLayArtiklLabels.addWidget(self.labelSnaga)

        self.text_snaga = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.text_snaga.setMinimumSize(QtCore.QSize(0, 25))
        self.text_snaga.setMaximumSize(QtCore.QSize(16777215, 25))
        self.vLayArtiklInput.addWidget(self.text_snaga)

        self.labelKvadratura = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.labelKvadratura.setMinimumSize(QtCore.QSize(0, 25))
        self.labelKvadratura.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelKvadratura.setFont(font)
        self.labelKvadratura.setText("Kvadrat")
        self.labelKvadratura.hide()
        self.vLayArtiklLabels.addWidget(self.labelKvadratura)

        self.text_kvadratura = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.text_kvadratura.setMinimumSize(QtCore.QSize(0, 25))
        self.text_kvadratura.setMaximumSize(QtCore.QSize(16777215, 25))
        self.text_kvadratura.hide()
        self.vLayArtiklInput.addWidget(self.text_kvadratura)

        self.hLayKorisnikArtikl.addWidget(self.artiklGroupBox)
        self.artiklGroupBox.setTitle("Artikl")

        # prodaja
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 310, 1058, 281))

        self.hLayProdaja = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.hLayProdaja.setContentsMargins(0, 0, 0, 0)

        self.prodajaGroupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget_2)
        self.prodajaGroupBox.setMinimumSize(QtCore.QSize(525, 279))
        self.prodajaGroupBox.setMaximumSize(QtCore.QSize(525, 279))
        self.prodajaGroupBox.setTitle("Prodaja")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.prodajaGroupBox)

        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(68, 40, 131, 137))
        self.vLayProdajaComboBox = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)

        self.vLayProdajaComboBox.setContentsMargins(0, 0, 0, 0)

        self.comboBoxProdajaKorisnik = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        self.comboBoxProdajaKorisnik.setMinimumSize(QtCore.QSize(0, 25))
        # ovo sam default sakrio
        self.comboBoxProdajaKorisnik.hide()
        self.comboBoxProdajaKorisnik.setMaximumSize(QtCore.QSize(16777215, 25))
        self.vLayProdajaComboBox.addWidget(self.comboBoxProdajaKorisnik)

        self.comboBoxProdaja = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        # ovo isto sam default sakrio
        self.comboBoxProdaja.hide()
        self.comboBoxProdaja.setMinimumSize(QtCore.QSize(0, 25))
        self.vLayProdajaComboBox.addWidget(self.comboBoxProdaja)

        self.datumProdaja = QtWidgets.QDateEdit(self.verticalLayoutWidget_5)
        self.vLayProdajaComboBox.addWidget(self.datumProdaja)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.prodajaGroupBox)

        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(22, 40, 43, 137))
        self.vLayProdajaLabels = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)

        self.vLayProdajaLabels.setContentsMargins(0, 0, 0, 0)
        self.labelProdajaKorisnik = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.labelProdajaKorisnik.setMinimumSize(QtCore.QSize(47, 25))
        # ovo isto sam sakrio samo
        self.labelProdajaKorisnik.hide()
        self.labelProdajaKorisnik.setMaximumSize(QtCore.QSize(47, 25))
        self.labelProdajaKorisnik.setText("Korisnik")

        self.vLayProdajaLabels.addWidget(self.labelProdajaKorisnik)
        self.labelProdaja = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.labelProdaja.setMinimumSize(QtCore.QSize(47, 25))
        self.labelProdaja.setMaximumSize(QtCore.QSize(47, 25))
        # ovo isto sam sakrio samo
        self.labelProdaja.hide()
        self.labelProdaja.setText("Prodaja")
        self.vLayProdajaLabels.addWidget(self.labelProdaja)

        self.labelDatum = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.labelDatum.setMinimumSize(QtCore.QSize(47, 25))
        self.labelDatum.setMaximumSize(QtCore.QSize(47, 25))
        self.labelDatum.setText("Datum")
        self.vLayProdajaLabels.addWidget(self.labelDatum)

        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.prodajaGroupBox)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(208, 26, 297, 191))
        self.gLayPopisProdaja = QtWidgets.QGridLayout(self.gridLayoutWidget_3)

        self.gLayPopisProdaja.setContentsMargins(0, 0, 0, 0)
        self.labelPopisProdaja = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.labelPopisProdaja.setText("Popis prodaja")
        self.gLayPopisProdaja.addWidget(self.labelPopisProdaja, 0, 1, 1, 1)

        self.pushButtonDodajProdaju = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButtonDodajProdaju.setText("Dodaj prodaju")
        self.pushButtonDodajProdaju.clicked.connect(self.unos_prodaje)
        self.gLayPopisProdaja.addWidget(self.pushButtonDodajProdaju, 2, 1, 1, 1)

        self.pushButtonObrisiProdaju = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButtonObrisiProdaju.setText("Obriši prodaju")
        self.pushButtonObrisiProdaju.clicked.connect(self.obrisi_prodaju)
        self.gLayPopisProdaja.addWidget(self.pushButtonObrisiProdaju, 2, 2, 1, 1)

        self.listPopisProdaja = QtWidgets.QListWidget(self.gridLayoutWidget_3)
        self.gLayPopisProdaja.addWidget(self.listPopisProdaja, 1, 1, 1, 2)

        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setMinimumSize(QtCore.QSize(295, 122))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setLayout(QtWidgets.QVBoxLayout())
        self.scrollArea.setWidget(self.listPopisProdaja)
        self.gLayPopisProdaja.addWidget(self.scrollArea, 1, 1, 1, 2)

        self.label_errorProdaja = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_errorProdaja.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_errorProdaja.setAlignment(QtCore.Qt.AlignCenter)
        self.gLayPopisProdaja.addWidget(self.label_errorProdaja, 3, 1, 1, 2)

        self.hLayProdaja.addWidget(self.prodajaGroupBox)

        # tu ga definiras
        self.popup_korisnik = QtWidgets.QMessageBox(self)
        self.popup_korisnik.setWindowTitle('Uspjesan unos')
        self.popup_korisnik.setIcon(QtWidgets.QMessageBox.Information)
        self.popup_korisnik.setText('Usjpesno ste unijeli korisnika!')
        self.popup_korisnik.setStandardButtons(QtWidgets.QMessageBox.Cancel)

    def combobox_changed(self):
        if self.comboBoxTipKorisnika.currentText() == TipKorisnika.POSLOVNI.value:
            self.labelIme.hide()
            self.text_ime.hide()
            self.text_prezime.hide()
            self.labelPrezime.hide()
            self.text_web.show()
            self.text_naziv.show()
            self.labelWeb.show()
            self.labelNaziv.show()

        elif self.comboBoxTipKorisnika.currentText() == TipKorisnika.PRIVATNI.value:
            self.labelWeb.hide()
            self.labelNaziv.hide()
            self.text_web.hide()
            self.text_naziv.hide()
            self.text_ime.show()
            self.text_prezime.show()
            self.labelIme.show()
            self.labelPrezime.show()

    def combobox_changed_artikl(self):
        if self.comboBoxArtikl.currentText() == TipArtikla.AUTOMOBIL.value:
            self.labelKvadratura.hide()
            self.text_kvadratura.hide()
            self.text_snaga.show()
            self.labelSnaga.show()

        elif self.comboBoxArtikl.currentText() == TipArtikla.STAN.value:
            self.labelSnaga.hide()
            self.text_snaga.hide()
            self.text_kvadratura.show()
            self.labelKvadratura.show()

    def unos_korisnika(self):

        if self.comboBoxTipKorisnika.currentText() == TipKorisnika.PRIVATNI.value:
            error_privatni = provjera_korisnickog_unosa_privatni(self.text_telefon.text(), self.text_email.text()
                                                                 , self.text_ime.text(), self.text_prezime.text())

            if error_privatni is None:
                korisnici.append(PrivatniKorisnik(self.text_ime.text(), self.text_prezime.text(),
                                                  self.text_telefon.text(), self.text_email.text()))

                # pozoves ovdje za uspjesan unos
                self.popup_korisnik.exec_()
                self.text_telefon.setText('')
                self.text_email.setText('')
                self.text_naziv.setText('')
                self.text_web.setText('')
                self.text_ime.setText('')
                self.text_prezime.setText('')
                self.label_error.setText('')

                korisnik = korisnici[len(korisnici) - 1]
                self.listPopisKorisnika.addItem(korisnik.ispis())
                # ovdje onda otkrio ProdajaKorisnika
                self.comboBoxProdajaKorisnik.show()
                self.labelProdajaKorisnik.show()
                self.comboBoxProdajaKorisnik.addItem(str(korisnik.email))
            else:
                self.label_error.setText(error_privatni)

        elif self.comboBoxTipKorisnika.currentText() == TipKorisnika.POSLOVNI.value:
            error_poslovni = provjera_korisnickog_unosa_poslovni(self.text_telefon.text(), self.text_email.text()
                                                                 , self.text_naziv.text(), self.text_web.text())
            if error_poslovni is None:
                korisnici.append(PoslovniKorisnik(self.text_naziv.text(), self.text_web.text(),
                                                  self.text_telefon.text(), self.text_email.text()))
                # tu isto pozoves
                self.popup_korisnik.exec_()
                self.text_telefon.setText('')
                self.text_email.setText('')
                self.text_naziv.setText('')
                self.text_web.setText('')
                self.text_ime.setText('')
                self.text_prezime.setText('')
                self.label_error.setText('')

                korisnik = korisnici[len(korisnici) - 1]
                self.listPopisKorisnika.addItem(korisnik.ispis())
                # ovdje onda otkrio ProdajaKorisnika
                self.comboBoxProdajaKorisnik.show()
                self.labelProdajaKorisnik.show()
                self.comboBoxProdajaKorisnik.addItem(str(korisnik.email))

            else:
                self.label_error.setText(error_poslovni)

    def obrisi_korisnika(self):
        list_items = self.listPopisKorisnika.selectedItems()
        list_row = self.listPopisKorisnika.currentRow()

        if not list_items:
            return

        for item in list_items:
            self.listPopisKorisnika.takeItem(self.listPopisKorisnika.row(item))

        self.comboBoxProdajaKorisnik.removeItem(list_row)
        # stavio sam da ak ne pise nist u comboboxu da ga opet sakrije samo
        if self.comboBoxProdajaKorisnik.currentText() == '':
            self.comboBoxProdajaKorisnik.hide()
            self.labelProdajaKorisnik.hide()

        del korisnici[list_row]

    def unos_artikla(self):
        if self.comboBoxArtikl.currentText() == TipArtikla.AUTOMOBIL.value:
            error_artikl = provjera_unosa_artikla(self.text_naslov.text(), self.text_opis.text(),
                                                  self.text_cijena.text(),
                                                  self.text_snaga.text())

        elif self.comboBoxArtikl.currentText() == TipArtikla.STAN.value:
            error_artikl = provjera_unosa_artikla(self.text_naslov.text(), self.text_opis.text(),
                                                  self.text_cijena.text(),
                                                  self.text_kvadratura.text())

        if error_artikl is None:
            if self.comboBoxArtikl.currentText() == TipArtikla.AUTOMOBIL.value:
                artikli.append(Automobil(self.text_naslov.text(), self.text_opis.text(), self.text_cijena.text(),
                                         self.text_snaga.text()))

            elif self.comboBoxArtikl.currentText() == TipArtikla.STAN.value:
                artikli.append(Stan(self.text_naslov.text(), self.text_opis.text(), self.text_cijena.text(),
                                    self.text_kvadratura.text()))

            artikl = artikli[len(artikli) - 1]
            self.listPopisArtikala.addItem(artikl.ispis())

            self.comboBoxProdaja.addItem(str(artikl.opis))
            # opet samo prikaz pri unosu artikla
            self.comboBoxProdaja.show()
            self.labelProdaja.show()

            self.text_naslov.setText('')
            self.text_opis.setText('')
            self.text_cijena.setText('')
            self.text_snaga.setText('')
            self.text_kvadratura.setText('')
            self.label_errorArtikl.setText('')

        else:
            self.label_errorArtikl.setText(error_artikl)

    def obrisi_artikl(self):
        list_items = self.listPopisArtikala.selectedItems()
        list_row = self.listPopisArtikala.currentRow()

        if not list_items:
            return

        for item in list_items:
            self.listPopisArtikala.takeItem(self.listPopisArtikala.row(item))

        self.comboBoxProdaja.removeItem(list_row)

        if self.comboBoxProdaja.currentText() == '':
            self.comboBoxProdaja.hide()
            self.labelProdaja.hide()

        del artikli[list_row]

    def unos_prodaje(self):
        error_prodaja = provjera_unosa_prodaje(self.comboBoxProdajaKorisnik.currentText(),
                                               self.comboBoxProdaja.currentText())

        if error_prodaja is None:
            broj_korisnika = int(self.comboBoxProdajaKorisnik.currentIndex())
            broj_artikla = int(self.comboBoxProdaja.currentIndex())

            prodaje.append(Prodaja(self.datumProdaja.date(), korisnici[broj_korisnika], artikli[broj_artikla]))

            prodaja = prodaje[len(prodaje) - 1]
            self.listPopisProdaja.addItem(prodaja.ispis())

            self.label_errorProdaja.setText('')

        else:
            self.label_errorProdaja.setText(error_prodaja)

    def obrisi_prodaju(self):
        list_items = self.listPopisProdaja.selectedItems()
        list_row = self.listPopisProdaja.currentRow()

        if not list_items:
            return

        for item in list_items:
            self.listPopisProdaja.takeItem(self.listPopisProdaja.row(item))

        del prodaje[list_row]


app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
