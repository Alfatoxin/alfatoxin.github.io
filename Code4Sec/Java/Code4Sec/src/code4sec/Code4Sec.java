package code4sec;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;

public class Code4Sec {

    public static void main(String[] args) throws NoSuchAlgorithmException {
//        String text = "Sakarin Kaewsathitwong";
//        MessageDigest digest = MessageDigest.getInstance("SHA-256");
//        byte[] hash = digest.digest(text.getBytes(StandardCharsets.UTF_8));
//        String encoded = Base64.getEncoder().encodeToString(hash);
//        System.out.println("Encoded is " + encoded);

        int a, b;
        a = 5;
        b = 100;
        
        a = b;
        a = a + 10;
        
        System.out.println("a is " + a);
        System.out.println("b is " + b);
    }
    
}
