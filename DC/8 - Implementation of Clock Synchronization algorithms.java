// File Name : BerkeleyAlgorithm

import java.text.SimpleDateFormat;
import java.util.*;

public class BerkeleyAlgorithm {
    static void berkeleyAlgo(String sTime, String c1Time, String c2Time) throws Exception {
        System.out.println("Server Clock   = " + sTime);
        System.out.println("Client Clock1  = " + c1Time);
        System.out.println("Client Clock2  = " + c2Time);

        SimpleDateFormat sdf = new SimpleDateFormat("mm:ss");
        long s = sdf.parse(sTime).getTime();
        long t1 = sdf.parse(c1Time).getTime();
        long t2 = sdf.parse(c2Time).getTime();

        long st1 = t1 - s, st2 = t2 - s;
        long avg = (st1 + st2) / 2;
        long adj1 = avg - st1, adj2 = avg - st2;

        System.out.println("t1 - s = " + st1 / 1000);
        System.out.println("t2 - s = " + st2 / 1000);
        System.out.println(" (st1 + st2) / 2 = " + avg / 1000);
        System.out.println(" t1 adjustment = " + adj1 / 1000);
        System.out.println(" t2 adjustment = " + adj2 / 1000);
        System.out.println(" Synchronized Server Clock = " + sdf.format(new Date(avg + s)));
        System.out.println(" Synchronized Client1 Clock = " + sdf.format(new Date(t1 + adj1)));
        System.out.println(" Synchronized Client2 Clock = " + sdf.format(new Date(t2 + adj2)));
    }

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Server Time (mm:ss): ");
        String s = sc.nextLine();
        System.out.print("Enter Client 1 Time (mm:ss): ");
        String c1 = sc.nextLine();
        System.out.print("Enter Client 2 Time (mm:ss): ");
        String c2 = sc.nextLine();
        berkeleyAlgo(s, c1, c2);
        sc.close();
    }
}