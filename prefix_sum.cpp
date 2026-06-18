#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int a[n];
    int prefix[n];

    for(int i = 0; i < n; i++) {
        cin >> a[i];
    }

    prefix[0] = a[0];

    for(int i = 1; i < n; i++) {
        prefix[i] = prefix[i-1] + a[i];
    }

    int q;
    cin >> q;

    while(q--) {
        int l, r;
        cin >> l >> r;

        if(l == 0)
            cout << prefix[r] << endl;
        else
            cout << prefix[r] - prefix[l-1] << endl;
    }

    return 0;
}