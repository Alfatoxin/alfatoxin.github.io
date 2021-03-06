# วิธีการ Hash บนภาษา Java ด้วย อัลกอริทึม SHA-256

### **Hash** เป็น **One-way function** ซึ่งไม่สามารถทำให้กลับมาเป็นข้อมูลเดิมได้ เว้นแต่มีการเก็บข้อมูลเป็น Dictionary มากพอซึ่งใน Dictionary จะประกอบไปด้วย **ข้อความ** และค่า **Hash** ซึ่งจะเอาค่า **Hash** มาเทียบเพื่อหาข้อความ แต่อย่าลืมไปข้อความ 2 ข้อความที่ทำการ Hash อาจจะได้ค่าเดียวกันก็เป็นได้ ซึ่งการใช้ Function **sha256** ก็คือการ **Hash** เช่นกัน
<br>

![](../../assets/img/Java00.png) 
<br>
<br>

การที่จะป้องข้อมูลบางอย่างหลุดออกไปนั้นทำได้หลากหลายวิธี ถึงแม้ว่าข้อมูลจะหลุดออกไปแต่ก็ไม่สามารถนำไปใช้งานได้หรือไม่สามารถเห็นข้อมูลจริงๆ ได้ หนึ่งในวิธีนั้นก็หนีไม่พ้น Hash Function ซึ่งการ Hash ก็มีอัลกอริทึมในการทำที่แตกต่างกันไปไม่ว่าจะเป็น **md5**, **sha1**, **sha256**

### เริ่มกันเลย
1. เตรียม Package ที่จำเป็นต้องใช้
    ```java
    import java.nio.charset.StandardCharsets;
    import java.security.MessageDigest;
    import java.security.NoSuchAlgorithmException;
    import java.util.Base64;
    ```
1. ตัวอย่างการเรียกใช้งาน 
    ```java
    public static void main(String[] args) throws NoSuchAlgorithmException {
        String text = "Sakarin Kaewsathitwong";
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        byte[] hash = digest.digest(text.getBytes(StandardCharsets.UTF_8));
        String encoded = Base64.getEncoder().encodeToString(hash);
        System.out.println("Encoded is " + encoded);
    }
    ```
    ผลลัพธ์ที่ได้
    ```
    Encoded is 36XdouX0jUOVfMNY2eTwgk1mqXX3egMog5+zhqjSIsI=
    ```
    ![](../../assets/img/Java01.png)
<br>
<br>

### แล้วทำไมต้อง hash ข้อมูลให้มันยุ่งยาก ?
ก็เพื่อป้องกันไม่ให้ทำการ de-hash ข้อมูลเดิมกลับมาได้นั้นเองเพราะ Hash เป็น One-way function มีทางเดียวที่อยากจะรู้ข้อมูลข้างในก็คือการ Brute-force ซึ่งการทำแบบนั้นก็อาจจะไม่ใช่คำตอบที่ถูกต้องก็ได้

#### Knowledge base อื่นๆ ที่น่าสนใจ
* **[ซ่อนภาพที่คุณไม่อยากให้ใครเห็นง่ายๆ ด้วยภาษา Python](../Python/)**
* **[ข้ารหัสและถอดรหัสด้วย CryptographyHelper.EncryptString() ในภาษา C#](../Csharp/)**
* **[ป้องกันรหัสผ่านรั่วไหลบน MySQL ด้วย Function PASSWORD](../MySQL/)**
* **[Function sha1 บน Node.JS](../JavaScript/)**
* **[วิธีการ Hash บนภาษา Java ด้วย อัลกอริทึม SHA-256](../Java/)**
* **[วิธีการ Hash บนภาษา Golang ด้วย อัลกอริทึม SHA-256](../Golang/)**
* **[Function empty คืออะไรในภาษา PHP](../PHP/)**
<br>
<br>

created by Sakarin Kaewsathitwong