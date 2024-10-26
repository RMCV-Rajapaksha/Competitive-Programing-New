#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;
const int MAXN = 12;

// Custom state compressor using bit manipulation
class StateManager {
private:
    vector<uint32_t> states;
    const static int SHIFT1 = 20;  // Bits 20-31 for last1
    const static int SHIFT2 = 8;   // Bits 8-19 for last2
    
public:
    void init(int size) {
        states.resize(1 << (2 * MAXN), -1);
    }
    
    // Pack state into 32-bit integer
    inline uint32_t pack(int last1, int last2) const {
        return (last1 << SHIFT1) | (last2 << SHIFT2);
    }
    
    // Get/Set state values
    inline int get(int mask, int last1, int last2) const {
        return states[mask] & ((1 << 8) - 1);
    }
    
    inline void set(int mask, int last1, int last2, int value) {
        uint32_t packed = pack(last1, last2) | (value & ((1 << 8) - 1));
        states[mask] = packed;
    }
    
    inline bool exists(int mask, int last1, int last2) const {
        return (states[mask] != -1) && 
               ((states[mask] >> SHIFT1) == last1) && 
               (((states[mask] >> SHIFT2) & ((1 << 12) - 1)) == last2);
    }
};

// Constraint manager using bit manipulation
class ConstraintManager {
private:
    uint32_t a_mask;  // Bit mask for numbers that must be in row A
    uint32_t b_mask;  // Bit mask for numbers that must be in row B
    
public:
    void init(const vector<int>& A, const vector<int>& B) {
        a_mask = b_mask = 0;
        for (int x : A) a_mask |= (1U << (x - 1));
        for (int x : B) b_mask |= (1U << (x - 1));
    }
    
    inline bool must_be_in_A(int num) const {
        return (a_mask & (1U << (num - 1))) != 0;
    }
    
    inline bool must_be_in_B(int num) const {
        return (b_mask & (1U << (num - 1))) != 0;
    }
};

// Global variables to minimize stack usage
int N;
StateManager dp;
ConstraintManager constraints;

int solve_recursive(int mask, int last1, int last2) {
    // Base case
    if (__builtin_popcount(mask) == 2 * N) return 1;
    
    // Check memoized state
    if (dp.exists(mask, last1, last2)) 
        return dp.get(mask, last1, last2);
    
    int result = 0;
    int col = __builtin_popcount(mask) / 2;
    
    // Try numbers for first row
    for (int i = last1 + 1; i <= 2 * N; i++) {
        if ((mask & (1U << (i - 1))) || constraints.must_be_in_B(i)) 
            continue;
            
        // Try numbers for second row
        for (int j = max(last2 + 1, i + 1); j <= 2 * N; j++) {
            if ((mask & (1U << (j - 1))) || constraints.must_be_in_A(j)) 
                continue;
            
            int new_mask = mask | (1U << (i - 1)) | (1U << (j - 1));
            result = (result + solve_recursive(new_mask, i, j)) % MOD;
        }
    }
    
    dp.set(mask, last1, last2, result);
    return result;
}

int solve(int n, vector<int>& A_nums, vector<int>& B_nums) {
    N = n;
    
    // Initialize managers
    dp.init(1 << (2 * N));
    constraints.init(A_nums, B_nums);
    
    return solve_recursive(0, 0, 0);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N, X, Y;
    cin >> N;
    
    if (N <= 0 || N > MAXN) {
        cout << "0\n";
        return 0;
    }
    
    cin >> X;
    vector<int> A(X);
    for (int i = 0; i < X; i++) cin >> A[i];
    
    cin >> Y;
    vector<int> B(Y);
    for (int i = 0; i < Y; i++) cin >> B[i];
    
    cout << solve(N, A, B) << '\n';
    return 0;
}