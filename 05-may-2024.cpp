class Solution{
  public:
    void solve(Node* root, map<int,vector<int>>& mp, int i){
        // base case
        if(root == NULL) return;
        
        mp[i].push_back(root->data);
        solve(root->left,mp,i-1);
        solve(root->right,mp,i+1);
    }
  
    vector <int> verticalSum(Node *root) {
        // add code here.
        map<int,vector<int>> mp;
        vector<int> ans;
        solve(root,mp,0);
        
        for(auto i : mp){
            int sum = 0;
            // int left = i.first;
            vector<int> right = i.second;
            for(auto j : right){
                sum += j;
            }
            ans.push_back(sum);
        }
        
        return ans;
    }
};