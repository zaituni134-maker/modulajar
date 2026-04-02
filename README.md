# Modulajar

Aplikasi generator modul ajar untuk pendidikan.

## Cara Menjalankan

1. Pastikan Python dan virtual environment sudah dikonfigurasi.
2. Install dependencies: `pip install streamlit python-docx`
3. Jalankan aplikasi: `streamlit run generator.py`
4. Buka browser di http://localhost:8501

## Fitur

- Input data modul ajar melalui interface web
- Generate dokumen Word (.docx) dengan struktur lengkap modul ajar
- Download modul ajar langsung dari browser

## Cara jalankan (script otomatis)

1. Pastikan `run.sh` executable:
   - `chmod +x run.sh`
2. Jalankan:
   - `./run.sh`
3. Buka:
   - `http://localhost:8502`

## Deploy ke platform hosting

### Streamlit Cloud
- Upload ke GitHub
- Buka `https://share.streamlit.io`
- Pilih repo `zaituni134-maker/modulajar`, branch `main`, file `generator.py`

### Heroku / Render / Railway
- Gunakan file `Procfile`:
  - `web: streamlit run generator.py --server.port $PORT --server.enableCORS false`
- Buat project baru, konek ke repo GitHub, deploy.
