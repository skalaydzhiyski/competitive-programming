#include <iostream>
#include <vector>
using namespace std;

class OrgChart {
public:
  char name;
  vector<OrgChart *> directReports;

  OrgChart(char name) {
    this->name = name;
    this->directReports = {};
  }

  void addDirectReports(vector<OrgChart *> directReports) {
    this->directReports = directReports;
  }
};

OrgChart *getLowestCommonManager(
    OrgChart* topManager,
    OrgChart* reportOne, OrgChart* reportTwo) {
  // write your solution here
  return NULL;
}

// For this problem there is no main method since the testing of the code requires 
// too much unnecessary work and the solution here is copied from the 
// AlgoExpert platform without providing tests. Sorrty :( 

