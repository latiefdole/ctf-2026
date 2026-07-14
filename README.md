# CTF-2026 Repository

Ini adalah repository untuk solusi dan file terkait CTF 2026 yang telah dirapikan.

## Struktur Folder & Indexing File

`	ext
Folder PATH listing for volume Windows
Volume serial number is 00000090 F2CA:77FD
C:.
|   .gitignore
|   tree.txt
|   
+---.claude
|       settings.local.json
|       
+---Cryptography
|   +---High
|   |   +---w4a1
|   |   |       ciphertext.txt
|   |   |       pubkey.txt
|   |   |       solve_w4a1.py
|   |   |       Writeup.md
|   |   |       _SOLVED.md
|   |   |       
|   |   \---w4b1
|   |       |   dec_log.txt
|   |       |   dec_log2.txt
|   |       |   rahasia.enc
|   |       |   README.md
|   |       |   repo_dika.tar.gz
|   |       |   requirements.txt
|   |       |   solve_w4b1.py
|   |       |   Writeup.md
|   |       |   
|   |       \---src
|   |               app.py
|   |               config.json
|   |               
|   +---Low
|   |   \---w3a1
|   |           config.bin
|   |           decode_config.py
|   |           decode_stub.c
|   |           key_hint.txt
|   |           Writeup.md
|   |           
|   \---Medium
|       +---w2d3
|       |       dekripsi_darurat
|       |       indonesian_phrases.txt
|       |       Writeup.md
|       |       
|       +---w3a2
|       |       decrypt_flag.py
|       |       encrypted.bin
|       |       extract_exif.py
|       |       extract_jpg_strings.py
|       |       iv.txt
|       |       key_source.jpg
|       |       readme (1).txt
|       |       solve_aes.py
|       |       Writeup.md
|       |       
|       \---w3a3
|               cipher_info.txt
|               decrypt_target.py
|               reconstruct_cipher.py
|               samples.txt
|               target.txt
|               Writeup.md
|               
+---Digital_Forensics
|   |   generate_writeups.py
|   |   test.pdf
|   |   
|   +---High
|   |   +---c6v4
|   |   |       ciphertext.txt
|   |   |       disasm.txt
|   |   |       feistel_enc
|   |   |       keys.txt
|   |   |       solve_c6v4.py
|   |   |       test_vector.txt
|   |   |       Writeup.md
|   |   |       
|   |   +---case1v4
|   |   |       disasm.txt
|   |   |       func_table
|   |   |       solve_xor.py
|   |   |       Writeup.md
|   |   |       
|   |   \---case2v4
|   |           params.txt
|   |           readme (2).txt
|   |           solve.py
|   |           Writeup.md
|   |           
|   +---Low
|   |   +---case2
|   |   |       analyst_note.txt
|   |   |       encoded_memo.txt
|   |   |       server_log.txt
|   |   |       solve_case2.py
|   |   |       Writeup.md
|   |   |       
|   |   +---case3
|   |   |       narasi.txt
|   |   |       traffic.pcap
|   |   |       Writeup.md
|   |   |       
|   |   +---case3v2
|   |   |       hint.txt
|   |   |       image.png
|   |   |       Writeup.md
|   |   |       
|   |   +---case5v4
|   |   |       dokumen_biasa.bin
|   |   |       hint.txt
|   |   |       rahasia.hash
|   |   |       rahasia.zip
|   |   |       Writeup.md
|   |   |       
|   |   +---case6
|   |   |       case6_strings.txt
|   |   |       perangkat_lunak_terkunci
|   |   |       Writeup.md
|   |   |       
|   |   +---case7 foto mencurigakan
|   |   |   |   foto_kantor.jpg
|   |   |   |   hidden.txt
|   |   |   |   readme_analis.txt
|   |   |   |   steghide.zip
|   |   |   |   steghide_extract.py
|   |   |   |   stego_check.py
|   |   |   |   Writeup.md
|   |   |   |   
|   |   |   +---steghide
|   |   |   |   |   about-nls.txt
|   |   |   |   |   bugs.txt
|   |   |   |   |   copying.txt
|   |   |   |   |   credits.txt
|   |   |   |   |   cygiconv-2.dll
|   |   |   |   |   cygintl-2.dll
|   |   |   |   |   cygjpeg-62.dll
|   |   |   |   |   cygmcrypt-4.dll
|   |   |   |   |   cygmhash-2.dll
|   |   |   |   |   cygwin1.dll
|   |   |   |   |   cygz.dll
|   |   |   |   |   history.txt
|   |   |   |   |   LEAME.txt
|   |   |   |   |   manual.pdf
|   |   |   |   |   manual_es.pdf
|   |   |   |   |   README.txt
|   |   |   |   |   steghide.exe
|   |   |   |   |   todo.txt
|   |   |   |   |   
|   |   |   |   \---locale
|   |   |   |       +---de
|   |   |   |       |   \---LC_MESSAGES
|   |   |   |       |           steghide.mo
|   |   |   |       |           
|   |   |   |       +---es
|   |   |   |       |   \---LC_MESSAGES
|   |   |   |       |           steghide.mo
|   |   |   |       |           
|   |   |   |       +---fr
|   |   |   |       |   \---LC_MESSAGES
|   |   |   |       |           steghide.mo
|   |   |   |       |           
|   |   |   |       \---ro
|   |   |   |           \---LC_MESSAGES
|   |   |   |                   steghide.mo
|   |   |   |                   
|   |   |   \---steghide_ext
|   |   |       \---steghide
|   |   |           |   about-nls.txt
|   |   |           |   bugs.txt
|   |   |           |   copying.txt
|   |   |           |   credits.txt
|   |   |           |   cygiconv-2.dll
|   |   |           |   cygintl-2.dll
|   |   |           |   cygjpeg-62.dll
|   |   |           |   cygmcrypt-4.dll
|   |   |           |   cygmhash-2.dll
|   |   |           |   cygwin1.dll
|   |   |           |   cygz.dll
|   |   |           |   history.txt
|   |   |           |   LEAME.txt
|   |   |           |   manual.pdf
|   |   |           |   manual_es.pdf
|   |   |           |   README.txt
|   |   |           |   steghide.exe
|   |   |           |   todo.txt
|   |   |           |   
|   |   |           \---locale
|   |   |               +---de
|   |   |               |   \---LC_MESSAGES
|   |   |               |           steghide.mo
|   |   |               |           
|   |   |               +---es
|   |   |               |   \---LC_MESSAGES
|   |   |               |           steghide.mo
|   |   |               |           
|   |   |               +---fr
|   |   |               |   \---LC_MESSAGES
|   |   |               |           steghide.mo
|   |   |               |           
|   |   |               \---ro
|   |   |                   \---LC_MESSAGES
|   |   |                           steghide.mo
|   |   |                           
|   |   \---case8 aktivasi sistem
|   |           aktivasi_sistem
|   |           case8_strings.txt
|   |           Writeup.md
|   |           
|   +---Medium
|   |   +---case1
|   |   |       cipher_text.txt
|   |   |       company_logo - Copy.txt
|   |   |       company_logo.jpg
|   |   |       readme (1).txt
|   |   |       solve_case1.py
|   |   |       solve_vig.py
|   |   |       Writeup.md
|   |   |       
|   |   +---case2v2
|   |   |       analyze.py
|   |   |       decode.py
|   |   |       kode_akses
|   |   |       solve_strings.py
|   |   |       Writeup.md
|   |   |       
|   |   +---case4
|   |   |       pemeriksa_kredensial
|   |   |       Writeup.md
|   |   |       
|   |   +---case4v4
|   |   |       aperisolve.py
|   |   |       aperisolve2.py
|   |   |       aperisolve3.py
|   |   |       assembly_note.txt
|   |   |       city_map.txt
|   |   |       foto_1.jpg
|   |   |       foto_2.jpg
|   |   |       foto_3.jpg
|   |   |       gps_parse.py
|   |   |       jawa_cities.txt
|   |   |       jpeg_analyze.py
|   |   |       jpeg_dct_extract.py
|   |   |       profile.jpg
|   |   |       Writeup.md
|   |   |       
|   |   +---case5
|   |   |       config.bin
|   |   |       key_hint.txt
|   |   |       partial_source.c
|   |   |       Writeup.md
|   |   |       
|   |   \---case_redacted_report
|   |           analyze2.py
|   |           analyze3.py
|   |           analyze_redacted.py
|   |           email_thread_dl.txt
|   |           index_dl.html
|   |           jpeg_analyze.py
|   |           notes_raw.html
|   |           operator_note.txt
|   |           profile.jpg
|   |           redacted_report.html
|   |           signal.txt
|   |           signal_raw.py
|   |           static_noise.txt
|   |           Writeup.md
|   |           
|   \---Unclassified
|       +---w2a2
|       |       cert_cn.txt
|       |       encoded_data.txt
|       |       key_hint.txt
|       |       partial_src.py
|       |       
|       +---w2a3
|       |       hidden_a3.txt
|       |       lampiran_surat.jpg
|       |       laporan_ancaman.html
|       |       solve_w2a3.py
|       |       
|       +---w2e1
|       |       mem_fragment.bin
|       |       process_list.txt
|       |       readme_forensik.txt
|       |       
|       +---w2e2
|       |       disk.img
|       |       tool_guide.txt
|       |       
|       +---w3b1
|       |   |   readme (1).txt
|       |   |   repo.zip
|       |   |   
|       |   \---repo
|       |       \---devnusa_repo
|       |           |   client.py
|       |           |   config.py
|       |           |   README.md
|       |           |   
|       |           \---.git
|       |               |   COMMIT_EDITMSG
|       |               |   config
|       |               |   description
|       |               |   HEAD
|       |               |   index
|       |               |   
|       |               +---hooks
|       |               |       applypatch-msg.sample
|       |               |       commit-msg.sample
|       |               |       fsmonitor-watchman.sample
|       |               |       post-update.sample
|       |               |       pre-applypatch.sample
|       |               |       pre-commit.sample
|       |               |       pre-merge-commit.sample
|       |               |       pre-push.sample
|       |               |       pre-rebase.sample
|       |               |       pre-receive.sample
|       |               |       prepare-commit-msg.sample
|       |               |       push-to-checkout.sample
|       |               |       sendemail-validate.sample
|       |               |       update.sample
|       |               |       
|       |               +---info
|       |               |       exclude
|       |               |       
|       |               +---logs
|       |               |   |   HEAD
|       |               |   |   
|       |               |   \---refs
|       |               |       \---heads
|       |               |               master
|       |               |               
|       |               +---objects
|       |               |   +---05
|       |               |   |       ec7fd6adeb8f692a7af1e0829fc4fa390526f3
|       |               |   |       
|       |               |   +---08
|       |               |   |       234b6f32e3468157e9b344b4be51ea3f1634b0
|       |               |   |       
|       |               |   +---17
|       |               |   |       cc2d46d8f67fd6725a6573cfbb92dc3014728c
|       |               |   |       
|       |               |   +---22
|       |               |   |       5e277c284a688b1e923ea7f4ee114c8a8dbcfc
|       |               |   |       
|       |               |   +---39
|       |               |   |       0ab795a0a2bb57a36bc4c76c525900da8a6102
|       |               |   |       
|       |               |   +---5a
|       |               |   |       bd1c472d3734b96e3072c34fa054913f3ebfe8
|       |               |   |       
|       |               |   +---7a
|       |               |   |       db5b0afaa937251e79c59362dba2fba7ee7cb5
|       |               |   |       
|       |               |   +---a0
|       |               |   |       e090be51f44e0cfa56a0db6e18a3af3bcace64
|       |               |   |       
|       |               |   +---ba
|       |               |   |       2d32adcdc86c8c525764a4f6569eb87dad1f50
|       |               |   |       
|       |               |   +---c3
|       |               |   |       930bb67039f9b7ea3da5306f6633994dd5ced5
|       |               |   |       
|       |               |   +---info
|       |               |   \---pack
|       |               \---refs
|       |                   +---heads
|       |                   |       master
|       |                   |       
|       |                   \---tags
|       +---w3e1
|       |       decrypt_tls.py
|       |       parse_pcap.py
|       |       parse_pcapng.py
|       |       sslkeys.txt
|       |       traffic.pcap
|       |       
|       +---w3e2
|       |       analyze_disk.py
|       |       case_notes.txt
|       |       forensic_disk.img
|       |       search_flag.py
|       |       
|       +---w4e1
|       |       case_info.txt
|       |       linux_profile.zip
|       |       memory.lime
|       |       
|       \---w4e2
|               encrypted_note.enc
|               hid_usage.txt
|               keyboard_session.pcap
|               readme (1).txt
|               
+---Misc
|   |   ctf_main.html
|   |   
|   +---ctf_downloads
|   +---High
|   +---loose_scripts
|   |       cookies_new.txt
|   |       crack.py
|   |       exploit.py
|   |       exploit2.py
|   |       login_1c8.py
|   |       payload_uploaded.html
|   |       public.pem
|   |       resp.html
|   |       resp2.html
|   |       resp3.html
|   |       section_data.bin
|   |       section_rodata.bin
|   |       section_text.bin
|   |       solve_w2a2.py
|   |       solve_w2d2.py
|   |       ssrf2.py
|   |       ssrf3.py
|   |       ssrf4.py
|   |       ssrf5.py
|   |       ssrf6.py
|   |       ssrf7.py
|   |       ssrf8.py
|   |       ssrf_backup.py
|   |       ssrf_cron.py
|   |       ssrf_enum.py
|   |       ssrf_flag.py
|   |       ssrf_privesc.py
|   |       ssrf_redis.py
|   |       ssrf_resp.py
|   |       ssrf_sudo.py
|   |       ssrf_test.py
|   |       ssti_find.py
|   |       test.php
|   |       test_bypass.py
|   |       upload.php
|   |       uploads_dir.html
|   |       upload_page.html
|   |       upload_source.html
|   |       w3c1_response.html
|   |       
|   +---Low
|   \---Medium
|       \---w3f1
|               protocol_log.bin
|               protocol_spec.txt
|               solve_w3f1.py
|               Writeup.md
|               _SOLVED.md
|               
+---OSINT
|   +---High
|   |   \---w3b3
|   |       |   analisis.html
|   |       |   bypass_403.py
|   |       |   candidates_list.txt
|   |       |   crawl_output.txt
|   |       |   crawl_result.json
|   |       |   downloader.py
|   |       |   forum_post.html
|   |       |   generate_candidates.py
|   |       |   generate_grouped_candidates.py
|   |       |   generate_new_candidates.py
|   |       |   grouped_candidates.md
|   |       |   index.html
|   |       |   poll_crawl.ps1
|   |       |   probe.py
|   |       |   probe_private.py
|   |       |   probe_root.py
|   |       |   profil.html
|   |       |   profile_analysis.txt
|   |       |   search_patterns.py
|   |       |   solve.py
|   |       |   Writeup.md
|   |       |   _ANALYSIS.md
|   |       |   
|   |       \---downloads
|   |               analisis.html
|   |               archive_archived_post.html
|   |               decoy_token.txt
|   |               forum_post.html
|   |               index.html
|   |               index_root.html
|   |               operator_note.txt
|   |               persona_cross.json
|   |               pgp_pubkey.asc
|   |               profil.html
|   |               profile_analysis.txt
|   |               robots.txt
|   |               
|   +---Low
|   |   \---w3b2
|   |           attacker_site.html
|   |           config_leak.txt
|   |           email_thread.txt
|   |           index.html
|   |           internal_doc.pdf.txt
|   |           kasus_aktif.html
|   |           linkedin_export.html
|   |           profile_photo.jpg
|   |           tentang.html
|   |           whois_record.txt
|   |           Writeup.md
|   |           _SOLVED.md
|   |           
|   \---Medium
|       \---W2-B3
|               attacker_cv.html
|               company_doc.html
|               email_thread.txt
|               index.html
|               leaked_config.txt
|               linkedin_export.txt
|               robots.txt
|               solve_w2b3.py
|               whois_dump.txt
|               Writeup.md
|               _ANALISA.md
|               
+---Reverse_Engineering
|   +---High
|   |   \---w4d3
|   |           disasm.txt
|   |           solve_w4d3.py
|   |           vm8_chall
|   |           vm8_spec.txt
|   |           Writeup.md
|   |           xor_key_hint.txt
|   |           
|   +---Low
|   |   \---w2d2
|   |           validator
|   |           Writeup.md
|   |           
|   \---Medium
|       +---w3d1
|       |       solve_w3d1.py
|       |       vm_chall
|       |       vm_spec.txt
|       |       Writeup.md
|       |       _SOLVED.md
|       |       
|       +---w3d2
|       |       analyze_elf.py
|       |       antidebug
|       |       dump_data.py
|       |       Writeup.md
|       |       
|       +---w3d3
|       |       analyze_vm2_binary.py
|       |       simulate_vm2.py
|       |       vm2_chall
|       |       vm2_spec.txt
|       |       Writeup.md
|       |       
|       \---w4d1
|               checker.pyc
|               solve_w4d1.py
|               Writeup.md
|               _SOLVED.md
|               
\---Web_Exploitation
    +---High
    |   +---W2-C3
    |   |       .pass
    |   |       .user
    |   |       cj.txt
    |   |       dash_admin.html
    |   |       dash_guest.html
    |   |       diag1.html
    |   |       diag2.html
    |   |       index.hdr
    |   |       index.html
    |   |       login.hdr
    |   |       login.php.html
    |   |       login2.html
    |   |       login_resp.html
    |   |       monitor_index.html
    |   |       monitor_listing.txt
    |   |       r.html
    |   |       register.php.html
    |   |       reg_resp.html
    |   |       robots.txt
    |   |       src_diag.php.txt
    |   |       src_login.php.txt
    |   |       Writeup.md
    |   |       _SOLVED.md
    |   |       
    |   \---w3c3
    |           exploit.py
    |           out54.txt
    |           out67.txt
    |           out70.txt
    |           parse_transcript.py
    |           phase10.py
    |           phase100.py
    |           phase101.py
    |           phase102.py
    |           phase103.py
    |           phase104.py
    |           phase105.py
    |           phase106.py
    |           phase107.py
    |           phase108.py
    |           phase109.py
    |           phase10_new.py
    |           phase11.py
    |           phase110.py
    |           phase111.py
    |           phase112.py
    |           phase113.py
    |           phase114.py
    |           phase115.py
    |           phase116.py
    |           phase117.py
    |           phase118.py
    |           phase119.py
    |           phase11_new.py
    |           phase12.py
    |           phase120.py
    |           phase121.py
    |           phase122.py
    |           phase123.py
    |           phase124.py
    |           phase125.py
    |           phase126.py
    |           phase127.py
    |           phase128.py
    |           phase129.py
    |           phase12_new.py
    |           phase13.py
    |           phase130.py
    |           phase131.py
    |           phase132.py
    |           phase133.py
    |           phase134.py
    |           phase135.py
    |           phase136.py
    |           phase137.py
    |           phase138.py
    |           phase139.py
    |           phase13_new.py
    |           phase14.py
    |           phase140.py
    |           phase141.py
    |           phase142.py
    |           phase143.py
    |           phase144.py
    |           phase145.py
    |           phase146.py
    |           phase147.py
    |           phase148.py
    |           phase149.py
    |           phase14_new.py
    |           phase15.py
    |           phase15_new.py
    |           phase16.py
    |           phase16_new.py
    |           phase17.py
    |           phase17_new.py
    |           phase18.py
    |           phase18_new.py
    |           phase19.py
    |           phase19_new.py
    |           phase1_new.py
    |           phase2.py
    |           phase20.py
    |           phase20_new.py
    |           phase21.py
    |           phase21_new.py
    |           phase22.py
    |           phase22_new.py
    |           phase23.py
    |           phase23_new.py
    |           phase24.py
    |           phase24_new.py
    |           phase25.py
    |           phase25_new.py
    |           phase26.py
    |           phase26_new.py
    |           phase27.py
    |           phase27_new.py
    |           phase28.py
    |           phase28_new.py
    |           phase29.py
    |           phase29_new.py
    |           phase2_new.py
    |           phase3.py
    |           phase30.py
    |           phase30_new.py
    |           phase31.py
    |           phase31_new.py
    |           phase32.py
    |           phase32_new.py
    |           phase33.py
    |           phase33_new.py
    |           phase34.py
    |           phase34_new.py
    |           phase35.py
    |           phase35_new.py
    |           phase36.py
    |           phase36_new.py
    |           phase37.py
    |           phase37_new.py
    |           phase38.py
    |           phase38_new.py
    |           phase39.py
    |           phase39_new.py
    |           phase3_new.py
    |           phase4.py
    |           phase40.py
    |           phase40_new.py
    |           phase41.py
    |           phase41_new.py
    |           phase42.py
    |           phase42_new.py
    |           phase43.py
    |           phase43_new.py
    |           phase44.py
    |           phase44_new.py
    |           phase45.py
    |           phase45_new.py
    |           phase46.py
    |           phase46_new.py
    |           phase47.py
    |           phase47_new.py
    |           phase48.py
    |           phase48_new.py
    |           phase49.py
    |           phase49_new.py
    |           phase4_new.py
    |           phase5.py
    |           phase50.py
    |           phase50_new.py
    |           phase51.py
    |           phase51_new.py
    |           phase52.py
    |           phase52_new.py
    |           phase53.py
    |           phase53_new.py
    |           phase54.py
    |           phase54_new.py
    |           phase55.py
    |           phase55_new.py
    |           phase56.py
    |           phase56_new.py
    |           phase57.py
    |           phase58.py
    |           phase59.py
    |           phase5_new.py
    |           phase6.py
    |           phase60.py
    |           phase61.py
    |           phase62.py
    |           phase63.py
    |           phase64.py
    |           phase65.py
    |           phase66.py
    |           phase67.py
    |           phase68.py
    |           phase69.py
    |           phase6_new.py
    |           phase7.py
    |           phase70.py
    |           phase71.py
    |           phase72.py
    |           phase73.py
    |           phase74.py
    |           phase75.py
    |           phase76.py
    |           phase77.py
    |           phase78.py
    |           phase79.py
    |           phase7_new.py
    |           phase8.py
    |           phase80.py
    |           phase81.py
    |           phase82.py
    |           phase83.py
    |           phase84.py
    |           phase85.py
    |           phase86.py
    |           phase87.py
    |           phase88.py
    |           phase89.py
    |           phase8_new.py
    |           phase9.py
    |           phase90.py
    |           phase90b.py
    |           phase91.py
    |           phase92.py
    |           phase93.py
    |           phase94.py
    |           phase95.py
    |           phase96.py
    |           phase97.py
    |           phase98.py
    |           phase99.py
    |           phase9_new.py
    |           raft-small-files.txt
    |           rockyou.txt
    |           setup_webhook.py
    |           solve.py
    |           test.dtd
    |           test_app.py
    |           test_cdata.py
    |           test_lxml.py
    |           transcript_search_results.txt
    |           web_wordlist.txt
    |           web_wordlist2.txt
    |           Writeup.md
    |           
    +---Low
    |   +---w2c1
    |   |       cookies.txt
    |   |       login_page.html
    |   |       Writeup.md
    |   |       
    |   \---w2c2
    |           cookies.txt
    |           login_page.html
    |           Writeup.md
    |           
    \---Medium
        +---w3c1
        |       admin_api_root.html
        |       advanced_bypass.py
        |       analyze_source.py
        |       blacklist_analysis.py
        |       bypass_tricks.py
        |       ctf_routes.py
        |       deep_scan.py
        |       docker_services.py
        |       encoded_flag_auth.py
        |       encoded_path_bypass.py
        |       encoding_bypass.py
        |       encoding_test.py
        |       error_body_probe.py
        |       final_probe.py
        |       flag_full_response.html
        |       full_response.py
        |       parse_responses.py
        |       portscan.py
        |       probe10.py
        |       probe11.py
        |       probe12.py
        |       probe2.py
        |       probe3.py
        |       probe4.py
        |       probe5.py
        |       probe6.py
        |       probe7.py
        |       probe8.py
        |       probe9.py
        |       probe_api.py
        |       query_explore.py
        |       query_flag_test.py
        |       redirect_bypass.py
        |       redirect_result.html
        |       resp_root8081.html
        |       resp__admin.html
        |       resp__api.html
        |       resp__api_flag.html
        |       resp__config.html
        |       resp__debug.html
        |       resp__env.html
        |       resp__flag.html
        |       resp__health.html
        |       resp__info.html
        |       resp__internal.html
        |       resp__secret.html
        |       resp__status.html
        |       route_enum.py
        |       short_paths.py
        |       ssrf_login.html
        |       ssrf_profile.html
        |       ssrf_proxy.html
        |       ssrf_register.html
        |       ssrf_root.html
        |       ssrf_services.html
        |       ssrf_webapp.py
        |       ssrf_webapp2.py
        |       threaded_scan.py
        |       webapp_source.html
        |       Writeup.md
        |       
        +---w3c1v2
        |       .p
        |       .u
        |       cj.txt
        |       dash.html
        |       dh.txt
        |       f.html
        |       h.txt
        |       home2.html
        |       index.html
        |       ir.html
        |       pr.html
        |       proxy.html
        |       reg.html
        |       rh.txt
        |       root.html
        |       services.html
        |       t.html
        |       Writeup.md
        |       
        \---w3c2
                .htaccess
                cookies.txt
                exploit.py
                headers.txt
                payload.php.jpg
                payload.phtml
                payload_output.html
                phase2.py
                phase3.py
                phase4.py
                session.txt
                Writeup.md
                
``n
