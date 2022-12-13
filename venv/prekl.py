from PyQt5 import QtWidgets  #nutné nainstalovat knihovnu
import sys

#Program přepisu azbuky do české abecedy (háčky, čárky, proto jsem nevyužil list alphabet)

print(sys.argv)
class Prepis(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.tacitko_konce = QtWidgets.QPushButton('konec')
        self.tacitko_konce.clicked.connect(self.close)
        self.textpole1 = QtWidgets.QLineEdit()
        self.textik1 = QtWidgets.QLabel('prepis')
        self.tlacitko_prepis = QtWidgets.QPushButton('azbuka')
        self.tlacitko_prepis.clicked.connect(self.prek)
        p = QtWidgets.QGridLayout()
        p.addWidget(self.textpole1, 1, 0)
        p.addWidget(self.textik1, 2, 0)
        p.addWidget(self.tlacitko_prepis, 3,0)
        p.addWidget(self.tacitko_konce, 4, 0)
        self.setLayout(p)
        self.show()


    def prek(self):
        self.a=self.textpole1.text()
        self.azb=("А", "а", "Б", "б", "В", "в", "Г", "г", "Д", "д", "Е", "е", "Ё", "ё", "Ж", "ж", "З", "з", "И", "и", "Й", "й", "К", "к", "Л", "л", "М", "м", "Н", "н", "О", "о", "П", "п", "Р", "р", "С", "с", "Т", "т", "У", "у", "Ф", "ф", "Х", "х", "Ц", "ц", "Ч", "ч", "Ш", "ш", "Щ", "щ", "Ъ", "ъ", "Ы", "ы", "Ь", "ь", "Э", "э", "Ю", "ю", "Я", "я")
        self.abc=("A","a","B","b","V","v","G","g","D","d","Ě","ě","JO","jo","Ž","ž","Z","z","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","R","r","S","s","T","t","U","u","F","f","CH","ch","C","c","Č","č","Š","š","ŠČ","šč","^^","^","Y","y","ˇˇ","ˇ","E","e","JU","ju","JA","ja")
        self.b=""
        for j,i in enumerate(self.a):
            print(i,j)
            if i in self.azb:
                self.g=self.azb.index(str(i))
                self.b+=str(self.abc[self.g])
            else:
                self.b+=str(self.a[j])

        self.textik1.setText(str(self.b))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    a = Prepis(windowTitle='Prepis')
    sys.exit(app.exec_())


