import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.InputMismatchException;

public class CloudyDay {

    InputStream is;
    PrintWriter out;
    String INPUT = "";

    void solve() {
        int n = ni();  // number of towns
        int[][] pt = new int[n][2];  // towns with population and position

        for (int i = 0; i < n; i++) pt[i][0] = ni();  // population
        for (int i = 0; i < n; i++) pt[i][1] = ni();  // position

        // Sort towns by position
        Arrays.sort(pt, (a, b) -> a[1] - b[1]);

        int m = ni();  // number of clouds
        int[][] cs = new int[m][2];  // clouds with position and extent

        for (int i = 0; i < m; i++) cs[i][0] = ni();  // cloud position
        for (int i = 0; i < m; i++) cs[i][1] = ni();  // cloud extent

        // Adjust clouds to represent their left and right extents
        for (int i = 0; i < m; i++) {
            int l = cs[i][0] - cs[i][1];
            int r = cs[i][0] + cs[i][1];
            cs[i][0] = l;
            cs[i][1] = r;
        }

        int[] ts = new int[n];  // town positions
        for (int i = 0; i < n; i++) ts[i] = pt[i][1];

        long[] imos = new long[n + 2];  // prefix sum array for cloud coverage

        // Mark cloud coverage using the imos method
        for (int i = 0; i < m; i++) {
            int l = Arrays.binarySearch(ts, cs[i][0]);
            if (l < 0) l = -l - 1;
            int r = Arrays.binarySearch(ts, cs[i][1]);
            if (r < 0) r = -r - 2;
            imos[l]++;
            imos[r + 1]--;
        }

        // Accumulate the prefix sums
        for (int i = 0; i < n; i++) imos[i + 1] += imos[i];

        long base = 0;  // base population not covered by any cloud
        for (int i = 0; i < n; i++) {
            if (imos[i] != 1) {
                if (imos[i] == 0) base += pt[i][0];
                imos[i] = 0;
            } else {
                imos[i] = pt[i][0];
            }
        }

        // Compute prefix sums again for imos
        for (int i = 0; i < n; i++) imos[i + 1] += imos[i];

        long ans = 0;
        // Calculate the maximum number of people in sunny towns after removing one cloud
        for (int i = 0; i < m; i++) {
            int l = Arrays.binarySearch(ts, cs[i][0]);
            if (l < 0) l = -l - 1;
            int r = Arrays.binarySearch(ts, cs[i][1]);
            if (r < 0) r = -r - 2;
            ans = Math.max(ans, (r < 0 ? 0 : imos[r]) - (l - 1 < 0 ? 0 : imos[l - 1]));
        }

        out.println(base + ans);
    }

    void run() throws Exception {
        is = INPUT.isEmpty() ? System.in : new ByteArrayInputStream(INPUT.getBytes());
        out = new PrintWriter(System.out);

        long s = System.currentTimeMillis();
        solve();
        out.flush();
        if (!INPUT.isEmpty()) tr(System.currentTimeMillis() - s + "ms");
    }

    public static void main(String[] args) throws Exception {
        new CloudyDay().run();
    }

    private byte[] inbuf = new byte[1024];
    public int lenbuf = 0, ptrbuf = 0;

    private int readByte() {
        if (lenbuf == -1) throw new InputMismatchException();
        if (ptrbuf >= lenbuf) {
            ptrbuf = 0;
            try {
                lenbuf = is.read(inbuf);
            } catch (IOException e) {
                throw new InputMismatchException();
            }
            if (lenbuf <= 0) return -1;
        }
        return inbuf[ptrbuf++];
    }

    private boolean isSpaceChar(int c) {
        return !(c >= 33 && c <= 126);
    }

    private int skip() {
        int b;
        while ((b = readByte()) != -1 && isSpaceChar(b)) ;
        return b;
    }

    private double nd() {
        return Double.parseDouble(ns());
    }

    private char nc() {
        return (char) skip();
    }

    private String ns() {
        int b = skip();
        StringBuilder sb = new StringBuilder();
        while (!(isSpaceChar(b))) {
            sb.appendCodePoint(b);
            b = readByte();
        }
        return sb.toString();
    }

    private char[] ns(int n) {
        char[] buf = new char[n];
        int b = skip(), p = 0;
        while (p < n && !(isSpaceChar(b))) {
            buf[p++] = (char) b;
            b = readByte();
        }
        return n == p ? buf : Arrays.copyOf(buf, p);
    }

    private char[][] nm(int n, int m) {
        char[][] map = new char[n][];
        for (int i = 0; i < n; i++) map[i] = ns(m);
        return map;
    }

    private int[] na(int n) {
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = ni();
        return a;
    }

    private int ni() {
        int num = 0, b;
        boolean minus = false;
        while ((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-')) ;
        if (b == '-') {
            minus = true;
            b = readByte();
        }

        while (true) {
            if (b >= '0' && b <= '9') {
                num = num * 10 + (b - '0');
            } else {
                return minus ? -num : num;
            }
            b = readByte();
        }
    }

    private long nl() {
        long num = 0;
        int b;
        boolean minus = false;
        while ((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-')) ;
        if (b == '-') {
            minus = true;
            b = readByte();
        }

        while (true) {
            if (b >= '0' && b <= '9') {
                num = num * 10 + (b - '0');
            } else {
                return minus ? -num : num;
            }
            b = readByte();
        }
    }

    private static void tr(Object... o) {
        System.out.println(Arrays.deepToString(o));
    }
}
