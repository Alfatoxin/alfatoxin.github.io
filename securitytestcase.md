# Security Test Case

อนุญาตให้สามารถดาวน์โหลดไฟล์ได้เฉพาะนามสกุล JPG และ PNG เท่านั้น

|     Test case objective     | Preconditions                                    | Input data     | Expected       | Postconditions | Status |
|:---------------------------:|--------------------------------------------------|----------------|----------------|----------------|--------|
| ไฟล์ที่พร้อมดาวน์โหลด นามสกุล jpg | รูป [filename].jpg อยู่บน Web Server พร้อมให้ดาวน์โหลด | image link URL | [fliename].jpg | [fliename].jpg | Pass   |