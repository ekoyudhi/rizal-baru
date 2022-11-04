from pyexpat import model
from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


doc = """
After Survey
"""


class Constants(BaseConstants):
    name_in_url = 'AfterSurvey'
    players_per_group = None
    num_rounds = 1

    header = "Kontak Peneliti (Rizal) <a href='http://wa.me/628569041762' target='_blank'>http://wa.me/628569041762</a>"

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    s1 = models.IntegerField(choices=[[1,"Ya, bekerja sebagai Wirausahawan"],[2,"Ya, bekerja sebagai Pekerja Paruh Waktu"],[3,"Ya, bekerja sebagai Pegawai Tetap"],[4,"Belum pernah bekerja"]], label="1) Apakah Anda pernah/sedang bekerja ?")
    s2 = models.IntegerField(choices=[[1,"0 – 3 tahun"],[2,"3 – 6 tahun"],[3,"Lebih dari 6 tahun"]], label="2) Berapa lama masa pengalaman kerja Anda?", blank=True)
    s3 = models.IntegerField(choices=[[1,"Kurang dari 20%"],[2,"20%"],[3,"30%"],[4,"40%"],[5,"50%"],[6,"Lebih dari 50%"]], label="3) Menurut Anda, berapa besar probabilitas dari kemungkinan diperiksa yang Anda rasakan dalam game ini?")
    s4 = models.IntegerField(choices=[[1,"Tidak Adil"],[2,"Cukup Adil"],[3,"Adil"],[4,"Sangat Adil"]], label="4) Seberapa adilkah penghitungan iuran wajib dalam penelitian ini? (tarif dikali dengan omset, bukan dikali laba)")
    s5 = models.IntegerField(choices=[[1,"Tidak Mudah"],[2,"Cukup Mudah"],[3,"Mudah"],[4,"Sangat Mudah"]], label="5) Seberapa mudahkah penghitungan iuran wajib dalam penelitian ini?")
    s6 = models.IntegerField(choices=[[1,"Tidak Setuju"],[2,"Cukup Setuju"],[3,"Setuju"],[4,"Sangat Setuju"]], label="6) Seberapa setuju Anda dengan penurunan tarif dari 20% ke 15% di Nusa Makmur?")
    s7 = models.IntegerField(choices=[[1,"Tidak Percaya"],[2,"Cukup Percaya"],[3,"Percaya"],[4,"Sangat Percaya"]], label="7) Seberapa besar kepercayaan Anda terhadap Nusa Makmur terkait dengan perhitungan estimasi prefilled omset yang diterapkan dalam form pelaporan iuran wajib?", blank=True)
    s8 = models.IntegerField(choices=[[1,"Tidak Perlu"],[2,"Cukup Perlu"],[3,"Perlu"],[4,"Sangat Perlu"]], label="8) Seberapa perlukah penerapan prefilled omset dalam form pelaporan iuran wajib?", blank=True)
    s9 = models.IntegerField(choices=[[1,"Tidak pernah lupa"],[2,"1 s.d. 2 periode"],[3,"3 s.d 5 periode"],[4,"6 s.d 10 periode"],[5,"Lebih dari 10 periode"]], label="9) Seberapa sering Anda lupa untuk mencatat omset usaha Anda dari game ini?")
    s10 = models.IntegerField(choices=[[1,"Tidak Mengerti"],[2,"Cukup Mengerti"],[3,"Mengerti"],[4,"Sangat Mengerti"]], label="10) Menurut Anda, seberapa mengertikah Anda tentang pajak?")
    s11 = models.IntegerField(choices=[[1,"Tidak Paham"],[2,"Cukup Paham"],[3,"Paham"],[4,"Sangat Paham"]], label="11) Seberapa besar pemahaman Anda terkait penggunaan pajak untuk pembiayaan negara?")
    s12 = models.IntegerField(choices=[[1,"Sudah punya"],[2,"Belum punya"]], label="12) Apakah Anda Sudah memiliki NPWP (Nomor Pokok Wajib Pajak)?")
    s13 = models.IntegerField(choices=[[1,"Tidak Berminat"],[2,"Cukup Berminat"],[3,"Berminat"],[4,"Sangat Berminat"]], label="13) Jika belum memiliki NPWP, Bagaimana minat Anda untuk memiliki NPWP?", blank=True)
    s14 = models.IntegerField(choices=[[1,"Belum pernah"],[2,"Sudah pernah"]], label="14) Jika sudah memiliki NPWP, apakah Anda pernah melaporkan SPT (Surat Pemberitahuan) Pajak?", blank=True)
       
    

    t11 = models.IntegerField(label="1) Umur")
    t12 = models.IntegerField(choices=[[1,'Laki-laki'],[2,'Perempuan']], label='2) Jenis Kelamin')
    t13 = models.IntegerField(choices=[[1,"Nanggore Aceh Darussalam"],[2,"Sumatera Utara"],[3,"Sumatera Selatan"],[4,"Sumatera Barat"],[5,"Bengkulu"],[6,"Riau"],[7,"Kepulauan Riau"],[8,"Jambi"],[9,"Lampung"],[10,"Bangka Belitung"],[11,"Kalimantan Barat"],[12,"Kalimantan Timur"],[13,"Kalimantan Selatan"],[14,"Kalimantan Tengah"],[15,"Kalimantan Utara"],[16,"Banten"],[17,"DKI Jakarta"],[18,"Jawa Barat"],[19,"Jawa Tengah"],[20,"DI Yogyakarta"],[21,"Jawa Timur"],[22,"Bali"],[23,"Nusa Tenggara Timur"],[24,"Nusa Tenggara Barat"],[25,"Gorontalo"],[26,"Sulawesi Barat"],[27,"Sulawesi Tengah"],[28,"Sulawesi Utara"],[29,"Sulawesi Tenggara"],[30,"Sulawesi Selatan"],[31,"Maluku Utara"],[32,"Maluku"],[33,"Papua Barat"],[34,"Papua"]], label='3) Provinsi Anda berada saat ini')
    t14 = models.IntegerField(choices=[[1,'Diploma 3 (D3)'],[2,'Sarjana (S1/D4)'],[3,'Magister (S2)'],[4,'Doktoral (S3)']], label='4) Tingkat pendidikan yang sedang berlangsung atau sudah diselesaikan')
    t15 = models.StringField(label="5) Fakultas")
    t16 = models.StringField(label="6) Program Studi")
    t17 = models.IntegerField(choices=[[1,"Matrikulasi"],[2,"Semester I"],[3,"Semester II"],[4,"Semester III"],[5,"Semester IV"],[6,"Semester V"],[7,"Semester VI"],[8,"Semester VII"],[9,"Semester VIII"],[10,"Semester IX"],[11,"Semester X"],[12,"Semester XI"],[13,"Semester XII"],[14,"Semester Lainnya"],[15,"Sudah lulus"]], label='7)	Saat ini Anda sedang di semester berapa?')
    t18 = models.IntegerField(choices=[[1,'Di bawah 500 ribu'],[2,'500 ribu s.d 1 juta'],[3,'1 jt s.d 1,5 jt'],[4,'1,5 jt s.d 2 jt'],[5,'2 jt s.d 2,5 jt'],[6,'di atas 2,5 jt']], label='8)	Rata-rata pengeluaran setiap bulan')
    t19 = models.StringField(label="9) Nomor HP OVO/GOPAY")
    t20 = models.StringField(label="10)	Alamat email alternatif")
    t21 = models.IntegerField(choices=[[1,'OVO'],[2,'GOPAY']], label='11) Metode penerimaan yang diinginkan:')
    t22 = models.IntegerField(choices=[[1,"Tidak Menarik"],[2,"Cukup Menarik"],[3,"Menarik"],[4,"Sangat Menarik"]], label="12) Seberapa menariknya eksperimen ini bagi Anda?")
    t23 = models.LongStringField(label="13)	Kritik dan saran yang ingin Anda sampaikan")
    

    angka_random = models.IntegerField(min=11, max=99, label="2 digit angka")
    periode_terpilih = models.IntegerField(initial=0, blank=False)
    payoff_real = models.FloatField(initial=0, blank=False)

