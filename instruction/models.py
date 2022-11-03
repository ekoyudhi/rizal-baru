from cProfile import label
from tokenize import blank_re
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
)

doc = """
Instruction
"""


class Constants(BaseConstants):
    players_per_group = None
    num_rounds = 3
    name_in_url = 'Instruction'

    letters_per_word = 1

    use_timeout = True
    seconds_per_period = 60
    tarif_pajak = 0.15

    header = "Kontak Peneliti (Rizal) <a href='http://wa.me/628569041762' target='_blank'>http://wa.me/628569041762</a>"

class Subsession(BaseSubsession):
    pass
    # dictionary = models.StringField()

    # def creating_session(self):
    #     # Create dictionary
    #     letters = list(string.ascii_uppercase)
    #     random.shuffle(letters)
    #     numbers = []
    #     N = list(range(100, 1000))
    #     for i in range(27):
    #         choice = random.choice(N)
    #         N.remove(choice)
    #         numbers.append(choice)
    #     d = [letters, numbers]
    #     dictionary = dict([(d[0][i], d[1][i]) for i in range(26)])
    #     self.dictionary = json.dumps(dictionary)

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    q1 = models.IntegerField(choices=[[1,'Nusa Jaya'],[2,'Nusa Makmur']], label='1) Anda adalah warga desa?')
    q2 = models.IntegerField(choices=[[1,'Karyawan'],[2,'Kepala Desa'],[3,'Pengusaha']], label='2)	Apa pekerjaan Anda di desa tersebut?')
    q3 = models.IntegerField(choices=[[1,'Usaha Mikro Kecil dan Menengah (UMKM)'],[2,'Usaha Besar']], label='3)	Skala kategori besar usaha Anda di desa tersebut adalah')
    q4 = models.IntegerField(choices=[[1,'Mencatat dan membayar iuran wajib'],[2,'Membayar dan melaporkan iuran wajib'],[3,'Mencatat dan melaporkan iuran wajib'],[4,'Mencatat, membayar, dan melaporkan iuran wajib']], label='4)	Kewajiban Anda sebagai pengusaha UMKM di desa Nusa Makmur adalah?')
    q8 = models.IntegerField(choices=[[1,'12 Periode'],[2,'15 Periode']], label='8) Anda harus melaporkan iuran wajib dalam berapa periode?')
    q5 = models.IntegerField(choices=[[1,'Laba (Rugi)'],[2,'Omset Usaha']], label='5) Besarnya pembayaran iuran wajib dihitung dari? (Dasar pengenaan iuran wajib)')
    q6 = models.IntegerField(choices=[[1,'Tidak ada'],[2,'Ada, dari 20% ke 15% dari Laba'],[3,'Ada, dari 20% ke 10% dari Omset Usaha'],[4,'Ada, dari 20% ke 15% dari Omset Usaha']], label='6) Apakah ada penurunan tarif, berapa besarannya?')
    q7 = models.IntegerField(choices=[[1,'a'],[2,'b'],[3,'c'],[4,'d']], label='7) Pilih penghitungan iuran wajib dan pendapatan bersih yang paling tepat (Anda dapat menggunakan kalkulator)<br><img src="https://i.ibb.co/HKSwPJ3/qa.png" alt="2022-02-21-195502" border="0" width="600" height="300"><br>Pilih jawaban di bawah?')
    q9 = models.IntegerField(choices=[[1,'Tidak diketahui'],[2,'20% dari total seluruh wajib iuran wajib Nusa Makmur'],[3,'20% dari total seluruh periode pelaporan iuran wajib'],[4,'20% untuk masing-masing pengusaha pada setiap pelaporan iuran wajib-nya']], label='9) Berapa probabilitas pemeriksaan yang dilakukan oleh Nusa Makmur?')
    q10 = models.IntegerField(choices=[[1,'sebesar 100% dari selisih iuran wajib yang kurang dibayar'],[2,'sebesar 200% dari selisih iuran wajib yang kurang dibayar'],[3,'sebesar 300% dari selisih iuran wajib yang kurang dibayar']],label='10) Besar total denda jika terdapat iuran wajib yang masing kurang dibayar?')
    q11 = models.IntegerField(choices=[[1,'a'],[2,'b'],[3,'c']],label='11) Dari beberapa pilihan di bawah ini, pilih hitungan denda yang tepat (Anda dapat menggunakan kalkulator)<br><img src="https://i.ibb.co/stwPvb6/qb.png" alt="q11" border="0" width="600" height="400"><br>Pilih jawaban di bawah?')
    #Ins2
    q11a = models.IntegerField(choices=[[1,'17'],[2,'80'],[3,'15']],label='1) Jika Anda mendapatkan pertanyaan seperti ini, maka code angka yang benar adalah:<br><img src="https://i.ibb.co/rd2fsss/image-gr1.jpg" alt="q11" border="0" width="600" height="400">')
    q11b = models.IntegerField(choices=[[1,'70'],[2,'80'],[3,'76']],label='2) Dari beberapa pilihan di bawah ini, pilih hitungan denda yang tepat (Anda dapat menggunakan kalkulator)<br><img src="https://i.ibb.co/WgtYfMD/image-gr2.jpg" alt="q11" border="0" width="600" height="400"><br>Pilih jawaban di bawah?')
    #Ins3
    q12 = models.IntegerField(choices=[[1,'a'],[2,'b'],[3,'c']],label='1) Jika Anda melaporkan omset sebesar 100juta, berapakah pendapatan bersih Anda setelah dikurangi iuran wajib? Tarif iuran wajib adalah 15% dikali dengan omset dilaporkan<br><img src="https://i.ibb.co/84cSqdd/q1.png" alt="q12" border="0" width="600" height="300"><br>Pilih jawaban di bawah?')
    q13 = models.IntegerField(choices=[[1,'a'],[2,'b'],[3,'c']],label='2) Jika Anda melaporkan omset hanya sebesar 40juta (melaporkan omset lebih rendah dari omset usaha), berapakah pendapatan bersih Anda setelah dikurangi iuran wajib?<br><img src="https://i.ibb.co/fXWDR44/q2.png" alt="q13" border="0" width="600" height="300"><br>Pilih jawaban di bawah?')
    q14 = models.IntegerField(choices=[[1,'a'],[2,'b'],[3,'c']],label='3) Jika dalam kondisi nomor 2 dan kemudian Anda diperiksa, berapakah pendapatan bersih Anda setelah dikurangi denda yang harus Anda bayarkan? Tarif denda adalah 200% dikali dengan iuran wajib yang masih kurang dibayar (yaitu: iuran wajib yang sebenarnya dikurangi dengan iuran wajib yang dilaporkan).<br><img src="https://i.ibb.co/W3Cg9qK/q3.png" alt="q14" border="0" width="600" height="250"><br>Pilih jawaban di bawah?')
    q15 = models.IntegerField(choices=[[1,'Tetap 49 juta'],[2,'Turun menjadi 35 juta'],[3,'Turun menjadi 22 juta']],label='4) Jika dalam kondisi nomor 2 (melaporkan omset lebih rendah dari omset usaha) namun Anda tidak termasuk dalam probabilitas pengusaha yang diperiksa, berapakah pendapatan bersih Anda?')
    performance = models.IntegerField(initial=0, blank=False)
    waktu = models.IntegerField(widget=widgets.RadioSelect, label='Waktu', choices=[[30,'30 detik'],[45,'45 detik'],[60,'60 detik']])
    total_omset = models.FloatField(initial=0, blank=False)
    total_biaya = models.FloatField(initial=0, blank=False)
    omset_input = models.FloatField(initial=0, blank=False)
    total_payoff = models.FloatField(initial=0, blank=False)