import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        int arr[] = {0,1,3,5,9,13,17,25,33,41,49,65,81,97,113,129,161,193,225,257,289,321,385,449,513,577,641,705,769,897,1025,1153,1281,1409,1537,1665,1793,2049,2305,2561,2817,3073,3329,3585,3841,4097,4609,5121,5633,6145,6657,7169,7681,8193,8705,9217};
        Scanner in = new Scanner(System.in);
        int tc = in.nextInt();
        int n;
        long m;
        for (int t = 0; t < tc; t++) {
            n = in.nextInt();
            m = in.nextLong();
            if (m >= arr[n])
                System.out.println("YES");
            else
                System.out.println("NO");
        }
        
    }
}