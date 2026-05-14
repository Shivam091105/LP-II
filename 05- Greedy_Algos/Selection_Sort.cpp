#include<iostream>
using namespace std;

void sSort(int nums[], int n){
    for(int i=0;i<n;i++){
        int minIndex=i;
        for(int j=i+1;j<n;j++){
            if(nums[j]<nums[minIndex]){
                minIndex = j;
            }
        }
        swap(nums[i], nums[minIndex]);
    }
}

int main(){
    int arr[5] = {15, 8, 19, 5, 4};
    sSort(arr, 5);
    for(int i:arr){
        cout<<i<<" ";
    }
    return 0;
}