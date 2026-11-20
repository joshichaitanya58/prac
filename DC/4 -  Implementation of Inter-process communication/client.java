import java.io.*;
import java.net.*;
import java.util.*;

public class client {
    public static void main(String[] args) throws Exception {
        Socket s = new Socket("localhost", 6666);
        DataOutputStream dout = new DataOutputStream(s.getOutputStream());
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter 1st no:");
        dout.writeInt(sc.nextInt());
        System.out.println("Enter 2nd no:");
        dout.writeInt(sc.nextInt());

        dout.flush();
        dout.close();
        s.close();
        sc.close();
    }
}