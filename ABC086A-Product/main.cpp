#include<iostream>
using namespace std;
int main(){
	int a,b,product;
	cin >> a >> b;
	product = a * b;
	if(product % 2 == 0){
		cout << "Even" << endl;
		return 0;
	}

	cout << "Odd" << endl;
	return 0;
}
