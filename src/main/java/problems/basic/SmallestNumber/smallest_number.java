// { Driver Code Starts
// Initial Template for Java
package problems.basic.SmallestNumber;

import java.io.*;

@SuppressWarnings("PMD")
class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            String[] inp = read.readLine().split(" ");
            int S = Integer.parseInt(inp[0]);
            int D = Integer.parseInt(inp[1]);

            Solution ob = new Solution();
            System.out.println(ob.smallestNumber(S, D));
        }
    }
} // } Driver Code Ends

// User function Template for Java
class Solution {
    static String smallestNumber(int S, int D) {
        // code here
        return "";
    }
}
