#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;
const int MAXN = 10;  // Maximum value of N
const int MAXSZ = 20; // Maximum size for arrays (2*N)

int dp[1 << (2 * MAXN)];
bool used[1 << (2 * MAXN)];
int N, A_mask, B_mask;

inline int solve_dp(int mask, int last1, int last2) {
    if (__builtin_popcount(mask) == 2 * N) return 1;
    
    if (used[mask] && dp[mask] != -1) return dp[mask];
    used[mask] = true;
    
    int result = 0;
    // Try placing next pair of numbers
    for (int num1 = last1 + 1; num1 <= 2 * N; num1++) {
        // Skip if number is used or constrained
        if ((mask & (1 << (num1 - 1))) || (B_mask & (1 << (num1 - 1)))) 
            continue;
        
        for (int num2 = max(last2 + 1, num1 + 1); num2 <= 2 * N; num2++) {
            // Skip if number is used or constrained
            if ((mask & (1 << (num2 - 1))) || (A_mask & (1 << (num2 - 1)))) 
                continue;
            
            int new_mask = mask | (1 << (num1 - 1)) | (1 << (num2 - 1));
            result = (result + solve_dp(new_mask, num1, num2)) % MOD;
        }
    }
    
    return dp[mask] = result;
}

int solve(int n, vector<int>& A_nums, vector<int>& B_nums) {
    N = n;
    
    // Reset arrays safely
    int total_states = 1 << (2 * N);
    for (int i = 0; i < total_states; i++) {
        dp[i] = -1;
        used[i] = false;
    }
    
    // Create constraint masks
    A_mask = B_mask = 0;
    for (int x : A_nums) {
        if (x > 0 && x <= 2 * N) // Bounds check
            A_mask |= (1 << (x - 1));
    }
    for (int x : B_nums) {
        if (x > 0 && x <= 2 * N) // Bounds check
            B_mask |= (1 << (x - 1));
    }
    
    return solve_dp(0, 0, 0);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    
    int N, X, Y;
    cin >> N;
    
    if (N <= 0 || N > MAXN) {
        cout << "0\n";
        return 0;
    }
    
    cin >> X;
    vector<int> A(X);
    for (int i = 0; i < X; i++) {
        cin >> A[i];
    }
    
    cin >> Y;
    vector<int> B(Y);
    for (int i = 0; i < Y; i++) {
        cin >> B[i];
    }
    
    cout << solve(N, A, B) << '\n';
    return 0;
}