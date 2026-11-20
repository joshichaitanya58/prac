import java.io.*;
import java.net.*;

public class server {
    public static void main(String[] args) throws Exception {
        ServerSocket ss = new ServerSocket(6666);
        Socket s = ss.accept();
        DataInputStream dis = new DataInputStream(s.getInputStream());
        System.out.println(dis.readInt() + dis.readInt());
        s.close();
        ss.close();
    }
}