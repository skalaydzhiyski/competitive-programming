#include <stdlib.h>
#include <iostream>
using namespace std;

template<typename T>
class Array {
  T* begin;
  int size = 0;
public:
  Array(const int size) {
    this->begin = (T*)malloc(size*sizeof(T));
    this->size = size;
  }
  // this is the same as arr[i] = x;
  void add(int idx, T val) {
    begin[idx] = val;
  }
  T& operator[](int idx) {
    return begin[idx];
  }
};

int main(void) {
  Array<int> arr(3);
  arr.add(0, 128);
  cout << arr[0] << endl;
  return 0;
}

