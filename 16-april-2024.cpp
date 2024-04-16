class Solution {
  public:
    int minimizeDifference(int n, int k, vector<int> &arr) {
        // code here
        vector<pair<int, int>> l(n), r(n);
        l[0] = {arr[0], arr[0]};
        r[n - 1] = {arr[n - 1], arr[n - 1]};
        for(int i = 1; i < n; i++) {
            l[i] = {min(l[i - 1].first, arr[i]), max(l[i - 1].second, arr[i])};
            r[n - i - 1] = {min(r[n - i].first, arr[n - i - 1]), max(r[n - i].second, arr[n - i - 1])};
        }
        int j = 0;
        int ans = r[k].second - r[k].first;
        for(int i = k + 1; i < n; i++) {
            int minn = min(l[j].first, r[i].first);
            int maxx = max(l[j].second, r[i].second);
            ans = min(ans, maxx - minn);
            j++;
        }
        ans = min(ans, l[n - k - 1].second - l[n - k - 1].first);
        return ans;
    }
};