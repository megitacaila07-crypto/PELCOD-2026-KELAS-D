nama = "caila"
nilai_tugas = 90
nilai_kuis = 93
nilai_ujian = 98
kehadiran = 97

nilai_akhir = ((nilai_tugas * 0.30) + (nilai_kuis * 0.20) + (nilai_ujian * 0.50))

if kehadiran < 75:
    status = "Tidak Lulus"
elif nilai_akhir >= 85 and kehadiran >= 80:
    status = "Lulus dengan Predikat A"
elif nilai_akhir >= 75 and kehadiran >= 80:
    status = "Lulus dengan Predikat B"
elif nilai_akhir >= 65 and kehadiran >= 75:
    status = "Lulus dengan Predikat C"
else:
    status = "Tidak Lulus"

print("===== HASIL PENILAIAN =====")
print("Nama           :", nama)
print("Nilai Akhir    :", nilai_akhir)
print("Kehadiran      :", str(kehadiran) + "%")
print("Status         :", status)