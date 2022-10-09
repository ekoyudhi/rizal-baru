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
    tarif_pajak = 0.1

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
    q4 = models.IntegerField(choices=[[1,'Mencatat dan membayar konstribusi wajib'],[2,'Membayar dan melaporkan konstribusi wajib'],[3,'Mencatat dan membayar konstribusi wajib'],[4,'Mencatat, membayar, dan melaporkan konstribusi wajib']], label='4)	Kewajiban Anda sebagai pengusaha UMKM di warga desa Nusa Makmur adalah?')
    q5 = models.IntegerField(choices=[[1,'15 Periode'],[2,'12 Periode']], label='5)Anda harus melaporkan iuran  wajib dalam berapa periode?')
    q6 = models.IntegerField(choices=[[1,'Laba (Rugi)'],[2,'Omset']], label='6) Besarnya pembayaran iuran wajib dihitung dari? (Dasar pengenaan iuran wajib)')
    q7 = models.IntegerField(choices=[[1,'Tidak ada'],[2,'Ada, dari 20% ke 10% dari Laba'],[3,'Ada, dari 10% ke 5% dari Laba'],[4,'Ada, dari 20% ke 10% dari Omset']], label='7) Apakah ada penurunan tarif, berapa besarannya?')
    q8 = models.IntegerField(choices=[[1,'a'],[2,'b'],[3,'c'],[4,'d']], label='8) Pilih penghitungan konstribusi wajib dan pendapatan bersih yang paling tepat (Anda dapat menggunakan kalkulator)<br><img src="https://i.ibb.co/p0DwHt6/q8.png" alt="2022-02-21-195502" border="0" width="600" height="200"><br>Pilih jawaban di bawah?')
    q9 = models.IntegerField(choices=[[1,'Tidak diketahui'],[2,'20% dari total seluruh wajib konstribusi wajib Nusa Makmur'],[3,'20% dari total seluruh periode pelaporan konstribusi wajib'],[4,'20% untuk masing-masing pengusaha pada setiap pelaporan iuran wajib-nya']], label='9) Berapa probabilitas pemeriksaan yang dilakukan oleh Nusa Makmur?')
    q10 = models.IntegerField(choices=[[1,'sebesar 100% dari selisih iuran wajib yang kurang dibayar'],[2,'sebesar 200% dari selisih iuran wajib yang kurang dibayar'],[3,'sebesar 300% dari selisih iuran wajib yang kurang dibayar']],label='10) Besar total denda jika terdapat iuran wajib yang masing kurang dibayar?')
    q11 = models.IntegerField(choices=[[1,'a'],[2,'b'],[3,'c']],label='11) Dari beberapa opsi di bawah ini, pilih hitungan denda yang tepat (Anda dapat menggunakan kalkulator)<br><img src="https://i.ibb.co/PrnvQ1Y/q11.png" alt="q11" border="0" width="600" height="200"><br>Pilih jawaban di bawah?')
    q12 = models.IntegerField(choices=[[1,'a'],[2,'b'],[3,'c']],label='12)	Jika Anda melaporkan omset sebesar 100juta, berapakah pendapatan bersih Anda setelah dikurangi iuran wajib?<br><img src="https://i.ibb.co/cNnKLTJ/q12.png" alt="q12" border="0" width="600" height="200"><br>Pilih jawaban di bawah?')
    q13 = models.IntegerField(choices=[[1,'a'],[2,'b'],[3,'c']],label='13) Jika Anda melaporkan omset hanya sebesar 40juta, berapakah pendapatan bersih Anda setelah dikurangi iuran wajib?<br><img src="https://i.ibb.co/KsQ9CjF/q13.png" alt="q13" border="0" width="600" height="200"><br>Pilih jawaban di bawah?')
    q14 = models.IntegerField(choices=[[1,'a'],[2,'b'],[3,'c']],label='14)	Jika dalam kondisi nomor 13 dan kemudian Anda diperiksa, berapakah pendapatan bersih Anda setelah dikurangi denda yang harus Anda bayarkan?<br><img src="https://i.ibb.co/8K4LtRC/q14.png" alt="q14" border="0" width="600" height="200"><br>Pilih jawaban di bawah?')
    q15 = models.IntegerField(choices=[[1,'51 juta'],[2,'45 juta'],[3,'39 juta']],label='15) Jika dalam kondisi nomor 13 namun Anda tidak termasuk dalam probabilitas pengusaha yang diperiksa, berapakah pendapatan bersih Anda?')
    performance = models.IntegerField(initial=0, blank=False)
    waktu = models.IntegerField(widget=widgets.RadioSelect, label='Waktu', choices=[[30,'30 detik'],[45,'45 detik'],[60,'60 detik']])
    total_omset = models.FloatField(initial=0, blank=False)
    total_biaya = models.FloatField(initial=0, blank=False)
    omset_input = models.FloatField(initial=0, blank=False)
    total_payoff = models.FloatField(initial=0, blank=False)