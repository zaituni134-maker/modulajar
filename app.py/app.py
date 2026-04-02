from generator import *
    doc.add_heading('2. Kegiatan Inti (50 Menit)', level=2)
    p2 = doc.add_paragraph()
    p2.add_run("• Tahap 1: Pemberian Rangsangan (Stimulation)\n").bold = True
    p2.add_run(f"Siswa mengamati tayangan visual atau benda konkret yang berkaitan dengan konsep {data['materi']}.\n")
    
    p2.add_run("• Tahap 2: Identifikasi Masalah (Problem Statement)\n").bold = True
    p2.add_run("Guru memberikan pertanyaan pemantik untuk memicu rasa ingin tahu siswa dan diskusi awal secara klasikal.\n")
    
    p2.add_run("• Tahap 3: Pengumpulan Data & Kolaborasi (Data Collection)\n").bold = True
    p2.add_run(f"Siswa dibagi ke dalam kelompok heterogen untuk mengeksplorasi materi {data['materi']} melalui LKPD atau aktivitas praktik mandiri.\n")
    
    p2.add_run("• Tahap 4: Pengolahan Data & Komunikasi (Data Processing)\n").bold = True
    p2.add_run("Setiap kelompok mendiskusikan hasil temuan mereka dan menyajikannya dalam bentuk karya (tulisan/gambar/presentasi).\n")
    
    p2.add_run("• Tahap 5: Pembuktian & Refleksi (Verification)\n").bold = True
    p2.add_run("Guru memberikan penguatan (feedback) terhadap hasil presentasi kelompok untuk meluruskan miskonsepsi.")

    # 3. Penutup
    doc.add_heading('3. Kegiatan Penutup (10 Menit)', level=2)
    p3 = doc.add_paragraph()
    p3.add_run("• Menyimpulkan: ").bold = True
    p3.add_run(f"Siswa bersama guru menyimpulkan poin-poin utama dari pembelajaran materi {data['materi']}.\n")
    p3.add_run("• Evaluasi: ").bold = True
    p3.add_run("Guru melakukan penilaian singkat (post-test) atau refleksi perasaan siswa setelah belajar hari ini.\n")
    p3.add_run("• Tindak Lanjut: ").bold = True
    p3.add_run("Guru memberikan tugas pembiasaan atau menginformasikan materi untuk pertemuan berikutnya, lalu menutup dengan doa.")