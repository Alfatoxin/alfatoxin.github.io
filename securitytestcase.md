# Security Test Case

อนุญาตให้สามารถดาวน์โหลดไฟล์ได้เฉพาะนามสกุล JPG และ PNG เท่านั้น

| Test Case ID |     Test case objective     | Preconditions                                    | Input data     | Expected       | Postconditions      | Status |
|-------------:|:---------------------------:|--------------------------------------------------|----------------|----------------|---------------------|--------|
|       1      | ไฟล์ที่พร้อมดาวน์โหลด นามสกุล jpg | รูป [filename].jpg อยู่บน Web Server พร้อมให้ดาวน์โหลด | image link URL | [fliename].jpg | [fliename].jpg      | Pass   |
|       2      | ไฟล์ที่พร้อมดาวน์โหลด นามสกุล png | รูป [filename].png อยู่บน Web Server พร้อมให้ดาวน์โหลด | image link URL | [fliename].png | [fliename].png      | Pass   |
|       3      | ไฟล์ที่พร้อมดาวน์โหลด นามสกุล zip | รูป [filename].zip อยู่บน Web Server พร้อมให้ดาวน์โหลด | file link URL  | [fliename].zip | ERROR 403 Forbidden | Pass   |